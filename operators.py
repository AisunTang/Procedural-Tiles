import bpy
from bpy.props import IntProperty, BoolProperty, EnumProperty, StringProperty
from . import utils


class PT_OT_Add_Custom_Node_Group(bpy.types.Operator):
    bl_idname = "pt.add_custom_node_group"
    bl_label = "Add Custom Node Group"
    bl_description = "Add new node"
    bl_options = {"REGISTER", "UNDO"}
    node_name: StringProperty(  # type: ignore
        name="node_name", description="", default="", subtype="NONE", maxlen=0
    )
    node_label: StringProperty(name="node_label", default="")  # type: ignore
    node_description: StringProperty(  # type: ignore
        name="node_description",
        description="",
        default="Add procedural tiles custom node group.",
        subtype="NONE",
    )
    node_link: BoolProperty(name="node_link", default=True)

    @classmethod
    def description(cls, context, properties):
        return properties.node_description

    def execute(self, context):
        try:
            utils.append_shader_nodetree(self.node_name)
            utils.add_node_group(self.node_name, context)  # , label=self.node_label)
        except RuntimeError:
            self.report(
                {"ERROR"},
                message="Failed to add node. Exit edit mode",
            )
            return {"CANCELLED"}
        return {"FINISHED"}


CLASSES = [PT_OT_Add_Custom_Node_Group]
