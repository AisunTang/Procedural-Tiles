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
    "General": [
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
        NodeGroupItem(label="QuadBoard", name="PT_QuadBoard"),
        NodeGroupItem(label="HexLens", name="PT_HexLens"),
        NodeGroupItem(label="HexBricks", name="PT_HexBricks"),
        NodeGroupItem(label="SquaryMedal", name="PT_SquaryMedal"),
        NodeGroupItem(label="SquaryFan", name="PT_SquaryFan"),
        NodeGroupItem(label="GlareStar", name="PT_GlareStar"),
        NodeGroupItem(label="HexParallelogram", name="PT_HexParallelogram"),
        NodeGroupItem(label="RoseBoards", name="PT_RoseBoards"),
        NodeGroupItem(label="SquaryDiamondBoard", name="PT_SquaryDiamondBoard"),
        NodeGroupItem(label="SquaryOctstar", name="PT_SquaryOctstar"),
        NodeGroupItem(label="SquaryFlower", name="PT_SquaryFlower"),
    ],
    "Arabic": [
        NodeGroupItem(label="BachchaTajTomb", name="PT_ARB_BachchaTajTomb"),
        NodeGroupItem(label="Hive", name="PT_ARB_Hive"),
        NodeGroupItem(label="MultiAngleHive", name="PT_ARB_MultiAngleHive"),
        NodeGroupItem(label="MiniSuns", name="PT_ARB_MiniSuns"),
        NodeGroupItem(label="ScatteredSuns", name="PT_ARB_ScatteredSuns"),
        NodeGroupItem(label="Cosmos(106)", name="PT_ARB_Cosmos(106)"),
        NodeGroupItem(label="Cosmos(42)", name="PT_ARB_Cosmos(42)"),
        NodeGroupItem(label="Cosmos(96)", name="PT_ARB_Cosmos(96)"),
        NodeGroupItem(label="Cosmos(171)", name="PT_ARB_Cosmos(171)"),
        NodeGroupItem(label="Constellation(44)", name="PT_ARB_Constellation(44)"),
        NodeGroupItem(label="StarSquare(13)", name="PT_ARB_StarSquare(13)"),
        NodeGroupItem(label="CrossHatch(59)", name="PT_ARB_CrossHatch(59)"),
        NodeGroupItem(label="PentaHexa(35)", name="PT_ARB_PentaHexa(35)"),
        NodeGroupItem(label="EightStars(48)", name="PT_ARB_EightStars(48)"),
        NodeGroupItem(label="ShipWheel(46)", name="PT_ARB_ShipWheel(46)"),
        NodeGroupItem(label="TiedStars(8)", name="PT_ARB_TiedStars(8)"),
        NodeGroupItem(label="HookedStars(9)", name="PT_ARB_HookedStars(9)"),
        NodeGroupItem(label="PointingStars(45)", name="PT_ARB_PointingStars(45)"),
        NodeGroupItem(label="HookedHexagons(7)", name="PT_ARB_HookedHexagons(7)"),
        NodeGroupItem(label="HookedVs(10)", name="PT_ARB_HookedVs(10)"),
        NodeGroupItem(label="Web(28)", name="PT_ARB_Web(28)"),
        NodeGroupItem(label="Web(21)", name="PT_ARB_Web(21)"),
        NodeGroupItem(label="Web(41)", name="PT_ARB_Web(41)"),
        NodeGroupItem(label="ThreeSpikes(20)", name="PT_ARB_ThreeSpikes(20)"),
        NodeGroupItem(label="CircularMaze(103)", name="PT_ARB_CircularMaze(103)"),
    ],
    "Random": [
        NodeGroupItem(label="45Maze", name="PT_TCH_45Maze"),
        NodeGroupItem(label="CyberChip", name="PT_TCH_CyberChip"),
        NodeGroupItem(label="FullWire", name="PT_TCH_FullWire"),
        NodeGroupItem(label="HexTruchet", name="PT_TCH_HexTruchet"),
        NodeGroupItem(label="QuarterDisk", name="PT_TCH_QuarterDisk"),
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
        NodeGroupItem(label="p1", name="WPG_1(p1)"),
        NodeGroupItem(label="p2", name="WPG_2(p2)"),
        NodeGroupItem(label="pm", name="WPG_3(pm)"),
        NodeGroupItem(label="pg", name="WPG_4(pg)"),
        NodeGroupItem(label="pmm", name="WPG_5(pmm)"),
        NodeGroupItem(label="pmg", name="WPG_6(pmg)"),
        NodeGroupItem(label="pgg", name="WPG_7(pgg)"),
        NodeGroupItem(label="cm", name="WPG_8(cm)"),
        NodeGroupItem(label="cmm", name="WPG_9(cmm)"),
        NodeGroupItem(label="p4", name="WPG_10(p4)"),
        NodeGroupItem(label="p4m", name="WPG_11(p4m)"),
        NodeGroupItem(label="p4g", name="WPG_12(p4g)"),
        NodeGroupItem(label="p3", name="WPG_13(p3)"),
        NodeGroupItem(label="p3ml", name="WPG_14(p3ml)"),
        NodeGroupItem(label="p3lm", name="WPG_15(p3lm)"),
        NodeGroupItem(label="p6", name="WPG_16(p6)"),
        NodeGroupItem(label="p6m", name="WPG_17(p6m)"),
    ],
}

