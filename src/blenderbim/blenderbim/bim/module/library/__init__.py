# BlenderBIM Add-on - OpenBIM Blender Add-on
# Copyright (C) 2021 Dion Moult <dion@thinkmoult.com>
#
# This file is part of BlenderBIM Add-on.
#
# BlenderBIM Add-on is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BlenderBIM Add-on is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BlenderBIM Add-on.  If not, see <http://www.gnu.org/licenses/>.

import bpy
from . import ui, prop, operator

classes = (
    operator.AddLibrary,
    operator.RemoveLibrary,
    operator.EnableEditingLibraryReferences,
    operator.DisableEditingLibraryReferences,
    operator.EnableEditingLibrary,
    operator.DisableEditingLibrary,
    operator.EditLibrary,
    operator.AddLibraryReference,
    operator.RemoveLibraryReference,
    operator.EnableEditingLibraryReference,
    operator.DisableEditingLibraryReference,
    operator.EditLibraryReference,
    prop.LibraryReference,
    prop.BIMLibraryProperties,
    ui.BIM_PT_libraries,
    ui.BIM_UL_library_references,
)


def register():
    bpy.types.Scene.BIMLibraryProperties = bpy.props.PointerProperty(type=prop.BIMLibraryProperties)


def unregister():
    del bpy.types.Scene.BIMLibraryProperties
