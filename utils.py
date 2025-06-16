import bpy
import os
from pathlib import Path
from databpy.nodes import (
    NodeGroupCreationError,
    append_from_blend,
)

ADDON_DIR = Path(__file__).resolve().parent
MN_DATA_FILE = os.path.join(ADDON_DIR, "proceduralTilesData.blend")
# MN_DATA_FILE = "C:/Users/andre/Documents/Ipan/Blender/Projects/proceduralTiles2.blend"


def append_shader_nodetree(name: str, link: bool = False) -> bpy.types.ShaderNodeTree:
    trees_path = os.path.join(MN_DATA_FILE, "NodeTree")
    return append_from_blend(name, filepath=trees_path, link=link)


def get_current_node_tree():
    space = bpy.context.space_data
    if space and space.type == "NODE_EDITOR":
        return space.edit_tree  # This is the node tree you're working on
    return None


def add_node_group(node_name, context, show_options=False):
    bpy.ops.node.add_node("INVOKE_DEFAULT", type="ShaderNodeGroup", use_transform=True)
    node = context.active_node
    node.node_tree = bpy.data.node_groups[node_name]
    node.width = 190
    node.show_options = show_options
    node.label = node_name
    node.name = node_name
