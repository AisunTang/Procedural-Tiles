# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from . import menu
from . import operators

bl_info = {
    "name": "Proceduraltiles",
    "author": "proceduralTiles",
    "description": "",
    "blender": (4, 30, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Generic",
}

from . import auto_load

auto_load.init()

auto_load.ordered_classes = menu.CLASSES + operators.CLASSES


def register():
    bpy.types.NODE_MT_add.append(menu.PT_add_node_menu)
    auto_load.register()


def unregister():
    bpy.types.NODE_MT_add.remove(menu.PT_add_node_menu)
    auto_load.unregister()
