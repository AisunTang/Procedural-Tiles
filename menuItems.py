from bl_ui.properties_texture import texture_filter_common
import bpy

from .icons import Icon

from .operators import PT_OT_Add_Custom_Node_Group


class NodeGroupItem:
    def __init__(
        self,
        name: str,
        label: str | None = None,
        description: str = "",
    ) -> None:
        self.name = name
        self.label = label
        if self.label is None:
            self.label = self.name
        self.description = description

    def menu(
        self, layout: bpy.types.UILayout, context: bpy.types.Context = None
    ) -> None:
        if self.label is None:
            self.label = self.name

        # if self.name.startswith("pt."):
        #     layout.operator(self.name)
        #     return None

        op = layout.operator(
            PT_OT_Add_Custom_Node_Group.bl_idname,
            text=self.label,
            icon_value=Icon.get_icon(self.name),
        )
        op.node_label = self.label
        op.node_name = self.name
        op.node_description = self.description
        op.node_link = False

    def to_dict(self) -> dict:
        return {
            self.name: {
                "name": self.name,
                "label": self.label,
                "description": self.description,
            }
        }


class Separator:
    def __init__(self) -> None:
        pass

    def menu(self, layout: bpy.types.UILayout, context: bpy.types.Context = None):
        layout.separator()


menu_items = {
    "ProceduralTiles": [
        NodeGroupItem(label="BasicBrick", name="PT_BasicBrick"),
        NodeGroupItem(label="BoxStar", name="PT_BoxStar"),
        NodeGroupItem(label="CircleCoin", name="PT_CircleCoin"),
        NodeGroupItem(label="ConvergingLeafs", name="PT_ConvergingLeafs"),
        NodeGroupItem(label="Diamond", name="PT_Diamond"),
        NodeGroupItem(label="DoubleQuad", name="PT_DoubleQuad"),
        NodeGroupItem(label="DoubleSquareTile", name="PT_DoubleSquareTile"),
        NodeGroupItem(label="HexBoards", name="PT_HexBoards"),
        NodeGroupItem(label="HexTile", name="PT_HexTile"),
        NodeGroupItem(label="HVBoards", name="PT_HVBoards"),
        NodeGroupItem(label="LampLikeTile", name="PT_LampLikeTile"),
        NodeGroupItem(label="Penrose", name="PT_Penrose"),
        NodeGroupItem(label="PolyDiamond", name="PT_PolyDiamond"),
        NodeGroupItem(label="QuadFlower", name="PT_QuadFlower"),
        NodeGroupItem(label="RectV", name="PT_RectV"),
        NodeGroupItem(label="RotatedScales", name="PT_RotatedScales"),
        NodeGroupItem(label="Scales", name="PT_Scales"),
        NodeGroupItem(label="SquareAndRhombus", name="PT_SquareAndRhombus"),
        NodeGroupItem(label="SquareDiamond", name="PT_SquareDiamond"),
        NodeGroupItem(label="SquareNet", name="PT_SquareNet"),
        NodeGroupItem(label="StarInOctagon", name="PT_StarInOctagon"),
        NodeGroupItem(label="TriangleTile", name="PT_TriangleTile"),
        NodeGroupItem(label="VTile", name="PT_VTile"),
        NodeGroupItem(label="WireHexOverlap", name="PT_WireHexOverlap"),
        Separator(),
        NodeGroupItem(label="ISL_BachchaTajTomb", name="PT_ISL_BachchaTajTomb"),
        NodeGroupItem(label="ISL_Hive", name="PT_ISL_Hive"),
        Separator(),
        NodeGroupItem(label="TCH_45Maze", name="PT_TCH_45Maze"),
        NodeGroupItem(label="TCH_CyberChip", name="PT_TCH_CyberChip"),
        NodeGroupItem(label="TCH_FullWire", name="PT_TCH_FullWire"),
        NodeGroupItem(label="TCH_HexTruchet", name="PT_TCH_HexTruchet"),
        NodeGroupItem(label="TCH_QuarterDisk", name="PT_TCH_QuarterDisk"),
    ],
    "SignDistanceFields": [
        NodeGroupItem(label="Segment", name="SDF_Segment"),
        NodeGroupItem(label="Rectangle", name="SDF_Rectangle"),
        NodeGroupItem(label="Arc", name="SDF_Arc"),
        NodeGroupItem(label="Circle", name="SDF_Circle"),
        NodeGroupItem(label="Ellipse", name="SDF_Ellipse"),
        NodeGroupItem(label="Pie", name="SDF_Pie"),
        NodeGroupItem(label="Hexagon", name="SDF_Hexagon"),
        NodeGroupItem(label="NStar", name="SDF_NStar"),
        Separator(),
        NodeGroupItem(label="Union", name="SDF_Union"),
        NodeGroupItem(label="Intersect", name="SDF_Intersect"),
        NodeGroupItem(label="Subtract", name="SDF_Subtract"),
        NodeGroupItem(label="Exclude", name="SDF_Exclude"),
        NodeGroupItem(label="rIntersect", name="SDF_rIntersect"),
        NodeGroupItem(label="rUnion", name="SDF_rUnion"),
    ],
    "WallpaperGroups": [
        NodeGroupItem(name="WPG_1(p1)", label="p1"),
        NodeGroupItem(name="WPG_2(p2)", label="p2"),
        NodeGroupItem(name="WPG_3(pm)", label="pm"),
        NodeGroupItem(name="WPG_4(pg)", label="pg"),
        NodeGroupItem(name="WPG_5(pmm)", label="pmm"),
        NodeGroupItem(name="WPG_6(pmg)", label="pmg"),
        NodeGroupItem(name="WPG_7(pgg)", label="pgg"),
        NodeGroupItem(name="WPG_8(cm)", label="cm"),
        NodeGroupItem(name="WPG_9(cmm)", label="cmm"),
        NodeGroupItem(name="WPG_10(p4)", label="p4"),
        NodeGroupItem(name="WPG_11(p4m)", label="p4m"),
        NodeGroupItem(name="WPG_12(p4g)", label="p4g"),
        NodeGroupItem(name="WPG_13(p3)", label="p3"),
        NodeGroupItem(name="WPG_14(p3ml)", label="p3ml"),
        NodeGroupItem(name="WPG_15(p3lm)", label="p3lm"),
        NodeGroupItem(name="WPG_16(p6)", label="p6"),
        NodeGroupItem(name="WPG_17(p6m)", label="p6m"),
    ],
}

#  PT (ISL, TCH), SDF, WPG
