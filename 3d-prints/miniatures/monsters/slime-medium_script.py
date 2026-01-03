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


# Create metaball sphere: slime_meta
bpy.ops.object.metaball_add(type='BALL', radius=0.008, location=(0, 0, 0.012))
obj = bpy.context.active_object
obj.name = "slime_meta"


# Add metaball element to: slime_meta
mball = bpy.data.metaballs[bpy.data.objects["slime_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.006
elem.co = (0.005, 0.003, 0.01)


# Add metaball element to: slime_meta
mball = bpy.data.metaballs[bpy.data.objects["slime_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.005
elem.co = (-0.004, 0.004, 0.008)


# Add metaball element to: slime_meta
mball = bpy.data.metaballs[bpy.data.objects["slime_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.0055
elem.co = (0.003, -0.005, 0.009)


# Add metaball element to: slime_meta
mball = bpy.data.metaballs[bpy.data.objects["slime_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.0045
elem.co = (-0.003, -0.003, 0.011)


# Add metaball element to: slime_meta
mball = bpy.data.metaballs[bpy.data.objects["slime_meta"].data.name]
elem = mball.elements.new(type='CAPSULE')
elem.radius = 0.003
elem.co = (0.006, 0, 0.018)


# Add metaball element to: slime_meta
mball = bpy.data.metaballs[bpy.data.objects["slime_meta"].data.name]
elem = mball.elements.new(type='CAPSULE')
elem.radius = 0.0025
elem.co = (-0.004, 0.005, 0.016)


# Add metaball element to: slime_meta
mball = bpy.data.metaballs[bpy.data.objects["slime_meta"].data.name]
elem = mball.elements.new(type='CAPSULE')
elem.radius = 0.002
elem.co = (0, -0.006, 0.015)


# Add metaball element to: slime_meta
mball = bpy.data.metaballs[bpy.data.objects["slime_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.002
elem.co = (0.007, 0.002, 0.015)


# Add metaball element to: slime_meta
mball = bpy.data.metaballs[bpy.data.objects["slime_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.0015
elem.co = (-0.005, -0.002, 0.014)


# Add metaball element to: slime_meta
mball = bpy.data.metaballs[bpy.data.objects["slime_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.0018
elem.co = (0.002, 0.006, 0.013)


# Convert metaball to mesh: slime_meta
obj = bpy.data.objects["slime_meta"]
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
bpy.ops.object.convert(target='MESH')

bpy.context.active_object.name = "slime_body"

# Add displacement: slime_body
obj = bpy.data.objects["slime_body"]
tex = bpy.data.textures.new("slime_body_displace_tex", type='CLOUDS')
mod = obj.modifiers.new(name="Displace", type='DISPLACE')
mod.texture = tex
mod.strength = 0.001


# Add smooth: slime_body
obj = bpy.data.objects["slime_body"]
mod = obj.modifiers.new(name="Smooth", type='SMOOTH')
mod.factor = 0.3
mod.iterations = 2


# Apply all modifiers: slime_body
obj = bpy.data.objects["slime_body"]
bpy.context.view_layer.objects.active = obj
for mod in obj.modifiers[:]:
    bpy.ops.object.modifier_apply(modifier=mod.name)


# Union objects into: slime-medium
# Using boolean EXACT solver for watertight results
base_obj = bpy.data.objects["base"]
bpy.context.view_layer.objects.active = base_obj


# Boolean union: adding slime_body
tool_obj = bpy.data.objects["slime_body"]
mod = base_obj.modifiers.new(name="Boolean_0", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_0")
bpy.data.objects.remove(tool_obj, do_unlink=True)


base_obj.name = "slime-medium"


# Clean mesh for printing: slime-medium
obj = bpy.data.objects["slime-medium"]
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
print(f"Mesh cleaned: slime-medium")


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
    filepath="C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/slime-medium.stl",
    export_selected_objects=True,
    global_scale=1.0,
    ascii_format=False  # Binary STL is smaller and faster
)
print("Exported: C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/slime-medium.stl")
