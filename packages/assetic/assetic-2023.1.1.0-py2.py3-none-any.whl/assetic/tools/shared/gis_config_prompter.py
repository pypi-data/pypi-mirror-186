"""
https://stackoverflow.com/questions/33646605/how-to-access-variables-from-different-classes-in-tkinter
TODO Get list of asset attributes via v1 api: https://integration.assetic.net/api/SearchApi/GetSearchFields/Assets/airportbuilding/true/false
"""
# import tkFont
from tkinter import font

import logging

import six

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import *

import xml.etree.ElementTree as ET
import struct  # use for unicode symbol packing
import xml.dom.minidom
from assetic.api_client import ApiClient
from assetic.api import AssetConfigurationApi
from assetic.api import SystemConfigurationApi
from assetic.api import MaintenanceConfigurationApi
from assetic.rest import ApiException
from assetic.tools.shared.xml_config_reader import XMLConfigReader
from .messager_base import MessagerBase
from assetic.tools.apihelper import APIHelper

import os
import enum


class MainApp(tk.Tk):

    def __init__(self, layer_dict: dict, asseticsdk, target_gis: enum):
        """

        :param layer_dict:
        :param asseticsdk:
        :param gis:
        :type: GIS
        """
        self.layer_dict = layer_dict
        self._selected_layer_name = None
        self._current_config_frame = None
        self._current_tree_frame = None
        self._current_treeview_widget = None
        self._is_initialising = True
        self._current_asset_tree_node = None
        self._asset_treeview_instance = None

        self.tree_container = None

        self._current_component = None
        self._current_dimension = None

        if not isinstance(target_gis, TargetGis):
            raise TypeError("Error! GIS parameter is required to be an enum of "
                            "type GIS.  Import the GIS class ")
            return
        self._gis = target_gis

        tk.Tk.__init__(self)
        # TlDefaultFont is 'Segoe UI 9'
        self.font_normal = font.Font(family='Arial', size=10, weight="normal")
        self.font_header = font.Font(family='Arial', size=10, weight="bold")
        self.font_strike = font.Font(family='Arial', size=10, weight="normal"
                                     , overstrike=1)
        self.coloured_bg = "#349cbc"
        self.common_tools = CommonTools(asseticsdk, gis=self._gis)
        self._assetic_sdk = asseticsdk
        self.assetic_api_tools = AsseticApiTools(
            api_client=asseticsdk.client)

        self.layer_option = sorted(
            self.layer_dict.keys(), key=lambda x: x.lower())

        tree_container = tk.Frame(self, bg=self.coloured_bg)
        tree_container.pack(side="left", fill=tk.BOTH, expand=False)
        tree_container.grid_rowconfigure(0, weight=1)
        tree_container.grid_columnconfigure(0, weight=1)
        self.tree_container = tree_container

        operation_chooser_container = tk.Frame(self, background="#349cbc")
        operation_chooser_container.pack(fill=tk.BOTH, expand=False)
        operation_chooser_container.grid_rowconfigure(0, weight=0)
        operation_chooser_container.grid_columnconfigure(1, weight=0)

        # in the bulk of the window have the configuration frames
        container = tk.Frame(self)
        container.pack(fill=tk.BOTH, expand=True)
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(1, weight=1)
        self.container = container

        self.frames = {}
        self.tree_frames = {}

        for F in (AssetTreeViewFrame, FLTreeViewFrame, EmptyTreeViewFrame):
            frame = F(tree_container, self)
            self.tree_frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        lf = OperationChooserFrame(operation_chooser_container, self)
        lf.grid(row=0, column=0, sticky="nsew")
        self.frames[OperationChooserFrame] = lf
        self.show_frame(OperationChooserFrame)

        for F in (SettingsFrame, CategoryFrame, AssetCoreFrame
                  , AssetAttributesFrame, ComponentFrame, DimensionFrame
                  , AddressFrame, AssetFLAssociationFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=1, column=0, sticky="nsew")

        self.show_frame(SettingsFrame)
        self.is_initialising = False

        # Start with no tree frames visible because the initial operation is
        # overall config
        for F in (AssetTreeViewFrame, FLTreeViewFrame):
            self.hide_tree_frame(F)
        self.current_tree_frame = EmptyTreeViewFrame
        for F in (CategoryFrame, AssetCoreFrame, AssetAttributesFrame
                  , ComponentFrame, DimensionFrame, AddressFrame
                  , AssetFLAssociationFrame):
            self.hide_frame(F)
        self.show_frame(SettingsFrame)

    def show_frame(self, c):
        frame = self.frames[c]
        frame.tkraise()
        self.current_config_frame = c

    def hide_frame(self, c):
        frame = self.frames[c]
        frame.grid_forget()

    def show_tree_frame(self, c):
        frame = self.tree_frames[c]
        frame.tkraise()
        self.current_tree_frame = c

    def refresh_frame(self, c):
        frame = self.frames[c]
        frame.refresh(parent=self.container, controller=self)
        frame.grid(row=0, column=1, sticky="nsew")

    def refresh_tree_frame(self, c):
        frame = self.tree_frames[c]
        frame.refresh(parent=self.tree_container, controller=self)
        frame.grid(row=0, column=0, sticky="nsew")

    def hide_tree_frame(self, c):
        frame = self.tree_frames[c]
        frame.grid_forget()

    def hide_current_config_frame(self):
        frame = self.frames[self._current_config_frame]
        frame.grid_forget()

    def get_existing_xml(self):
        return self.common_tools.get_existing_xml()

    def get_asset_config_dict(self):
        return self.common_tools.get_asset_config_dict()

    # def save_layer_info(self, curr_layer, layer_name, delete=0):
    #    self.common_tools.save_layer_info(
    #        curr_layer=curr_layer, delete=delete, layer_name=layer_name)

    def save_settings_info(self):
        chk = self.frames[self._current_config_frame].save_settings_config()
        return chk

    @property
    def selected_layer_name(self):
        return self._selected_layer_name

    @selected_layer_name.setter
    def selected_layer_name(self, value):
        self._selected_layer_name = value

    @property
    def current_config_frame(self):
        return self._current_config_frame

    @current_config_frame.setter
    def current_config_frame(self, value):
        self._current_config_frame = value

    @property
    def current_tree_frame(self):
        """
        Currently selected tree frame
        :return: tree frame
        """
        return self._current_tree_frame

    @current_tree_frame.setter
    def current_tree_frame(self, value):
        self._current_tree_frame = value

    @current_config_frame.setter
    def current_config_frame(self, value):
        self._current_config_frame = value

    @property
    def current_treeview_widget(self):
        """
        Currently selected treeview widget
        :return: treeview widget
        """
        return self._current_treeview_widget

    @current_treeview_widget.setter
    def current_treeview_widget(self, value):
        self._current_treeview_widget = value

    @property
    def asset_treeview_instance(self):
        """
        asset treeview instance
        :return: asset treeview instance
        """
        return self._asset_treeview_instance

    @asset_treeview_instance.setter
    def asset_treeview_instance(self, value):
        self._asset_treeview_instance = value

    @property
    def current_component(self):
        """
        Currently selected component
        :return: dict
        """
        return self._current_component

    @current_component.setter
    def current_component(self, value):
        self._current_component = value

    @property
    def current_dimension(self):
        """
        Currently selected dimension (network measure)
        :return: dict
        """
        return self._current_dimension

    @current_dimension.setter
    def current_dimension(self, value):
        """
        Set the Currently selected dimension (network measure)
        :param value: value to set
        """
        self._current_dimension = value

    @property
    def is_initialising(self):
        return self._is_initialising

    @is_initialising.setter
    def is_initialising(self, value):
        self._is_initialising = value

    @property
    def current_asset_tree_node(self):
        return self._current_asset_tree_node

    @current_asset_tree_node.setter
    def current_asset_tree_node(self, value):
        self._current_asset_tree_node = value

    @property
    def gis(self):
        return self._gis

    @gis.setter
    def gis(self, value):
        self._gis = value

    def save_current_asset_frame(self, delete=False):
        """
        Save the current asset frame
        :return: true if success, else false
        """
        if not self._current_config_frame:
            # No config to save
            return True

        chk = 0
        current_frame = self._current_config_frame
        if current_frame.__name__ == "CategoryFrame":
            self.frames[current_frame].save_layer_category_config()
        elif current_frame.__name__ == "AssetCoreFrame":
            chk = self.frames[current_frame].save_asset_info()
        elif current_frame.__name__ == "AssetAttributesFrame":
            chk = self.frames[current_frame].save_asset_attribute_info()
        elif current_frame.__name__ == "ComponentFrame":
            chk = self.frames[current_frame].save_component_info(delete)
        elif current_frame.__name__ == "DimensionFrame":
            chk = self.frames[current_frame].save_dimension_info(delete)
        elif current_frame.__name__ == "AddressFrame":
            self.frames[current_frame].save_address_info(delete)
        elif current_frame.__name__ == "AssetFLAssociationFrame":
            chk = self.frames[current_frame].save_fl_association_info(delete)
        if chk == 0:
            return True
        else:
            return False


class TargetGis(enum.Enum):
    ESRI = "esri"
    QGIS = "qgis"
    MapInfo = "mapinfo"


class AssetTreeViewFrame(tk.Frame):
    """
    This class sets up the tree hierarch navigator
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.existing_layer = None
        self.controller = controller
        controller.asset_treeview_instance = self
        self.logger = logging.getLogger("Assetic")

        font_normal = controller.font_normal
        font_header = controller.font_header
        font_strike = controller.font_strike
        self.configure()

        self.configured_layers = controller.get_asset_config_dict()

        if controller.layer_dict is None:
            message = "No layer found from the file"
            self.logger.error(message)
            return
        # get a list of layer names for the combobox and insert an empty row
        # so that no layer is selected when initialising the form
        layer_option = sorted(controller.layer_dict.keys()
                              , key=lambda x: x.lower())
        self.selected_layer = tk.StringVar()

        self.layer_tree_order = dict()

        tv = ttk.Treeview(self, show='tree')
        self.tv = tv
        self.controller.current_treeview_widget = tv

        tv.heading('#0', text='Asset Hierarchy', anchor=tk.W)

        if self.controller.is_initialising:
            # still in app startup so no need yet to build tree
            return

        # Build the tree contents
        self.build_assets_tree(tv, layer_option)

        tv.tag_configure('TkTextFont', font=font_normal)
        tv.update()
        tvscroll = ttk.Scrollbar(self)
        tvscroll.configure(command=tv.yview)
        tv.configure(yscrollcommand=tvscroll.set)
        tvscroll.pack(side="right", fill="both")

        tv.pack(expand=True, fill='both')
        # tv.grid(row=0, column=0)

        # bind the callback on node selection
        tv.bind("<<TreeviewSelect>>", self.on_node_select)
        # tv.bind("<FocusOut>", self.on_node_leave)
        # set selected node to the first layer
        tv.selection_set("0_layer")
        tv.focus("0_layer")
        tv.focus_set()

    def refresh(self, parent, controller):
        self.destroy()
        self.__init__(parent, controller)

    def on_node_leave(self, event):
        """
        callback for when a tree node is left - cant find the right event to
        trigger this
        :param event:
        """
        tree = event.widget
        # tree.item(tree.selection()[0])['text'] = "juju"
        # tree.update()
        node_id = tree.focus()

        # tree.set(tree.focus(), value="gt")
        # tree.item(tree.selection()[0], text="blub")
        tree.item(node_id, text="blub")
        tree.update()

    def on_node_select(self, event):
        """
        callback for when an tree node is selected
        :param event: the node selection event
        """

        # if self.controller.current_asset_tree_node:
        #    current_node_text = self.tv.item(
        #        self.controller.current_asset_tree_node)["text"]
        chk = 0
        selected_node = event.widget
        new_selection_node = selected_node.focus()

        if self.controller.current_config_frame and \
                self.controller.current_asset_tree_node != new_selection_node:
            # the selection is different to what was the current selection
            if self.controller.current_config_frame.__name__ == "CategoryFrame":
                self.controller.frames[
                    self.controller.current_config_frame
                ].save_layer_category_config()
                # TODO Save
            elif self.controller.current_config_frame.__name__ == \
                    "AssetCoreFrame":
                chk = self.controller.frames[
                    self.controller.current_config_frame].save_asset_info()
            elif self.controller.current_config_frame.__name__ == \
                    "AssetAttributesFrame":
                chk = self.controller.frames[
                    self.controller.current_config_frame
                ].save_asset_attribute_info()
            elif self.controller.current_config_frame.__name__ == \
                    "ComponentFrame":
                chk = self.controller.frames[
                    self.controller.current_config_frame].save_component_info()
                # update the node label if it was "<New Component>"
                if chk == 0:
                    # No issues with save
                    # update the node label if it was "<New Component>"
                    self._on_component_stub_node_exit()
            elif self.controller.current_config_frame.__name__ == \
                    "DimensionFrame":
                chk = self.controller.frames[
                    self.controller.current_config_frame].save_dimension_info()
                if chk == 0:
                    # No issues with save
                    # update the node label if it was "<New Dimension>"
                    self._on_dimension_stub_node_exit()

            elif self.controller.current_config_frame.__name__ == \
                    "AddressFrame":
                self.controller.frames[
                    self.controller.current_config_frame].save_address_info()
            elif self.controller.current_config_frame.__name__ == \
                    "AssetFLAssociationFrame":
                chk = self.controller.frames[
                    self.controller.current_config_frame
                ].save_fl_association_info()
            # was there an issue saving - set selected node back to one we
            # just left
        if chk != 0:
            # change the focus back to the prior node as it did not pass save
            # testing
            self.tv.focus(self.controller.current_asset_tree_node)
            self.tv.selection_set(self.controller.current_asset_tree_node)
        else:
            # remove the current config frame
            self.controller.hide_current_config_frame()

            # Prior frame saved successfully so now load newly selected frame
            self._prepare_newly_selected_node(event)

    def _prepare_newly_selected_node(self, event):

        selected_node = event.widget
        node_id = selected_node.focus()

        self.controller.current_asset_tree_node = node_id
        print("selected node id:", node_id)

        node_parts = node_id.split("_")
        # get the node order id number, so we can get layer from dict
        if len(node_parts) == 1:
            # this is unexpected, all nodes should have minimum 2 parts,
            # just return
            return
        if not node_parts[0]:
            # should not be null
            return
        try:
            # first part should be an integer
            node = int(node_parts[0])
        except ValueError:
            # Didn't find the integer ID which is unexpected
            return

        dimension = None

        # get layer name
        self.controller.selected_layer_name = \
            self.layer_tree_order[node]["layer"]

        existing = False
        for l in self.configured_layers:
            if self.controller.selected_layer_name == l["layer"]:
                existing = True
                break
        if not existing:
            # add dummy layer def because it is new
            self.configured_layers.append(
                {"layer": self.controller.selected_layer_name}
            )

        # get type - e.g. layer, core asset, component etc
        # the type is the second part of the node id
        node_type = node_parts[1]

        # is there a component?
        component = dict()
        c_index = -1
        if len(node_parts) >= 3:
            # yes it is a component or dimension
            # component is 3rd part
            try:
                c_index = int(node_parts[2])
            except ValueError:
                # this shouldn't happen
                return
            component = self.layer_tree_order[node]["components"][c_index]

        # is it a dimension
        d_index = -1
        if len(node_parts) == 5:
            # it is a dimension within the above component
            # component id is the 3rd part, dimension is the 5th
            try:
                d_index = int(node_parts[4])
            except ValueError:
                # this shouldn't happen
                return
            node_type = "dimension"
            if component and "dimensions" in component and \
                    len(component["dimensions"]) >= d_index - 1:
                dimension = component["dimensions"][d_index]

        # now load the frame corresponding to the node type
        if node_type == "layer":
            # load layer frame
            self.load_category_frame()
        elif node_type == "assetcore":
            # load asset core frame
            self.load_asset_core_frame()
        elif node_type == "assetatt":
            # load asset attributes frame
            self.load_asset_attributes_frame()
        elif node_type == "component":
            # if the selected node is <Add Component> then rename
            # as <New Component> and add another node for <Add Component>
            if c_index >= 0:
                self._on_component_stub_entry(
                    component, node_id, node, c_index)
            # now load component frame
            self.controller.current_component = component
            self.load_component_frame(component)
        elif node_type == "dimension":
            # load dimension frame
            if c_index >= 0 and d_index >= 0:
                self._on_dimension_stub_entry(
                    dimension, node_id, node, c_index, d_index)
            self.controller.current_component = component
            self.controller.current_dimension = dimension
            self.load_dimension_frame(component, dimension)
            pass
        elif node_type == "address":
            # load address frame
            self.load_address_frame()
        elif node_type == "flassociation":
            # load functional location association frame
            self.load_fl_association_frame()

    def _on_component_stub_node_exit(self):
        """
        When a tree node is a component and the label is <New Component> and
        the user has just left that node update the node label to the
        component type and name
        :return:
        """
        if self.controller.current_asset_tree_node:
            current_node_text = self.tv.item(
                self.controller.current_asset_tree_node)["text"]
        else:
            return

        if self.controller.current_asset_tree_node:
            # this is the node we have just left.
            # If it is a 'New' component we need to
            # change the label and insert a new dummy node below
            if current_node_text == "<New Component>":
                # Need to update the tree label to reflect set values
                if self.controller.current_component["type"] and \
                        self.controller.current_component["label"]:
                    # change the label to reflect the selection
                    new_node_label = "{0} ({1})".format(
                        self.controller.current_component["type"]
                        , self.controller.current_component["label"]
                    )
                self.tv.item(self.controller.current_asset_tree_node
                             , text=new_node_label)

                # Need to add a 'Add Dimension' stub now we have a component
                node_parts = self.controller.current_asset_tree_node.split("_")
                if len(node_parts) == 3:
                    layer_node = int(node_parts[0])
                    component_index = int(node_parts[2])
                d_index = 0
                new_dim_node = "{0}_component_{1}_dimension_{2}".format(
                    layer_node, component_index, d_index)
                # insert the new node
                self.tv.insert(
                    self.controller.current_asset_tree_node, tk.END
                    , text='<Add Dimension>', iid=new_dim_node, open=False,
                    tags='TkTextFont')
                # add a corresponding def to the layer_tree_order
                dimensions = dict()
                dimensions[0] = {
                    "record_type": None, "network_measure_type": None
                    , "id": d_index}
                self.layer_tree_order[layer_node]["components"][
                    component_index]["dimensions"] = dimensions

                chk = 0

                self.tv.update()

    def _on_dimension_stub_node_exit(self):
        """
        When a tree node is a dimension and the label is <New Dimension> and
        the user has just left that node update the node label to the
        dimension type and name
        :return:
        """
        if self.controller.current_asset_tree_node:
            current_node_text = self.tv.item(
                self.controller.current_asset_tree_node)["text"]
        else:
            return

        if self.controller.current_asset_tree_node:
            # this is the node we have just left.
            # If it is a 'New' component we need to
            # change the label and insert a new dummy node below
            if current_node_text == "<New Dimension>":
                # Need to update the tree label to reflect set values
                if self.controller.current_dimension["record_type"] and \
                        self.controller.current_dimension[
                            "network_measure_type"]:
                    new_node_label = "{0} ({1})".format(
                        self.controller.current_dimension["record_type"]
                        , self.controller.current_dimension[
                            "network_measure_type"])

                    self.tv.item(self.controller.current_asset_tree_node
                                 , text=new_node_label)
                    self.tv.update()

    def _on_component_stub_entry(self, component, node_id, layer_node, c_index):
        """
        When a component tree node is entered, if it is '<Add Component>' then
        relabel it as '<New Component>' and create a
        new tree node '<Add Component>'
        :param component: the component object held against the tree node
        :param node_id: the string identifier of the node
        :param layer_node: the integer id of the layer
        :param c_index: the component index -  each component is recorded
        with an incrementing integer value to help identify iy
        """
        node_text = self.tv.item(node_id)["text"]

        if not component["type"] and not component["label"] and \
                node_text == "<Add Component>":
            # this is a stub for a new component
            # rename stub
            self.tv.item(node_id, text="<New Component>")
            # tree.update()
            # Add new stub to tree for another 'add'
            new_node = "{0}_component_{1}".format(layer_node, c_index + 1)
            parent = "{0}_components".format(layer_node)
            self.tv.insert(parent, tk.END, text='<Add Component>'
                           , iid=new_node, open=False, tags='TkTextFont')
            self.layer_tree_order[layer_node]["components"][c_index + 1] = {
                "type": None, "label": None, node_id: c_index + 1
            }
            self.tv.update()

    def _on_dimension_stub_entry(
            self, dimension, node_id, layer_node, component_index, d_index):
        """
        When a dimension tree node is entered, if it is '<Add Dimension>' then
        relabel it as '<New Dimension>' and create a
        new tree node '<Add Dimension>'
        :param dimension: the dimension object held against the tree node
        :param node_id: the string identifier of the node
        :param layer_node: the integer id of the layer
        :param component_index: the component index -  each component is
        recorded with an incrementing integer value to help identify it
        :param d_index: the dimension index
        """
        node_text = self.tv.item(node_id)["text"]

        if not dimension["record_type"] and \
                not dimension["network_measure_type"] and \
                node_text == "<Add Dimension>":
            # this is a stub for a new dimension
            # rename stub
            self.tv.item(node_id, text="<New Dimension>")

            new_node = "{0}_component_{1}_dimension_{2}".format(
                layer_node, component_index, d_index + 1)
            parent = "{0}_component_{1}".format(layer_node, component_index)
            self.tv.insert(parent, tk.END, text='<Add Dimension>'
                           , iid=new_node, open=False, tags='TkTextFont')
            self.layer_tree_order[layer_node]["components"][component_index] \
                ["dimensions"][d_index + 1] = {
                "record_type": None, "network_measure_type": None
                , "shape_name": None
                , "id": d_index + 1}
            self.tv.update()

    def build_assets_tree(self, tv, layer_option):
        """
        Populate the treeview with asset structure
        This is populated when the operation frame is set to 'Asset'
        :param tv: treeview widget
        :param layer_option: list of layers from gis
        :return:
        """
        cnt = 0
        # Iterate over each GIS layer and add a layernode and sub nodes
        for layer in layer_option:
            # record layer name in a dict where the id is the id we will
            # attach to node id
            layer_def = dict()
            layer_def["layer"] = layer

            # create a basic def in case one not already in XML
            current_layer_config = layer_def
            # Get the current xml config for the layer.
            for conf_layer in self.configured_layers:
                if layer == conf_layer["layer"]:
                    current_layer_config = conf_layer
                    break

            # Add the layer node
            l_node = "{0}_layer".format(cnt)
            tv.insert('', tk.END, text=layer, iid=l_node, open=False
                      , tags='TkTextFont')

            # Add the core assets node
            node = "{0}_assetcore".format(cnt)
            tv.insert(l_node, tk.END, text='Asset Core', iid=node, open=False
                      , tags='TkTextFont')

            # Add the Asset attributes node
            node = "{0}_assetatt".format(cnt)
            tv.insert(l_node, tk.END, text='Asset Attributes', iid=node,
                      open=False
                      , tags='TkTextFont')

            # Add the component parent node (will have 1 more children
            c_node = "{0}_components".format(cnt)
            tv.insert(l_node, tk.END, text='Components', iid=c_node, open=False
                      , tags='TkTextFont')

            # Add the nodes for the components, plus a node to support adding
            # another component config called '<Add Component>'
            components_def = dict()
            compid = 0
            if current_layer_config:
                config_comps = self.get_configured_components(
                    current_layer_config)
            else:
                config_comps = list()
            for comp_def in config_comps:
                # create unique node id
                node = "{0}_component_{1}".format(cnt, compid)
                comp_lbl = "{0} ({1})".format(
                    comp_def["label"], comp_def["type"])
                tv.insert(c_node, tk.END, text=comp_lbl, iid=node,
                          open=False, tags='TkTextFont')
                # record node id with type and name so we can get it later if
                # node is clicked
                comp_def["node_id"] = compid

                # Add dimensions
                dim_id = 0
                dimensions_def = dict()
                for dimension in comp_def["dimensions"]:
                    # create unique node id
                    d_node = "{0}_component_{1}_dimension_{2}".format(
                        cnt, compid, dim_id)
                    if "shape_name" in dimension:
                        tree_text = "{0} ({1} - {2})".format(
                            dimension["record_type"]
                            , dimension["network_measure_type"]
                            , dimension["shape_name"]
                        )
                    else:
                        tree_text = "{0} ({1})".format(
                            dimension["record_type"]
                            , dimension["network_measure_type"]
                        )
                    tv.insert(node, tk.END, text=tree_text,
                              iid=d_node, open=False, tags='TkTextFont')
                    # record node id with type and name so we can get it
                    # later if node is clicked
                    dimension["id"] = dim_id
                    dimensions_def[dim_id] = dimension
                    dim_id += 1

                # Add a default node to allow a new dimension to be created
                dimension = dict()
                dimension["record_type"] = None
                dimension["network_measure_type"] = None
                dimension["shape_name"] = None
                dimension["id"] = dim_id
                dimensions_def[dim_id] = dimension
                d_node = "{0}_component_{1}_dimension_{2}".format(
                    cnt, compid, dim_id)
                tv.insert(node, tk.END, text='<Add Dimension>', iid=d_node,
                          open=False, tags='TkTextFont')

                # add the dimensions to the component dict
                comp_def["dimensions"] = dimensions_def
                components_def[compid] = comp_def
                compid += 1

            # Now add a default node to allow a new node to be created
            comp_def = dict()
            comp_def["type"] = None
            comp_def["label"] = None
            comp_def["node_id"] = compid
            components_def[compid] = comp_def
            current_layer_config["components"] = components_def
            node = "{0}_component_{1}".format(cnt, compid)
            tv.insert(c_node, tk.END, text='<Add Component>', iid=node,
                      open=False, tags='TkTextFont')

            # Add Address node
            node = "{0}_address".format(cnt)
            tv.insert(l_node, tk.END, text='Address', iid=node, open=False
                      , tags='TkTextFont')

            # Add FL Association Node
            node = "{0}_flassociation".format(cnt)
            tv.insert(l_node, tk.END, text='Functional Location', iid=node,
                      open=False, tags='TkTextFont')

            if current_layer_config:
                # there is a layer definition already
                self.layer_tree_order[cnt] = current_layer_config

            cnt += 1

    def load_category_frame(self):
        all_config = self.controller.get_existing_xml()
        self.existing_layer = all_config.assetconfig

        self.controller.refresh_frame(CategoryFrame)
        self.controller.current_config_frame = CategoryFrame

    def load_asset_core_frame(self):
        all_config = self.controller.get_existing_xml()
        self.existing_layer = all_config.assetconfig

        self.controller.refresh_frame(AssetCoreFrame)
        self.controller.current_config_frame = AssetCoreFrame

    def load_asset_attributes_frame(self):
        all_config = self.controller.get_existing_xml()
        self.existing_layer = all_config.assetconfig

        self.controller.refresh_frame(AssetAttributesFrame)
        self.controller.current_config_frame = AssetAttributesFrame

    def load_component_frame(self, component):
        all_config = self.controller.get_existing_xml()
        self.existing_layer = all_config.assetconfig

        self.controller.refresh_frame(ComponentFrame)
        self.controller.current_config_frame = ComponentFrame
        self.controller.current_component = component

    def load_dimension_frame(self, component, dimension):
        all_config = self.controller.get_existing_xml()
        self.existing_layer = all_config.assetconfig

        self.controller.refresh_frame(DimensionFrame)
        self.controller.current_config_frame = DimensionFrame
        self.controller.current_component = component
        self.controller.current_dimension = dimension

    def load_address_frame(self):
        all_config = self.controller.get_existing_xml()
        self.existing_layer = all_config.assetconfig

        self.controller.refresh_frame(AddressFrame)
        self.controller.current_config_frame = AddressFrame

    def load_fl_association_frame(self):
        all_config = self.controller.get_existing_xml()
        self.existing_layer = all_config.assetconfig

        self.controller.refresh_frame(AssetFLAssociationFrame)
        self.controller.current_config_frame = AssetFLAssociationFrame

    def get_configured_components(self, config):
        """
        Get the components configured in the XML for the layer
        :param config: the xml config dict for the layer
        :type config: dict
        :return: list of dicts where each dict has key component identifiers
        :rtype: list
        """
        component_key_list = list()
        if 'components' not in config or len(config["components"]) == 0:
            return component_key_list
        for component in config["components"]:
            if not isinstance(component, dict):
                continue
            component_keys = dict()
            label = None
            type = None
            if "attributes" in component:
                if "label" in component["attributes"]:
                    label = component["attributes"]["label"]
                if "component_type" in component["attributes"]:
                    type = component["attributes"]["component_type"]
            if "defaults" in component:
                if "label" in component["defaults"]:
                    label = component["defaults"]["label"]
                if "component_type" in component["defaults"]:
                    type = component["defaults"]["component_type"]
            if label and type:
                component_keys["label"] = label
                component_keys["type"] = type
                dimensions_list = self.get_configured_dimensions(component)
                component_keys["dimensions"] = dimensions_list
                component_key_list.append(component_keys)

        return component_key_list

    def get_configured_dimensions(self, component):
        """
        For the given component get the dimensions in the xml config
        :param component: component dict from xml config
        :return: list of dicts where each dict has key dimension identifiers
        """
        dimensions_list = list()
        for dimension in component["dimensions"]:
            record_type = None
            nm_type = None
            dimension_keys = dict()

            if "record_type" in dimension["defaults"]:
                record_type = dimension["defaults"]["record_type"]
            elif "record_type" in dimension["attributes"]:
                record_type = dimension["attributes"]["record_type"]
            if not record_type:
                continue
            if "network_measure_type" in dimension["defaults"]:
                nm_type = dimension["defaults"]["network_measure_type"]
            elif "network_measure_type" in dimension["attributes"]:
                nm_type = dimension["attributes"][
                    "network_measure_type"]
            if not nm_type:
                continue

            dimension_keys["record_type"] = record_type
            dimension_keys["network_measure_type"] = nm_type
            dimensions_list.append(dimension_keys.copy())
        return dimensions_list


class FLTreeViewFrame(tk.Frame):
    """
    This class sets up the tree hierarchy navigator for functional location
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.existing_layer = None
        self.controller = controller

        self.logger = logging.getLogger("Assetic")

        font_normal = controller.font_normal
        font_header = controller.font_header
        font_strike = controller.font_strike

        self.configured_layers = controller.get_asset_config_dict()

        if controller.layer_dict is None:
            message = "No layer found from the file"
            self.logger.error(message)
            return
        # get a list of layer names for the combobox and insert an empty row
        # so that no layer is selected when initialising the form
        layer_option = sorted(controller.layer_dict.keys()
                              , key=lambda x: x.lower())
        self.selected_layer = tk.StringVar()

        self.layer_tree_order = dict()

        fltv = ttk.Treeview(self, show='tree')
        self.fltv = fltv
        fltv.tag_configure('TkTextFont', font=font_normal)
        fltv["columns"] = ("layer", "functional_location", 'level3', 'level4')
        fltv.column("layer", width=20)
        fltv.column("functional_location", width=20)
        fltv.column("level3", width=20)
        fltv.column("level4", width=20)
        fltv.heading("layer", text="layer")
        fltv.heading("functional_location", text="functional_location")
        fltv.heading("level3", text="level3")
        fltv.heading("level4", text="level4")

        self.build_fl_tree(fltv, layer_option)

        fl_tvscroll = ttk.Scrollbar(self)
        fl_tvscroll.configure(command=fltv.yview)
        fltv.configure(yscrollcommand=fl_tvscroll.set)
        fl_tvscroll.pack(side="right", fill="both")

        fltv.pack(expand=True, fill='both')

    def refresh(self, parent, controller):
        self.destroy()
        self.__init__(parent, controller)

    def build_fl_tree(self, fl_tv, layer_option):
        """
        Populate the treeview with asset structure
        This is populated when the operation frame is set to 'Asset'
        :param fl_tv: treeview widget
        :param layer_option: list of layers from gis
        :return:
        """
        cnt = 0
        # Iterate over each GIS layer and add a layernode and sub nodes
        for layer in layer_option:
            # record layer name in a dict where the id is the id we will
            # attach to node id
            layer_def = dict()
            layer_def["layer"] = layer

            # Get the current xml config for the layer.
            current_layer_config = None
            for layer_def in self.configured_layers:
                if layer == layer_def["layer"]:
                    current_layer_config = layer_def
                    break

            # Add the layer node
            l_node = "{0}_fllayer".format(cnt)
            fl_tv.insert('', tk.END, text=layer, iid=l_node, open=False
                         , tags='TkTextFont')

            # Add the core assets node
            node = "{0}_flcore".format(cnt)
            fl_tv.insert(l_node, tk.END, text='Functional Location Core',
                         iid=node, open=False
                         , tags='TkTextFont')

            cnt += 1


class EmptyTreeViewFrame(tk.Frame):
    """
    This class sets up the tree hierarchy navigator for functional location
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.existing_layer = None
        self.controller = controller

        self.logger = logging.getLogger("Assetic")

        font_normal = controller.font_normal
        font_header = controller.font_header
        font_strike = controller.font_strike

        emptytv = ttk.Treeview(self, show='tree')
        self.emptytv = emptytv
        emptytv.tag_configure('TkTextFont', font=font_normal)
        emptytv["columns"] = ("level1", "level2", 'level3', 'level4')
        emptytv.column("level1", width=20)
        emptytv.column("level2", width=20)
        emptytv.column("level3", width=20)
        emptytv.column("level4", width=20)
        emptytv.heading("level1", text="level1")
        emptytv.heading("level2", text="level2")
        emptytv.heading("level3", text="level3")
        emptytv.heading("level4", text="level4")

        emptytv.pack(expand=True, fill='both')

    def refresh(self, parent, controller):
        self.destroy()
        self.__init__(parent, controller)


class OperationChooserFrame(tk.Frame):
    """
    Setup the frame that has a combobox list of the operations to be
    configured - eg Asset config, functional location config, basic settings
    Changing the option will change the treeview contents
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.existing_layer = None
        self.existing_fl = None
        self.controller = controller
        self.configure(bg="#349cbc")
        self.logger = logging.getLogger("Assetic")

        font_normal = controller.font_normal
        font_header = controller.font_header
        font_strike = controller.font_strike
        coloured_bg = controller.coloured_bg

        self.selected_operation = tk.StringVar()

        operation_option = ["Settings", "Asset Layers"
            , "Functional Location Layers"]
        Label(self, text="Configure: "
              , bg=coloured_bg, fg='gray92', font=font_normal).grid(
            row=0, column=0)

        self.cmb_operation = ttk.Combobox(
            self, values=operation_option, width=40, state='readonly'
            , textvariable=self.selected_operation, font=font_normal
        )
        self.but_save = Button(
            self, text="Save", command=self.but_save_selected
            , font=font_normal)
        self.but_delete = Button(
            self, text="Delete", command=self.but_delete_selected
            , font=font_normal)
        self.cmb_operation.current(0)
        self.cmb_operation.grid(row=0, column=1)
        self.but_save.grid(row=0, column=2, padx=5)
        self.but_delete.grid(row=0, column=3, padx=5)

        self.cmb_operation.bind(
            '<<ComboboxSelected>>', self.cmb_operation_changed)

    def cmb_operation_changed(self, event):
        """
        handle the combobox layer changed event
        save changes to current frame
        and then prepare new treeview based on selection
        """

        # First save config of current frame
        if self.controller.current_tree_frame.__name__ == "EmptyTreeViewFrame":
            chk = self.controller.save_settings_info()
            if not chk:
                # there was an issue, stay on page
                self.controller.show_frame(SettingsFrame)
                return
        elif self.controller.current_tree_frame.__name__ == \
                "AssetTreeViewFrame":
            chk = self.controller.save_current_asset_frame()
            if not chk:
                # there was an issue, stay on page
                self.selected_operation.set("Asset Layers")
                return
        elif self.controller.current_tree_frame.__name__ == \
                "FLTreeViewFrame":
            # TODO
            pass

        # Hide existing tree frame
        self.controller.hide_tree_frame(AssetTreeViewFrame)
        self.controller.hide_tree_frame(FLTreeViewFrame)

        # Hide current config frame
        self.controller.hide_frame(self.controller.current_config_frame)

        # build tree

        print('Selected operation is {0}'.format(self.selected_operation.get()))
        new_operation = self.selected_operation.get()
        if new_operation == "Settings":
            self.load_empty_tree_frame()
            # not need empty tree frame
            self.controller.hide_tree_frame(EmptyTreeViewFrame)
            self.controller.show_frame(SettingsFrame)
            self.controller.refresh_frame(SettingsFrame)
            self.controller.current_config_frame = SettingsFrame
        elif new_operation == "Asset Layers":
            self.load_asset_tree_frame()
        elif new_operation == "Functional Location Layers":
            self.load_fl_tree_frame()

    def but_save_selected(self):
        """
        Save the current frame
        """
        c = self.controller
        if c.current_tree_frame.__name__ == "AssetTreeViewFrame":
            chk = c.save_current_asset_frame()

            # The component and dimension labels are based on their config so
            # need to refresh the label.  Also need to add a new stub for the
            # component/dimension
            if c.current_config_frame.__name__ == "ComponentFrame":
                c.asset_treeview_instance._on_component_stub_node_exit()
            elif c.current_config_frame.__name__ == "DimensionFrame":
                c.asset_treeview_instance._on_dimension_stub_node_exit()

            if chk and chk == 0:
                messagebox.showinfo('Info', 'Successfully Saved')
        elif c.current_tree_frame.__name__ == "EmptyTreeViewFrame":
            chk = self.controller.save_settings_info()
            if not chk:
                # there was an issue, stay on page
                self.controller.show_frame(SettingsFrame)
                return

    def but_delete_selected(self):
        """
        Delete the record in the current frame
        """
        c = self.controller

        chk = messagebox.askokcancel(
            'Confirm Delete', 'Delete currently viewed setting?')
        if not chk:
            # user selected cancel
            return

        if c.current_tree_frame.__name__ == "AssetTreeViewFrame":
            # remove record from xml
            chk = c.save_current_asset_frame(delete=True)
            self.controller.hide_tree_frame(AssetTreeViewFrame)
            self.controller.hide_current_config_frame()
            self.load_asset_tree_frame()

    def load_empty_tree_frame(self):
        all_config = self.controller.get_existing_xml()
        self.existing_layer = None
        self.existing_fl = None

        self.controller.refresh_tree_frame(EmptyTreeViewFrame)
        self.controller.current_tree_frame = EmptyTreeViewFrame

    def load_asset_tree_frame(self):
        all_config = self.controller.get_existing_xml()
        self.existing_layer = all_config.assetconfig
        self.existing_fl = None

        self.controller.refresh_tree_frame(AssetTreeViewFrame)
        self.controller.current_tree_frame = AssetTreeViewFrame

    def load_fl_tree_frame(self):
        all_config = self.controller.get_existing_xml()
        self.existing_layer = None
        self.existing_fl = all_config.fl_layerconfig

        self.controller.refresh_tree_frame(FLTreeViewFrame)
        self.controller.current_tree_frame = FLTreeViewFrame


class SettingsFrame(tk.Frame):

    def __init__(self, parent, controller, use_existing_file=True):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.delete_label = {}
        self.use_existing_file = use_existing_file
        self.l_button = {}
        self.delete_button = {}
        self.configuration = controller.get_existing_xml()
        self.extra_fields = 14
        self.current_layer = None
        self.form_loaded = False
        self.save_path = self.controller.common_tools.config_file_path

        font_normal = controller.font_normal
        font_header = controller.font_header
        font_strike = controller.font_strike
        coloured_bg = controller.coloured_bg

        self.var_log_file = StringVar()
        tk.Label(self, text="General Settings: "
                 , font=font_header).grid(
            row=0, column=0, columnspan=2, sticky=EW)

        # other configs
        log_level_list = ["", "Info", "Debug", "Error", "Warning"]

        # Prepare the form widgets
        wid = 40
        extra_wid = 100
        # Add labels for each core field, first column

        # Log file
        Label(self, text="Log File", font=font_normal).grid(
            row=1, column=0, sticky=W)
        if self.configuration.logfile:
            self.var_log_file.set(self.configuration.logfile)
        self.log_file_field = ttk.Entry(
            self, width=extra_wid, justify=LEFT
            , textvariable=self.var_log_file, font=font_normal
        )
        self.butlogfilechooser = ttk.Button(
            self, text="...", command=self.select_log_file)

        # Log Level
        Label(self, text="Log Level", font=font_normal).grid(
            row=2, column=0, sticky=W)
        if self.configuration.logfile:
            self.var_log_file.set(self.configuration.logfile)
        self.cmb_log_level = ttk.Combobox(
            self, values=log_level_list, width=wid, font=font_normal)

        # set log level
        xml_log_level = self.configuration.loglevel
        if xml_log_level and xml_log_level.strip() != "" and \
                xml_log_level.title() in log_level_list:
            self.cmb_log_level.current(log_level_list.index(
                xml_log_level.title()))

        # position the fields - need to do this after setting 'current'
        self.log_file_field.grid(row=1, column=1, sticky=W)
        self.butlogfilechooser.grid(row=1, column=2, sticky=W)
        self.cmb_log_level.grid(row=2, column=1, sticky=W)

        # indicate the form was built (used by save method)
        self.form_loaded = True

    def refresh(self, parent, controller, use_existing_file=True):
        self.destroy()
        self.__init__(parent, controller, use_existing_file)

    def save_settings_config(self):
        # save first - perhaps better to have a save button?
        if not self.form_loaded:
            return True

        chk = self.save_setting_to_xml_file()
        # after save refresh xml
        self.controller.configured_layers = self.controller.get_existing_xml()
        return chk

    def select_log_file(self):
        """
        Save As prompter to choose log file name and location
        :return: selected filename via variable
        """
        filetypes = (('Log Files', '*.log'),)
        title = 'Save As'
        assetic_folder = os.environ['APPDATA'] + '\\Assetic'
        filename = fd.asksaveasfilename(
            filetypes=filetypes, title=title, initialdir=assetic_folder
            , initialfile='gis_integration.log')
        self.var_log_file.set(filename)

    def save_setting_to_xml_file(self):
        """
        Save the settings (log level, log file etc)to the XML file
        :return: 0 if success, else error
        """

        if os.path.isfile(self.controller.common_tools.config_file_path):
            tree = ET.parse(self.save_path)
        else:
            messagebox.showerror("Error", "No arcmap_edit_config.xml is found")
            return False
        root = tree.getroot()

        # log file
        log_file_node = root.find("logfile")
        if log_file_node == None:
            log_file_node = ET.SubElement(root, "logfile")
        if self.log_file_field.get().strip():
            log_file_node.text = self.log_file_field.get()

        # log level
        log_level_node = root.find("loglevel")
        if log_level_node == None:
            log_level_node = ET.SubElement(root, "loglevel")
        if self.cmb_log_level.get().strip():
            log_level_node.text = self.cmb_log_level.get()

        dom = xml.dom.minidom.parseString(ET.tostring(root))
        xmlstring = dom.toprettyxml(encoding='UTF-8')
        dom_string = b'\n'.join(
            [s for s in xmlstring.splitlines() if s.strip()])
        with open(self.save_path, 'wb') as file:
            file.write(dom_string)
            file.close()
        return True


class CategoryFrame(tk.Frame):

    def __init__(self, parent, controller, use_existing_file=True):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.delete_label = {}
        self.use_existing_file = use_existing_file
        self.l_button = {}
        self.delete_button = {}
        self.configuration = controller.get_existing_xml()
        self.configured_layers = self.configuration.assetconfig
        self.extra_fields = 14
        self.current_layer = None
        self.form_loaded = False
        self.save_path = self.controller.common_tools.config_file_path

        font_normal = controller.font_normal
        font_header = controller.font_header
        font_strike = controller.font_strike

        self.var_upload_spatial = IntVar(value=0)
        self.var_resolve_lookups = IntVar(value=0)

        tk.Label(self, text="Asset Category Configuration"
                 , font=font_header).grid(
            row=0, column=0, columnspan=2, sticky=EW)

        selected_layer = controller.selected_layer_name
        if not selected_layer or selected_layer.strip() == "":
            # No layer is selected so don't populate anything more
            # returning after creating label above so that a form exists
            return

        # Get the current xml config for the layer.
        for config in self.configured_layers:
            if selected_layer == config["layer"]:
                self.current_layer = config
                break

        # Getting the labels from Assetic APIs may take some time
        category_label = controller.assetic_api_tools.asset_category_list
        # Got configs from Assetic APIs
        # category_label = ["Buildings", "Roads"]

        # other configs
        status_list = ["Active", "Proposed", "Notional Asset"]

        # Prepare the form widgets
        wid = 40
        # set the label justification 'sticky' - N, S, E, W
        st = tk.E

        # Add labels for each core field, first column
        # Category
        Label(self, text="Category*").grid(row=1, column=0, sticky=st)
        self.category_field = ttk.Combobox(
            self, values=category_label, width=wid)

        # Asset Status on Creation
        Label(self, text="Status").grid(row=2, column=0, sticky=st)
        self.status_field = ttk.Combobox(
            self, values=status_list, width=wid)

        # Asset Spatial Upload
        Label(self, text="Upload Spatial").grid(row=3, column=0, sticky=st)
        self.upload_spatial_chk = ttk.Checkbutton(
            self, variable=self.var_upload_spatial, onvalue=1, offvalue=0)

        # Resolve lookups (ESRI)
        self.lbl_resolve_lookup = Label(self, text="Resolve Lookups")
        self.lbl_resolve_lookup.grid(row=4, column=0, sticky=st)
        self.resolve_lookups_chk = ttk.Checkbutton(
            self, variable=self.var_resolve_lookups, onvalue=1, offvalue=0)

        if self.current_layer and "asset_category" in self.current_layer \
                and self.current_layer["asset_category"] in category_label:
            # layer currently configured so populate widgets
            self.category_field.current(category_label.index(
                self.current_layer["asset_category"]))

        if self.current_layer and "creation_status" in self.current_layer \
                and self.current_layer["creation_status"] in status_list:
            # layer currently configured so populate widgets
            self.status_field.current(status_list.index(
                self.current_layer["creation_status"]))

        self.var_upload_spatial.set(0)
        self.upload_spatial_chk.state(['!alternate'])
        if self.current_layer and "upload_feature" in self.current_layer:
            # layer currently configured so populate widgets
            if self.current_layer["upload_feature"] == True:
                self.var_upload_spatial.set(1)
                self.upload_spatial_chk.state(['selected'])

        self.var_resolve_lookups.set(0)
        self.resolve_lookups_chk.state(['!alternate'])
        if self.current_layer and "resolve_lookups" in self.current_layer:
            # layer currently configured so populate widgets
            if self.current_layer["resolve_lookups"] == True:
                self.var_resolve_lookups.set(1)
                self.resolve_lookups_chk.state(['selected'])

        # position the combobox fields - need to do this after setting 'current'
        self.category_field.grid(row=1, column=1)
        self.status_field.grid(row=2, column=1)
        self.upload_spatial_chk.grid(row=3, column=1)
        self.resolve_lookups_chk.grid(row=4, column=1)

        if self.controller.gis != TargetGis.ESRI:
            # hide the ESRI specific fields
            self.lbl_resolve_lookup.grid_remove()
            self.resolve_lookups_chk.grid_remove()

        # indicate the form was built (used by save method)
        self.form_loaded = True

    def refresh(self, parent, controller, use_existing_file=True):
        self.destroy()
        self.__init__(parent, controller, use_existing_file)

    def save_layer_category_config(self):

        if not self.form_loaded:
            return

        if not self.current_layer:
            # layer not in XML yet, so create dict with values
            self.current_layer = dict()
            self.current_layer["layer"] = self.controller.selected_layer_name
            self.current_layer["category"] = self.category_field.get()
        # self.controller.save_layer_info(
        #    curr_layer=self.current_layer
        #    , layer_name=self.controller.selected_layer_name)
        self.add_layer_to_xml_file()

        # after save refresh xml
        self.controller.configured_layers = self.controller.get_existing_xml()

    def add_layer_to_xml_file(self, delete=0):
        """
        Save the layer-category config for the current layer to the XML file
        :param delete: optionally delete the current layer
        :return:
        """

        if os.path.isfile(self.controller.common_tools.config_file_path):
            tree = ET.parse(self.save_path)
        else:
            messagebox.showerror("Error", "No arcmap_edit_config.xml is found")
            return
        root = tree.getroot()

        for operation in root.iter('operation'):
            action = operation.get("action")
            if action == "Asset":
                # create a reference for the layer config
                onelayer = None

                for layer in operation.iter("layer"):
                    if layer.get("name") == self.current_layer["layer"]:
                        onelayer = layer
                        break
                if not onelayer:
                    # layer currently doesn't exist, add a layer element
                    onelayer = ET.SubElement(operation, "layer")
                    onelayer.set("name", self.current_layer["layer"])

                # category = onelayer.find('category')
                category = onelayer.find('category')
                if category is None:
                    category = ET.SubElement(onelayer, "category")
                category.text = self.category_field.get()

                # Creation status
                if self.status_field.get():
                    status = onelayer.find("creation_status")
                    if status is None:
                        status = ET.SubElement(
                            onelayer, "creation_status")
                        status.text = self.status_field.get()

                # Flag to upload spatial
                if self.var_upload_spatial:
                    upload_spatial = onelayer.find("upload_feature")
                    if upload_spatial is None:
                        upload_spatial = ET.SubElement(
                            onelayer, "upload_feature")
                    if self.var_upload_spatial.get() == 1:
                        upload_spatial.text = "True"
                    else:
                        upload_spatial.text = "False"

                # Resolve lookups if ESRI
                if self.var_resolve_lookups and \
                        self.controller.gis == TargetGis.ESRI:
                    resolve_lookups = onelayer.find("resolve_lookups")
                    if resolve_lookups is None:
                        resolve_lookups = ET.SubElement(
                            onelayer, "resolve_lookups")
                    if self.var_resolve_lookups.get() == 1:
                        resolve_lookups.text = "True"
                    else:
                        resolve_lookups.text = "False"

        dom = xml.dom.minidom.parseString(ET.tostring(root))
        xmlstring = dom.toprettyxml(encoding='UTF-8')
        dom_string = b'\n'.join(
            [s for s in xmlstring.splitlines() if s.strip()])
        with open(self.save_path, 'wb') as file:
            file.write(dom_string)
            file.close()


class AssetCoreFrame(tk.Frame):
    def __init__(self, parent, controller, use_existing_file=True):
        """
        Asset Core Attributes configuration page
        :param parent: The main window
        :type parent:
        :param controller: class from main window with common functions and
        variables
        :type controller:
        :param use_existing_file: read existing xml or create a new one?
        :type use_existing_file: boolean
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.delete_label = {}
        self.use_existing_file = use_existing_file
        self.l_button = {}
        self.delete_button = {}
        self.configuration = controller.get_existing_xml()
        self.configured_layers = self.configuration.assetconfig
        self.layer_dict = controller.layer_dict

        self.asset_sub_class_list = list()
        self.asset_sub_type_list = list()
        self.maint_sub_type_list = list()
        self.fin_sub_class_list = list()

        api_client = ApiClient()
        self.api_client = api_client
        self.asset_buttons = {}
        self.current_layer = None
        self.logger = api_client.configuration.packagelogger
        self.host = self.api_client.configuration.host

        self.save_path = self.controller.common_tools.config_file_path

        # These fields set by validator, used when saving config
        self.xml_asset_ID = None
        self.xml_asset_GUID_core_field = None
        self.xml_asset_name_core_field = None
        self.xml_asset_name_core_default = None
        self.xml_asset_class_field = None
        self.xml_asset_subclass_field = None
        self.xml_asset_class_field_default = None
        self.xml_asset_subclass_field_default = None
        self.xml_asset_type_field = None
        self.xml_asset_subtype_field = None
        self.xml_asset_type_field_default = None
        self.xml_asset_subtype_field_default = None
        self.xml_maint_type_field = None
        self.xml_maint_subtype_field = None
        self.xml_maint_type_field_default = None
        self.xml_maint_subtype_field_default = None

        font_normal = controller.font_normal
        font_header = controller.font_header
        font_strike = controller.font_strike

        # set padding between rows and columns
        xp = 1
        yp = 1
        # set the label justification 'sticky' - N, S, E, W
        st = tk.E

        tk.Label(self, text="Asset Attribute Configuration"
                 , font=font_header).grid(row=0, column=0, columnspan=2,
                                          sticky=EW)

        selected_layer = controller.selected_layer_name
        if not selected_layer or selected_layer.strip() == "":
            # No layer is selected so don't populate anything more
            # returning after creating label above so that a form exists
            return

        # Get the current xml config for the layer.  If there is none the
        # exit without building form further
        # User needs to first assign category and higher level config
        for config in self.configured_layers:
            if selected_layer == config["layer"]:
                self.current_layer = config
                break
        if not self.current_layer:
            self.config(cursor="")
            messagebox.showerror(
                "Error",
                "Assign Asset Category before setting Asset Attributes")
            return
        if "asset_category" not in self.current_layer or \
                not self.current_layer["asset_category"]:
            self.config(cursor="")
            messagebox.showerror(
                "Error",
                "Assign Asset Category before setting Asset Attributes")
            return
        category = self.current_layer["asset_category"]

        # local variable just to keep the name a bit shorter
        current_layer = self.current_layer

        # set wait cursor as initial load can take time to read Assetic APIs
        self.config(cursor="wait")
        self.update()

        # Getting the labels from Assetic APIs may take some time
        self.asset_class_labels = controller.assetic_api_tools.asset_class_list
        self.asset_type_labels = controller.assetic_api_tools.asset_type_list
        self.maint_type_labels = controller.assetic_api_tools.maint_type_list
        self.criticality_labels = controller.assetic_api_tools. \
            get_criticality_list_for_category(category)
        self.workgroup_labels = controller.assetic_api_tools.workgroup_list
        # Got labels from Assetic

        # Add grid headers
        Label(self, text="GIS Field").grid(row=2, column=1, padx=xp, pady=yp)
        Label(self, text="Hardcode Value").grid(
            row=2, column=2, padx=xp, pady=yp)

        # Add labels for each core field, first column
        Label(self, text="Asset ID*").grid(
            row=3, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Asset Name*").grid(
            row=4, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Asset GUID").grid(
            row=5, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Asset Class").grid(
            row=6, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Asset SubClass").grid(
            row=7, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Asset Type").grid(
            row=8, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Asset SubType").grid(
            row=9, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Maintenance Type").grid(
            row=10, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Maintenance SubType").grid(
            row=11, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Criticality").grid(
            row=12, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Work Group").grid(
            row=13, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Security Group").grid(
            row=14, column=0, padx=xp, pady=yp, sticky=st)
        self.layer_fields = list()
        if selected_layer in self.layer_dict:
            self.layer_fields = sorted(self.layer_dict[selected_layer]
                                       , key=lambda x: x.lower())
        self.layer_fields.insert(0, " ")

        # set width
        wid = 40

        # First create the comboboxes with GIS field list
        self.asset_id_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.asset_name_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.asset_guid_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.asset_class_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.asset_sub_class_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.asset_type_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.asset_sub_type_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.maint_type_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.maint_sub_type_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.criticality_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.workgroup_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.securitygroup_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        # Now the widgets for defaults
        try:
            value = current_layer["coredefaults"]["asset_name"]
        except KeyError:
            value = None
        self.asset_name_default = Entry(
            self
            , textvariable=StringVar(
                self, value=value)
            , width=wid, justify=LEFT)

        # asset class is a lookup from Assetic REST API
        self.asset_class_default = ttk.Combobox(
            self, values=self.asset_class_labels, width=wid)
        self.asset_class_default.bind(
            "<<ComboboxSelected>>", self.asset_subclass_fields__)

        # asset subclass list depends on asset class selected
        self.asset_sub_class_default = ttk.Combobox(self, values=[], width=wid)

        # asset type is a lookup from Assetic REST API
        self.asset_type_default = ttk.Combobox(
            self, values=self.asset_type_labels, width=wid)
        self.asset_type_default.bind(
            "<<ComboboxSelected>>", self.asset_subtype_fields__)
        # asset subtype list depends on asset type selected
        self.asset_sub_type_default = ttk.Combobox(self, values=[], width=wid)

        # maint type is a lookup from Assetic REST API
        self.maint_type_default = ttk.Combobox(
            self, values=self.maint_type_labels, width=wid)
        self.maint_type_default.bind(
            "<<ComboboxSelected>>", self.maint_subtype_fields__)
        # maint subtype list depends on asset type selected
        self.maint_sub_type_default = ttk.Combobox(self, values=[], width=wid)

        # asset criticality default
        self.criticality_default = ttk.Combobox(
            self, values=self.criticality_labels, width=wid)
        # asset work group
        self.workgroup_default = ttk.Combobox(
            self, values=self.workgroup_labels, width=wid)
        # asset security group default - no API for getting the list
        self.securitygroup_default = Entry(self, width=wid + 3)

        # populate the fields from the xml config
        self.apply_current_config(current_layer)

        # position fields in grid
        self.asset_id_field.grid(row=3, column=1, padx=xp, pady=yp)

        self.asset_name_field.grid(row=4, column=1, padx=xp, pady=yp)
        self.asset_name_default.grid(row=4, column=2, padx=xp, pady=yp
                                     , sticky=W)

        self.asset_guid_field.grid(row=5, column=1, padx=xp, pady=yp)

        self.asset_class_field.grid(row=6, column=1, padx=xp, pady=yp)
        self.asset_class_default.grid(row=6, column=2, padx=xp, pady=yp)

        self.asset_sub_class_field.grid(row=7, column=1, padx=xp, pady=yp)
        self.asset_sub_class_default.grid(row=7, column=2, padx=xp, pady=yp)

        self.asset_type_field.grid(row=8, column=1, padx=xp, pady=yp)
        self.asset_type_default.grid(row=8, column=2, padx=xp, pady=yp)

        self.asset_sub_type_field.grid(row=9, column=1, padx=xp, pady=yp)
        self.asset_sub_type_default.grid(row=9, column=2, padx=xp, pady=yp)

        self.maint_type_field.grid(row=10, column=1, padx=xp, pady=yp)
        self.maint_type_default.grid(row=10, column=2, padx=xp, pady=yp)

        self.maint_sub_type_field.grid(row=11, column=1, padx=xp, pady=yp)
        self.maint_sub_type_default.grid(row=11, column=2, padx=xp, pady=yp)

        self.criticality_field.grid(row=12, column=1, padx=xp, pady=yp)
        self.criticality_default.grid(row=12, column=2, padx=xp, pady=yp)

        self.workgroup_field.grid(row=13, column=1, padx=xp, pady=yp)
        self.workgroup_default.grid(row=13, column=2, padx=xp, pady=yp)

        self.securitygroup_field.grid(row=14, column=1, padx=xp, pady=yp)
        self.securitygroup_default.grid(row=14, column=2, padx=xp, pady=yp)

        self.config(cursor="")

    def refresh(self, parent, controller, use_existing_file=True):
        self.destroy()
        self.__init__(parent, controller, use_existing_file)

    def set_config_from_ui(self):
        self.current_layer['corefields']["asset_id"] = self.asset_id_field.get()
        self.current_layer['corefields']["asset_name"] = \
            self.asset_name_field.get()
        self.current_layer['corefields']["id"] = self.asset_guid_field.get()

    def apply_current_config(self, current_layer):
        """
        Load the current asset core config from XML to the UI
        :param current_layer: current selected layer
        """
        # set current config

        # set the combobox label based on current xml config
        # asset ID - gis field
        if self.is_core_attribute_configured(current_layer, "asset_id"):
            self.asset_id_field.current(self.layer_fields.index(
                current_layer['corefields']["asset_id"]))

        # asset name - gis field
        if self.is_core_attribute_configured(current_layer, "asset_name"):
            self.asset_name_field.current(self.layer_fields.index(
                current_layer['corefields']["asset_name"]))

        # asset GUID - gis field
        if self.is_core_attribute_configured(current_layer, "id"):
            self.asset_guid_field.current(self.layer_fields.index(
                current_layer['corefields']["id"]))

        # asset class - gis field
        if self.is_core_attribute_configured(current_layer, "asset_class"):
            self.asset_class_field.current(self.layer_fields.index(
                current_layer['corefields']["asset_class"]))

        # asset sub class - gis field
        if self.is_core_attribute_configured(current_layer, "asset_sub_class"):
            self.asset_sub_class_field.current(self.layer_fields.index(
                current_layer['corefields']["asset_sub_class"]))

        # maint type - gis field
        if self.is_core_attribute_configured(current_layer, "maintenance_type"):
            self.maint_type_field.current(self.layer_fields.index(
                current_layer['corefields']["maintenance_type"]))

        # maint sub type - gis field
        if self.is_core_attribute_configured(current_layer,
                                             "maintenance_sub_type"):
            self.maint_sub_type_field.current(self.layer_fields.index(
                current_layer['corefields']["maintenance_sub_type"]))

        # criticality - gis field
        if self.is_core_attribute_configured(current_layer,
                                             "asset_criticality"):
            self.criticality_field.current(self.layer_fields.index(
                current_layer['corefields']["asset_criticality"]))

        # work group - gis field
        if self.is_core_attribute_configured(current_layer,
                                             "asset_work_group"):
            self.workgroup_field.current(self.layer_fields.index(
                current_layer['corefields']["asset_work_group"]))

        # security group - gis field
        if self.is_core_attribute_configured(current_layer,
                                             "asset_security_group"):
            self.securitygroup_field.current(self.layer_fields.index(
                current_layer['corefields']["asset_security_group"]))

        # Now the default hardcode fields
        # asset class default
        if self.is_core_default_configured(current_layer, "asset_class"):
            self.asset_class_default.current(self.asset_class_labels.index(
                current_layer['coredefaults']["asset_class"]))
        # asset sub class default
        if self.is_core_default_configured(current_layer, "asset_sub_class"):
            # populate the list of asset subclasses for the current class
            self.asset_subclass_fields__()
            # now set the combobox
            if current_layer['coredefaults']["asset_sub_class"] in \
                    self.asset_sub_class_list:
                self.asset_sub_class_default.current(
                    self.asset_sub_class_list.index(
                        current_layer['coredefaults']["asset_sub_class"]))

        # set asset type default
        if self.is_core_default_configured(current_layer, "asset_type"):
            self.asset_type_default.current(self.asset_type_labels.index(
                current_layer['coredefaults']["asset_type"]))
        # asset sub type default
        if self.is_core_default_configured(current_layer, "asset_sub_type"):
            # populate the list of asset subtypes for the current type
            self.asset_subtype_fields__()
            # now set the combobox
            if current_layer['coredefaults']["asset_sub_type"] in \
                    self.asset_sub_type_list:
                self.asset_sub_type_default.current(
                    self.asset_sub_type_list.index(
                        current_layer['coredefaults']["asset_sub_type"]))

        # set maintenance type default
        if self.is_core_default_configured(
                current_layer, "asset_maintenance_type"):
            self.maint_type_default.current(self.asset_type_labels.index(
                current_layer['coredefaults']["asset_maintenance_type"]))
        # asset maintenance sub type default
        if self.is_core_default_configured(
                current_layer, "asset_maintenance_sub_type"):
            # populate the list of maintenance subtypes for the current type
            self.maint_subtype_fields__()
            # now set the combobox
            if current_layer['coredefaults']["asset_maintenance_sub_type"] in \
                    self.maint_sub_type_list:
                self.maint_sub_type_default.current(
                    self.maint_sub_type_list.index(
                        current_layer['coredefaults'][
                            "asset_maintenance_sub_type"]))

        # criticality default
        if self.is_core_default_configured(current_layer, "asset_criticality"):
            self.criticality_default.current(self.criticality_labels.index(
                current_layer['coredefaults']["asset_criticality"]))
        # work group default
        if self.is_core_default_configured(current_layer, "asset_work_group"):
            self.workgroup_default.current(self.workgroup_labels.index(
                current_layer['coredefaults']["asset_work_group"]))

        # security group default
        if self.is_core_default_configured(
                current_layer, "asset_security_group"):
            self.securitygroup_default.insert(
                0, current_layer['coredefaults']["asset_security_group"])

    def is_core_attribute_configured(self, config, field):
        """
        Convenience method just to test if the a field has an xml configuration
        :param config: the xml config dict for the layer
        :type config: dict
        :param field: the xml field to test
        :type field: string
        :return: True if the field has an xml config with a valid GIS field
        :rtype: Bool
        """
        if field in config['corefields'] and \
                config['corefields'][field] in self.layer_fields:
            return True
        else:
            return False

    def is_core_default_configured(self, config, field, within_list=None):
        """
        Convenience method just to test if the a field has an xml configuration
        :param config: the xml config dict for the layer
        :type config: dict
        :param field: the xml field to test
        :type field: string
        :param within_list: is the value in the list
        :type within_list: list
        :return: True if the field has an xml config with a valid GIS field
        :rtype: Bool
        """
        if field in config['coredefaults']:
            if isinstance(within_list, list):
                if not config['coredefaults'][field] in within_list:
                    return False
            # the field is configured and in the list
            return True
        else:
            return False

    def asset_subclass_fields__(self, e=None):
        """
        callback for asset_class combobox that gets the asset subclass list for
        the selected asset class.  It then sets the asset sub class combobox
        values.
        :param e: event
        :type e:
        """
        # alias this just to make the text shorter :)
        api_tools = self.controller.assetic_api_tools

        # get the selected asset class from the combobox
        asset_class = self.asset_class_default.get()

        self.asset_sub_class_list = [' ']
        if not asset_class or asset_class.strip() == '':
            pass
        else:
            chk = api_tools.get_asset_sub_class_list_for_class(asset_class)
            if chk:
                self.asset_sub_class_list = chk

        # set values for sub class combobox
        self.asset_sub_class_default.config(value=self.asset_sub_class_list)

    def asset_subtype_fields__(self, e=None):
        """
        callback for asset_type combobox that gets the asset subtype list for
        the selected asset type.  It then sets the asset sub type combobox
        values.
        :param e: event
        :type e:
        """
        # alias this just to make the text shorter :)
        api_tools = self.controller.assetic_api_tools

        # get the selected asset type from the combobox
        asset_type = self.asset_type_default.get()

        self.asset_sub_type_list = [' ']
        if not asset_type or asset_type.strip() == '':
            pass
        else:
            chk = api_tools.get_asset_sub_type_list_for_type(asset_type)
            if chk:
                self.asset_sub_type_list = chk

        # set values for sub class combobox
        self.asset_sub_type_default.config(value=self.asset_sub_type_list)

    def maint_subtype_fields__(self, e=None):
        """
        callback for maint_type combobox that gets the maintenance subtype
        list for the selected maintenance type.
        It then sets the asset sub type combobox values.
        :param e: event
        :type e:
        """
        # alias this just to make the text shorter :)
        api_tools = self.controller.assetic_api_tools

        # get the selected asset type from the combobox
        type_ = self.maint_type_default.get()

        self.maint_sub_type_list = [' ']
        if not type_ or type_.strip() == '':
            pass
        else:
            chk = api_tools.get_maint_sub_type_list_for_type(type_)
            if chk:
                self.maint_sub_type_list = chk

        # set values for sub class combobox
        self.maint_sub_type_default.config(value=self.maint_sub_type_list)

    def fin_subclass_fields__(self, e=None):
        """
        callback for financial class combobox that gets the financial subclass
        list for the selected financial class.
        It then sets the financial sub class combobox values.
        :param e: event
        :type e:
        """
        # alias this just to make the text shorter :)
        api_tools = self.controller.assetic_api_tools

        # get the selected asset type from the combobox
        class_ = self.fin_class_default.get()

        self.fin_sub_class_list = [' ']
        if not class_ or class_.strip() == '':
            pass
        else:
            chk = api_tools.get_financial_sub_class_list_for_class(class_)
            if chk:
                self.fin_sub_class_list = chk

        # set values for sub class combobox
        self.maint_sub_type_default.config(value=self.fin_sub_class_list)

    def save_asset_info(self, delete=False):
        """
        Save the current config or delete the config
        :param delete: If True then delete the core asset config, default is
        False
        :return: 0 is success else error
        """
        # check asset id
        if self.asset_id_field.get() in ["", ' ']:
            self.xml_asset_ID = None
        else:
            self.xml_asset_ID = self.asset_id_field.get()

        # check asset GUID
        if self.asset_guid_field.get() in ["", ' ']:
            self.xml_asset_GUID_core_field = None
        else:
            self.xml_asset_GUID_core_field = self.asset_guid_field.get()

        # asset name
        if self.asset_name_default.get() in ["", ' '] and \
                self.asset_name_field.get() in ["", ' ']:
            messagebox.showerror('Error', 'Asset Name cannot be empty')
            return 1
        elif self.asset_name_default.get():
            # if asset name in core default is not empty
            self.xml_asset_name_core_default = self.asset_name_default.get()
            # if asset name in core field not empty
            if self.asset_name_field.get() not in [" ", ''] and \
                    self.asset_name_field.get() not in self.layer_fields:
                messagebox.showerror(
                    'Error', 'Asset Name Fields in Core Fields does not exist')
                return 1
            elif self.asset_name_field.get() in [" ", ""]:
                self.xml_asset_name_core_field = None
            elif self.asset_name_field.get() in self.layer_fields:
                self.xml_asset_name_core_field = self.asset_name_field.get()
        else:
            self.xml_asset_name_core_field = self.asset_name_field.get()
            self.xml_asset_name_core_default = None
            if self.xml_asset_name_core_field not in self.layer_fields:
                messagebox.showerror(
                    'Error', 'Asset Name Fields in Core Fields does not exist')
                return 1
        # check asset class and subclass
        error = self.check_asset_class_subclass()
        if error:
            return 1
        # check asset type and subtype
        error = self.check_asset_type_subtype()
        if error:
            return 1
        # check maintenance type and subtype
        error = self.check_maintenance_type_subtype()
        if error:
            return 1
        if not error:
            chk = self.add_asset_to_xml_file(delete=0)
            return chk
        else:
            messagebox.showerror("Error", 'check again')
            return 2

    def check_asset_class_subclass(self):
        """
        Validate the Asset Sub Class
        :return: 0=valid, else error
        :rtype: boolean
        """
        self.xml_asset_class_field_default = None
        self.xml_asset_class_field = None
        self.xml_asset_subclass_field = None
        self.xml_asset_subclass_field_default = None
        error = 0
        api_tools = self.controller.assetic_api_tools
        xml_asset_class = None

        if self.asset_class_field.get() in ["", ' '] and \
                self.asset_class_default.get() in ["", ' ']:
            xml_asset_class = None
        # AssetClass in  Core Default is not Null
        # , it should exist in (assetic UI)
        elif self.asset_class_default.get() and \
                self.asset_class_default.get() not in [" ", '']:
            xml_asset_class = self.asset_class_default.get()
            self.xml_asset_class_field_default = xml_asset_class

            if xml_asset_class not in api_tools.asset_class_list:
                error = 1
                messagebox.showerror(
                    'Error', 'Asset Class in Core Default does not exist')
                return error
            elif len(self.asset_sub_class_list) <= 1:
                error = 1
                messagebox.showerror(
                    'Error', 'Asset SubClass in Core Default not found')
                return error
            # if asset class is in core fields is not null ,
            # it should exist in GIS table
            if self.asset_class_field.get() and \
                    self.asset_class_field.get() not in [" ", '']:
                xml_asset_class = self.asset_class_field.get()
                self.xml_asset_class_field = xml_asset_class
                if xml_asset_class and xml_asset_class not in self.layer_fields:
                    error = 1
                    messagebox.showerror(
                        'Error'
                        , 'Asset Class Fields in Core Fields does not exist')
                    return error

        # Asset Class in core fields is not Null but asset class in core
        # defaults is null, then Asset Class in core fields
        # should exist in GIS table
        elif self.asset_class_field.get():
            self.xml_asset_class_field_default = None
            xml_asset_class = self.asset_class_field.get()
            self.xml_asset_class_field = xml_asset_class
            if xml_asset_class and xml_asset_class not in self.layer_fields:
                error = 1
                messagebox.showerror(
                    'Error', 'Asset Class Fields in Core Fields does not exist')
                return error
        # Asset Subclass equals to Null in both fields
        if self.asset_sub_class_field.get() in ["", ' '] and \
                self.asset_sub_class_default.get() in ["", ' ']:
            xml_asset_subclass = None
        # Asset Subclass in Core Defaults is not Null,
        # it should exist in assetic UI
        elif self.asset_sub_class_default.get() and \
                self.asset_sub_class_default.get() not in [" ", ""]:
            xml_asset_subclass = self.asset_sub_class_default.get()
            self.xml_asset_subclass_field_default = self.asset_sub_class_default.get()
            if xml_asset_subclass not in self.asset_sub_class_list:
                error = 1
                messagebox.showerror(
                    'Error', 'Asset SubClass in Core Default does not exist')
                return error
            # Asset Subclass in Core Defaults and Core Fields are not Null,
            # Asset Subclass in Core Fields should exist in GIS Table
            if self.asset_sub_class_field.get() and \
                    self.asset_sub_class_field.get() not in [" ", ""]:
                xml_asset_subclass = self.asset_sub_class_field.get()
                self.xml_asset_subclass_field = self.asset_sub_class_field.get()
                if xml_asset_subclass not in self.layer_fields:
                    error = 1
                    messagebox.showerror(
                        'Error'
                        , 'Asset SubClass Fields in Core Fields does not exist')
                    return error
            else:
                self.xml_asset_subclass_field = None


        # Asset Subclass in Core Fields is not Null and Asset Subclass in core
        # defaults is null,Asset Subclass in Core Fields
        # should exist in GIS Table
        else:
            self.xml_asset_subclass_field_default = None
            xml_asset_subclass = self.asset_sub_class_field.get()
            self.xml_asset_subclass_field = self.asset_sub_class_field.get()
            if xml_asset_subclass not in self.layer_fields:
                error = 1
                messagebox.showerror(
                    'Error'
                    , 'Asset SubClass Fields in Core Fields does not exist')
                return error

        # Asset class and Asset Subclass should either be None
        # or not None together
        if xml_asset_class is None and xml_asset_subclass is not None:
            error = 1
            messagebox.showerror(
                'Error', 'Asset Class need to select to save Asset SubClass')
            return error
        if xml_asset_class is not None and xml_asset_subclass is None:
            error = 1
            messagebox.showerror(
                'Error', 'Asset SubClass need to select to save Asset Class')
            return error
        if not error:
            error = 0
            return error

    def check_asset_type_subtype(self):
        """
        Validate the chosen Asset Sub Type
        :return: 0=valid, else error
        :rtype: boolean
        """
        error = 0
        api_tools = self.controller.assetic_api_tools
        self.xml_asset_subtype_field_default = None
        self.xml_asset_type_field_default = None
        self.xml_asset_type_field = None
        self.xml_asset_subtype_field = None
        xml_asset_type = None
        if self.asset_type_field.get() in ["",
                                           ' '] and self.asset_type_default.get() in [
            "", ' ']:
            xml_asset_type = None

        # Asset Type is not Null in Core Default, it should exist in
        # core defaults (assetic UI)
        elif self.asset_type_default.get() and self.asset_type_default.get() not in [
            "", ' ']:
            xml_asset_type = self.asset_type_default.get()
            self.xml_asset_type_field_default = xml_asset_type
            if xml_asset_type not in api_tools.asset_type_list:
                error = 1
                messagebox.showerror(
                    'Error', 'Asset Type in Core Default does not exist')
                return error
            elif len(self.asset_sub_type_list) <= 1:
                error = 1
                messagebox.showerror(
                    'Error', 'Asset SubType in Core Default not found')
                return error
            # if Asset Type is in core fields is not null and  Asset Type in
            # Core Default is not Null, Asset Type in Core Default should
            # exist in GIS table
            if self.asset_type_field.get() and self.asset_type_field.get() not in [
                "", ' ']:
                xml_asset_type = self.asset_type_field.get()
                self.xml_asset_type_field = xml_asset_type
                if xml_asset_type and xml_asset_type not in self.layer_fields:
                    error = 1
                    messagebox.showerror(
                        'Error'
                        , 'Asset Type Fields in Core Fields does not exist')
                    return error
        # Asset Type in core fields is not Null, it should exist in GIS table
        elif self.asset_type_field.get():
            xml_asset_type = self.asset_type_field.get()
            self.xml_asset_type_field = xml_asset_type
            if xml_asset_type and xml_asset_type not in self.layer_fields:
                error = 1
                messagebox.showerror(
                    'Error', 'Asset Type Fields in Core Fields does not exist')
                return error

        # Asset SubType equals to Null in both fields
        if self.asset_sub_type_field.get() in ["", ' '] and \
                self.asset_sub_type_default.get() in ["", ' ']:
            xml_asset_subtype = None
        # Asset SubType in Core Defaults is not Null,
        # it should exist in assetic UI
        elif self.asset_sub_type_default.get() and \
                self.asset_sub_type_default.get() not in [" ", ""]:
            xml_asset_subtype = self.asset_sub_type_default.get()
            self.xml_asset_subtype_field_default = self.asset_sub_type_default.get()
            if xml_asset_subtype not in self.asset_sub_type_list:
                error = 1
                messagebox.showerror(
                    'Error', 'Asset SubType in Core Default does not exist')
                return error
                # Asset Subtype in Core Defaults and Core Fields are not Null
                # , Asset SubType in Core Fields should exist in GIS Table
            if self.asset_sub_type_field.get() and self.asset_sub_type_field.get() not in [
                " ", ""]:
                xml_asset_subtype = self.asset_sub_type_field.get()
                self.xml_asset_subtype_field = self.asset_sub_type_field.get()
                if xml_asset_subtype not in self.layer_fields:
                    error = 1
                    messagebox.showerror(
                        'Error'
                        , 'Asset SubType Fields in Core Fields does not exist')
                    return error
            else:
                self.xml_asset_subtype_field = None

        # Asset SubType in Core Fields is not Null, it should exist in GIS Table
        else:
            self.xml_asset_subtype_field_default = None
            xml_asset_subtype = self.asset_sub_type_field.get()
            self.xml_asset_subtype_field = self.asset_sub_type_field.get()
            if xml_asset_subtype not in self.layer_fields:
                error = 1
                messagebox.showerror('Error',
                                     'Asset SubType Fields in Core Fields does not exist')
                return error

        # Asset Type and Asset SubType should either be None
        # or not None together
        if xml_asset_type is None and xml_asset_subtype is not None:
            error = 1
            messagebox.showerror(
                'Error', 'Asset Type need to select to save Asset SubType')
            return error
        if xml_asset_type is not None and xml_asset_subtype is None:
            error = 1
            messagebox.showerror(
                'Error', 'Asset SubType need to select to save Asset Type')
            return error
        if not error:
            error = 0
            return error
        return 0

    def check_maintenance_type_subtype(self):
        """
        Validate the chosen Maintenance Sub Type
        :return: 0=valid, else error
        :rtype: boolean
        """
        error = 0
        api_tools = self.controller.assetic_api_tools
        self.xml_maint_subtype_field_default = None
        self.xml_maint_type_field_default = None
        self.xml_maint_type_field = None
        self.xml_maint_subtype_field = None

        xml_maint_type = None
        if self.maint_type_field.get() in ["", ' '] and \
                self.maint_type_default.get() in ["", ' ']:
            xml_maint_type = None

        # Maintenance Type is not Null in Core Default, it should exist in
        # core defaults (assetic UI)
        elif self.maint_type_default.get() and self.maint_type_default.get() \
                not in ["", ' ']:
            xml_maint_type = self.maint_type_default.get()
            self.xml_maint_type_field_default = xml_maint_type
            if xml_maint_type not in api_tools.maint_type_list:
                error = 1
                messagebox.showerror(
                    'Error', 'Maintenance Type in Core Default does not exist')
                return error
            elif len(self.maint_sub_type_list) <= 1:
                error = 1
                messagebox.showerror(
                    'Error', 'Maintenance SubType in Core Default not found')
                return error
            # if Asset Type is in core fields is not null and  Asset Type in
            # Core Default is not Null, Asset Type in Core Default should
            # exist in GIS table
            if self.maint_type_field.get() and self.maint_type_field.get() not \
                    in ["", ' ']:
                xml_maint_type = self.maint_type_field.get()
                self.xml_maint_type_field = xml_maint_type
                if xml_maint_type and xml_maint_type not in self.layer_fields:
                    error = 1
                    messagebox.showerror(
                        'Error'
                        , 'Maintenance Type Fields in Core Fields does not '
                          'exist')
                    return error
        # Maintenance Type in core fields is not Null, it should exist in GIS
        # table
        elif self.maint_type_field.get():
            xml_maint_type = self.maint_type_field.get()
            self.xml_maint_type_field = xml_maint_type
            if xml_maint_type and xml_maint_type not in self.layer_fields:
                error = 1
                messagebox.showerror(
                    'Error', 'Maintenance Type Fields in Core Fields does not '
                             'exist')
                return error

        # Maintenance SubType equals to Null in both fields
        if self.maint_sub_type_field.get() in ["", ' '] and \
                self.maint_sub_type_default.get() in ["", ' ']:
            xml_maint_subtype = None
        # Maintenance SubType in Core Defaults is not Null,
        # it should exist in assetic UI
        elif self.maint_sub_type_default.get() and \
                self.maint_sub_type_default.get() not in [" ", ""]:
            xml_maint_subtype = self.maint_sub_type_default.get()
            self.xml_maint_subtype_field_default = \
                self.maint_sub_type_default.get()
            if xml_maint_subtype not in self.maint_sub_type_list:
                error = 1
                messagebox.showerror(
                    'Error', 'Maintenance SubType in Core Default does not '
                             'exist')
                return error
                # Maintenance Subtype in Core Defaults and Core Fields are not
                # Null
                # , Maitenance SubType in Core Fields should exist in GIS Table
            if self.maint_sub_type_field.get() and \
                    self.maint_sub_type_field.get() not in [" ", ""]:
                xml_maint_subtype = self.maint_sub_type_field.get()
                self.xml_maint_subtype_field = self.maint_sub_type_field.get()
                if xml_maint_subtype not in self.layer_fields:
                    error = 1
                    messagebox.showerror(
                        'Error'
                        , 'Maintenance SubType Fields in Core Fields does not '
                          'exist')
                    return error
            else:
                self.xml_maint_subtype_field = None

        # Maintenance SubType in Core Fields is not Null, it should exist in
        # GIS Table
        else:
            self.xml_maint_subtype_field_default = None
            xml_maint_subtype = self.maint_sub_type_field.get()
            self.xml_maint_subtype_field = self.maint_sub_type_field.get()
            if xml_maint_subtype not in self.layer_fields:
                error = 1
                messagebox.showerror(
                    'Error'
                    , ' Maintenance Fields in Core Fields does not exist')
                return error

        # Asset Type and Asset SubType should either be None
        # or not None together
        if xml_maint_type is None and xml_maint_subtype is not None:
            error = 1
            messagebox.showerror(
                'Error', 'Maintenance Type need to select to save Maintenance '
                         'SubType')
            return error
        if xml_maint_type is not None and xml_maint_subtype is None:
            error = 1
            messagebox.showerror(
                'Error', 'Maintenance SubType need to select to save '
                         'Maintenance Type')
            return error
        if not error:
            error = 0
            return error
        return 0

    def add_asset_to_xml_file(self, delete=0):
        """
        Save the asset config for the current layer to the XML file
        :param delete: optionally delete the current layer
        :return:
        """
        layer = 1

        if os.path.isfile(self.controller.common_tools.config_file_path):
            tree = ET.parse(self.save_path)

        else:
            messagebox.showerror(
                "Error", "Configuration file {0} not found".format(
                    self.save_path))
            return
        root = tree.getroot()
        layerxml = None
        for operation in root.iter('operation'):
            action = operation.get("action")
            if action == "Asset":
                for onelayer in operation.iter("layer"):

                    if onelayer.get("name") == self.current_layer["layer"]:
                        layerxml = onelayer
                        break
        if not layerxml:
            # layer not found so exit
            return 0

        coredefaults = layerxml.find("coredefaults")
        corefields = layerxml.find("corefields")

        if coredefaults is None and not delete:
            # create a new one
            coredefaults = ET.SubElement(layerxml, "coredefaults")
        elif coredefaults is not None and delete:
            # remove element
            layerxml.remove(coredefaults)

        if corefields is None and not delete:
            corefields = ET.SubElement(layerxml, "corefields")
        elif corefields is not None and delete:
            # remove element
            layerxml.remove(corefields)

        if not delete:
            tools = self.controller.common_tools
            # add/update elements
            # asset Friendly ID
            chk = tools.apply_value_to_element(
                "asset_id", corefields, coredefaults
                , self.xml_asset_ID, None
                , "Asset Friendly Id")
            if not chk:
                return 1

            # asset name
            chk = tools.apply_value_to_element(
                "asset_name", corefields, coredefaults
                , self.xml_asset_name_core_field
                , self.xml_asset_name_core_default
                , "Asset Name")
            if not chk:
                return 1

            # asset internal GUID
            chk = tools.apply_value_to_element(
                "id", corefields, coredefaults
                , self.xml_asset_GUID_core_field
                , None
                , "Asset GUID")
            if not chk:
                return 1

            # asset class
            chk = tools.apply_value_to_element(
                "asset_class", corefields, coredefaults
                , self.xml_asset_class_field
                , self.xml_asset_class_field_default
                , "Asset Class")
            if not chk:
                return 1

            # asset class
            chk = tools.apply_value_to_element(
                "asset_sub_class", corefields, coredefaults
                , self.xml_asset_subclass_field
                , self.xml_asset_subclass_field_default
                , "Asset Sub Class")
            if not chk:
                return 1

            # maintenance type
            chk = tools.apply_value_to_element(
                "asset_maintenance_type", corefields, coredefaults
                , self.xml_maint_type_field
                , self.xml_maint_type_field_default
                , "Asset Type")
            if not chk:
                return 1

            # maintenance sub type
            chk = tools.apply_value_to_element(
                "asset_maintenance_sub_type", corefields,
                coredefaults
                , self.xml_maint_subtype_field
                , self.xml_maint_subtype_field_default
                , "Asset Sub Type")
            if not chk:
                return 1

            # criticality
            chk = tools.apply_value_to_element(
                "asset_criticality", corefields,
                coredefaults
                , self.criticality_field.get()
                , self.criticality_default.get()
                , "Asset Criticality")
            if not chk:
                return 1

            # work group
            chk = tools.apply_value_to_element(
                "asset_work_group", corefields,
                coredefaults
                , self.workgroup_field.get()
                , self.workgroup_default.get()
                , "Asset Work Group")
            if not chk:
                return 1

            # security Group
            chk = tools.apply_value_to_element(
                "asset_security_group", corefields,
                coredefaults
                , self.securitygroup_field.get()
                , self.securitygroup_default.get()
                , "Asset Work Group")
            if not chk:
                return 1

        dom = xml.dom.minidom.parseString(ET.tostring(root))
        xmlstring = dom.toprettyxml(encoding='UTF-8')
        dom_string = b'\n'.join(
            [s for s in xmlstring.splitlines() if s.strip()])
        with open(self.save_path, 'wb') as file:
            file.write(dom_string)
            file.close()
        return 0


class AssetAttributesFrame(tk.Frame):
    def __init__(self, parent, controller, use_existing_file=True):
        """
        Asset Attributes (non-core) configuration page
        :param parent: The main window
        :type parent:
        :param controller: class from main window with common functions and
        variables
        :type controller:
        :param use_existing_file: read existing xml or create a new one?
        :type use_existing_file: boolean
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.delete_label = {}
        self.use_existing_file = use_existing_file
        self.l_button = {}
        self.delete_button = {}
        self.configuration = controller.get_existing_xml()
        self.configured_layers = self.configuration.assetconfig
        self.layer_dict = controller.layer_dict

        api_client = ApiClient()
        self.api_client = api_client
        self.asset_buttons = {}
        self.current_layer = None
        self.logger = api_client.configuration.packagelogger
        self.host = self.api_client.configuration.host

        self.save_path = self.controller.common_tools.config_file_path

        # the list of attribute fields
        self.attributes_dict = dict()
        self.attributes_list = list()

        # track the rows
        self.att_num = 0
        self.grid_att_field = dict()
        self.grid_gis_field = dict()
        self.grid_default_field = dict()
        self.grid_default_var = dict()
        self.cmb_selected_att = dict()

        # set fonts
        font_normal = controller.font_normal
        font_header = controller.font_header
        font_strike = controller.font_strike

        # set padding between rows and columns
        xp = 1
        yp = 1
        # set width
        wid = 40

        tk.Label(self, text="Asset Additional Attributes Configuration"
                 , font=font_header).grid(row=0, column=0, columnspan=3,
                                          sticky=EW)

        selected_layer = controller.selected_layer_name
        if not selected_layer or selected_layer.strip() == "":
            # No layer is selected so don't populate anything more
            # returning after creating label above so that a form exists
            return

        # Get the current xml config for the layer.  If there is none the
        # exit without building form further
        # User needs to first assign category and higher level config
        for config in self.configured_layers:
            if selected_layer == config["layer"]:
                self.current_layer = config
                break
        if not self.current_layer:
            self.config(cursor="")
            messagebox.showerror(
                "Error",
                "Assign Asset Category before setting Asset Attributes")
            return

        # local variable just to keep the name a bit shorter
        current_layer = self.current_layer

        # get the category
        category = current_layer["asset_category"]

        # Getting the labels from Assetic APIs may take some time
        self.attributes_dict = \
            controller.assetic_api_tools.attribute_fields_for_category(category)

        # get the list of attributes for the category
        # self.attributes_dict["Zone"] = "Zone"
        # self.attributes_dict["Comment"] = "General Comments"
        self.attributes_list = list(self.attributes_dict.values())
        self.attributes_list.sort()

        # Get the GIS layer fields
        self.layer_fields = list()
        if selected_layer in self.layer_dict:
            self.layer_fields = sorted(self.layer_dict[selected_layer]
                                       , key=lambda x: x.lower())
        self.layer_fields.insert(0, " ")

        # set wait cursor as initial load can take time to read Assetic APIs
        self.config(cursor="wait")
        self.update()

        # Add grid headers
        Label(self, text="Assetic Attribute").grid(row=2, column=0, padx=xp,
                                                   pady=yp)
        Label(self, text="GIS Field").grid(row=2, column=1, padx=xp, pady=yp)
        Label(self, text="Hardcode Value").grid(
            row=2, column=2, padx=xp, pady=yp)

        # loop existing config for attribute (gis) fields
        if six.PY3:
            config_gis_fields = list(current_layer["attributefields"].items())
            config_def_fields = list(current_layer["attributedefaults"].items())
        else:
            config_gis_fields = current_layer["attributefields"].items()
            config_def_fields = current_layer["attributedefaults"].items()
        # loop through configured gis fields and add row to form
        for att_field, gis_field in config_gis_fields:
            self.add_row(self.att_num, att_field=att_field, gis_value=gis_field)
            self.att_num += 1
        # loop through configured default fields and add row to form
        for att_field, def_field in config_def_fields:
            self.add_row(
                self.att_num, att_field=att_field, default_value=def_field)
            self.att_num += 1

        # Add Empty Row at bottom
        self.att_num += 1
        self.add_row(self.att_num)

        self.config(cursor="")

    def refresh(self, parent, controller, use_existing_file=True):
        self.destroy()
        self.__init__(parent, controller, use_existing_file)

    def add_row(self, att_num, att_field=None, gis_value=None,
                default_value=None):
        """
        Add a config row.  If there is a config for the row set the values
        :param att_num: the attribute id. Allow us to track the controls we
        add and position the row in the grid
        :param att_field: set the attribute field if not null
        :param gis_value: set the gis field if not null
        :param default_value: set the default field if not null
        :return:
        """
        # set padding between rows and columns
        xp = 1
        yp = 1
        # set width
        wid = 40

        self.cmb_selected_att[att_num] = tk.StringVar()

        self.grid_att_field[att_num] = ttk.Combobox(
            self, values=self.attributes_list, width=wid
            , textvariable=self.cmb_selected_att[att_num])
        self.grid_gis_field[att_num] = ttk.Combobox(
            self, values=self.layer_fields, width=wid)

        # create and set default (hardcode) field
        if default_value:
            self.grid_default_var[self.att_num] = default_value
        else:
            self.grid_default_var[att_num] = None
        self.grid_default_field[att_num] = Entry(
            self
            , textvariable=StringVar(
                self, value=self.grid_default_var[att_num])
            , width=wid, justify=LEFT)

        # set the attribute field
        if att_field and att_field in self.attributes_dict:
            self.grid_att_field[att_num].current(
                self.attributes_list.index(self.attributes_dict[att_field]))

        # set the attribute field combobox label based on current xml config
        if gis_value and gis_value in self.layer_fields:
            self.grid_gis_field[att_num].current(
                self.layer_fields.index(gis_value))

        # set position in grid
        self.grid_att_field[att_num].grid(
            row=self.att_num + 3, column=0, padx=xp, pady=yp)
        self.grid_gis_field[att_num].grid(
            row=self.att_num + 3, column=1, padx=xp, pady=yp)
        self.grid_default_field[att_num].grid(
            row=self.att_num + 3, column=2, padx=xp, pady=yp)

        self.grid_att_field[att_num].bind(
            '<<ComboboxSelected>>', self._cmb_att_field_changed)

    def _cmb_att_field_changed(self, event):
        """
        One of the combobox list of assetic attributes was changed
        If the new value is already set in another row the change will be
        undone and the user alerted
        If the combobox in the last row in the form has a value we need to
        add a new empty row
        :param event: cmd changed event
        :return: None
        """

        # test if selected attribute already set in another row
        new_value = event.widget.get()
        for wid in self.grid_att_field.values():
            if wid != event.widget and new_value == wid.get():
                messagebox.showerror(
                    "Error",
                    "Attribute [{0}] already defined".format(new_value))
                event.widget.set("")
                return

        # get value of the attributes combobox in the last row
        value = self.cmb_selected_att[self.att_num].get()
        if value and value != "":
            # the last row has a value so add a new empty row so anotyher new
            # attribute can be defined
            self.att_num += 1
            self.add_row(att_num=self.att_num)

    def save_asset_attribute_info(self, delete=False):
        """
        Save asset attributes config
        :param delete: if true delete the attributes, default is false
        :return:
        """
        gis_flds = dict()
        def_flds = dict()
        # get the settings from the UI

        for index, control in self.grid_att_field.items():
            a = control.get()
            current_att = None
            for key, value in self.attributes_dict.items():
                if value == a:
                    current_att = key
                    break
            if current_att:
                # is the value a gis field or a default field
                if self.grid_default_field[index] and \
                        str(self.grid_default_field[index].get()).strip() != "":
                    if not self.grid_gis_field[index] or \
                            str(self.grid_gis_field[index].get()).strip() != "":
                        # it is a default field
                        def_flds[current_att] = self.grid_default_field[
                            index].get()
                    else:
                        # default and gis field defined - abort
                        messagebox.showerror(
                            "Error",
                            "Please only define GIS or Hardcode for a field.")
                        return 1
                elif self.grid_gis_field[index] and \
                        str(self.grid_gis_field[index].get()).strip() != "":
                    # it is a gis field
                    gis_flds[current_att] = self.grid_gis_field[index].get()

            # increment the grid index counter
            index += 1

        chk = self._add_asset_atts_to_xml_file(gis_flds, def_flds)
        return chk

    def _add_asset_atts_to_xml_file(self, gis_fields, default_fields,
                                    delete=False):
        """
        Write the asset attribute config for the current layer to the XML file

        :param gis_fields:
        :param default_fields:
        :param delete: If True delete the attributes.  Default is False
        :return:
        """

        if os.path.isfile(self.controller.common_tools.config_file_path):
            tree = ET.parse(self.save_path)
        else:
            messagebox.showerror(
                "Error", "Configuration file {0} not found".format(
                    self.save_path))
            return 1
        root = tree.getroot()

        layerxml = None
        for operation in root.iter('operation'):
            action = operation.get("action")
            if action == "Asset":
                for onelayer in operation.iter("layer"):
                    if onelayer.get("name") == self.current_layer["layer"]:
                        layerxml = onelayer
                        break
        if not layerxml:
            # no config for the layer
            return 0

        att_defaults = layerxml.find("attributedefaults")
        att_fields = layerxml.find("attributefields")

        if att_defaults is None and not delete:
            # create a new one
            att_defaults = ET.SubElement(
                layerxml, "attributedefaults")
        elif att_defaults is not None and delete:
            layerxml.remove(att_defaults)

        if att_fields is None and not delete:
            att_fields = ET.SubElement(
                layerxml, "attributefields")
        elif att_fields is not None and delete:
            layerxml.remove(att_fields)

        # loop over the att_fields and add
        if not delete:
            xml_fields = dict()
            for key, value in gis_fields.items():
                xml_fields[key] = att_fields.find(key)
                if xml_fields[key] is None and value:
                    xml_fields[key] = ET.SubElement(att_fields, key)
                if value:
                    xml_fields[key].text = value
                elif not value and xml_fields[key] is not None:
                    att_fields.remove(xml_fields[key])

            # loop over the defaults fields and add
            for key, value in default_fields.items():
                xml_fields[key] = att_defaults.find(key)
                if xml_fields[key] is None and value:
                    xml_fields[key] = ET.SubElement(
                        att_defaults, key)
                if value:
                    xml_fields[key].text = value
                elif not value and xml_fields[key] is not None:
                    default_fields.remove(xml_fields[key])

        dom = xml.dom.minidom.parseString(ET.tostring(root))
        xmlstring = dom.toprettyxml(encoding='UTF-8')
        dom_string = b'\n'.join(
            [s for s in xmlstring.splitlines() if s.strip()])
        with open(self.save_path, 'wb') as file:
            file.write(dom_string)
            file.close()
        return 0


class ComponentFrame(tk.Frame):
    def __init__(self, parent, controller):
        """
        Component configuration page
        :param parent: The main window
        :type parent:
        :param controller: class from main window with common functions and
        variables
        :type controller:
        :param use_existing_file: read existing xml or create a new one?
        :type use_existing_file: boolean
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.delete_label = {}
        self.l_button = {}
        self.delete_button = {}
        self.configuration = controller.get_existing_xml()
        self.configured_layers = self.configuration.assetconfig
        self.layer_dict = controller.layer_dict

        self.asset_buttons = {}
        self.current_layer = None
        self.current_component = self.controller.current_component

        self.save_path = self.controller.common_tools.config_file_path

        self.selected_unit_type = tk.StringVar()
        self.selected_nm_type = tk.StringVar()

        self.xml_c_label_default = None
        self.xml_c_label_field = None
        self.xml_c_type_default = None
        self.xml_c_type_field = None

        font_normal = controller.font_normal
        font_header = controller.font_header
        font_strike = controller.font_strike

        # set padding between rows and columns
        xp = 1
        yp = 1
        # set the label justification 'sticky' - N, S, E, W
        st = tk.E

        tk.Label(self, text="Component Configuration"
                 , font=font_header).grid(row=0, column=0, columnspan=3,
                                          sticky=EW)

        selected_layer = controller.selected_layer_name
        if not selected_layer or selected_layer.strip() == "":
            # No layer is selected so don't populate anything more
            # returning after creating label above so that a form exists
            return

        # Get the current xml config for the layer.  If there is none the
        # exit without building form further
        # User needs to first assign category and higher level config
        for config in self.configured_layers:
            if selected_layer == config["layer"]:
                self.current_layer = config
                break
        if not self.current_layer:
            self.config(cursor="")
            messagebox.showerror(
                "Error",
                "Assign Asset Category before setting Asset Components")
            return

        # local variable just to keep the name a bit shorter
        current_layer = self.current_layer

        # set wait cursor as initial load can take time to read Assetic APIs
        self.config(cursor="wait")
        self.update()

        # get lists for lookups
        # Get NM Type list
        self.nm_type_list = [
            "", "Area", "Depth", "Diameter", "Height", "Length"
            , "NotDefined", "Quantity", "Volume", "Weight", "Width"]
        try:
            self.unit_list = controller.assetic_api_tools.unit_list
        except:
            self.unit_list = ["Metre", "Square Metre"]
        if "" not in self.unit_list:
            self.unit_list.insert(0, "")

        # Add grid headers
        Label(self, text="GIS Field").grid(row=2, column=1, padx=xp, pady=yp)
        Label(self, text="Hardcode Value").grid(
            row=2, column=2, padx=xp, pady=yp)

        # Add labels for each core field, first column
        Label(self, text="Component ID*").grid(
            row=3, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Component Name*").grid(
            row=4, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Component Type").grid(
            row=5, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Useful Life").grid(
            row=6, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Material").grid(
            row=7, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Measure Unit").grid(row=8, column=0, padx=xp,
                                              pady=yp, sticky=st)
        Label(self, text="Measure Type").grid(
            row=9, column=0, padx=xp, pady=yp, sticky=st)

        self.layer_fields = list()
        if selected_layer in self.layer_dict:
            self.layer_fields = sorted(self.layer_dict[selected_layer]
                                       , key=lambda x: x.lower())
        self.layer_fields.insert(0, " ")

        # set width
        wid = 40

        # First create the comboboxes with GIS field list
        self.component_id_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.c_label_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.c_type_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.c_design_life_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.c_material_type_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.c_dimension_unit_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.c_network_measure_type_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)

        # Now the hardcode fields
        self.c_label_default = Entry(self, width=wid)
        self.c_type_default = Entry(self, width=wid)
        self.cmb_dimension_unit_default = ttk.Combobox(
            self, values=self.unit_list, width=wid - 3, state='readonly'
            , textvariable=self.selected_unit_type)
        self.c_network_measure_type_default = ttk.Combobox(
            self, values=self.nm_type_list, width=wid - 3, state='readonly'
            , textvariable=self.selected_nm_type)
        self.c_design_life_default = Entry(self, width=wid)
        self.c_material_type_default = Entry(self, width=wid)

        if self.controller.current_component:
            self.apply_current_config(self.controller.current_component)
        clear = False
        if clear:
            self.c_label_field.current(0)
            self.component_id_field.current(0)
            self.c_type_field.current(0)
            self.c_design_life_field.current(0)
            self.c_material_type_field.current(0)
            self.c_dimension_unit_field.current(0)
            self.c_network_measure_type_field.current(0)

        # position fields in grid
        self.component_id_field.grid(row=3, column=1, padx=xp, pady=yp)

        self.c_label_field.grid(row=4, column=1, padx=xp, pady=yp)
        self.c_label_default.grid(row=4, column=2, padx=xp, pady=yp, sticky=W)

        self.c_type_field.grid(row=5, column=1, padx=xp, pady=yp)
        self.c_type_default.grid(row=5, column=2, padx=xp, pady=yp)

        self.c_design_life_field.grid(row=6, column=1, padx=xp, pady=yp)
        self.c_design_life_default.grid(row=6, column=2, padx=xp, pady=yp)

        self.c_material_type_field.grid(row=7, column=1, padx=xp, pady=yp)
        self.c_material_type_default.grid(row=7, column=2, padx=xp, pady=yp)

        self.c_dimension_unit_field.grid(row=8, column=1, padx=xp, pady=yp)
        self.cmb_dimension_unit_default.grid(row=8, column=2, padx=xp, pady=yp)

        self.c_network_measure_type_field.grid(row=9, column=1, padx=xp,
                                               pady=yp)
        self.c_network_measure_type_default.grid(row=9, column=2, padx=xp,
                                                 pady=yp)

        self.config(cursor="")

    def refresh(self, parent, controller):
        self.destroy()
        self.__init__(parent, controller)

    def apply_current_config(self, selected_component):
        """
        Apply the current XML config for the component to the form fields
        :return:
        """
        current_layer = self.current_layer
        if "components" not in current_layer:
            return

        current_comp = None
        for component in current_layer["components"]:
            comp_label = None
            comp_type = None
            if "defaults" in component:
                if "label" in component["defaults"]:
                    comp_label = component["defaults"]["label"]
                if "component_type" in component["defaults"]:
                    comp_type = component["defaults"]["component_type"]
            if "attributes" in component:
                if "label" in component["attributes"] \
                        and component["attributes"]["label"]:
                    comp_label = component["attributes"]["label"]
                if "component_type" in component["attributes"] and \
                        component["attributes"]["component_type"]:
                    comp_type = component["attributes"]["component_type"]

            if comp_label == selected_component["label"] and \
                    comp_type == selected_component["type"]:
                current_comp = component
                break

        if not current_comp:
            return

        # set the combobox label based on current xml config
        # component ID - gis field
        if self.is_attribute_configured(current_comp, "component_id"):
            self.component_id_field.current(self.layer_fields.index(
                current_comp["attributes"]["component_id"]))

        # component name - gis field
        if self.is_attribute_configured(current_comp, "label"):
            self.c_label_field.current(self.layer_fields.index(
                current_comp["attributes"]["label"]))
            self.c_label_field.configure(state='disabled')
        self.c_type_field.configure(state='disabled')
        # component type - gis field
        if self.is_attribute_configured(current_comp, "component_type"):
            self.c_type_field.current(self.layer_fields.index(
                current_comp["attributes"]["component_type"]))

        # useful life - gis field
        if self.is_attribute_configured(current_comp, "design_life"):
            self.c_design_life_field.current(self.layer_fields.index(
                current_comp["attributes"]["design_life"]))

        # material - gis field
        if self.is_attribute_configured(current_comp, "material_type"):
            self.c_material_type_field.current(self.layer_fields.index(
                current_comp["attributes"]["material_type"]))

        # measure unit - gis field
        if self.is_attribute_configured(current_comp, "dimension_unit"):
            self.c_dimension_unit_field.current(self.layer_fields.index(
                current_comp["attributes"]["dimension_unit"]))

        # measure type - gis field
        if self.is_attribute_configured(current_comp, "network_measure_type"):
            self.c_network_measure_type_field.current(self.layer_fields.index(
                current_comp["attributes"]["network_measure_type"]))

        # Now set defaults if set
        # component name - hardcode field
        if self.is_default_configured(current_comp, "label"):
            self.c_label_default.insert(0, current_comp["defaults"]["label"])

        # component type - hardcode field
        if self.is_default_configured(current_comp, "component_type"):
            self.c_type_default.insert(
                0, current_comp["defaults"]["component_type"])

        # useful life - hardcode field
        if self.is_default_configured(current_comp, "design_life"):
            self.c_design_life_default.insert(
                0, current_comp["defaults"]["design_life"])

        # material - hardcode field
        if self.is_default_configured(current_comp, "material_type"):
            self.c_material_type_default.insert(
                0, current_comp["defaults"]["material_type"])

        # measure unit - hardcode field
        if self.is_default_configured(current_comp, "dimension_unit"):
            self.cmb_dimension_unit_default.current(self.unit_list.index(
                current_comp["defaults"]["dimension_unit"]))

        # measure type - hardcode field
        if self.is_default_configured(current_comp, "network_measure_type"):
            self.c_network_measure_type_default.current(self.nm_type_list.index(
                current_comp["defaults"]["network_measure_type"]))

        # set the key fields as read-only so they can't change, othewise it
        # is tricky to manage changes
        self.c_label_field.configure(state='disabled')
        self.c_type_field.configure(state='disabled')
        self.c_label_default.configure(state='disabled')
        self.c_type_default.configure(state='disabled')

    def is_attribute_configured(self, config, field):
        """
        Convenience method just to test if the a field has an xml configuration
        :param config: the xml config dict for the layer
        :type config: dict
        :param field: the xml field to test
        :type field: string
        :return: True if the field has an xml config with a valid GIS field
        :rtype: Bool
        """
        if field in config['attributes'] and \
                config['attributes'][field] in self.layer_fields:
            return True
        else:
            return False

    def is_default_configured(self, config, field, within_list=None):
        """
        Convenience method just to test if the a field has an xml configuration
        :param config: the xml config dict for the layer
        :type config: dict
        :param field: the xml field to test
        :type field: string
        :param within_list: is the value in the list
        :type within_list: list
        :return: True if the field has an xml config with a valid GIS field
        :rtype: Bool
        """
        if field in config['defaults']:
            if isinstance(within_list, list):
                if not config['defaults'][field] in within_list:
                    return False
            # the field is configured and in the list
            return True
        else:
            return False

    def save_component_info(self, delete=False):
        """
        save the component information from the form
        this method validates the input fields and if ok will then
        run method to update the xml
        :param delete: if true then remove component and children from xml
        :return: 0=success, else error
        """
        curr_comp = self.current_component

        c_label = 1
        c_type = 1
        error = 0
        self.xml_c_label_default = self.c_label_default.get()
        self.xml_c_label_field = self.c_label_field.get()
        self.xml_c_type_field = self.c_type_field.get()
        self.xml_c_type_default = self.c_type_default.get()
        if self.xml_c_label_default in [" ", '', None]:
            self.xml_c_label_default = None
        if self.xml_c_type_field in [" ", "", None]:
            self.xml_c_type_field = None
        if self.xml_c_label_field in [" ", '', None]:
            self.xml_c_label_field = None
        if self.xml_c_type_default in [" ", '', None]:
            self.xml_c_type_default = None
        label_list = [self.xml_c_label_default, self.xml_c_label_field]
        label_value = next((el for el in label_list if el is not None), None)
        if not label_value:
            c_label = 0

        type_list = [self.xml_c_type_field, self.xml_c_type_default]
        type_value = next((el for el in type_list if el is not None), None)
        if not type_value:
            c_type = 0

        if c_label == 1 and c_type == 1:
            # enough info to save xml
            chk = self.add_component_to_xml_file(
                curr_comp=curr_comp, delete=delete)
            if not delete:
                # set these because it may be a 'new component' so need to
                # update the treeview node label
                self.controller.current_component["type"] = type_value
                self.controller.current_component["label"] = label_value

                # set the key fields as read-only so they can't change,
                # othewise it
                # is tricky to manage changes
                self.c_label_field.configure(state='disabled')
                self.c_type_field.configure(state='disabled')
                self.c_label_default.configure(state='disabled')
                self.c_type_default.configure(state='disabled')
            return chk
        elif c_label == 0 and c_type == 1 and not delete:
            messagebox.showerror(
                'Error', 'Component Label need to select to save Component ')
            return 1
        elif c_label == 1 and c_type == 0 and not delete:
            messagebox.showerror(
                'Error', 'Component Type need to select to save Component')
            return 1
        elif c_label == 0 and c_type == 0 and not delete:
            messagebox.showerror(
                "Error"
                , message='Component is not saved if Label and Type are empty')
            return 1

    def add_component_to_xml_file(self, curr_comp, delete=False):
        """
        Add/save a component to the XML file
        :param curr_comp: component to add/save
        :param delete: flag to delete component
        :param add: indicate adding component
        """

        found = 0
        if os.path.isfile(self.controller.common_tools.config_file_path):
            tree = ET.parse(self.save_path)
        else:
            messagebox.showerror("Error", "No arcmap_edit_config.xml is found")
            return 1

        root = tree.getroot()
        # check if there is a layer name
        for operation in root.iter('operation'):
            action = operation.get("action")
            if action == "Asset":
                for onelayer in operation.iter("layer"):
                    if onelayer.get("name") == self.current_layer["layer"]:
                        # if  components found within a layer
                        components = onelayer.find('component')
                        if components is None:
                            found = 0
                            # create a new one
                            components = ET.SubElement(onelayer, "component")
                        else:
                            # in case there is more than 1 components
                            all_component = []
                            comp_num = 1
                            for components in onelayer.iter("component"):
                                # find the label from default and fields
                                componentdefaults = components.find(
                                    "componentdefaults")
                                component_gisfields = components.find(
                                    "componentfields")

                                try:
                                    l = componentdefaults.find("label")
                                    label = l.text
                                    all_component.append(label)
                                except:
                                    l = component_gisfields.find("label")
                                    label = l.text
                                    all_component.append(label)

                                # check by the label to see any matching label and edit. if it is add , then dont check
                                ui_label = curr_comp["label"]
                                if ui_label == label:
                                    if delete:
                                        onelayer.remove(components)
                                        break
                                    # if we found the component
                                    found = 1

                                    if (
                                            self.xml_c_label_default in all_component and self.xml_c_label_default != label) or (
                                            self.xml_c_label_field in all_component and self.xml_c_label_field != label):
                                        messagebox.showerror("Error",
                                                             "Do not provide duplicate Component")
                                        return 1
                                    if componentdefaults is None:
                                        componentdefaults = ET.SubElement(
                                            components, "componentdefaults")

                                    break
                                comp_num += 1
                            if delete:
                                break
                            if found == 0:
                                # when add a new component, make sure that there is no duplicate label
                                if self.xml_c_label_default in all_component or self.xml_c_label_field in all_component:
                                    messagebox.showerror("Error",
                                                         "Do not provide duplicate Component")
                                    return 1

                                # when a new component is added, create a new component tag
                                components = ET.SubElement(onelayer,
                                                           "component")

                        component_gisfields = components.find("componentfields")
                        if component_gisfields is None:
                            # add gis fields to xml
                            component_gisfields = ET.SubElement(
                                components, "componentfields")
                        componentdefaults = components.find("componentdefaults")
                        if componentdefaults is None:
                            componentdefaults = ET.SubElement(
                                components, "componentdefaults")
                        # now apply gis and default field settings for the
                        # component
                        chk = self.add_update_elements(
                            component_gisfields, componentdefaults)
                        if chk != 0:
                            return chk
                        break

        dom = xml.dom.minidom.parseString(ET.tostring(root))
        xmlstring = dom.toprettyxml(encoding='UTF-8')
        dom_string = b'\n'.join(
            [s for s in xmlstring.splitlines() if s.strip()])
        with open(self.save_path, 'wb') as outfile:
            outfile.write(dom_string)
            outfile.close()
        return 0

    def add_update_elements(self, component_gisfields, component_defaults):
        """
        Add/update the gis field and default field defs for a component
        :param component_gisfields: the parent element for gis fields
        :param component_defaults: the parent element for default fields
        :return: 0 if success, else error code
        """
        tools = self.controller.common_tools
        # add/update elements
        # component label
        chk = tools.apply_value_to_element(
            "label", component_gisfields, component_defaults
            , self.c_label_field.get(), self.c_label_default.get()
            , "Component Name")
        if not chk:
            return 1

        # component GUID
        chk = tools.apply_value_to_element(
            "id", component_gisfields, component_defaults
            , self.component_id_field.get(), None
            , "Component ID")
        if not chk:
            return 1

        # component type
        chk = tools.apply_value_to_element(
            "component_type", component_gisfields, component_defaults
            , self.c_type_field.get(), self.c_type_default.get()
            , "Component Type")
        if not chk:
            return 1

        # dimension_unit
        chk = tools.apply_value_to_element(
            "dimension_unit", component_gisfields, component_defaults
            , self.c_dimension_unit_field.get()
            , self.cmb_dimension_unit_default.get(), "Measure Unit")
        if not chk:
            return 1

        # network measure type
        chk = tools.apply_value_to_element(
            "network_measure_type", component_gisfields, component_defaults
            , self.c_network_measure_type_field.get()
            , self.c_network_measure_type_default.get(), "Measure Type")
        if not chk:
            return 1

        # material type
        chk = tools.apply_value_to_element(
            "material_type", component_gisfields, component_defaults
            , self.c_material_type_field.get()
            , self.c_material_type_default.get(), "Material Type")
        if not chk:
            return 1

        # design life
        chk = tools.apply_value_to_element(
            "design_life", component_gisfields, component_defaults
            , self.c_design_life_field.get()
            , self.c_design_life_default.get(), "Useful Life")
        if not chk:
            return 1

        return 0


class DimensionFrame(tk.Frame):
    def __init__(self, parent, controller):
        """
        Network Measure (Dimensions) configuration page
        :param parent: The main window
        :type parent:
        :param controller: class from main window with common functions and
        variables
        :type controller:
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.delete_label = {}
        self.l_button = {}
        self.delete_button = {}
        self.configuration = controller.get_existing_xml()
        self.configured_layers = self.configuration.assetconfig
        self.layer_dict = controller.layer_dict

        self.asset_buttons = {}
        self.current_layer = None
        self.current_component = self.controller.current_component
        self.current_dimension = self.controller.current_dimension

        self.save_path = self.controller.common_tools.config_file_path

        self.xml_c_label_default = None
        self.xml_c_label_field = None
        self.xml_c_type_default = None
        self.xml_c_type_field = None

        font_normal = controller.font_normal
        font_header = controller.font_header
        font_strike = controller.font_strike

        # set padding between rows and columns
        xp = 1
        yp = 1
        # set width
        wid = 40
        # set the label justification 'sticky' - N, S, E, W
        st = tk.E

        tk.Label(self, text="Network Measure Configuration"
                 , font=font_header).grid(row=0, column=0, columnspan=3,
                                          sticky=EW)

        selected_layer = controller.selected_layer_name
        if not selected_layer or selected_layer.strip() == "":
            # No layer is selected so don't populate anything more
            # returning after creating label above so that a form exists
            return

        # Get the current xml config for the layer.  If there is none then
        # exit without building form further
        # User needs to first assign category and higher level config
        for config in self.configured_layers:
            if selected_layer == config["layer"]:
                self.current_layer = config
                break
        if not self.current_layer:
            self.config(cursor="")
            messagebox.showerror(
                "Error",
                "Assign Asset Category before setting Asset Components")
            return

        # set wait cursor as initial load can take time to read Assetic APIs
        self.config(cursor="watch")
        self.update()

        # Build some lists
        self.record_type_list = ["Addition", "Info", "Subtraction"]
        self.nm_type_list = [
            "Area", "Depth", "Diameter", "Height", "Length"
            , "NotDefined", "Quantity", "Volume", "Weight", "Width"]
        self.shape_list = ["Box", "Circle", "HorizontalCylinder", "Irregular"
            , "Rectangle", "Trapezoid", "VerticalCylinder"]
        self.unit_list = ["Metre", "Square Metre"]
        # self.unit_list = controller.assetic_api_tools.unit_list
        self.selected_record_type = tk.StringVar()
        self.selected_nm_type = tk.StringVar()
        self.selected_nm_unit = tk.StringVar()
        self.selected_shape = tk.StringVar()
        self.selected_length_unit = tk.StringVar()
        self.selected_width_unit = tk.StringVar()
        self.selected_height_unit = tk.StringVar()
        self.selected_depth_unit = tk.StringVar()
        self.selected_diameter_unit = tk.StringVar()

        # Add grid headers
        Label(self, text="GIS Field").grid(row=2, column=1, padx=xp, pady=yp)
        Label(self, text="Hardcode Value").grid(
            row=2, column=2, padx=xp, pady=yp)

        # Add labels for each core field, first column
        self.label_record_type = Label(self, text="Record Type*")
        self.label_nm_type = Label(self, text="Network Measure Type*")
        self.label_nm = Label(self, text="Network Measure")
        self.label_nm_unit = Label(self, text="Unit")
        self.label_shape_name = Label(self, text="Shape Name")
        self.label_length = Label(self, text="Length")
        self.label_length_unit = Label(self, text="Length Unit")
        self.label_width = Label(self, text="Width")
        self.label_width_unit = Label(self, text="Width Unit")
        self.label_height = Label(self, text="Height")
        self.label_height_unit = Label(self, text="Height Unit")
        self.label_depth = Label(self, text="Depth")
        self.label_depth_unit = Label(self, text="Depth Unit")
        self.label_diameter = Label(self, text="Diameter")
        self.label_diameter_unit = Label(self, text="Diameter Unit")

        self.layer_fields = list()
        if selected_layer in self.layer_dict:
            self.layer_fields = sorted(self.layer_dict[selected_layer]
                                       , key=lambda x: x.lower())
        self.layer_fields.insert(0, " ")

        # First create the comboboxes with GIS field list
        self.record_type_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.nm_type_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.nm_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.nm_unit_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.shape_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.length_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.length_unit_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.width_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.width_unit_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.height_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.height_unit_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.depth_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.depth_unit_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.diameter_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.diameter_unit_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)

        # Now the hardcode fields
        self.cmb_record_type_default = ttk.Combobox(
            self, values=self.record_type_list, width=wid - 3, state='readonly'
            , textvariable=self.selected_record_type)
        self.cmb_nm_type_default = ttk.Combobox(
            self, values=self.nm_type_list, width=wid - 3, state='readonly'
            , textvariable=self.selected_nm_type)
        self.nm_field_default = Entry(self, width=wid)
        self.cmb_nm_unit_default = ttk.Combobox(
            self, values=self.unit_list, width=wid - 3, state='readonly'
            , textvariable=self.selected_nm_unit)
        self.cmb_shape_default = ttk.Combobox(
            self, values=self.shape_list, width=wid - 3, state='readonly'
            , textvariable=self.selected_shape)
        self.length_default = Entry(self, width=wid)
        self.length_unit_default = ttk.Combobox(
            self, values=self.unit_list, width=wid - 3, state='readonly'
            , textvariable=self.selected_length_unit)
        self.width_default = Entry(self, width=wid)
        self.width_unit_default = ttk.Combobox(
            self, values=self.unit_list, width=wid - 3, state='readonly'
            , textvariable=self.selected_width_unit)
        self.height_default = Entry(self, width=wid)
        self.height_unit_default = ttk.Combobox(
            self, values=self.unit_list, width=wid - 3, state='readonly'
            , textvariable=self.selected_height_unit)
        # depth
        self.depth_default = Entry(self, width=wid)
        self.depth_unit_default = ttk.Combobox(
            self, values=self.unit_list, width=wid - 3, state='readonly'
            , textvariable=self.selected_depth_unit)
        # diameter
        self.diameter_default = Entry(self, width=wid)
        self.diameter_unit_default = ttk.Combobox(
            self, values=self.unit_list, width=wid - 3, state='readonly'
            , textvariable=self.selected_diameter_unit)

        # now populate with current data
        if self.controller.current_component and \
                self.controller.current_dimension:
            self.apply_current_config(
                self.controller.current_component
                , self.controller.current_dimension)
        clear = False
        if clear:
            self.nm_type_field.current(0)
            self.record_type_field.current(0)
            self.nm_field.current(0)
            self.nm_unit_field.current(0)
            self.length_field.current(0)
            self.length_unit_field.current(0)
            self.width_field.current(0)

        # position fields in grid
        self.label_record_type.grid(row=3, column=0, padx=xp, pady=yp
                                    , sticky=st)
        self.record_type_field.grid(row=3, column=1, padx=xp, pady=yp)
        self.cmb_record_type_default.grid(row=3, column=2, padx=xp, pady=yp)

        self.label_nm_type.grid(row=4, column=0, padx=xp, pady=yp, sticky=st)
        self.nm_type_field.grid(row=4, column=1, padx=xp, pady=yp)
        self.cmb_nm_type_default.grid(row=4, column=2, padx=xp, pady=yp)

        self.label_nm.grid(row=5, column=0, padx=xp, pady=yp, sticky=st)
        self.nm_field.grid(row=5, column=1, padx=xp, pady=yp)
        self.nm_field_default.grid(row=5, column=2, padx=xp, pady=yp)

        self.label_nm_unit.grid(row=6, column=0, padx=xp, pady=yp, sticky=st)
        self.nm_unit_field.grid(row=6, column=1, padx=xp, pady=yp)
        self.cmb_nm_unit_default.grid(row=6, column=2, padx=xp, pady=yp)

        self.label_shape_name.grid(row=7, column=0, padx=xp, pady=yp, sticky=st)
        self.shape_field.grid(row=7, column=1, padx=xp, pady=yp)
        self.cmb_shape_default.grid(row=7, column=2, padx=xp, pady=yp)

        self.label_length.grid(row=8, column=0, padx=xp, pady=yp, sticky=st)
        self.length_field.grid(row=8, column=1, padx=xp, pady=yp)
        self.length_default.grid(row=8, column=2, padx=xp, pady=yp)
        self.label_length_unit.grid(row=9, column=0, padx=xp, pady=yp,
                                    sticky=st)
        self.length_unit_field.grid(row=9, column=1, padx=xp, pady=yp)
        self.length_unit_default.grid(row=9, column=2, padx=xp, pady=yp)

        self.label_width.grid(row=10, column=0, padx=xp, pady=yp, sticky=st)
        self.width_field.grid(row=10, column=1, padx=xp, pady=yp)
        self.width_default.grid(row=10, column=2, padx=xp, pady=yp)
        self.label_width_unit.grid(row=11, column=0, padx=xp, pady=yp,
                                   sticky=st)
        self.width_unit_field.grid(row=11, column=1, padx=xp, pady=yp)
        self.width_unit_default.grid(row=11, column=2, padx=xp, pady=yp)

        self.label_height.grid(row=12, column=0, padx=xp, pady=yp, sticky=st)
        self.height_field.grid(row=12, column=1, padx=xp, pady=yp)
        self.height_default.grid(row=12, column=2, padx=xp, pady=yp)
        self.label_height_unit.grid(
            row=13, column=0, padx=xp, pady=yp, sticky=st)
        self.height_unit_field.grid(row=13, column=1, padx=xp, pady=yp)
        self.height_unit_default.grid(row=13, column=2, padx=xp, pady=yp)

        self.label_depth.grid(row=14, column=0, padx=xp, pady=yp, sticky=st)
        self.depth_field.grid(row=14, column=1, padx=xp, pady=yp)
        self.depth_default.grid(row=14, column=2, padx=xp, pady=yp)
        self.label_depth_unit.grid(row=15, column=0, padx=xp, pady=yp,
                                   sticky=st)
        self.depth_unit_field.grid(row=15, column=1, padx=xp, pady=yp)
        self.depth_unit_default.grid(row=15, column=2, padx=xp, pady=yp)

        self.label_diameter.grid(row=16, column=0, padx=xp, pady=yp, sticky=st)
        self.diameter_field.grid(row=16, column=1, padx=xp, pady=yp)
        self.diameter_default.grid(row=16, column=2, padx=xp, pady=yp)
        self.label_diameter_unit.grid(
            row=17, column=0, padx=xp, pady=yp, sticky=st)
        self.diameter_unit_field.grid(row=17, column=1, padx=xp, pady=yp)
        self.diameter_unit_default.grid(row=17, column=2, padx=xp, pady=yp)

        self.config(cursor="")

        # bind methods to some of the comboboxes
        self.cmb_record_type_default.bind(
            '<<ComboboxSelected>>', self.cmb_record_type_changed)
        self.cmb_nm_type_default.bind(
            '<<ComboboxSelected>>', self.cmb_nm_type_changed)
        self.cmb_shape_default.bind(self.cmb_shape_changed)

        # depending on the config, hide some rows
        # self.set_visible_widgets()

    def cmb_record_type_changed(self, event):
        """
        handle the record type combobox layer changed event
        Could be 'addition','info','subtraction'
        May need to check if the selection is valid - i.e. can we have 2
        addition definitions for the component?
        """
        # TODO
        pass

    def cmb_nm_type_changed(self, event):
        """
        handle the nm type combobox changed event
        Based on the nm_type remove fields not relevant
        e.g. width fields not relevant to 'length' type
        """
        # TODO
        pass

    def cmb_shape_changed(self, event):
        """
        handle the shape combobox changed event
        Based on the shape remove fields not relevant
        e.g. height fields not relevant to 'Rectangle' shape
        """
        # TODO
        pass

    def refresh(self, parent, controller):
        self.destroy()
        self.__init__(parent, controller)

    def apply_current_config(self, selected_component, selected_nm):
        """
        Apply the current XML config for the dimension to the form fields
        :return:
        """
        current_layer = self.current_layer
        if "components" not in current_layer:
            return

        current_comp = None
        for component in current_layer["components"]:
            comp_label = None
            comp_type = None
            if "defaults" in component:
                if "label" in component["defaults"]:
                    comp_label = component["defaults"]["label"]
                if "component_type" in component["defaults"]:
                    comp_type = component["defaults"]["component_type"]
            if "attributes" in component:
                if "label" in component["attributes"] \
                        and component["attributes"]["label"]:
                    comp_label = component["attributes"]["label"]
                if "component_type" in component["attributes"] and \
                        component["attributes"]["component_type"]:
                    comp_type = component["attributes"]["component_type"]

            if comp_label == selected_component["label"] and \
                    comp_type == selected_component["type"]:
                current_comp = component
                break

        if not current_comp:
            return

        if "dimensions" not in current_comp:
            return

        # have component, now get nm setting
        record_type = None
        nm_type = None
        current_nm = None
        for nm in current_comp["dimensions"]:
            if self.is_attribute_configured(nm, "record_type"):
                record_type = nm["attributes"]["record_type"]
            elif self.is_default_configured(nm, "record_type"):
                record_type = nm["defaults"]["record_type"]

            if self.is_attribute_configured(nm, "network_measure_type"):
                nm_type = nm["attributes"]["network_measure_type"]
            elif self.is_default_configured(nm, "network_measure_type"):
                nm_type = nm["defaults"]["network_measure_type"]

            if record_type == selected_nm["record_type"] and \
                    nm_type == selected_nm["network_measure_type"]:
                current_nm = nm
                break

        if not current_nm:
            return

        # set the combobox label based on current xml config
        # record_type - gis field
        if self.is_attribute_configured(current_nm, "record_type"):
            self.record_type_field.current(self.layer_fields.index(
                current_nm["attributes"]["record_type"]))

        # network measure type - gis field
        if self.is_attribute_configured(current_nm, "network_measure_type"):
            self.nm_type_field.current(self.layer_fields.index(
                current_nm["attributes"]["network_measure_type"]))

        # network measure  - gis field
        if self.is_attribute_configured(current_nm, "network_measure"):
            self.nm_field.current(self.layer_fields.index(
                current_nm["attributes"]["network_measure"]))

        # network measure unit - gis field
        if self.is_attribute_configured(current_nm, "unit"):
            self.nm_unit_field.current(self.layer_fields.index(
                current_nm["attributes"]["unit"]))

        # shape - gis field
        if self.is_attribute_configured(current_nm, "shape_name"):
            self.shape_field.current(self.layer_fields.index(
                current_nm["attributes"]["shape_name"]))

        # length - gis field
        if self.is_attribute_configured(current_nm, "length"):
            self.length_field.current(self.layer_fields.index(
                current_nm["attributes"]["length"]))

        # length unit - gis field
        if self.is_attribute_configured(current_nm, "length_unit"):
            self.length_unit_field.current(self.layer_fields.index(
                current_nm["attributes"]["length_unit"]))

        # width - gis field
        if self.is_attribute_configured(current_nm, "width"):
            self.width_field.current(self.layer_fields.index(
                current_nm["attributes"]["width"]))

        # width unit - gis field
        if self.is_attribute_configured(current_nm, "width_unit"):
            self.width_unit_field.current(self.layer_fields.index(
                current_nm["attributes"]["width_unit"]))

        # height - gis field
        if self.is_attribute_configured(current_nm, "height"):
            self.height_field.current(self.layer_fields.index(
                current_nm["attributes"]["height"]))

        # height unit - gis field
        if self.is_attribute_configured(current_nm, "height_unit"):
            self.height_unit_field.current(self.layer_fields.index(
                current_nm["attributes"]["height_unit"]))

        # depth - gis field
        if self.is_attribute_configured(current_nm, "depth"):
            self.depth_field.current(self.layer_fields.index(
                current_nm["attributes"]["depth"]))

        # depth unit - gis field
        if self.is_attribute_configured(current_nm, "depth_unit"):
            self.depth_unit_field.current(self.layer_fields.index(
                current_nm["attributes"]["depth_unit"]))

        # diameter - gis field
        if self.is_attribute_configured(current_nm, "diameter"):
            self.diameter_field.current(self.layer_fields.index(
                current_nm["attributes"]["diameter"]))

        # diameter unit - gis field
        if self.is_attribute_configured(current_nm, "diameter_unit"):
            self.diameter_unit_field.current(self.layer_fields.index(
                current_nm["attributes"]["diameter_unit"]))

        # Now set defaults if set
        # record type - hardcode field
        if self.is_default_configured(current_nm, "record_type"):
            self.cmb_record_type_default.current(self.record_type_list.index(
                current_nm["defaults"]["record_type"]))

        # network measure type - hardcode field
        if self.is_default_configured(current_nm, "network_measure_type"):
            self.cmb_nm_type_default.current(self.nm_type_list.index(
                current_nm["defaults"]["network_measure_type"]))

        # network measure - hardcode field
        if self.is_default_configured(current_nm, "network_measure"):
            self.nm_field_default.insert(
                0, current_nm["defaults"]["network_measure"])

        # network measure unit - hardcode field
        if self.is_default_configured(current_nm, "unit"):
            self.cmb_nm_unit_default.current(self.unit_list.index(
                current_nm["defaults"]["unit"]))

        # network measure unit - hardcode field
        if self.is_default_configured(current_nm, "shape_name"):
            self.cmb_shape_default.current(self.shape_list.index(
                current_nm["defaults"]["shape_name"]))

        # length - hardcode field
        if self.is_default_configured(current_nm, "length"):
            self.length_default.insert(
                0, current_nm["defaults"]["length"])

        # length unit - hardcode field
        if self.is_default_configured(current_nm, "length_unit"):
            self.length_unit_default.current(self.unit_list.index(
                current_nm["defaults"]["length_unit"]))

        # width - hardcode field
        if self.is_default_configured(current_nm, "width"):
            self.width_default.insert(
                0, current_nm["defaults"]["width"])

        # width unit - hardcode field
        if self.is_default_configured(current_nm, "width_unit"):
            self.width_unit_default.current(self.unit_list.index(
                current_nm["defaults"]["width_unit"]))

        # height - hardcode field
        if self.is_default_configured(current_nm, "height"):
            self.width_default.insert(
                0, current_nm["defaults"]["height"])

        # height unit - hardcode field
        if self.is_default_configured(current_nm, "height_unit"):
            self.height_unit_default.current(self.unit_list.index(
                current_nm["defaults"]["height_unit"]))

        # depth - hardcode field
        if self.is_default_configured(current_nm, "depth"):
            self.depth_default.insert(
                0, current_nm["defaults"]["depth"])

        # depth unit - hardcode field
        if self.is_default_configured(current_nm, "depth_unit"):
            self.depth_unit_default.current(self.unit_list.index(
                current_nm["defaults"]["depth_unit"]))

        # diameter - hardcode field
        if self.is_default_configured(current_nm, "diameter"):
            self.diameter_default.insert(
                0, current_nm["defaults"]["diameter"])

        # diameter unit - hardcode field
        if self.is_default_configured(current_nm, "diameter_unit"):
            self.diameter_unit_default.current(self.unit_list.index(
                current_nm["defaults"]["diameter_unit"]))

        # set the fields used to identify the config as read only so they
        # can't be changed.  If they change then we need to manage the
        # original and new value so we can find the right entry in the xml and
        # change it.  Possible, but not an initial priority
        self.nm_type_field.configure(state='disabled')
        self.record_type_field.configure(state='disabled')
        self.cmb_nm_type_default.configure(state='disabled')
        self.cmb_record_type_default.configure(state='disabled')
        self.shape_field.configure(state='disabled')
        self.cmb_shape_default.configure(state='disabled')

    def set_visible_widgets(self):
        """
        Depending on current selection of record type, share etc remove
        fields that are not relevant, make others visible
        :return:
        """
        #
        record_type = self.record_type_field.get()
        if not record_type:
            record_type = self.cmb_record_type_default.get()
        if record_type and record_type.lower() == "info":
            # don't set network measure if info record
            self.label_nm.grid_remove()
            self.nm_field.grid_remove()
            self.nm_field_default.grid_remove()
        else:
            # ensure network measure field is visible
            self.label_nm.grid()
            self.nm_field.grid()
            self.nm_field_default.grid()

        shape_type = self.shape_field.get()
        if not shape_type:
            shape_type = self.cmb_shape_default.get()
        if shape_type and shape_type.strip() != "":
            # there is a shape so we need the fields for the shapes
            pass
        else:
            # no shape so hide the shape fields
            self.label_length.grid_remove()
            self.length_field.grid_remove()
            self.length_default.grid_remove()
            self.label_length_unit.grid_remove()
            self.length_unit_field.grid_remove()
            self.length_unit_default.grid_remove()

            self.label_width.grid_remove()
            self.width_field.grid_remove()
            self.width_default.grid_remove()
            self.label_width_unit.grid_remove()
            self.width_unit_field.grid_remove()
            self.width_unit_default.grid_remove()

            self.label_height.grid_remove()
            self.height_field.grid_remove()
            self.height_default.grid_remove()
            self.label_height_unit.grid_remove()
            self.height_unit_field.grid_remove()
            self.height_unit_default.grid_remove()

    def is_attribute_configured(self, config, field):
        """
        Convenience method just to test if the field has a xml configuration
        :param config: the xml config dict for the layer
        :type config: dict
        :param field: the xml field to test
        :type field: string
        :return: True if the field has an xml config with a valid GIS field
        :rtype: Bool
        """
        if field in config['attributes'] and \
                config['attributes'][field] in self.layer_fields:
            return True
        else:
            return False

    def is_default_configured(self, config, field, within_list=None):
        """
        Convenience method just to test if the a field has an xml configuration
        :param config: the xml config dict for the layer
        :type config: dict
        :param field: the xml field to test
        :type field: string
        :param within_list: is the value in the list
        :type within_list: list
        :return: True if the field has an xml config with a valid GIS field
        :rtype: Bool
        """
        if field in config['defaults']:
            if isinstance(within_list, list):
                if not config['defaults'][field] in within_list:
                    return False
            # the field is configured and in the list
            return True
        else:
            return False

    def save_dimension_info(self, delete=False):
        """
        Save the current network measure frame
        :param delete: if true then the record is removed from XML
        :return: 0=success else failure
        """
        current_dim = self.current_dimension
        current_comp = self.current_component
        record_type = self.record_type_field.get()
        if not record_type:
            record_type = self.cmb_record_type_default.get()
        nm_type = self.nm_type_field.get()
        if not nm_type:
            nm_type = self.cmb_nm_type_default.get()

        if not record_type and not nm_type:
            if not delete:
                # assume nothing to save
                messagebox.showerror(
                    'Error', 'Record Type and Measure Type not set')
                return 1
            else:
                return 0

        self.controller.current_dimension["record_type"] = record_type
        self.controller.current_dimension["network_measure_type"] = nm_type

        chk = self.save_dimension_to_xml_file(
            curr_dim=current_dim, curr_comp=current_comp, delete=delete)

        # set the fields used to identify the config as read only so they
        # can't be changed - makes it harder to manage
        self.nm_type_field.configure(state='disabled')
        self.record_type_field.configure(state='disabled')
        self.cmb_nm_type_default.configure(state='disabled')
        self.cmb_record_type_default.configure(state='disabled')

        return chk

    def save_dimension_to_xml_file(self, curr_dim, curr_comp, delete=False):
        """
        Save dimension to xml file using passed in dimension
        :param curr_dim: the dimension definition to save
        :param curr_comp: the component that the dim is part of
        :param delete: if true then remove the current dimension setting from
        the xml file
        :return: 0=success, else failure
        """
        if os.path.isfile(self.controller.common_tools.config_file_path):
            tree = ET.parse(self.save_path)
        else:
            messagebox.showerror("Error", "No arcmap_edit_config.xml is found")
            return 1

        root = tree.getroot()
        # check if there is a layer name
        for operation in root.iter('operation'):
            action = operation.get("action")
            if action == "Asset":
                for onelayer in operation.iter("layer"):
                    if onelayer.get("name") == self.current_layer["layer"]:
                        # if  components found within a layer
                        components = onelayer.find('component')
                        if components is None:
                            messagebox.showerror(
                                "Error"
                                , "Unable to edit because existing component "
                                  "not found"
                            )
                            return 1
                        component = None
                        for components in onelayer.iter("component"):
                            # find the label from default and fields
                            componentdefaults = components.find(
                                "componentdefaults")
                            component_corefields = components.find(
                                "componentfields")

                            try:
                                l = componentdefaults.find("label")
                                label = l.text
                            except:
                                l = component_corefields.find("label")
                                label = l.text

                            if curr_comp["label"] == label:
                                # we found the component
                                component = components
                                break

                        if not component:
                            messagebox.showerror(
                                "Error"
                                ,
                                "Unable to edit because existing component not found"
                            )
                            return 1

                        # we have the component - now for the dimension
                        curr_xml_dim = None
                        for xml_nm in component.iter("dimension"):
                            xml_dim_fields = xml_nm.find("dimensionfields")
                            xml_dim_defaults = xml_nm.find("dimensiondefaults")
                            xml_record_type = None
                            xml_nm_type = None
                            if xml_dim_fields:
                                xml_record_type = xml_dim_fields.find(
                                    "record_type")
                                xml_nm_type = xml_dim_fields.find(
                                    "network_measure_type")
                            if xml_dim_defaults:
                                if not xml_record_type:
                                    xml_record_type = xml_dim_defaults.find(
                                        "record_type")
                                if not xml_nm_type:
                                    xml_nm_type = xml_dim_defaults.find(
                                        "network_measure_type")
                            if xml_record_type == None or xml_nm_type == None:
                                # need both for a match
                                continue

                            if xml_record_type.text == curr_dim["record_type"] \
                                    and xml_nm_type.text == curr_dim[
                                "network_measure_type"]:
                                # found the dim
                                curr_xml_dim = xml_nm
                                break

                        if delete:
                            if curr_xml_dim != None:
                                # remove the dimension from the component
                                component.remove(curr_xml_dim)
                        else:
                            if curr_xml_dim == None:
                                # create a new dim in xml
                                curr_xml_dim = ET.SubElement(
                                    component, "dimension")
                            # now apply the updates
                            chk = self.add_update_elements(curr_xml_dim)
                            if chk != 0:
                                return chk

        dom = xml.dom.minidom.parseString(ET.tostring(root))
        xmlstring = dom.toprettyxml(encoding='UTF-8')
        dom_string = b'\n'.join(
            [s for s in xmlstring.splitlines() if s.strip()])
        with open(self.save_path, 'wb') as outfile:
            outfile.write(dom_string)
            outfile.close()
        return 0

    def add_update_elements(self, curr_xml_dim):
        """
        Add/update the gis field and default field defs for a dimension
        :param curr_xml_dim:
        :return:
        """

        xml_dim_fields = curr_xml_dim.find("dimensionfields")
        if xml_dim_fields is None:
            # add the dim field
            xml_dim_fields = ET.SubElement(curr_xml_dim, "dimensionfields")
        xml_dim_defaults = curr_xml_dim.find("dimensiondefaults")
        if xml_dim_defaults is None:
            # add the dim defaults
            xml_dim_defaults = ET.SubElement(curr_xml_dim, "dimensiondefaults")

        tools = self.controller.common_tools
        # add/update elements
        # record type
        chk = tools.apply_value_to_element(
            "record_type", xml_dim_fields, xml_dim_defaults
            , self.record_type_field.get(), self.cmb_record_type_default.get()
            , self.label_record_type.cget("text"))
        if not chk:
            return 1

        # network_measure_type
        chk = tools.apply_value_to_element(
            "network_measure_type", xml_dim_fields, xml_dim_defaults
            , self.nm_type_field.get(), self.cmb_nm_type_default.get()
            , self.label_nm_type.cget("text"))
        if not chk:
            return 1

        # network_measure
        chk = tools.apply_value_to_element(
            "network_measure", xml_dim_fields, xml_dim_defaults
            , self.nm_field.get(), self.nm_field_default.get()
            , self.label_nm.cget("text"))
        if not chk:
            return 1

        # unit
        chk = tools.apply_value_to_element(
            "unit", xml_dim_fields, xml_dim_defaults
            , self.nm_unit_field.get(), self.cmb_nm_unit_default.get()
            , self.label_nm_unit.cget("text"))
        if not chk:
            return 1

        # shape_name
        chk = tools.apply_value_to_element(
            "shape_name", xml_dim_fields, xml_dim_defaults
            , self.shape_field.get(), self.cmb_shape_default.get()
            , self.label_shape_name.cget("text"))
        if not chk:
            return 1

        # length
        chk = tools.apply_value_to_element(
            "length", xml_dim_fields, xml_dim_defaults
            , self.length_field.get(), self.length_default.get()
            , self.label_length.cget("text"))
        if not chk:
            return 1

        # length unit
        chk = tools.apply_value_to_element(
            "length_unit", xml_dim_fields, xml_dim_defaults
            , self.length_unit_field.get(), self.length_unit_default.get()
            , self.label_length_unit.cget("text"))
        if not chk:
            return 1

        # width
        chk = tools.apply_value_to_element(
            "width", xml_dim_fields, xml_dim_defaults
            , self.width_field.get(), self.width_default.get()
            , self.label_width.cget("text"))
        if not chk:
            return 1

        # width unit
        chk = tools.apply_value_to_element(
            "width_unit", xml_dim_fields, xml_dim_defaults
            , self.width_unit_field.get(), self.width_unit_default.get()
            , self.label_width_unit.cget("text"))
        if not chk:
            return 1

        # height
        chk = tools.apply_value_to_element(
            "height", xml_dim_fields, xml_dim_defaults
            , self.height_field.get(), self.height_default.get()
            , self.label_height.cget("text"))
        if not chk:
            return 1

        # height unit
        chk = tools.apply_value_to_element(
            "height_unit", xml_dim_fields, xml_dim_defaults
            , self.height_unit_field.get(), self.height_unit_default.get()
            , self.label_height_unit.cget("text"))
        if not chk:
            return 1

        # depth
        chk = tools.apply_value_to_element(
            "depth", xml_dim_fields, xml_dim_defaults
            , self.depth_field.get(), self.depth_default.get()
            , self.label_depth.cget("text"))
        if not chk:
            return 1

        # depth unit
        chk = tools.apply_value_to_element(
            "depth_unit", xml_dim_fields, xml_dim_defaults
            , self.depth_unit_field.get(), self.depth_unit_default.get()
            , self.label_depth_unit.cget("text"))
        if not chk:
            return 1

        # diameter
        chk = tools.apply_value_to_element(
            "diameter", xml_dim_fields, xml_dim_defaults
            , self.diameter_field.get(), self.diameter_default.get()
            , self.label_diameter.cget("text"))
        if not chk:
            return 1

        # diameter unit
        chk = tools.apply_value_to_element(
            "diameter_unit", xml_dim_fields, xml_dim_defaults
            , self.diameter_unit_field.get(), self.diameter_unit_default.get()
            , self.label_diameter_unit.cget("text"))
        if not chk:
            return 1

        return 0


class AddressFrame(tk.Frame):
    def __init__(self, parent, controller):
        """
        Address configuration page
        :param parent: The main window
        :type parent:
        :param controller: class from main window with common functions and
        variables
        :type controller:
        :param use_existing_file: read existing xml or create a new one?
        :type use_existing_file: boolean
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.delete_label = {}
        self.l_button = {}
        self.delete_button = {}
        self.configuration = controller.get_existing_xml()
        self.configured_layers = self.configuration.assetconfig
        self.layer_dict = controller.layer_dict

        self.asset_buttons = {}
        self.current_layer = None

        self.save_path = self.controller.common_tools.config_file_path

        font_normal = controller.font_normal
        font_header = controller.font_header
        font_strike = controller.font_strike

        # set padding between rows and columns
        xp = 1
        yp = 1
        # set the label justification 'sticky' - N, S, E, W
        st = tk.E

        tk.Label(self, text="Asset Address Configuration"
                 , font=font_header).grid(row=0, column=0, columnspan=3,
                                          sticky=EW)

        selected_layer = controller.selected_layer_name
        if not selected_layer or selected_layer.strip() == "":
            # No layer is selected so don't populate anything more
            # returning after creating label above so that a form exists
            return

        # Get the current xml config for the layer.  If there is none the
        # exit without building form further
        # User needs to first assign category and higher level config
        for config in self.configured_layers:
            if selected_layer == config["layer"]:
                self.current_layer = config
                break
        if not self.current_layer:
            self.config(cursor="")
            messagebox.showerror(
                "Error",
                "Assign Asset Category before setting Asset Address")
            return

        # local variable just to keep the name a bit shorter
        current_layer = self.current_layer

        # set wait cursor as initial load can take time to read Assetic APIs
        self.config(cursor="wait")
        self.update()

        # Get component Type list

        # Add grid headers
        Label(self, text="GIS Field").grid(row=2, column=1, padx=xp, pady=yp)
        Label(self, text="Hardcode Value").grid(
            row=2, column=2, padx=xp, pady=yp)

        # Add labels for each core field, first column
        Label(self, text="Street Number").grid(row=3, column=0, padx=xp,
                                               pady=yp, sticky=st)
        Label(self, text="Street Address").grid(row=4, column=0, padx=xp,
                                                pady=yp, sticky=st)
        Label(self, text="City/Suburb").grid(row=5, column=0, padx=xp,
                                             pady=yp, sticky=st)
        Label(self, text="State").grid(row=6, column=0, padx=xp, pady=yp
                                       , sticky=st)
        Label(self, text="Post Code").grid(row=7, column=0, padx=xp, pady=yp
                                           , sticky=st)
        Label(self, text="Country").grid(row=8, column=0, padx=xp,
                                         pady=yp, sticky=st)

        self.layer_fields = list()
        if selected_layer in self.layer_dict:
            self.layer_fields = sorted(self.layer_dict[selected_layer]
                                       , key=lambda x: x.lower())
        self.layer_fields.insert(0, " ")

        # set width
        wid = 40

        # First create the comboboxes with GIS field list
        self.street_num_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.street_name_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.suburb_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.state_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.postcode_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.country_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)

        # Now the hardcode fields
        self.street_num_default = Entry(self, width=wid)
        self.street_name_default = Entry(self, width=wid)
        self.suburb_default = Entry(self, width=wid)
        self.state_default = Entry(self, width=wid)
        self.postcode_default = Entry(self, width=wid)
        self.country_default = Entry(self, width=wid)

        self.apply_current_config()

        # might need capacity to clear fields in the future?
        clear = False
        if clear:
            self.street_name_field.current(0)
            self.street_num_field.current(0)
            self.suburb_field.current(0)
            self.state_field.current(0)
            self.postcode_field.current(0)
            self.country_field.current(0)

        # position fields in grid
        self.street_num_field.grid(row=3, column=1, padx=xp, pady=yp)
        self.street_num_default.grid(row=3, column=2, padx=xp, pady=yp)

        self.street_name_field.grid(row=4, column=1, padx=xp, pady=yp)
        self.street_name_default.grid(row=4, column=2, padx=xp, pady=yp)

        self.suburb_field.grid(row=5, column=1, padx=xp, pady=yp)
        self.suburb_default.grid(row=5, column=2, padx=xp, pady=yp)

        self.state_field.grid(row=6, column=1, padx=xp, pady=yp)
        self.state_default.grid(row=6, column=2, padx=xp, pady=yp)

        self.postcode_field.grid(row=7, column=1, padx=xp, pady=yp)
        self.postcode_default.grid(row=7, column=2, padx=xp, pady=yp)

        self.country_field.grid(row=8, column=1, padx=xp, pady=yp)
        self.country_default.grid(row=8, column=2, padx=xp, pady=yp)

        self.config(cursor="")

    def refresh(self, parent, controller):
        self.destroy()
        self.__init__(parent, controller)

    def apply_current_config(self):
        """
        Apply the current XML config for the address to the form fields
        :return:
        """
        current_layer = self.current_layer
        xml_address_fields = dict()
        xml_address_defaults = dict()
        if "addressfields" in current_layer:
            xml_address_fields = current_layer["addressfields"]
        if "addressdefaults" in current_layer:
            xml_address_defaults = current_layer["addressdefaults"]

        if not len(xml_address_defaults) == 0 and len(xml_address_fields) == 0:
            # No address data so return
            return

        # set the combobox label based on current xml config
        # street number - gis field
        if "street_number" in xml_address_fields:
            self.street_num_field.current(self.layer_fields.index(
                xml_address_fields["street_number"]))

        # street address - gis field
        if "street_address" in xml_address_fields:
            self.street_name_field.current(self.layer_fields.index(
                xml_address_fields["street_address"]))

        # suburb - gis field
        if "city_suburb" in xml_address_fields:
            self.suburb_field.current(self.layer_fields.index(
                xml_address_fields["city_suburb"]))

        # state - gis field
        if "state" in xml_address_fields:
            self.state_field.current(self.layer_fields.index(
                xml_address_fields["state"]))

        # postcode - gis field
        if "zip_postcode" in xml_address_fields:
            self.postcode_field.current(self.layer_fields.index(
                xml_address_fields["zip_postcode"]))

        # country - gis field
        if "country" in xml_address_fields:
            self.country_field.current(self.layer_fields.index(
                xml_address_fields["country"]))

        # Now set defaults if set
        # street number - hardcode field
        if "street_number" in xml_address_defaults:
            self.street_num_default.insert(
                0, xml_address_defaults["street_number"])

        # street name - hardcode field
        if "street_name" in xml_address_defaults:
            self.street_name_default.insert(
                0, xml_address_defaults["street_name"])

        # suburb - hardcode field
        if "city_suburb" in xml_address_defaults:
            self.suburb_default.insert(
                0, xml_address_defaults["city_suburb"])

        # state - hardcode field
        if "state" in xml_address_defaults:
            self.state_default.insert(
                0, xml_address_defaults["state"])
        # postcode - hardcode field
        if "zip_postcode" in xml_address_defaults:
            self.postcode_default.insert(
                0, xml_address_defaults["zip_postcode"])

        # country - hardcode field
        if "country" in xml_address_defaults:
            self.country_default.insert(
                0, xml_address_defaults["country"])

    def is_attribute_configured(self, config, field):
        """
        Convenience method just to test if the a field has an xml configuration
        :param config: the xml config dict for the layer
        :type config: dict
        :param field: the xml field to test
        :type field: string
        :return: True if the field has an xml config with a valid GIS field
        :rtype: Bool
        """
        if field in config['attributes'] and \
                config['attributes'][field] in self.layer_fields:
            return True
        else:
            return False

    def is_default_configured(self, config, field, within_list=None):
        """
        Convenience method just to test if the a field has an xml configuration
        :param config: the xml config dict for the layer
        :type config: dict
        :param field: the xml field to test
        :type field: string
        :param within_list: is the value in the list
        :type within_list: list
        :return: True if the field has an xml config with a valid GIS field
        :rtype: Bool
        """
        if field in config['defaults']:
            if isinstance(within_list, list):
                if not config['defaults'][field] in within_list:
                    return False
            # the field is configured and in the list
            return True
        else:
            return False

    def save_address_info(self, delete=False):
        """
        save the Asset Address information from the form
        :param delete: delete the record if True, default is False
        :return: 0 if success, else non zero if error

        """
        chk = self.save_address_to_xml_file(delete)
        return chk

    def save_address_to_xml_file(self, delete=False):
        """
        Add/save a address to the XML file, or delete
        :param delete: Remove address settings from XML? Default is False
        :returns: 0 if success, else non zero
        """

        if os.path.isfile(self.controller.common_tools.config_file_path):
            tree = ET.parse(self.save_path)

        else:
            messagebox.showerror(
                "Error"
                , "Configuration file {0} not found".format(self.save_path))
            return 1

        root = tree.getroot()
        # check if there is a layer name
        xml_layer = None
        for operation in root.iter('operation'):
            action = operation.get("action")
            if action == "Asset":
                for onelayer in operation.iter("layer"):
                    if onelayer.get("name") == self.current_layer["layer"]:
                        xml_layer = onelayer
                        break
        if not xml_layer:
            return 0

        # Get the elements for GIS and default fields
        addr_fields = xml_layer.find("addressfields")
        addr_defaults = xml_layer.find("addressdefaults")
        # create the elements if undefined, or delete if defined and in del mode
        if addr_fields is None and not delete:
            # add the address fields node
            addr_fields = ET.SubElement(xml_layer, "addressfields")
        elif addr_fields is not None and delete:
            xml_layer.remove(addr_fields)

        if addr_defaults is None and not delete:
            # add the address fields node
            addr_defaults = ET.SubElement(xml_layer, "addressdefaults")
        elif addr_defaults is not None and delete:
            xml_layer.remove(addr_defaults)

        if not delete:
            tools = self.controller.common_tools
            # apply values to the elements
            # street number field
            chk = tools.apply_value_to_element(
                "street_number", addr_fields, addr_defaults
                , self.street_num_field.get(), self.street_num_default.get()
                , "Street Number")
            if not chk:
                return 1

            # street number field
            chk = tools.apply_value_to_element(
                "street_number", addr_fields, addr_defaults
                , self.street_num_field.get(), self.street_num_default.get()
                , "Street Number")
            if not chk:
                return 1

            # street name field
            chk = tools.apply_value_to_element(
                "street_name", addr_fields, addr_defaults
                , self.street_name_field.get(), self.street_name_default.get()
                , "Street Name")
            if not chk:
                return 1

            # suburb field
            chk = tools.apply_value_to_element(
                "city_suburb", addr_fields, addr_defaults
                , self.suburb_field.get(), self.suburb_default.get()
                , "City/Suburb")
            if not chk:
                return 1

            # gis - state field
            chk = tools.apply_value_to_element(
                "state", addr_fields, addr_defaults
                , self.state_field.get(), self.state_default.get()
                , "State")
            if not chk:
                return 1

            # country field
            chk = tools.apply_value_to_element(
                "country", addr_fields, addr_defaults
                , self.country_field.get(), self.country_default.get()
                , "Country")
            if not chk:
                return 1

            # postcode field
            chk = tools.apply_value_to_element(
                "zip_postcode", addr_fields, addr_defaults
                , self.state_field.get(), self.state_default.get()
                , "Postcode")
            if not chk:
                return 1

        dom = xml.dom.minidom.parseString(ET.tostring(root))
        xmlstring = dom.toprettyxml(encoding='UTF-8')
        dom_string = b'\n'.join(
            [s for s in xmlstring.splitlines() if s.strip()])
        with open(self.save_path, 'wb') as outfile:
            outfile.write(dom_string)
            outfile.close()
        return 0


class AssetFLAssociationFrame(tk.Frame):
    def __init__(self, parent, controller):
        """
        Association of Asset to Functional Location configuration page
        :param parent: The main window
        :type parent:
        :param controller: class from main window with common functions and
        variables
        :type controller:
        :param use_existing_file: read existing xml or create a new one?
        :type use_existing_file: boolean
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.delete_label = {}
        self.l_button = {}
        self.delete_button = {}
        self.configuration = controller.get_existing_xml()
        self.configured_layers = self.configuration.assetconfig
        self.layer_dict = controller.layer_dict

        self.asset_buttons = {}
        self.current_layer = None
        # self.selected_fl_type = tk.StringVar()

        self.save_path = self.controller.common_tools.config_file_path

        font_normal = controller.font_normal
        font_header = controller.font_header
        font_strike = controller.font_strike

        # set padding between rows and columns
        xp = 1
        yp = 1
        # set label justification 'sticky' N,S,E,W
        st = tk.E

        tk.Label(self, text="Asset Association with Functional Location "
                            "Configuration"
                 , font=font_header).grid(row=0, column=0, columnspan=2,
                                          sticky=EW)

        selected_layer = controller.selected_layer_name
        if not selected_layer or selected_layer.strip() == "":
            # No layer is selected so don't populate anything more
            # returning after creating label above so that a form exists
            return

        # Get the current xml config for the layer.  If there is none the
        # exit without building form further
        # User needs to first assign category and higher level config
        for config in self.configured_layers:
            if selected_layer == config["layer"]:
                self.current_layer = config
                break
        if not self.current_layer:
            self.config(cursor="")
            messagebox.showerror(
                "Error",
                "Assign Asset Category before setting Functional Location "
                "Association")
            return

        # local variable just to keep the name a bit shorter
        current_layer = self.current_layer

        # set wait cursor as initial load can take time to read Assetic APIs
        self.config(cursor="wait")
        self.update()

        # Get FL Type list
        # self.fl_type_list = self.controller.assetic_api_tools.fl_type_list

        # Add grid headers
        Label(self, text="GIS Field").grid(row=2, column=1, padx=xp, pady=yp)
        # Label(self, text="Hardcode Value").grid(
        #    row=2, column=2, padx=xp, pady=yp)

        # Add labels for each core field, first column
        Label(self, text="Functional Location Id").grid(
            row=3, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Functional Location Name").grid(
            row=4, column=0, padx=xp, pady=yp, sticky=st)
        Label(self, text="Functional Location Type").grid(
            row=5, column=0, padx=xp, pady=yp, sticky=st)

        self.layer_fields = list()
        if selected_layer in self.layer_dict:
            self.layer_fields = sorted(self.layer_dict[selected_layer]
                                       , key=lambda x: x.lower())
        self.layer_fields.insert(0, " ")

        # set width
        wid = 40

        # First create the comboboxes with GIS field list
        self.fl_id_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.fl_name_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)
        self.fl_type_field = ttk.Combobox(
            self, values=self.layer_fields, width=wid)

        # Now the hardcode fields
        """
        self.fl_id_default = Entry(self, width=wid)
        self.fl_name_default = Entry(self, width=wid)
        self.cmb_fl_type_default = ttk.Combobox(
            self, values=self.fl_type_list, width=wid-3
            , textvariable=self.selected_fl_type)
        """
        self.apply_current_config()

        # position fields in grid
        self.fl_id_field.grid(row=3, column=1, padx=xp, pady=yp)
        # self.fl_id_default.grid(row=3, column=2, padx=xp, pady=yp)

        self.fl_name_field.grid(row=4, column=1, padx=xp, pady=yp)
        # self.fl_name_default.grid(row=4, column=2, padx=xp, pady=yp)

        self.fl_type_field.grid(row=5, column=1, padx=xp, pady=yp)
        # self.cmb_fl_type_default.grid(row=5, column=2, padx=xp, pady=yp)

        self.config(cursor="")

    def refresh(self, parent, controller):
        self.destroy()
        self.__init__(parent, controller)

    def apply_current_config(self):
        """
        Apply the current XML config for the fl to the form fields
        :return:
        """
        current_layer = self.current_layer

        if "functionallocation" not in current_layer:
            return

        xml_fl_fields = current_layer["functionallocation"]

        # set the combobox label based on current xml config
        # fl id - gis field
        if "functional_location_id" in xml_fl_fields:
            self.fl_id_field.current(self.layer_fields.index(
                xml_fl_fields["functional_location_id"]))

        if "functional_location_name" in xml_fl_fields:
            self.fl_name_field.current(self.layer_fields.index(
                xml_fl_fields["functional_location_name"]))

        if "functional_location_type" in xml_fl_fields:
            self.fl_type_field.current(self.layer_fields.index(
                xml_fl_fields["functional_location_type"]))

    def save_fl_association_info(self, delete=False):
        """
        initiate save the Asset FL association information from the form
        this is where we do some preliminary validation
        """
        chk = self.add_fl_association_to_xml_file(delete)
        return chk

    def add_fl_association_to_xml_file(self, delete=False):
        """
        Add/save a FL association to the XML file
        """

        if os.path.isfile(self.controller.common_tools.config_file_path):
            tree = ET.parse(self.save_path)
        else:
            messagebox.showerror(
                "Error"
                , "Configuration file [{0}] not found".format(
                    self.save_path)
            )
            return 1

        root = tree.getroot()
        # check if there is a layer name
        xml_layer = None
        for operation in root.iter('operation'):
            action = operation.get("action")
            if action == "Asset":
                for onelayer in operation.iter("layer"):
                    if onelayer.get("name") == self.current_layer["layer"]:
                        xml_layer = onelayer
                        break
        if not xml_layer:
            return 0

        fl_fields = xml_layer.find("functional_location")

        if fl_fields is None and not delete:
            # add the functional fields node
            fl_fields = ET.SubElement(xml_layer, "functional_location")
        elif fl_fields is not None and delete:
            # remove setting from xml
            xml_layer.remove(fl_fields)

        if not delete:
            # apply settings
            # gis - FL Id field
            if self.fl_id_field.get():
                xml_fl_id_field = fl_fields.find("functional_location_id")
                if xml_fl_id_field is None:
                    xml_fl_id_field = ET.SubElement(
                        fl_fields, "functional_location_id")
                xml_fl_id_field.text = self.fl_id_field.get()

            # gis - FL name field
            if self.fl_name_field.get():
                xml_fl_name_field = fl_fields.find("functional_location_name")
                if xml_fl_name_field is None:
                    xml_fl_name_field = ET.SubElement(
                        fl_fields, "functional_location_name")
                xml_fl_name_field.text = self.fl_name_field.get()

            # gis - FL type field
            if self.fl_type_field.get():
                xml_fl_type_field = fl_fields.find("functional_location_type")
                if xml_fl_type_field is None:
                    xml_fl_type_field = ET.SubElement(
                        fl_fields, "functional_location_type")
                xml_fl_type_field.text = self.fl_type_field.get()

        dom = xml.dom.minidom.parseString(ET.tostring(root))
        xmlstring = dom.toprettyxml(encoding='UTF-8')
        dom_string = b'\n'.join(
            [s for s in xmlstring.splitlines() if s.strip()])
        with open(self.save_path, 'wb') as outfile:
            outfile.write(dom_string)
            outfile.close()

        return 0


class AsseticApiTools(object):
    """
    Tools that interact with the Assetic APIs
    """

    def __init__(self, api_client=None):
        if not api_client:
            api_client = ApiClient()
            self.api_client = api_client
        self.logger = api_client.configuration.packagelogger

        self.asset_configuration_api = AssetConfigurationApi(
            api_client=api_client)
        self.maint_config_api = MaintenanceConfigurationApi(
            api_client=api_client)
        self.unit_api = SystemConfigurationApi(api_client=api_client)
        self.apihelper = APIHelper(api_client=api_client)

        self._asset_category_list = None
        self._asset_category_dict = None
        self._asset_category_guid_dict = None
        self._asset_class_config = None
        self._asset_class_list = None
        self._asset_type_config = None
        self._asset_type_list = None
        self._maint_type_config = None
        self._maint_type_list = None
        self._fin_class_config = None
        self._fin_class_list = None
        self._category_asset_attributes_dict = dict()
        self._unit_list = None
        self._fl_type_list = None
        self._fl_type_dict = None
        self._asset_criticality_dict = dict()
        self._workgroup_list = None

    @property
    def asset_category_list(self):
        ac_dict = self.asset_category_dict
        self._asset_category_list = sorted(ac_dict.keys(),
                                           key=lambda x: x.lower())
        return self._asset_category_list

    @property
    def asset_category_dict(self):
        if not self._asset_category_dict:
            category = self.get_category_list()

            if "ResourceList" not in category:
                msg = "No Asset Categories found"
                self.logger.error(msg)
            else:
                category_dict = {}
                for i in category["ResourceList"]:
                    category_dict[i["Label"]] = i["Name"]
                self._asset_category_dict = category_dict
        return self._asset_category_dict

    @property
    def asset_category_guid_dict(self):
        if not self._asset_category_guid_dict:
            category = self.get_category_list()

            if "ResourceList" not in category:
                msg = "No Asset Categories found"
                self.logger.error(msg)
            else:
                category_guid_dict = {}
                for i in category["ResourceList"]:
                    category_guid_dict[i["Label"]] = i["Id"]
                self._asset_category_guid_dict = category_guid_dict
        return self._asset_category_guid_dict

    @property
    def fl_type_list(self):
        type_dict = self.fl_type_dict
        self._fl_type_list = sorted(type_dict.keys(), key=lambda x: x.lower())
        return self._fl_type_list

    @property
    def fl_type_dict(self):
        if not self._fl_type_dict:
            fl_type = self.fl_type_list()

            if not fl_type or "ResourceList" not in fl_type:
                msg = "No Functional Location Types found"
                self.logger.error(msg)
            else:
                fl_type_dict = {}
                for i in fl_type["ResourceList"]:
                    fl_type_dict[i["Label"]] = i["Name"]
                self._fl_type_dict = fl_type_dict
        return self._fl_type_dict

    @property
    def unit_list(self):
        if not self._unit_list:
            units = self.get_unit_list()

            if "ResourceList" not in units:
                msg = "No Unit Types found"
                self.logger.error(msg)
            else:
                unit_list = [i["SingularName"] for i in units["ResourceList"]]
                self._unit_list = unit_list
        return self._unit_list

    @property
    def workgroup_list(self):
        if not self._workgroup_list or len(self._workgroup_list) == 0:
            wgl = self.get_workgroup_list()

            if "ResourceList" not in wgl:
                msg = "No Work Groups found"
                self._workgroup_list = list()
                self.logger.error(msg)
            else:
                wg = [i["Name"] for i in wgl["ResourceList"]]
                self._workgroup_list = wg
        return self._workgroup_list

    @property
    def asset_class_config(self):
        if not self._asset_class_config:
            self._asset_class_config = self.get_asset_class_config()

        return self._asset_class_config

    @property
    def asset_class_list(self):
        """
        Get a list of the configured asset class names
        :return: asset class names
        :rtype: list
        """
        if not self._asset_class_list:
            asset_class_config = self.asset_class_config
            if asset_class_config:
                self._asset_class_list = [i["Name"] for i in asset_class_config]
                self._asset_class_list.insert(0, " ")
        return self._asset_class_list

    @property
    def asset_type_config(self):
        if not self._asset_type_config:
            self._asset_type_config = self.get_asset_type_config()

        return self._asset_type_config

    @property
    def asset_type_list(self):
        """
        Get a list of the configured asset type names
        :return: asset type names
        :rtype: list
        """
        if not self._asset_type_list:
            asset_type_config = self.asset_type_config
            if asset_type_config:
                self._asset_type_list = [i["Name"] for i in asset_type_config]
                self._asset_type_list.insert(0, " ")
        return self._asset_type_list

    @property
    def maint_type_config(self):
        if not self._maint_type_config:
            self._maint_type_config = self.get_maint_type_config()

        return self._asset_type_config

    @property
    def maint_type_list(self):
        """
        Get a list of the configured maintenance type names
        :return: maintenance type names
        :rtype: list
        """
        if not self._maint_type_list:
            config = self.maint_type_config
            if config:
                self._maint_type_list = [i["Name"] for i in config]
                self._maint_type_list.insert(0, " ")
        return self._maint_type_list

    @property
    def fin_class_config(self):
        if not self._fin_class_config:
            self._fin_class_config = self.get_fin_class_config()
        return self._fin_class_config

    @property
    def fin_class_list(self):
        """
        Get a list of the configured financial class names
        :return: financial class names
        :rtype: list
        """
        if not self._fin_class_list:
            config = self.fin_class_config
            if config:
                self._fin_class_list = [i["Name"] for i in config]
                self._fin_class_config.insert(0, " ")
        return self._fin_class_config

    def get_category_list(self):
        """
        Get the list of the visible Asset Categories from Assetic
        :return: All Asset categories
        :rtype:
        """
        try:
            category = \
                self.asset_configuration_api.asset_configuration_get_asset_category()
        except ApiException as e:
            self.logger.error(
                "Error getting Asset Category.\n"
                "Status: {0}, Reason: {1} \n "
                "{2}".format(e.status, e.reason, e.body))
            return None
        return category

    def get_fl_type_list(self):
        """
        Get the list of the configured FL Types
        :return: All FL types
        """
        try:
            fl_type = \
                self.asset_configuration_api.asset_configuration_get_group_asset_types()
        except ApiException as e:
            self.logger.error(
                "Error getting Functional Location Types.\n"
                "Status: {0}, Reason: {1} \n "
                "{2}".format(e.status, e.reason, e.body))
            return None
        return fl_type

    def get_criticality_list_for_category(self, category):
        if category not in self._asset_criticality_dict:
            criticality = self._get_criticality_for_category(category)

            if "AssetCategoryCriticality" not in criticality:
                self._asset_criticality_dict[category] = list()
            else:
                criticality_list = [i["Label"] for i in criticality[
                    "AssetCategoryCriticality"]]
                self._asset_criticality_dict[category] = criticality_list
        return self._asset_criticality_dict[category]

    def _get_criticality_for_category(self, category):
        """
        Get the list of the configured Asset Criticality for given Asset
        Category label (friendly name)
        :return: All criticality
        """
        category_guid = None
        if category in self.asset_category_guid_dict:
            category_guid = self.asset_category_guid_dict[category]
        else:
            self.logger.error(
                "Error getting Asset Category GUID from Category Dictionary.")
            return None

        try:
            criticality = \
                self.asset_configuration_api.asset_configuration_get_asset_criticality_by_id(
                    category_guid
                )
        except ApiException as e:
            self.logger.error(
                "Error getting Asset Criticality.\n"
                "Status: {0}, Reason: {1} \n "
                "{2}".format(e.status, e.reason, e.body))
            return None
        return criticality

    def get_asset_class_config(self):
        """
        Get the list of configured Asset Class and Sub Class
        :return: the asset class config with subclasses
        :rtype:
        """
        kwargs = {
            'request_params_page': 1,
            'request_params_page_size': 500
        }
        try:
            asset_class = self.asset_configuration_api.asset_configuration_get_asset_classes(
                **kwargs)
        except ApiException as e:
            self.logger.error(
                "Error getting Asset Classes.\n"
                "Status: {0}, Reason: {1} \n "
                "{2}".format(e.status, e.reason, e.body))
            return None
        if "ResourceList" not in asset_class:
            return dict()
        return asset_class["ResourceList"]

    def get_asset_sub_class_list_for_class(self, asset_class):
        """
        For the given asset class get the list of sub classes
        :param asset_class: the name of the asset class that we want the
        subclass list for
        :type asset_class: string
        :return: the asset sub_class name list
        """
        asset_class_config = self.asset_class_config
        asset_subclass_list = None

        if asset_class_config:
            asset_subclass_list = [' ']
            for one_class in asset_class_config:
                # if the type exist
                if one_class['Name'] == asset_class:
                    # check if type contain subtype
                    if len(one_class["SubTypes"]) != 0:
                        asset_subclass_list = [j["Name"] for j in
                                               one_class["SubTypes"]]
                        asset_subclass_list.insert(0, " ")
                    break
        return asset_subclass_list

    def get_asset_type_config(self):
        """
        Get the list of configured Asset Type and Sub Type
        :return: the asset type config with subtypes
        :rtype:
        """
        kwargs = {
            'request_params_page': 1,
            'request_params_page_size': 500
        }
        try:
            asset_type = \
                self.asset_configuration_api.asset_configuration_get_asset_types(
                    **kwargs)
        except ApiException as e:
            self.logger.error(
                "Error getting Asset Types.\n"
                "Status: {0}, Reason: {1} \n "
                "{2}".format(e.status, e.reason, e.body))
            return None
        if "ResourceList" not in asset_type:
            return dict()
        return asset_type["ResourceList"]

    def get_asset_sub_type_list_for_type(self, asset_type):
        """
        For the given asset type get the list of sub types
        :param asset_type: the name of the asset type that we want the
        subtype list for
        :type asset_type: string
        :return: the asset sub_type name list
        """
        asset_type_config = self.asset_type_config
        asset_subtype_list = None

        if asset_type_config:
            asset_subtype_list = [' ']
            for one_class in asset_type_config:
                # if the type exist
                if one_class['Name'] == asset_type:
                    # check if type contain subtype
                    if len(one_class["SubTypes"]) != 0:
                        asset_subtype_list = [j["Name"] for j in
                                              one_class["SubTypes"]]
                        asset_subtype_list.insert(0, " ")
                    break
        return asset_subtype_list

    def get_maint_type_config(self):
        """
        Get the list of configured Maintenance Type and Sub Type
        :return: the maintenance type config with subtypes
        :rtype:
        """

        kwargs = {
            'request_params_page': 1,
            'request_params_page_size': 500
        }
        try:
            maint_type = \
                self.maint_config_api.maintenance_configuration_get(**kwargs)
        except ApiException as e:
            self.logger.error(
                "Error getting Maintenance Types.\n"
                "Status: {0}, Reason: {1} \n "
                "{2}".format(e.status, e.reason, e.body))
            return None
        if "ResourceList" not in maint_type:
            return dict()
        return maint_type["ResourceList"]

    def get_maint_sub_type_list_for_type(self, maint_type):
        """
        For the given maintenance type get the list of sub types
        :param maint_type: the name of the maintenance type that we want the
        subtype list for
        :type maint_type: string
        :return: the maintenance sub_type name list
        """

        type_config = self.maint_type_config
        subtype_list = None

        if type_config:
            subtype_list = [' ']
            for one_class in type_config:
                # if the type exist
                if one_class['Name'] == maint_type:
                    # check if type contain subtype
                    if len(one_class["SubTypes"]) != 0:
                        subtype_list = [j["Name"] for j in
                                        one_class["SubTypes"]]
                        subtype_list.insert(0, " ")
                    break
        return subtype_list

    def get_fin_class_config(self):
        """
        Get the list of configured Financial Classes
        :return: the Financial config with subclasses
        """

        kwargs = {
            'request_params_page': 1,
            'request_params_page_size': 500
        }
        try:
            fin_class = \
                self.asset_configuration_api.asset_configuration_get_asset_classes(
                    **kwargs)
        except ApiException as e:
            self.logger.error(
                "Error getting Financial Classes.\n"
                "Status: {0}, Reason: {1} \n "
                "{2}".format(e.status, e.reason, e.body))
            return None
        if "ResourceList" not in fin_class:
            return dict()
        return fin_class["ResourceList"]

    def get_financial_sub_class_list_for_class(self, fin_class):
        """
        For the given financial class get the list of sub classes
        :param fin_class: the name of the financial class that we want the
        subtype list for
        :type fin_class: string
        :return: the financial sub_class name list
        """

        class_config = self.fin_class_config
        subtype_list = None

        if class_config:
            subtype_list = [' ']
            for one_class in class_config:
                # if the type exist
                if one_class['Name'] == fin_class:
                    # check if class contain subclass
                    if len(one_class["FinancialSubClasses"]) != 0:
                        subtype_list = [j["Name"] for j in
                                        one_class["FinancialSubClasses"]]
                        subtype_list.insert(0, " ")
                    break
        return subtype_list

    def attribute_fields_for_category(self, category_name):
        """
        For the given category name return a dictionary of asset attribute
        fields (non-core fields).  Dict key is the label and value is the
        internal field name
        Caches the attributes list for the category, so it only needs
        retrieving once per category (per session)
        :param category_name: The internal name of the category
        :return: dict of field name and internal name , or empty dict if error
        """
        if category_name in self._category_asset_attributes_dict:
            return self._category_asset_attributes_dict[category_name]
        else:
            field_dict = self._get_attribute_fields_for_category(category_name)
            if len(field_dict) > 0:
                self._category_asset_attributes_dict[category_name] = field_dict
                return field_dict

        # couldn't find or build the dict for the category so return empty dict
        return dict()

    def _get_attribute_fields_for_category(self, category_name):
        """
        For the given category name (UI friendly name) get the list of
        attribute fields.
        This uses an internal API which is unsupported
        :param category_name: Name of the asset category (friendly name)
        :return: list of attribute fields (core attributes, FL attributes,
        address attributes are removed)
        """

        attributes_dict = dict()
        # asset_category_dict is a property that caches the list of categories
        category_dict = self.asset_category_dict
        if category_name in category_dict.keys():
            # the dict value is the internal name, dict key is friendly name
            internal_name = category_dict[category_name]
        else:
            return attributes_dict
        url = "/api/SearchApi/GetSearchFields/Assets/{0}/true/false".format(
            internal_name
        )
        try:
            response = self.apihelper.generic_get(url)
            for field_dict in response:
                type(field_dict)
                internal = field_dict['Fields']['SearchField']['FieldName']
                label = field_dict['Fields']['SearchField']['Label']
                module = field_dict['Fields']['SearchField']['FieldModule'][
                    'ModuleIdentifier']
                group = field_dict['Fields']['SearchField']['Group']
                if module not in ["GroupAssets"] and group not in [
                    "Asset Information", "Asset Parent"
                    , "Asset Service Classification", "Other Information"
                    , "Asset Address"
                ] and "Service Criteria" not in group:
                    # print("{0}: {1}".format(group, label))
                    attributes_dict[internal] = label
        except Exception as ex:
            print("Error for retrieving attribute fields for category: {0}, "
                  "error is: {1}".format(category_name, ex))
            return attributes_dict

        # fix field names that don't match DB
        # attributes_dict["Zone"] = attributes_dict.pop("Asset Zone")
        attributes_dict["Zone"] = "Zone"
        return attributes_dict

    def get_unit_list(self):
        """
        Get the list of the Unit names from Assetic
        :return: All singular unit names
        :rtype:
        """

        kw = {
            "request_params_page": 1,
            "request_params_page_size": 500
        }
        try:
            unit = \
                self.unit_api.system_configuration_get_unit_type(**kw)
        except ApiException as e:
            self.logger.error(
                "Error getting Unit Type list from Assetic.\n"
                "Status: {0}, Reason: {1} \n "
                "{2}".format(e.status, e.reason, e.body))
            return None
        return unit

    def get_workgroup_list(self):
        """
        Get the list of the workgroup from Assetic
        :return: All workgroups
        """

        kw = {
            "request_params_page": 1,
            "request_params_page_size": 500
        }
        try:
            wg = \
                self.asset_configuration_api.asset_configuration_get_work_group(
                    **kw)
        except ApiException as e:
            self.logger.error(
                "Error getting Work Group list from Assetic.\n"
                "Status: {0}, Reason: {1} \n "
                "{2}".format(e.status, e.reason, e.body))
            return None
        return wg


class CommonTools(object):
    def __init__(self, asseticsdk, xml_file_path=None, gis=None):
        """
        Tools common to all classes of the UI, but not API calls
        :param asseticsdk: instance of asseticSDK
        :param xml_file_path: the full filename and path of the config file
        """

        self.assetic_folder = os.environ['APPDATA'] + '\\Assetic'
        if not os.path.exists(self.assetic_folder):
            os.makedirs(self.assetic_folder)

        # Get the xml file if it exists.  Use default location
        if xml_file_path:
            self._config_file_path = xml_file_path
        elif gis == TargetGis.ESRI:
            self._config_file_path = os.environ['APPDATA'] + \
                                     '\\Assetic\\arcmap_edit_config.xml'
        elif gis == TargetGis.QGIS:
            self._config_file_path = os.environ['APPDATA'] + \
                                     '\\Assetic\\qgis_edit_config.xml'
        elif gis == TargetGis.MapInfo:
            self._config_file_path = os.environ['APPDATA'] + \
                                     '\\Assetic\\mapinfo_edit_config.xml'

        if not os.path.exists(self.config_file_path):
            self.create_initial_xml_file(gis.name)

        # some defaults
        self.bulk_threshold = "200"  # needs to be a strinf for xml parser
        self.loglevelname = "Info"
        self.logfile = self.assetic_folder + "\\gisintegration.log"
        self.upload_feature = "True"
        self.resolve_lookups = "False"
        self.creation_status = "Active"
        self._gis = gis
        if not gis:
            self._gis = TargetGis.ESRI
        self.existing_layer = dict()

        self.logger = logging.getLogger("Assetic")
        self.logger.info("The GIS is {0}".format(gis.name))
        # the common gis tools have a messager object, set it to use our logger
        self._messager = ConfigMessager()
        self._asseticsdk = asseticsdk

    @property
    def config_file_path(self):
        return self._config_file_path

    def get_existing_xml(self):
        config = XMLConfigReader(self._messager, self._config_file_path,
                                 self._asseticsdk)
        return config

    def get_asset_config_dict(self):
        config = XMLConfigReader(self._messager, self._config_file_path,
                                 self._asseticsdk)
        return config._assetlayerconfig

    def apply_value_to_element(
            self, element_name, field_parent, default_parent
            , gis_field_value, default_value, description):
        """
        If a not null value is provided apply that to the xml element of the
        parent.  Can't have both a GIS field setting and default setting
        :param element_name: The name of the xml element
        :param field_parent: The parent element of the GIS field element
        :param default_parent: The parent element of the default field element
        :param gis_field_value: The value to apply to the GIS field element
        :param default_value: The value to apply to the default field value
        :param description: The user friendly name of the element so
        meaningful error messages can be returned
        :return: True if no errors, else False
        """
        if gis_field_value and gis_field_value.strip() == "":
            gis_field_value = None
        if default_value and default_value.strip() == "":
            default_value = None

        # Are the fields both not null?
        if gis_field_value and default_value:
            # can't define both GIS field and hardcoded field
            messagebox.showerror(
                "Error", "GIS Field and Hardcode Value both defined "
                         "for {0}".format(description))
            return False

        # set GIS field (may need to set to empty)
        element = field_parent.find(element_name)
        if gis_field_value:
            if element is None:
                # Need to create element
                element = ET.SubElement(field_parent, element_name)
            # set value of element
            element.text = gis_field_value
        else:
            if element is not None:
                # set element to empty
                element.text = ""

        # set default field first (may need to set to empty)
        element = default_parent.find(element_name)
        if default_value:
            if element is None:
                # Need to create element
                element = ET.SubElement(default_parent, element_name)
            # set value of element
            element.text = default_value
        else:
            if element is not None:
                # set element to empty
                element.text = ""
        return True

    def save_common_settings(self):
        """
        Create/Update the XML file with common settings defined
        config_file_path is set in class init
        :return: found
        :rtype: int
        """

        if os.path.isfile(self.config_file_path):
            # existing file
            tree = ET.parse(self.config_file_path)

            root = tree.getroot()
            bulk_threshold = root.find("bulk_threshold")
            if bulk_threshold is None:
                # create a new one
                bulk_threshold = ET.SubElement(root, "bulk_threshold")
            bulk_threshold.text = self.bulk_threshold
            loglevel = root.find("loglevel")
            if loglevel is None:
                # create a new one
                loglevel = ET.SubElement(root, "loglevel")
            loglevel.text = self.loglevelname
            logfile = root.find("logfile")
            if logfile is None:
                logfile = ET.SubElement(root, "logfile")
            logfile.text = self.logfile
            for operation in root.iter("operation"):
                action = operation.get("action")
                # if action equal to asset
                if action in ["Asset", "asset"]:
                    operation.set("action", "Asset")
            dom = xml.dom.minidom.parseString(ET.tostring(root))
            xml_string = dom.toprettyxml()
            dom_string = '\n'.join(
                [s for s in xml_string.splitlines() if s.strip()])
            # put this one a file called arcmap_edit_config0.xml
            with open(self.config_file_path, "w") as f:
                f.write(dom_string)
                f.close()
        else:
            # if not exist, create a new file
            m_encoding = 'UTF-8'
            # root element
            self.use_existing_file = 1
            root = ET.Element("asseticconfig", {'name': self.gis})

            logfile = ET.SubElement(root, "logfile")
            logfile.text = self.logfile
            loglevel = ET.SubElement(root, "loglevel")
            loglevel.text = self.loglevelname
            bulk_threshold = ET.SubElement(root, "bulk_threshold")
            bulk_threshold.text = self.bulk_threshold
            operation = ET.SubElement(root, "operation", action="Asset")
            dom = xml.dom.minidom.parseString(ET.tostring(root))
            xml_string = dom.toprettyxml()
            part1, part2 = xml_string.split('?>')
            # write to file
            with open(self.config_file_path, 'wb') as f:
                f.write(
                    part1 + 'encoding=\"{}\"?>\n'.format(m_encoding) + part2)
                f.close()
        return True

    def save_settings_info(self):
        pass

    def create_initial_xml_file(self, gis):
        """
        Create the initial xml file with minimum settings
        :param gis: the GIS type eg ESRI, QGIS, MapInfo
        """
        m_encoding = 'UTF-8'
        # root element
        root = ET.Element("asseticconfig", {'name': gis})

        dom = xml.dom.minidom.parseString(ET.tostring(root))
        dom = xml.dom.minidom.parseString(ET.tostring(root))
        xmlstring = dom.toprettyxml(encoding='UTF-8')
        dom_string = b'\n'.join(
            [s for s in xmlstring.splitlines() if s.strip()])
        with open(self._config_file_path, 'wb') as file:
            file.write(dom_string)
            file.close()
        return 0

    def save_layer_info(self, curr_layer, layer_name=None, delete=0):
        """
        Save the XML file
        :param curr_layer: current XML
        :type curr_layer: dict
        :param layer_name: the name of the layer being processed
        :type layer_name: string
        :param delete: 0=don't delete layer, 1=delete layer
        :type delete: int
        :return: found
        :rtype: int
        """
        found = 0
        if self.use_existing_file:

            if os.path.isfile(self.config_file_path):
                tree = ET.parse(self.config_file_path)
            else:
                messagebox.showerror("Error",
                                     "No arcmap_edit_config.xml is found")
                return
            root = tree.getroot()
            bulk_threshold = root.find("bulk_threshold")
            if bulk_threshold is None:
                # create a new one
                bulk_threshold = ET.SubElement(root, "bulk_threshold")
            bulk_threshold.text = self.bulk_threshold
            loglevel = root.find("loglevel")
            if loglevel is None:
                # create a new one
                loglevel = ET.SubElement(root, "loglevel")
            loglevel.text = self.loglevelname
            logfile = root.find("logfile")
            if logfile is None:
                logfile = ET.SubElement(root, "logfile")
            logfile.text = self.logfile
            for operation in root.iter("operation"):
                action = operation.get("action")
                # if action equal to asset
                if action in ["Asset", "asset"]:
                    operation.set("action", "Asset")
                    onelayer = operation.find("layer")

                    if onelayer is None:
                        onelayer = ET.SubElement(operation, "layer")
                    else:
                        num_layer = 1
                        found = 0
                        for onelayer in operation.iter("layer"):

                            try:
                                # find the first layer name. Use try because curr layer may be more which means user want to add layer
                                if onelayer.get("name") == curr_layer[
                                    "layer_name"]:

                                    if delete:
                                        delete_found = 1
                                        operation.remove(onelayer)
                                        break
                                    if layer_name is None or layer_name in [
                                        None, '', ' ']:
                                        messagebox.showerror("Error",
                                                             "Layer name is missing")
                                        return
                                    found = 1
                                    # if found the layer,check if layer exist/ not
                                    all_layer = operation.findall("layer")
                                    all_layer = [i.attrib["name"] for i in
                                                 all_layer]
                                    if layer_name in all_layer:
                                        # messagebox.showerror(
                                        #    "Error", "Layer already exists")
                                        # return
                                        category = onelayer.find('category')
                                        if onelayer.find('category') is None:
                                            found = 0
                                            category = ET.SubElement(onelayer,
                                                                     "category")
                                        category.text = curr_layer["category"]
                                    break
                                else:
                                    num_layer += 1
                            except KeyError:

                                # means adding a new layer
                                found = 0
                                category = onelayer.find('category')
                                if onelayer.find('category') is None:
                                    found = 0
                                    category = ET.SubElement(onelayer,
                                                             "category")
                                category.text = curr_layer["asset_category"]
                                # check if the newly added layer has exist in or not, if yes


                                # if onelayer.get("name") == layer_name:
                                #    messagebox.showerror("Error", "Layer
                                #    name already exists")
                                #    return
                            except TypeError:
                                found = 0
                                # check if the newly added layer has exist in
                                # or not, if yes

                                # if onelayer.get("name") == layer_name:
                                #    messagebox.showerror("Error", "Layer
                                #    name already exists")
                                #    return
                                category = onelayer.find('category')
                                if onelayer.find('category') is None:
                                    found = 0
                                    category = ET.SubElement(onelayer,
                                                             "category")
                                category.text = curr_layer["asset_category"]

                        if delete:
                            break
                        if found == 0:
                            # if it is adding a new layer, and layer name hasnt exist before
                            onelayer = ET.SubElement(operation, "layer")
                            category = ET.SubElement(onelayer, "category")
                            category.text = curr_layer["category"]
                    if layer_name is None or layer_name in [None, '', ' ']:
                        messagebox.showerror("Error", "Layer name is missing")
                        return
                    onelayer.set("name", layer_name)
                    resolve_lookups = onelayer.find("resolve_lookups")
                    if resolve_lookups is None:
                        resolve_lookups = ET.SubElement(onelayer,
                                                        "resolve_lookups")
                    resolve_lookups.text = self.resolve_lookups
                    upload_feature = onelayer.find("upload_feature")
                    if upload_feature is None:
                        upload_feature = ET.SubElement(onelayer,
                                                       "upload_feature")
                    upload_feature.text = self.upload_feature
                    creation_status = onelayer.find("creation_status")
                    if creation_status is None:
                        creation_status = ET.SubElement(onelayer,
                                                        "creation_status")
                    creation_status.text = self.creation_status
                # else:
                #     # for functional location
                #     pass

            dom = xml.dom.minidom.parseString(ET.tostring(root))
            xml_string = dom.toprettyxml()
            dom_string = '\n'.join(
                [s for s in xml_string.splitlines() if s.strip()])
            # put this one a file called arcmap_edit_config0.xml
            with open(self.config_file_path, "w") as f:
                f.write(dom_string)
                f.close()
        else:
            # if not exist, create a new file

            m_encoding = 'UTF-8'
            # root element
            self.use_existing_file = 1
            root = ET.Element("asseticconfig", {'name': self.gis})

            logfile = ET.SubElement(root, "logfile")
            logfile.text = self.logfile
            loglevel = ET.SubElement(root, "loglevel")
            loglevel.text = self.loglevelname
            bulk_threshold = ET.SubElement(root, "bulk_threshold")
            bulk_threshold.text = self.bulk_threshold
            operation = ET.SubElement(root, "operation", action="Asset")
            layer = ET.SubElement(operation, "layer", name=layer_name)
            creation_status = ET.SubElement(layer, "creation_status")
            creation_status.text = self.creation_status
            category = ET.SubElement(layer, "category")
            category.text = curr_layer["category"]
            upload_feature = ET.SubElement(layer, "upload_feature")
            upload_feature.text = self.upload_feature
            resolve_lookups = ET.SubElement(layer, "resolve_lookups")
            resolve_lookups.text = self.resolve_lookups
            dom = xml.dom.minidom.parseString(ET.tostring(root))
            xml_string = dom.toprettyxml()
            part1, part2 = xml_string.split('?>')
            # write to file
            with open(self.config_file_path, 'wb') as f:
                f.write(
                    part1 + 'encoding=\"{}\"?>\n'.format(m_encoding) + part2)
                f.close()
        messagebox.showinfo('Info', 'Successfully Saved')
        return found


class ConfigMessager(MessagerBase):

    def __init__(self):
        super(ConfigMessager, self).__init__()

    def new_message(self, message, typeid=None):
        """
        Create a message dialogue for user if desktop, else print message
        :param message: the message string for the user
        :param typeid: the type of dialog.  Integer.  optional,Default is none
        :returns: The dialog response as a unicode string, or None
        """
        self.logger.info("Assetic Integration: {0}".format(message))


class LayerChooserFrame(tk.Frame):
    """
    OBSOLETE - not used
    Setup the frame that has a combobox list of GIS layers
    The treeview frame will make this obsolete
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.existing_layer = None
        self.controller = controller

        self.logger = logging.getLogger("Assetic")

        font_normal = controller.font_normal
        font_header = controller.font_header
        font_strike = controller.font_strike

        existing_configuration = controller.get_existing_xml()
        configured_layers = dict()
        if existing_configuration:
            configured_layers = existing_configuration.assetconfig

        if controller.layer_dict is None:
            message = "No layer found from the file"
            self.logger.error(message)
            return
        # get a list of layer names for the combobox and insert an empty row
        # so that no layer is selected when initialising the form
        layer_option = sorted(controller.layer_dict.keys()
                              , key=lambda x: x.lower())
        layer_option.insert(0, " ")

        config_layer_names = [v["layer"] for v in configured_layers]

        self.selected_layer = tk.StringVar()

        Label(self, text="Layer: "
              , bg="#349cbc", fg='gray92').grid(row=0, column=0)

        self.cmb_layer = ttk.Combobox(
            self, values=layer_option, width=40, state='readonly'
            , textvariable=self.selected_layer)
        self.cmb_layer.current(0)
        self.cmb_layer.grid(row=0, column=1)
        self.cmb_layer.bind('<<ComboboxSelected>>', self.cmb_layer_changed)


class MenuFrame(tk.Frame):
    """
    OBSOLETE - replaced by treeview.
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.existing_layer = None
        self.controller = controller

        font_normal = controller.font_normal
        font_header = controller.font_header
        font_strike = controller.font_strike

        # Add buttons to initiate each level of configuration
        tk.Button(self, text="Category", width='30',
                  height='2',
                  command=lambda: self.load_category_frame(),
                  bg="#349cbc", borderwidth=0,
                  fg='gray92').grid(row=0, column=0)

        tk.Button(self, text="Asset Core Attributes", width='30', height='2',
                  command=lambda: self.asset_window_1_(),
                  bg="#349cbc", borderwidth=0,
                  fg='gray92').grid(row=1, column=0)
        tk.Button(self, text="Component", width='30', height='2',
                  command=lambda: self.component_window_1_(),
                  bg="#349cbc", borderwidth=0,
                  fg='gray92').grid(row=2, column=0)
        tk.Button(self, text="Dimensions", width='30', height='2',
                  command=lambda: self.dimension_window_1_(),
                  bg="#349cbc", borderwidth=0,
                  fg='gray92').grid(row=3, column=0)

    def load_category_frame(self):
        self.existing_layer = self.controller.get_existing_xml()
        self.controller.refresh_frame(CategoryFrame)
        self.controller.current_config_frame = CategoryFrame
        # prompter = XML_Prompter_for_Layer(
        #    self.master, layer_dict=self.layer_dict,
        #    existing_layer=self.existing_layer)

    def asset_window_1_(self):
        self.existing_layer = self.controller.get_existing_xml()
        self.controller.refresh_frame(AssetCoreFrame)
        self.controller.current_config_frame = AssetCoreFrame
        # prompter = XMl_Prompter_for_Asset(
        #    self.master, layer_dict=self.layer_dict,
        #    existing_layer=self.existing_layer)

    def component_window_1_(self):
        self.existing_layer = self.controller.get_existing_xml()
        # prompter = XMl_Prompter_for_Component(
        #    self.master, layer_dict=self.layer_dict,
        #    existing_layer=self.existing_layer)

    def dimension_window_1_(self):
        self.existing_layer = self.controller.get_existing_xml()
        # prompter = XMl_Prompter_for_Dimension(
        #    self, layer_dict=self.layer_dict,
        #    existing_layer=self.existing_layer)
