import bpy
import bmesh
import math
from mathutils import Vector, Matrix

# Clear default scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)


# Create sphere: torso
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.161, segments=32,
    ring_count=16, location=(0, 0, 0.6669999999999999))
obj = bpy.context.active_object
obj.name = "torso"


# Scale: torso
bpy.data.objects["torso"].scale = (0.95, 0.7, 1.15)


# Create sphere: chest
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.11499999999999999, segments=32,
    ring_count=16, location=(0, 0.046, 0.782))
obj = bpy.context.active_object
obj.name = "chest"


# Scale: chest
bpy.data.objects["chest"].scale = (0.9, 0.65, 0.8)


# Create sphere: belly
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.092, segments=32,
    ring_count=16, location=(0, 0.034499999999999996, 0.5519999999999999))
obj = bpy.context.active_object
obj.name = "belly"


# Scale: belly
bpy.data.objects["belly"].scale = (0.85, 0.75, 0.75)


# Create sphere: head
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.08625, segments=32,
    ring_count=16, location=(0, 0.06899999999999999, 0.9429999999999998))
obj = bpy.context.active_object
obj.name = "head"


# Scale: head
bpy.data.objects["head"].scale = (0.9, 1.0, 0.95)


# Create cone: snout
bpy.ops.mesh.primitive_cone_add(radius1=0.05175, radius2=0.025299999999999996,
    depth=0.07475, vertices=32, location=(0, 0.1495, 0.9199999999999999))
obj = bpy.context.active_object
obj.name = "snout"


# Rotate: snout (degrees)
import math
bpy.data.objects["snout"].rotation_euler = (
    math.radians(75),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: brow_r
bpy.ops.mesh.primitive_cylinder_add(radius=0.020699999999999996, depth=0.04025,
    vertices=32, location=(0.034499999999999996, 0.11499999999999999, 1.0005))
obj = bpy.context.active_object
obj.name = "brow_r"


# Rotate: brow_r (degrees)
import math
bpy.data.objects["brow_r"].rotation_euler = (
    math.radians(65),
    math.radians(25),
    math.radians(0)
)


# Create cylinder: brow_l
bpy.ops.mesh.primitive_cylinder_add(radius=0.020699999999999996, depth=0.04025,
    vertices=32, location=(-0.034499999999999996, 0.11499999999999999, 1.0005))
obj = bpy.context.active_object
obj.name = "brow_l"


# Rotate: brow_l (degrees)
import math
bpy.data.objects["brow_l"].rotation_euler = (
    math.radians(65),
    math.radians(-25),
    math.radians(0)
)


# Create sphere: eye_r
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0161, segments=32,
    ring_count=16, location=(0.04025, 0.11499999999999999, 0.9659999999999999))
obj = bpy.context.active_object
obj.name = "eye_r"


# Create sphere: eye_l
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0161, segments=32,
    ring_count=16, location=(-0.04025, 0.11499999999999999, 0.9659999999999999))
obj = bpy.context.active_object
obj.name = "eye_l"


# Create torus: crown_ring
bpy.ops.mesh.primitive_torus_add(major_radius=0.06325, minor_radius=0.0092,
    major_segments=32, minor_segments=8, location=(0, 0.023, 1.058))
obj = bpy.context.active_object
obj.name = "crown_ring"


# Rotate: crown_ring (degrees)
import math
bpy.data.objects["crown_ring"].rotation_euler = (
    math.radians(15),
    math.radians(0),
    math.radians(0)
)


# Create cone: crown_spike_0
bpy.ops.mesh.primitive_cone_add(radius1=0.0115, radius2=0.00345,
    depth=0.034499999999999996, vertices=32, location=(0.030417886806135483, 0.06486662945890354, 1.058))
obj = bpy.context.active_object
obj.name = "crown_spike_0"


# Rotate: crown_spike_0 (degrees)
import math
bpy.data.objects["crown_spike_0"].rotation_euler = (
    math.radians(15),
    math.radians(0),
    math.radians(0)
)


# Create cone: crown_spike_1
bpy.ops.mesh.primitive_cone_add(radius1=0.0115, radius2=0.00345,
    depth=0.034499999999999996, vertices=32, location=(0.04610958762674803, 0.046494008361521545, 1.058))
obj = bpy.context.active_object
obj.name = "crown_spike_1"


# Rotate: crown_spike_1 (degrees)
import math
bpy.data.objects["crown_spike_1"].rotation_euler = (
    math.radians(15),
    math.radians(0),
    math.radians(0)
)


# Create cone: crown_spike_2
bpy.ops.mesh.primitive_cone_add(radius1=0.0115, radius2=0.00345,
    depth=0.046, vertices=32, location=(0.05175, 0.023000000000000003, 1.058))
obj = bpy.context.active_object
obj.name = "crown_spike_2"


# Rotate: crown_spike_2 (degrees)
import math
bpy.data.objects["crown_spike_2"].rotation_euler = (
    math.radians(15),
    math.radians(0),
    math.radians(0)
)


# Create cone: crown_spike_3
bpy.ops.mesh.primitive_cone_add(radius1=0.0115, radius2=0.00345,
    depth=0.034499999999999996, vertices=32, location=(0.046109587626748036, -0.0004940083615215425, 1.058))
obj = bpy.context.active_object
obj.name = "crown_spike_3"


# Rotate: crown_spike_3 (degrees)
import math
bpy.data.objects["crown_spike_3"].rotation_euler = (
    math.radians(15),
    math.radians(0),
    math.radians(0)
)


# Create cone: crown_spike_4
bpy.ops.mesh.primitive_cone_add(radius1=0.0115, radius2=0.00345,
    depth=0.034499999999999996, vertices=32, location=(0.03041788680613549, -0.018866629458903522, 1.058))
obj = bpy.context.active_object
obj.name = "crown_spike_4"


# Rotate: crown_spike_4 (degrees)
import math
bpy.data.objects["crown_spike_4"].rotation_euler = (
    math.radians(15),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: arm_r_up
bpy.ops.mesh.primitive_cylinder_add(radius=0.0322, depth=0.1495,
    vertices=32, location=(0.184, 0, 0.713))
obj = bpy.context.active_object
obj.name = "arm_r_up"


# Rotate: arm_r_up (degrees)
import math
bpy.data.objects["arm_r_up"].rotation_euler = (
    math.radians(-20),
    math.radians(55),
    math.radians(20)
)


# Create cylinder: arm_r_low
bpy.ops.mesh.primitive_cylinder_add(radius=0.025299999999999996, depth=0.1265,
    vertices=32, location=(0.299, 0.023, 0.8049999999999999))
obj = bpy.context.active_object
obj.name = "arm_r_low"


# Rotate: arm_r_low (degrees)
import math
bpy.data.objects["arm_r_low"].rotation_euler = (
    math.radians(-50),
    math.radians(30),
    math.radians(0)
)


# Create cylinder: arm_l_up
bpy.ops.mesh.primitive_cylinder_add(radius=0.0322, depth=0.1495,
    vertices=32, location=(-0.184, 0.023, 0.6669999999999999))
obj = bpy.context.active_object
obj.name = "arm_l_up"


# Rotate: arm_l_up (degrees)
import math
bpy.data.objects["arm_l_up"].rotation_euler = (
    math.radians(15),
    math.radians(-45),
    math.radians(0)
)


# Create cylinder: arm_l_low
bpy.ops.mesh.primitive_cylinder_add(radius=0.025299999999999996, depth=0.1265,
    vertices=32, location=(-0.27599999999999997, 0.057499999999999996, 0.5519999999999999))
obj = bpy.context.active_object
obj.name = "arm_l_low"


# Rotate: arm_l_low (degrees)
import math
bpy.data.objects["arm_l_low"].rotation_euler = (
    math.radians(30),
    math.radians(-25),
    math.radians(0)
)


# Create cylinder: scepter_shaft
bpy.ops.mesh.primitive_cylinder_add(radius=0.0092, depth=0.207,
    vertices=32, location=(0.345, 0.034499999999999996, 0.9429999999999998))
obj = bpy.context.active_object
obj.name = "scepter_shaft"


# Rotate: scepter_shaft (degrees)
import math
bpy.data.objects["scepter_shaft"].rotation_euler = (
    math.radians(-40),
    math.radians(20),
    math.radians(0)
)


# Create sphere: scepter_orb
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.023, segments=32,
    ring_count=16, location=(0.368, 0.046, 1.0924999999999998))
obj = bpy.context.active_object
obj.name = "scepter_orb"


# Create cylinder: leg_r_up
bpy.ops.mesh.primitive_cylinder_add(radius=0.046, depth=0.184,
    vertices=32, location=(0.0805, 0, 0.391))
obj = bpy.context.active_object
obj.name = "leg_r_up"


# Rotate: leg_r_up (degrees)
import math
bpy.data.objects["leg_r_up"].rotation_euler = (
    math.radians(8),
    math.radians(8),
    math.radians(0)
)


# Create cylinder: leg_l_up
bpy.ops.mesh.primitive_cylinder_add(radius=0.046, depth=0.184,
    vertices=32, location=(-0.0805, 0, 0.391))
obj = bpy.context.active_object
obj.name = "leg_l_up"


# Rotate: leg_l_up (degrees)
import math
bpy.data.objects["leg_l_up"].rotation_euler = (
    math.radians(8),
    math.radians(-8),
    math.radians(0)
)


# Create cylinder: leg_r_low
bpy.ops.mesh.primitive_cylinder_add(radius=0.0322, depth=0.1495,
    vertices=32, location=(0.092, 0.023, 0.1495))
obj = bpy.context.active_object
obj.name = "leg_r_low"


# Rotate: leg_r_low (degrees)
import math
bpy.data.objects["leg_r_low"].rotation_euler = (
    math.radians(-5),
    math.radians(5),
    math.radians(0)
)


# Create cylinder: leg_l_low
bpy.ops.mesh.primitive_cylinder_add(radius=0.0322, depth=0.1495,
    vertices=32, location=(-0.092, 0.023, 0.1495))
obj = bpy.context.active_object
obj.name = "leg_l_low"


# Rotate: leg_l_low (degrees)
import math
bpy.data.objects["leg_l_low"].rotation_euler = (
    math.radians(-5),
    math.radians(-5),
    math.radians(0)
)


# Create sphere: foot_r
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0322, segments=32,
    ring_count=16, location=(0.092, 0.046, 0.02))
obj = bpy.context.active_object
obj.name = "foot_r"


# Scale: foot_r
bpy.data.objects["foot_r"].scale = (0.7, 1.3, 0.4)


# Create sphere: foot_l
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0322, segments=32,
    ring_count=16, location=(-0.092, 0.046, 0.02))
obj = bpy.context.active_object
obj.name = "foot_l"


# Scale: foot_l
bpy.data.objects["foot_l"].scale = (0.7, 1.3, 0.4)


# Create cone: tail
bpy.ops.mesh.primitive_cone_add(radius1=0.04025, radius2=0.0138,
    depth=0.184, vertices=32, location=(0, -0.13799999999999998, 0.45999999999999996))
obj = bpy.context.active_object
obj.name = "tail"


# Rotate: tail (degrees)
import math
bpy.data.objects["tail"].rotation_euler = (
    math.radians(115),
    math.radians(0),
    math.radians(0)
)


# Union objects into: troglodyte-king
# Using boolean EXACT solver for watertight results
base_obj = bpy.data.objects["torso"]
bpy.context.view_layer.objects.active = base_obj


# Boolean union: adding chest
tool_obj = bpy.data.objects["chest"]
mod = base_obj.modifiers.new(name="Boolean_0", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_0")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding belly
tool_obj = bpy.data.objects["belly"]
mod = base_obj.modifiers.new(name="Boolean_1", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_1")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head
tool_obj = bpy.data.objects["head"]
mod = base_obj.modifiers.new(name="Boolean_2", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_2")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding snout
tool_obj = bpy.data.objects["snout"]
mod = base_obj.modifiers.new(name="Boolean_3", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_3")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding brow_r
tool_obj = bpy.data.objects["brow_r"]
mod = base_obj.modifiers.new(name="Boolean_4", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_4")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding brow_l
tool_obj = bpy.data.objects["brow_l"]
mod = base_obj.modifiers.new(name="Boolean_5", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_5")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_r
tool_obj = bpy.data.objects["eye_r"]
mod = base_obj.modifiers.new(name="Boolean_6", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_6")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_l
tool_obj = bpy.data.objects["eye_l"]
mod = base_obj.modifiers.new(name="Boolean_7", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_7")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding crown_ring
tool_obj = bpy.data.objects["crown_ring"]
mod = base_obj.modifiers.new(name="Boolean_8", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_8")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_r_up
tool_obj = bpy.data.objects["arm_r_up"]
mod = base_obj.modifiers.new(name="Boolean_9", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_9")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_r_low
tool_obj = bpy.data.objects["arm_r_low"]
mod = base_obj.modifiers.new(name="Boolean_10", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_10")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_l_up
tool_obj = bpy.data.objects["arm_l_up"]
mod = base_obj.modifiers.new(name="Boolean_11", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_11")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_l_low
tool_obj = bpy.data.objects["arm_l_low"]
mod = base_obj.modifiers.new(name="Boolean_12", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_12")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding scepter_shaft
tool_obj = bpy.data.objects["scepter_shaft"]
mod = base_obj.modifiers.new(name="Boolean_13", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_13")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding scepter_orb
tool_obj = bpy.data.objects["scepter_orb"]
mod = base_obj.modifiers.new(name="Boolean_14", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_14")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_r_up
tool_obj = bpy.data.objects["leg_r_up"]
mod = base_obj.modifiers.new(name="Boolean_15", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_15")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_l_up
tool_obj = bpy.data.objects["leg_l_up"]
mod = base_obj.modifiers.new(name="Boolean_16", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_16")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_r_low
tool_obj = bpy.data.objects["leg_r_low"]
mod = base_obj.modifiers.new(name="Boolean_17", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_17")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_l_low
tool_obj = bpy.data.objects["leg_l_low"]
mod = base_obj.modifiers.new(name="Boolean_18", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_18")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding foot_r
tool_obj = bpy.data.objects["foot_r"]
mod = base_obj.modifiers.new(name="Boolean_19", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_19")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding foot_l
tool_obj = bpy.data.objects["foot_l"]
mod = base_obj.modifiers.new(name="Boolean_20", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_20")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tail
tool_obj = bpy.data.objects["tail"]
mod = base_obj.modifiers.new(name="Boolean_21", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_21")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding crown_spike_0
tool_obj = bpy.data.objects["crown_spike_0"]
mod = base_obj.modifiers.new(name="Boolean_22", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_22")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding crown_spike_1
tool_obj = bpy.data.objects["crown_spike_1"]
mod = base_obj.modifiers.new(name="Boolean_23", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_23")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding crown_spike_2
tool_obj = bpy.data.objects["crown_spike_2"]
mod = base_obj.modifiers.new(name="Boolean_24", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_24")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding crown_spike_3
tool_obj = bpy.data.objects["crown_spike_3"]
mod = base_obj.modifiers.new(name="Boolean_25", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_25")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding crown_spike_4
tool_obj = bpy.data.objects["crown_spike_4"]
mod = base_obj.modifiers.new(name="Boolean_26", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_26")
bpy.data.objects.remove(tool_obj, do_unlink=True)


base_obj.name = "troglodyte-king"


# Add subdivision surface: troglodyte-king
obj = bpy.data.objects["troglodyte-king"]
mod = obj.modifiers.new(name="Subdivision", type='SUBSURF')
mod.levels = 1
mod.render_levels = 2


# Add displacement: troglodyte-king
obj = bpy.data.objects["troglodyte-king"]
tex = bpy.data.textures.new("troglodyte-king_displace_tex", type='VORONOI')
mod = obj.modifiers.new(name="Displace", type='DISPLACE')
mod.texture = tex
mod.strength = 0.003


# Apply all modifiers: troglodyte-king
obj = bpy.data.objects["troglodyte-king"]
bpy.context.view_layer.objects.active = obj
for mod in obj.modifiers[:]:
    bpy.ops.object.modifier_apply(modifier=mod.name)


# Create cylinder: troglodyte-king_base
bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=0.003,
    vertices=48, location=(0, 0, 0.0015))
obj = bpy.context.active_object
obj.name = "troglodyte-king_base"


# Add bevel: troglodyte-king_base
obj = bpy.data.objects["troglodyte-king_base"]
mod = obj.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.0004
mod.segments = 2


# Boolean union: troglodyte-king + troglodyte-king_base
target_obj = bpy.data.objects["troglodyte-king"]
tool_obj = bpy.data.objects["troglodyte-king_base"]
mod = target_obj.modifiers.new(name="Boolean", type='BOOLEAN')
mod.operation = 'UNION'
mod.object = tool_obj
bpy.context.view_layer.objects.active = target_obj
bpy.ops.object.modifier_apply(modifier='Boolean')
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Export to STL (Blender 4.0+ API)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.wm.stl_export(
    filepath="C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/troglodyte-king.stl",
    export_selected_objects=True,
    global_scale=1.0,
    ascii_format=False  # Binary STL is smaller and faster
)
print("Exported: C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/troglodyte-king.stl")
