import bpy
import bmesh
import math
from mathutils import Vector, Matrix

# Clear default scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)


# Create cylinder: base
bpy.ops.mesh.primitive_cylinder_add(radius=0.0125, depth=0.003,
    vertices=64, location=(0, 0, 0.0015))
obj = bpy.context.active_object
obj.name = "base"


# Add bevel: base
obj = bpy.data.objects["base"]
mod = obj.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.0003
mod.segments = 2


# Create cube: chest_bottom
bpy.ops.mesh.primitive_cube_add(size=0.016, location=(0, 0, 0.011))
obj = bpy.context.active_object
obj.name = "chest_bottom"


# Scale: chest_bottom
bpy.data.objects["chest_bottom"].scale = (1.0, 0.7, 0.5)


# Create cube: chest_lid
bpy.ops.mesh.primitive_cube_add(size=0.016, location=(0, -0.004, 0.02))
obj = bpy.context.active_object
obj.name = "chest_lid"


# Scale: chest_lid
bpy.data.objects["chest_lid"].scale = (1.0, 0.7, 0.3)


# Rotate: chest_lid (degrees)
import math
bpy.data.objects["chest_lid"].rotation_euler = (
    math.radians(-30),
    math.radians(0),
    math.radians(0)
)


# Create cone: tooth_upper_0
bpy.ops.mesh.primitive_cone_add(radius1=0.0015, radius2=0,
    depth=0.004, vertices=6, location=(-0.006, 0.004, 0.016))
obj = bpy.context.active_object
obj.name = "tooth_upper_0"


# Rotate: tooth_upper_0 (degrees)
import math
bpy.data.objects["tooth_upper_0"].rotation_euler = (
    math.radians(160),
    math.radians(0),
    math.radians(0)
)


# Create cone: tooth_upper_1
bpy.ops.mesh.primitive_cone_add(radius1=0.0015, radius2=0,
    depth=0.004, vertices=6, location=(-0.003, 0.004, 0.016))
obj = bpy.context.active_object
obj.name = "tooth_upper_1"


# Rotate: tooth_upper_1 (degrees)
import math
bpy.data.objects["tooth_upper_1"].rotation_euler = (
    math.radians(160),
    math.radians(0),
    math.radians(0)
)


# Create cone: tooth_upper_2
bpy.ops.mesh.primitive_cone_add(radius1=0.0015, radius2=0,
    depth=0.004, vertices=6, location=(0, 0.004, 0.016))
obj = bpy.context.active_object
obj.name = "tooth_upper_2"


# Rotate: tooth_upper_2 (degrees)
import math
bpy.data.objects["tooth_upper_2"].rotation_euler = (
    math.radians(160),
    math.radians(0),
    math.radians(0)
)


# Create cone: tooth_upper_3
bpy.ops.mesh.primitive_cone_add(radius1=0.0015, radius2=0,
    depth=0.004, vertices=6, location=(0.003, 0.004, 0.016))
obj = bpy.context.active_object
obj.name = "tooth_upper_3"


# Rotate: tooth_upper_3 (degrees)
import math
bpy.data.objects["tooth_upper_3"].rotation_euler = (
    math.radians(160),
    math.radians(0),
    math.radians(0)
)


# Create cone: tooth_upper_4
bpy.ops.mesh.primitive_cone_add(radius1=0.0015, radius2=0,
    depth=0.004, vertices=6, location=(0.006, 0.004, 0.016))
obj = bpy.context.active_object
obj.name = "tooth_upper_4"


# Rotate: tooth_upper_4 (degrees)
import math
bpy.data.objects["tooth_upper_4"].rotation_euler = (
    math.radians(160),
    math.radians(0),
    math.radians(0)
)


# Create cone: tooth_lower_0
bpy.ops.mesh.primitive_cone_add(radius1=0.0012, radius2=0,
    depth=0.0035, vertices=6, location=(-0.005, 0.005, 0.009))
obj = bpy.context.active_object
obj.name = "tooth_lower_0"


# Rotate: tooth_lower_0 (degrees)
import math
bpy.data.objects["tooth_lower_0"].rotation_euler = (
    math.radians(20),
    math.radians(0),
    math.radians(0)
)


# Create cone: tooth_lower_1
bpy.ops.mesh.primitive_cone_add(radius1=0.0012, radius2=0,
    depth=0.0035, vertices=6, location=(-0.002, 0.005, 0.009))
obj = bpy.context.active_object
obj.name = "tooth_lower_1"


# Rotate: tooth_lower_1 (degrees)
import math
bpy.data.objects["tooth_lower_1"].rotation_euler = (
    math.radians(20),
    math.radians(0),
    math.radians(0)
)


# Create cone: tooth_lower_2
bpy.ops.mesh.primitive_cone_add(radius1=0.0012, radius2=0,
    depth=0.0035, vertices=6, location=(0.002, 0.005, 0.009))
obj = bpy.context.active_object
obj.name = "tooth_lower_2"


# Rotate: tooth_lower_2 (degrees)
import math
bpy.data.objects["tooth_lower_2"].rotation_euler = (
    math.radians(20),
    math.radians(0),
    math.radians(0)
)


# Create cone: tooth_lower_3
bpy.ops.mesh.primitive_cone_add(radius1=0.0012, radius2=0,
    depth=0.0035, vertices=6, location=(0.005, 0.005, 0.009))
obj = bpy.context.active_object
obj.name = "tooth_lower_3"


# Rotate: tooth_lower_3 (degrees)
import math
bpy.data.objects["tooth_lower_3"].rotation_euler = (
    math.radians(20),
    math.radians(0),
    math.radians(0)
)


# Create metaball sphere: tongue_meta
bpy.ops.object.metaball_add(type='BALL', radius=0.003, location=(0, 0.012, 0.012))
obj = bpy.context.active_object
obj.name = "tongue_meta"


# Add metaball element to: tongue_meta
mball = bpy.data.metaballs[bpy.data.objects["tongue_meta"].data.name]
elem = mball.elements.new(type='CAPSULE')
elem.radius = 0.002
elem.co = (0, 0.018, 0.01)


# Add metaball element to: tongue_meta
mball = bpy.data.metaballs[bpy.data.objects["tongue_meta"].data.name]
elem = mball.elements.new(type='CAPSULE')
elem.radius = 0.0015
elem.co = (0, 0.024, 0.008)


# Add metaball element to: tongue_meta
mball = bpy.data.metaballs[bpy.data.objects["tongue_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.0025
elem.co = (0, 0.028, 0.007)


# Convert metaball to mesh: tongue_meta
obj = bpy.data.objects["tongue_meta"]
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
bpy.ops.object.convert(target='MESH')

bpy.context.active_object.name = "tongue"

# Create sphere: eye
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.003, segments=16,
    ring_count=12, location=(0.004, 0, 0.016))
obj = bpy.context.active_object
obj.name = "eye"


# Create sphere: pupil
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0015, segments=12,
    ring_count=8, location=(0.004, 0.002, 0.017))
obj = bpy.context.active_object
obj.name = "pupil"


# Create cube: band_front
bpy.ops.mesh.primitive_cube_add(size=0.018, location=(0, 0.0055, 0.011))
obj = bpy.context.active_object
obj.name = "band_front"


# Scale: band_front
bpy.data.objects["band_front"].scale = (1.0, 0.05, 0.6)


# Create cube: band_side_l
bpy.ops.mesh.primitive_cube_add(size=0.012, location=(-0.008, 0, 0.011))
obj = bpy.context.active_object
obj.name = "band_side_l"


# Scale: band_side_l
bpy.data.objects["band_side_l"].scale = (0.05, 0.8, 0.6)


# Create cube: band_side_r
bpy.ops.mesh.primitive_cube_add(size=0.012, location=(0.008, 0, 0.011))
obj = bpy.context.active_object
obj.name = "band_side_r"


# Scale: band_side_r
bpy.data.objects["band_side_r"].scale = (0.05, 0.8, 0.6)


# Create cylinder: lock
bpy.ops.mesh.primitive_cylinder_add(radius=0.002, depth=0.002,
    vertices=16, location=(0, 0.0065, 0.015))
obj = bpy.context.active_object
obj.name = "lock"


# Rotate: lock (degrees)
import math
bpy.data.objects["lock"].rotation_euler = (
    math.radians(90),
    math.radians(0),
    math.radians(0)
)


# Union objects into: mimic
# Using boolean EXACT solver for watertight results
base_obj = bpy.data.objects["base"]
bpy.context.view_layer.objects.active = base_obj


# Boolean union: adding chest_bottom
tool_obj = bpy.data.objects["chest_bottom"]
mod = base_obj.modifiers.new(name="Boolean_0", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_0")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding chest_lid
tool_obj = bpy.data.objects["chest_lid"]
mod = base_obj.modifiers.new(name="Boolean_1", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_1")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tongue
tool_obj = bpy.data.objects["tongue"]
mod = base_obj.modifiers.new(name="Boolean_2", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_2")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye
tool_obj = bpy.data.objects["eye"]
mod = base_obj.modifiers.new(name="Boolean_3", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_3")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding pupil
tool_obj = bpy.data.objects["pupil"]
mod = base_obj.modifiers.new(name="Boolean_4", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_4")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding band_front
tool_obj = bpy.data.objects["band_front"]
mod = base_obj.modifiers.new(name="Boolean_5", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_5")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding band_side_l
tool_obj = bpy.data.objects["band_side_l"]
mod = base_obj.modifiers.new(name="Boolean_6", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_6")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding band_side_r
tool_obj = bpy.data.objects["band_side_r"]
mod = base_obj.modifiers.new(name="Boolean_7", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_7")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding lock
tool_obj = bpy.data.objects["lock"]
mod = base_obj.modifiers.new(name="Boolean_8", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_8")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tooth_upper_0
tool_obj = bpy.data.objects["tooth_upper_0"]
mod = base_obj.modifiers.new(name="Boolean_9", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_9")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tooth_upper_1
tool_obj = bpy.data.objects["tooth_upper_1"]
mod = base_obj.modifiers.new(name="Boolean_10", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_10")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tooth_upper_2
tool_obj = bpy.data.objects["tooth_upper_2"]
mod = base_obj.modifiers.new(name="Boolean_11", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_11")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tooth_upper_3
tool_obj = bpy.data.objects["tooth_upper_3"]
mod = base_obj.modifiers.new(name="Boolean_12", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_12")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tooth_upper_4
tool_obj = bpy.data.objects["tooth_upper_4"]
mod = base_obj.modifiers.new(name="Boolean_13", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_13")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tooth_lower_0
tool_obj = bpy.data.objects["tooth_lower_0"]
mod = base_obj.modifiers.new(name="Boolean_14", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_14")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tooth_lower_1
tool_obj = bpy.data.objects["tooth_lower_1"]
mod = base_obj.modifiers.new(name="Boolean_15", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_15")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tooth_lower_2
tool_obj = bpy.data.objects["tooth_lower_2"]
mod = base_obj.modifiers.new(name="Boolean_16", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_16")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tooth_lower_3
tool_obj = bpy.data.objects["tooth_lower_3"]
mod = base_obj.modifiers.new(name="Boolean_17", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_17")
bpy.data.objects.remove(tool_obj, do_unlink=True)


base_obj.name = "mimic"


# Clean mesh for printing: mimic
obj = bpy.data.objects["mimic"]
bpy.context.view_layer.objects.active = obj
bpy.ops.object.mode_set(mode='EDIT')

# Select all geometry
bpy.ops.mesh.select_all(action='SELECT')

# Merge vertices that are very close (remove doubles)
bpy.ops.mesh.remove_doubles(threshold=0.0001)

# Delete loose vertices/edges/faces
bpy.ops.mesh.delete_loose(use_verts=True, use_edges=True, use_faces=True)

# Recalculate normals to point outward
bpy.ops.mesh.normals_make_consistent(inside=False)

# Deselect all
bpy.ops.mesh.select_all(action='DESELECT')

# Check for and select non-manifold geometry
bpy.ops.mesh.select_non_manifold(extend=False)

# Try to fill any small holes (non-manifold edges)
try:
    bpy.ops.mesh.fill_holes(sides=4)
except:
    pass  # May fail if no holes

bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.mode_set(mode='OBJECT')
print(f"Mesh cleaned: mimic")


# Ensure printable before export
for obj in bpy.context.selected_objects:
    if obj.type == 'MESH':
        bpy.context.view_layer.objects.active = obj

        # Voxel remesh to guarantee watertight
        mod = obj.modifiers.new(name="Remesh_Export", type='REMESH')
        mod.mode = 'VOXEL'
        mod.voxel_size = 0.0005  # 0.5mm for miniatures
        mod.adaptivity = 0
        bpy.ops.object.modifier_apply(modifier="Remesh_Export")

        # Light smoothing
        mod_smooth = obj.modifiers.new(name="Smooth_Export", type='SMOOTH')
        mod_smooth.factor = 0.3
        mod_smooth.iterations = 1
        bpy.ops.object.modifier_apply(modifier="Smooth_Export")


# Export to STL (Blender 4.0+ API)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.wm.stl_export(
    filepath="C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/mimic.stl",
    export_selected_objects=True,
    global_scale=1.0,
    ascii_format=False  # Binary STL is smaller and faster
)
print("Exported: C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/mimic.stl")
