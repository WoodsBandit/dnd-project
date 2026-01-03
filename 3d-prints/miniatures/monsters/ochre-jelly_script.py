import bpy
import bmesh
import math
from mathutils import Vector, Matrix

# Clear default scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)


# Create metaball sphere: ooze_meta
bpy.ops.object.metaball_add(type='BALL', radius=0.12, location=(0, 0, 0.12))
obj = bpy.context.active_object
obj.name = "ooze_meta"


# Add metaball element to: ooze_meta
mball = bpy.data.metaballs[bpy.data.objects["ooze_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.07
elem.co = (0.08, 0.06, 0.1)


# Add metaball element to: ooze_meta
mball = bpy.data.metaballs[bpy.data.objects["ooze_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.065
elem.co = (-0.07, 0.05, 0.11)


# Add metaball element to: ooze_meta
mball = bpy.data.metaballs[bpy.data.objects["ooze_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.06
elem.co = (0.05, -0.08, 0.09)


# Add metaball element to: ooze_meta
mball = bpy.data.metaballs[bpy.data.objects["ooze_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.055
elem.co = (-0.06, -0.06, 0.1)


# Add metaball element to: ooze_meta
mball = bpy.data.metaballs[bpy.data.objects["ooze_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.05
elem.co = (0, 0.1, 0.14)


# Add metaball element to: ooze_meta
mball = bpy.data.metaballs[bpy.data.objects["ooze_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.05
elem.co = (0.1, 0, 0.08)


# Add metaball element to: ooze_meta
mball = bpy.data.metaballs[bpy.data.objects["ooze_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.045
elem.co = (-0.09, 0.02, 0.07)


# Add metaball element to: ooze_meta
mball = bpy.data.metaballs[bpy.data.objects["ooze_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.04
elem.co = (0.03, -0.1, 0.06)


# Add metaball element to: ooze_meta
mball = bpy.data.metaballs[bpy.data.objects["ooze_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.06
elem.co = (0, 0, 0.18)


# Add metaball element to: ooze_meta
mball = bpy.data.metaballs[bpy.data.objects["ooze_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.04
elem.co = (0.06, 0.04, 0.16)


# Add metaball element to: ooze_meta
mball = bpy.data.metaballs[bpy.data.objects["ooze_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.035
elem.co = (-0.04, 0.06, 0.15)


# Add metaball element to: ooze_meta
mball = bpy.data.metaballs[bpy.data.objects["ooze_meta"].data.name]
elem = mball.elements.new(type='ELLIPSOID')
elem.radius = 0.035
elem.co = (0.15, 0.08, 0.08)


# Add metaball element to: ooze_meta
mball = bpy.data.metaballs[bpy.data.objects["ooze_meta"].data.name]
elem = mball.elements.new(type='ELLIPSOID')
elem.radius = 0.03
elem.co = (-0.14, 0.06, 0.09)


# Add metaball element to: ooze_meta
mball = bpy.data.metaballs[bpy.data.objects["ooze_meta"].data.name]
elem = mball.elements.new(type='ELLIPSOID')
elem.radius = 0.03
elem.co = (0.12, -0.1, 0.07)


# Add metaball element to: ooze_meta
mball = bpy.data.metaballs[bpy.data.objects["ooze_meta"].data.name]
elem = mball.elements.new(type='ELLIPSOID')
elem.radius = 0.025
elem.co = (0.08, 0.12, 0.12)


# Convert metaball to mesh: ooze_meta
obj = bpy.data.objects["ooze_meta"]
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
bpy.ops.object.convert(target='MESH')

bpy.context.active_object.name = "ooze_body"

# Create sphere: victim_skull
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.035, segments=32,
    ring_count=16, location=(0.04, 0.06, 0.17))
obj = bpy.context.active_object
obj.name = "victim_skull"


# Scale: victim_skull
bpy.data.objects["victim_skull"].scale = (0.8, 0.9, 1.0)


# Create sphere: socket_r
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.01, segments=32,
    ring_count=16, location=(0.055, 0.08, 0.18))
obj = bpy.context.active_object
obj.name = "socket_r"


# Create sphere: socket_l
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.01, segments=32,
    ring_count=16, location=(0.025, 0.08, 0.18))
obj = bpy.context.active_object
obj.name = "socket_l"


# Create sphere: victim_jaw
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.02, segments=32,
    ring_count=16, location=(0.04, 0.08, 0.14))
obj = bpy.context.active_object
obj.name = "victim_jaw"


# Scale: victim_jaw
bpy.data.objects["victim_jaw"].scale = (0.9, 0.7, 0.5)


# Create sphere: victim_palm
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.02, segments=32,
    ring_count=16, location=(-0.08, 0.08, 0.14))
obj = bpy.context.active_object
obj.name = "victim_palm"


# Scale: victim_palm
bpy.data.objects["victim_palm"].scale = (1.0, 0.7, 0.5)


# Create cylinder: victim_finger_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.004, depth=0.025,
    vertices=32, location=(-0.09, 0.1, 0.145))
obj = bpy.context.active_object
obj.name = "victim_finger_0"


# Rotate: victim_finger_0 (degrees)
import math
bpy.data.objects["victim_finger_0"].rotation_euler = (
    math.radians(70),
    math.radians(0),
    math.radians(-12)
)


# Create cylinder: victim_finger_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.004, depth=0.025,
    vertices=32, location=(-0.078, 0.1, 0.145))
obj = bpy.context.active_object
obj.name = "victim_finger_1"


# Rotate: victim_finger_1 (degrees)
import math
bpy.data.objects["victim_finger_1"].rotation_euler = (
    math.radians(70),
    math.radians(0),
    math.radians(-4)
)


# Create cylinder: victim_finger_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.004, depth=0.025,
    vertices=32, location=(-0.066, 0.1, 0.145))
obj = bpy.context.active_object
obj.name = "victim_finger_2"


# Rotate: victim_finger_2 (degrees)
import math
bpy.data.objects["victim_finger_2"].rotation_euler = (
    math.radians(70),
    math.radians(0),
    math.radians(4)
)


# Create cylinder: victim_finger_3
bpy.ops.mesh.primitive_cylinder_add(radius=0.004, depth=0.025,
    vertices=32, location=(-0.05399999999999999, 0.1, 0.145))
obj = bpy.context.active_object
obj.name = "victim_finger_3"


# Rotate: victim_finger_3 (degrees)
import math
bpy.data.objects["victim_finger_3"].rotation_euler = (
    math.radians(70),
    math.radians(0),
    math.radians(12)
)


# Create cylinder: victim_arm
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.06,
    vertices=32, location=(-0.06, 0.04, 0.11))
obj = bpy.context.active_object
obj.name = "victim_arm"


# Rotate: victim_arm (degrees)
import math
bpy.data.objects["victim_arm"].rotation_euler = (
    math.radians(45),
    math.radians(-20),
    math.radians(0)
)


# Create torus: victim_rib_0
bpy.ops.mesh.primitive_torus_add(major_radius=0.025, minor_radius=0.004,
    major_segments=16, minor_segments=6, location=(0.02, -0.02, 0.1))
obj = bpy.context.active_object
obj.name = "victim_rib_0"


# Scale: victim_rib_0
bpy.data.objects["victim_rib_0"].scale = (0.6, 0.4, 0.3)


# Rotate: victim_rib_0 (degrees)
import math
bpy.data.objects["victim_rib_0"].rotation_euler = (
    math.radians(80),
    math.radians(0),
    math.radians(0)
)


# Create torus: victim_rib_1
bpy.ops.mesh.primitive_torus_add(major_radius=0.025, minor_radius=0.004,
    major_segments=16, minor_segments=6, location=(0.02, -0.02, 0.12000000000000001))
obj = bpy.context.active_object
obj.name = "victim_rib_1"


# Scale: victim_rib_1
bpy.data.objects["victim_rib_1"].scale = (0.6, 0.4, 0.3)


# Rotate: victim_rib_1 (degrees)
import math
bpy.data.objects["victim_rib_1"].rotation_euler = (
    math.radians(80),
    math.radians(0),
    math.radians(0)
)


# Create torus: victim_rib_2
bpy.ops.mesh.primitive_torus_add(major_radius=0.025, minor_radius=0.004,
    major_segments=16, minor_segments=6, location=(0.02, -0.02, 0.14))
obj = bpy.context.active_object
obj.name = "victim_rib_2"


# Scale: victim_rib_2
bpy.data.objects["victim_rib_2"].scale = (0.6, 0.4, 0.3)


# Rotate: victim_rib_2 (degrees)
import math
bpy.data.objects["victim_rib_2"].rotation_euler = (
    math.radians(80),
    math.radians(0),
    math.radians(0)
)


# Create sphere: debris_0
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012, segments=32,
    ring_count=16, location=(0.1, 0.0, 0.08))
obj = bpy.context.active_object
obj.name = "debris_0"


# Scale: debris_0
bpy.data.objects["debris_0"].scale = (0.8, 0.8, 0.5)


# Create sphere: debris_1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012, segments=32,
    ring_count=16, location=(0.030901699437494747, 0.09510565162951536, 0.08))
obj = bpy.context.active_object
obj.name = "debris_1"


# Scale: debris_1
bpy.data.objects["debris_1"].scale = (0.8, 0.8, 0.5)


# Create sphere: debris_2
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012, segments=32,
    ring_count=16, location=(-0.08090169943749474, 0.05877852522924733, 0.08))
obj = bpy.context.active_object
obj.name = "debris_2"


# Scale: debris_2
bpy.data.objects["debris_2"].scale = (0.8, 0.8, 0.5)


# Create sphere: debris_3
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012, segments=32,
    ring_count=16, location=(-0.08090169943749476, -0.05877852522924731, 0.08))
obj = bpy.context.active_object
obj.name = "debris_3"


# Scale: debris_3
bpy.data.objects["debris_3"].scale = (0.8, 0.8, 0.5)


# Create sphere: debris_4
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012, segments=32,
    ring_count=16, location=(0.030901699437494726, -0.09510565162951537, 0.08))
obj = bpy.context.active_object
obj.name = "debris_4"


# Scale: debris_4
bpy.data.objects["debris_4"].scale = (0.8, 0.8, 0.5)


# Union objects into: ochre-jelly
# Using boolean EXACT solver for watertight results
base_obj = bpy.data.objects["ooze_body"]
bpy.context.view_layer.objects.active = base_obj


# Boolean union: adding victim_skull
tool_obj = bpy.data.objects["victim_skull"]
mod = base_obj.modifiers.new(name="Boolean_0", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_0")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding socket_r
tool_obj = bpy.data.objects["socket_r"]
mod = base_obj.modifiers.new(name="Boolean_1", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_1")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding socket_l
tool_obj = bpy.data.objects["socket_l"]
mod = base_obj.modifiers.new(name="Boolean_2", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_2")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding victim_jaw
tool_obj = bpy.data.objects["victim_jaw"]
mod = base_obj.modifiers.new(name="Boolean_3", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_3")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding victim_palm
tool_obj = bpy.data.objects["victim_palm"]
mod = base_obj.modifiers.new(name="Boolean_4", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_4")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding victim_arm
tool_obj = bpy.data.objects["victim_arm"]
mod = base_obj.modifiers.new(name="Boolean_5", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_5")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding victim_finger_0
tool_obj = bpy.data.objects["victim_finger_0"]
mod = base_obj.modifiers.new(name="Boolean_6", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_6")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding victim_finger_1
tool_obj = bpy.data.objects["victim_finger_1"]
mod = base_obj.modifiers.new(name="Boolean_7", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_7")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding victim_finger_2
tool_obj = bpy.data.objects["victim_finger_2"]
mod = base_obj.modifiers.new(name="Boolean_8", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_8")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding victim_finger_3
tool_obj = bpy.data.objects["victim_finger_3"]
mod = base_obj.modifiers.new(name="Boolean_9", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_9")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding victim_rib_0
tool_obj = bpy.data.objects["victim_rib_0"]
mod = base_obj.modifiers.new(name="Boolean_10", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_10")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding victim_rib_1
tool_obj = bpy.data.objects["victim_rib_1"]
mod = base_obj.modifiers.new(name="Boolean_11", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_11")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding victim_rib_2
tool_obj = bpy.data.objects["victim_rib_2"]
mod = base_obj.modifiers.new(name="Boolean_12", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_12")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding debris_0
tool_obj = bpy.data.objects["debris_0"]
mod = base_obj.modifiers.new(name="Boolean_13", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_13")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding debris_1
tool_obj = bpy.data.objects["debris_1"]
mod = base_obj.modifiers.new(name="Boolean_14", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_14")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding debris_2
tool_obj = bpy.data.objects["debris_2"]
mod = base_obj.modifiers.new(name="Boolean_15", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_15")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding debris_3
tool_obj = bpy.data.objects["debris_3"]
mod = base_obj.modifiers.new(name="Boolean_16", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_16")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding debris_4
tool_obj = bpy.data.objects["debris_4"]
mod = base_obj.modifiers.new(name="Boolean_17", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_17")
bpy.data.objects.remove(tool_obj, do_unlink=True)


base_obj.name = "ochre-jelly"


# Add subdivision surface: ochre-jelly
obj = bpy.data.objects["ochre-jelly"]
mod = obj.modifiers.new(name="Subdivision", type='SUBSURF')
mod.levels = 1
mod.render_levels = 2


# Add smooth: ochre-jelly
obj = bpy.data.objects["ochre-jelly"]
mod = obj.modifiers.new(name="Smooth", type='SMOOTH')
mod.factor = 0.4
mod.iterations = 2


# Apply all modifiers: ochre-jelly
obj = bpy.data.objects["ochre-jelly"]
bpy.context.view_layer.objects.active = obj
for mod in obj.modifiers[:]:
    bpy.ops.object.modifier_apply(modifier=mod.name)


# Create cylinder: ochre-jelly_base
bpy.ops.mesh.primitive_cylinder_add(radius=0.025, depth=0.003,
    vertices=64, location=(0, 0, 0.0015))
obj = bpy.context.active_object
obj.name = "ochre-jelly_base"


# Add bevel: ochre-jelly_base
obj = bpy.data.objects["ochre-jelly_base"]
mod = obj.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.0005
mod.segments = 2


# Boolean union: ochre-jelly + ochre-jelly_base
target_obj = bpy.data.objects["ochre-jelly"]
tool_obj = bpy.data.objects["ochre-jelly_base"]
mod = target_obj.modifiers.new(name="Boolean", type='BOOLEAN')
mod.operation = 'UNION'
mod.object = tool_obj
bpy.context.view_layer.objects.active = target_obj
bpy.ops.object.modifier_apply(modifier='Boolean')
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Export to STL (Blender 4.0+ API)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.wm.stl_export(
    filepath="C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/ochre-jelly.stl",
    export_selected_objects=True,
    global_scale=1.0,
    ascii_format=False  # Binary STL is smaller and faster
)
print("Exported: C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/ochre-jelly.stl")
