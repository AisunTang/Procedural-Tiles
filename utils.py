import bpy
import os
from pathlib import Path

ADDON_DIR = Path(__file__).resolve().parent
DATA_FILE = os.path.join(ADDON_DIR, "proceduralTilesData.blend")


def append_shader_nodetree(name: str):
    trees_path = os.path.join(DATA_FILE, "NodeTree")

    node_tree_name = "MyCustomNodeGroup"

    bpy.ops.wm.append(
        filepath=os.path.join(trees_path, node_tree_name),
        directory=trees_path + "/",
        filename=name,
    )


def add_node_group(node_name: str, context, show_options=False):
    bpy.ops.node.add_node("INVOKE_DEFAULT", type="ShaderNodeGroup", use_transform=True)
    node = context.active_node
    node.node_tree = bpy.data.node_groups[node_name]
    node.width = 190
    node.show_options = show_options
    node.label = node_name
    node.name = node_name


def get_all_files(root_path: str, extension: str = ".png"):
    png_files = []
    for root, _, files in os.walk(root_path):
        for file in files:
            if file.lower().endswith(extension):
                full_path = os.path.join(root, file)
                png_files.append(full_path)
    return png_files
