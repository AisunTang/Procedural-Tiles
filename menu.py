from bl_ui.properties_texture import texture_filter_common
import bpy
from bpy.ops import text
from .menuItems import menu_items


class PT_MT_Node_WallpaperGroup(bpy.types.Menu):
    bl_idname = "PT_MT_NODE_WPG"
    bl_label = ""

    def draw(self, context):
        for item in menu_items["WallpaperGroups"]:
            item.menu(layout=self.layout, context=context)


class PT_MT_Node_General(bpy.types.Menu):
    bl_idname = "PT_MT_NODE_TCH"
    bl_label = ""

    def draw(self, context):
        for item in menu_items["ProceduralTiles"]:
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
        layout.menu(PT_MT_Node_General.bl_idname, text="Ready Patters", icon="TEXTURE")
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


CLASSES = [PT_MT_Node, PT_MT_Node_Sdf, PT_MT_Node_General, PT_MT_Node_WallpaperGroup]
