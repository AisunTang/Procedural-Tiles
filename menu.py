from bl_ui.properties_texture import texture_filter_common
import bpy
from bpy.ops import text
from .menuItems import menu_items

class PT_MT_Node_General(bpy.types.Menu):
    bl_idname = "PT_MT_NODE_GENERAL"
    bl_label = ""

    def draw(self, context):
        for item in menu_items["General"]:
            item.menu(layout=self.layout, context=context)

class PT_MT_Node_Arabic(bpy.types.Menu):
    bl_idname = "PT_MT_NODE_ARB"
    bl_label = ""

    def draw(self, context):
        for item in menu_items["Arabic"]:
            item.menu(layout=self.layout, context=context)

class PT_MT_Node_Random(bpy.types.Menu):
    bl_idname = "PT_MT_NODE_TCH"
    bl_label = ""

    def draw(self, context):
        for item in menu_items["Random"]:
            item.menu(layout=self.layout, context=context)

class PT_MT_Node_WallpaperGroup(bpy.types.Menu):
    bl_idname = "PT_MT_NODE_WPG"
    bl_label = ""

    def draw(self, context):
        for item in menu_items["WallpaperGroups"]:
            item.menu(layout=self.layout, context=context)

class PT_MT_Node_Sdf(bpy.types.Menu):
    bl_idname = "PT_MT_NODE_SDF"
    bl_label = ""

    def draw(self, context):
        for item in menu_items["SignDistanceFields"]:
            item.menu(layout=self.layout, context=context)


class PT_MT_Node(bpy.types.Menu):
    bl_idname = "PT_MT_NODE"
    bl_label = "Menu for Adding Nodes in GN Tree"

    def draw(self, context):
        layout = self.layout
        layout.menu(PT_MT_Node_General.bl_idname, text="General Tiles", icon="MESH_GRID")
        layout.menu(PT_MT_Node_Arabic.bl_idname, text="Arabic Patters", icon="SOLO_ON")
        layout.menu(PT_MT_Node_Random.bl_idname, text="Organic/Random", icon="POINTCLOUD_POINT")
        layout.separator()
        layout.menu(
            PT_MT_Node_WallpaperGroup.bl_idname, text="Wallpaper Group", icon="OUTLINER_OB_LATTICE"
        )
        layout.menu(PT_MT_Node_Sdf.bl_idname, text="Sign Distance Fields", icon="DRIVER_DISTANCE")


def PT_add_node_menu(self, context):
    if "ShaderNodeTree" == bpy.context.area.spaces[0].tree_type:
        layout = self.layout
        layout.menu(
            PT_MT_Node.bl_idname, text="Procedural Tiles Nodes", icon="SEQ_CHROMA_SCOPE"
    )


CLASSES = [
    PT_MT_Node, 
    PT_MT_Node_General, 
    PT_MT_Node_Arabic,
    PT_MT_Node_Random,
    PT_MT_Node_WallpaperGroup,
    PT_MT_Node_Sdf
]
