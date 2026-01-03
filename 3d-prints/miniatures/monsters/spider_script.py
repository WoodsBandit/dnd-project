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


# Create sphere: abdomen
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.007, segments=24,
    ring_count=16, location=(0, -0.004, 0.012))
obj = bpy.context.active_object
obj.name = "abdomen"


# Scale: abdomen
bpy.data.objects["abdomen"].scale = (0.8, 1.2, 0.9)


# Create sphere: cephalothorax
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.005, segments=20,
    ring_count=14, location=(0, 0.006, 0.01))
obj = bpy.context.active_object
obj.name = "cephalothorax"


# Scale: cephalothorax
bpy.data.objects["cephalothorax"].scale = (1.0, 0.9, 0.7)


# Create sphere: head
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.003, segments=16,
    ring_count=12, location=(0, 0.012, 0.009))
obj = bpy.context.active_object
obj.name = "head"


# Create cone: fang_l
bpy.ops.mesh.primitive_cone_add(radius1=0.001, radius2=0,
    depth=0.004, vertices=8, location=(-0.002, 0.016, 0.007))
obj = bpy.context.active_object
obj.name = "fang_l"


# Rotate: fang_l (degrees)
import math
bpy.data.objects["fang_l"].rotation_euler = (
    math.radians(70),
    math.radians(0),
    math.radians(10)
)


# Create cone: fang_r
bpy.ops.mesh.primitive_cone_add(radius1=0.001, radius2=0,
    depth=0.004, vertices=8, location=(0.002, 0.016, 0.007))
obj = bpy.context.active_object
obj.name = "fang_r"


# Rotate: fang_r (degrees)
import math
bpy.data.objects["fang_r"].rotation_euler = (
    math.radians(70),
    math.radians(0),
    math.radians(-10)
)


# Create sphere: eye_0
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0006, segments=8,
    ring_count=6, location=(-0.0015, 0.014, 0.011))
obj = bpy.context.active_object
obj.name = "eye_0"


# Create sphere: eye_1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0006, segments=8,
    ring_count=6, location=(0.0015, 0.014, 0.011))
obj = bpy.context.active_object
obj.name = "eye_1"


# Create sphere: eye_2
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0006, segments=8,
    ring_count=6, location=(-0.002, 0.013, 0.0115))
obj = bpy.context.active_object
obj.name = "eye_2"


# Create sphere: eye_3
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0006, segments=8,
    ring_count=6, location=(0.002, 0.013, 0.0115))
obj = bpy.context.active_object
obj.name = "eye_3"


# Create sphere: eye_4
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0006, segments=8,
    ring_count=6, location=(-0.0025, 0.012, 0.0112))
obj = bpy.context.active_object
obj.name = "eye_4"


# Create sphere: eye_5
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0006, segments=8,
    ring_count=6, location=(0.0025, 0.012, 0.0112))
obj = bpy.context.active_object
obj.name = "eye_5"


# Create sphere: eye_6
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0006, segments=8,
    ring_count=6, location=(-0.001, 0.0125, 0.012))
obj = bpy.context.active_object
obj.name = "eye_6"


# Create sphere: eye_7
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0006, segments=8,
    ring_count=6, location=(0.001, 0.0125, 0.012))
obj = bpy.context.active_object
obj.name = "eye_7"


# Create cylinder: leg_r1_upper
bpy.ops.mesh.primitive_cylinder_add(radius=0.0008, depth=0.012,
    vertices=8, location=(0.004, 0.008, 0.01))
obj = bpy.context.active_object
obj.name = "leg_r1_upper"


# Rotate: leg_r1_upper (degrees)
import math
bpy.data.objects["leg_r1_upper"].rotation_euler = (
    math.radians(0),
    math.radians(15),
    math.radians(60)
)


# Create cylinder: leg_r1_lower
bpy.ops.mesh.primitive_cylinder_add(radius=0.0006, depth=0.01,
    vertices=8, location=(0.006699999999999999, 0.01267653718043597, 0.015215999461960969))
obj = bpy.context.active_object
obj.name = "leg_r1_lower"


# Rotate: leg_r1_lower (degrees)
import math
bpy.data.objects["leg_r1_lower"].rotation_euler = (
    math.radians(0),
    math.radians(60),
    math.radians(60)
)


# Create cylinder: leg_r2_upper
bpy.ops.mesh.primitive_cylinder_add(radius=0.0008, depth=0.012,
    vertices=8, location=(0.005, 0.004, 0.01))
obj = bpy.context.active_object
obj.name = "leg_r2_upper"


# Rotate: leg_r2_upper (degrees)
import math
bpy.data.objects["leg_r2_upper"].rotation_euler = (
    math.radians(0),
    math.radians(60),
    math.radians(30)
)


# Create cylinder: leg_r2_lower
bpy.ops.mesh.primitive_cylinder_add(radius=0.0006, depth=0.01,
    vertices=8, location=(0.009676537180435969, 0.006700000000000001, 0.0127))
obj = bpy.context.active_object
obj.name = "leg_r2_lower"


# Rotate: leg_r2_lower (degrees)
import math
bpy.data.objects["leg_r2_lower"].rotation_euler = (
    math.radians(0),
    math.radians(120),
    math.radians(30)
)


# Create cylinder: leg_r3_upper
bpy.ops.mesh.primitive_cylinder_add(radius=0.0008, depth=0.012,
    vertices=8, location=(0.005, 0, 0.01))
obj = bpy.context.active_object
obj.name = "leg_r3_upper"


# Rotate: leg_r3_upper (degrees)
import math
bpy.data.objects["leg_r3_upper"].rotation_euler = (
    math.radians(0),
    math.radians(60),
    math.radians(0)
)


# Create cylinder: leg_r3_lower
bpy.ops.mesh.primitive_cylinder_add(radius=0.0006, depth=0.01,
    vertices=8, location=(0.0104, 3.3065463576978538e-19, 0.0127))
obj = bpy.context.active_object
obj.name = "leg_r3_lower"


# Rotate: leg_r3_lower (degrees)
import math
bpy.data.objects["leg_r3_lower"].rotation_euler = (
    math.radians(0),
    math.radians(120),
    math.radians(0)
)


# Create cylinder: leg_r4_upper
bpy.ops.mesh.primitive_cylinder_add(radius=0.0008, depth=0.012,
    vertices=8, location=(0.004, -0.004, 0.01))
obj = bpy.context.active_object
obj.name = "leg_r4_upper"


# Rotate: leg_r4_upper (degrees)
import math
bpy.data.objects["leg_r4_upper"].rotation_euler = (
    math.radians(0),
    math.radians(50),
    math.radians(-30)
)


# Create cylinder: leg_r4_lower
bpy.ops.mesh.primitive_cylinder_add(radius=0.0006, depth=0.01,
    vertices=8, location=(0.00867653718043597, -0.006699999999999999, 0.013471053092307311))
obj = bpy.context.active_object
obj.name = "leg_r4_lower"


# Rotate: leg_r4_lower (degrees)
import math
bpy.data.objects["leg_r4_lower"].rotation_euler = (
    math.radians(0),
    math.radians(120),
    math.radians(-30)
)


# Create cylinder: leg_l1_upper
bpy.ops.mesh.primitive_cylinder_add(radius=0.0008, depth=0.012,
    vertices=8, location=(-0.004, 0.008, 0.01))
obj = bpy.context.active_object
obj.name = "leg_l1_upper"


# Rotate: leg_l1_upper (degrees)
import math
bpy.data.objects["leg_l1_upper"].rotation_euler = (
    math.radians(0),
    math.radians(15),
    math.radians(-60)
)


# Create cylinder: leg_l1_lower
bpy.ops.mesh.primitive_cylinder_add(radius=0.0006, depth=0.01,
    vertices=8, location=(-0.006699999999999999, 0.01267653718043597, 0.015215999461960969))
obj = bpy.context.active_object
obj.name = "leg_l1_lower"


# Rotate: leg_l1_lower (degrees)
import math
bpy.data.objects["leg_l1_lower"].rotation_euler = (
    math.radians(0),
    math.radians(60),
    math.radians(-60)
)


# Create cylinder: leg_l2_upper
bpy.ops.mesh.primitive_cylinder_add(radius=0.0008, depth=0.012,
    vertices=8, location=(-0.005, 0.004, 0.01))
obj = bpy.context.active_object
obj.name = "leg_l2_upper"


# Rotate: leg_l2_upper (degrees)
import math
bpy.data.objects["leg_l2_upper"].rotation_euler = (
    math.radians(0),
    math.radians(60),
    math.radians(-30)
)


# Create cylinder: leg_l2_lower
bpy.ops.mesh.primitive_cylinder_add(radius=0.0006, depth=0.01,
    vertices=8, location=(-0.009676537180435969, 0.006700000000000001, 0.0127))
obj = bpy.context.active_object
obj.name = "leg_l2_lower"


# Rotate: leg_l2_lower (degrees)
import math
bpy.data.objects["leg_l2_lower"].rotation_euler = (
    math.radians(0),
    math.radians(120),
    math.radians(-30)
)


# Create cylinder: leg_l3_upper
bpy.ops.mesh.primitive_cylinder_add(radius=0.0008, depth=0.012,
    vertices=8, location=(-0.005, 0, 0.01))
obj = bpy.context.active_object
obj.name = "leg_l3_upper"


# Rotate: leg_l3_upper (degrees)
import math
bpy.data.objects["leg_l3_upper"].rotation_euler = (
    math.radians(0),
    math.radians(60),
    math.radians(0)
)


# Create cylinder: leg_l3_lower
bpy.ops.mesh.primitive_cylinder_add(radius=0.0006, depth=0.01,
    vertices=8, location=(-0.0104, 3.3065463576978538e-19, 0.0127))
obj = bpy.context.active_object
obj.name = "leg_l3_lower"


# Rotate: leg_l3_lower (degrees)
import math
bpy.data.objects["leg_l3_lower"].rotation_euler = (
    math.radians(0),
    math.radians(120),
    math.radians(0)
)


# Create cylinder: leg_l4_upper
bpy.ops.mesh.primitive_cylinder_add(radius=0.0008, depth=0.012,
    vertices=8, location=(-0.004, -0.004, 0.01))
obj = bpy.context.active_object
obj.name = "leg_l4_upper"


# Rotate: leg_l4_upper (degrees)
import math
bpy.data.objects["leg_l4_upper"].rotation_euler = (
    math.radians(0),
    math.radians(50),
    math.radians(30)
)


# Create cylinder: leg_l4_lower
bpy.ops.mesh.primitive_cylinder_add(radius=0.0006, depth=0.01,
    vertices=8, location=(-0.00867653718043597, -0.006699999999999999, 0.013471053092307311))
obj = bpy.context.active_object
obj.name = "leg_l4_lower"


# Rotate: leg_l4_lower (degrees)
import math
bpy.data.objects["leg_l4_lower"].rotation_euler = (
    math.radians(0),
    math.radians(120),
    math.radians(30)
)


# Create cone: spinnerets
bpy.ops.mesh.primitive_cone_add(radius1=0.002, radius2=0.0005,
    depth=0.003, vertices=8, location=(0, -0.012, 0.01))
obj = bpy.context.active_object
obj.name = "spinnerets"


# Rotate: spinnerets (degrees)
import math
bpy.data.objects["spinnerets"].rotation_euler = (
    math.radians(-90),
    math.radians(0),
    math.radians(0)
)


# Union objects into: spider
# Using boolean EXACT solver for watertight results
base_obj = bpy.data.objects["base"]
bpy.context.view_layer.objects.active = base_obj


# Boolean union: adding abdomen
tool_obj = bpy.data.objects["abdomen"]
mod = base_obj.modifiers.new(name="Boolean_0", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_0")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding cephalothorax
tool_obj = bpy.data.objects["cephalothorax"]
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


# Boolean union: adding fang_l
tool_obj = bpy.data.objects["fang_l"]
mod = base_obj.modifiers.new(name="Boolean_3", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_3")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding fang_r
tool_obj = bpy.data.objects["fang_r"]
mod = base_obj.modifiers.new(name="Boolean_4", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_4")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding spinnerets
tool_obj = bpy.data.objects["spinnerets"]
mod = base_obj.modifiers.new(name="Boolean_5", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_5")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_0
tool_obj = bpy.data.objects["eye_0"]
mod = base_obj.modifiers.new(name="Boolean_6", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_6")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_1
tool_obj = bpy.data.objects["eye_1"]
mod = base_obj.modifiers.new(name="Boolean_7", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_7")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_2
tool_obj = bpy.data.objects["eye_2"]
mod = base_obj.modifiers.new(name="Boolean_8", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_8")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_3
tool_obj = bpy.data.objects["eye_3"]
mod = base_obj.modifiers.new(name="Boolean_9", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_9")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_4
tool_obj = bpy.data.objects["eye_4"]
mod = base_obj.modifiers.new(name="Boolean_10", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_10")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_5
tool_obj = bpy.data.objects["eye_5"]
mod = base_obj.modifiers.new(name="Boolean_11", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_11")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_6
tool_obj = bpy.data.objects["eye_6"]
mod = base_obj.modifiers.new(name="Boolean_12", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_12")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_7
tool_obj = bpy.data.objects["eye_7"]
mod = base_obj.modifiers.new(name="Boolean_13", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_13")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_r1_upper
tool_obj = bpy.data.objects["leg_r1_upper"]
mod = base_obj.modifiers.new(name="Boolean_14", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_14")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_r1_lower
tool_obj = bpy.data.objects["leg_r1_lower"]
mod = base_obj.modifiers.new(name="Boolean_15", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_15")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_r2_upper
tool_obj = bpy.data.objects["leg_r2_upper"]
mod = base_obj.modifiers.new(name="Boolean_16", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_16")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_r2_lower
tool_obj = bpy.data.objects["leg_r2_lower"]
mod = base_obj.modifiers.new(name="Boolean_17", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_17")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_r3_upper
tool_obj = bpy.data.objects["leg_r3_upper"]
mod = base_obj.modifiers.new(name="Boolean_18", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_18")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_r3_lower
tool_obj = bpy.data.objects["leg_r3_lower"]
mod = base_obj.modifiers.new(name="Boolean_19", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_19")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_r4_upper
tool_obj = bpy.data.objects["leg_r4_upper"]
mod = base_obj.modifiers.new(name="Boolean_20", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_20")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_r4_lower
tool_obj = bpy.data.objects["leg_r4_lower"]
mod = base_obj.modifiers.new(name="Boolean_21", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_21")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_l1_upper
tool_obj = bpy.data.objects["leg_l1_upper"]
mod = base_obj.modifiers.new(name="Boolean_22", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_22")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_l1_lower
tool_obj = bpy.data.objects["leg_l1_lower"]
mod = base_obj.modifiers.new(name="Boolean_23", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_23")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_l2_upper
tool_obj = bpy.data.objects["leg_l2_upper"]
mod = base_obj.modifiers.new(name="Boolean_24", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_24")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_l2_lower
tool_obj = bpy.data.objects["leg_l2_lower"]
mod = base_obj.modifiers.new(name="Boolean_25", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_25")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_l3_upper
tool_obj = bpy.data.objects["leg_l3_upper"]
mod = base_obj.modifiers.new(name="Boolean_26", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_26")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_l3_lower
tool_obj = bpy.data.objects["leg_l3_lower"]
mod = base_obj.modifiers.new(name="Boolean_27", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_27")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_l4_upper
tool_obj = bpy.data.objects["leg_l4_upper"]
mod = base_obj.modifiers.new(name="Boolean_28", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_28")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_l4_lower
tool_obj = bpy.data.objects["leg_l4_lower"]
mod = base_obj.modifiers.new(name="Boolean_29", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_29")
bpy.data.objects.remove(tool_obj, do_unlink=True)


base_obj.name = "spider"


# Clean mesh for printing: spider
obj = bpy.data.objects["spider"]
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
print(f"Mesh cleaned: spider")


# Add subdivision surface: spider
obj = bpy.data.objects["spider"]
mod = obj.modifiers.new(name="Subdivision", type='SUBSURF')
mod.levels = 2
mod.render_levels = 2


# Apply all modifiers: spider
obj = bpy.data.objects["spider"]
bpy.context.view_layer.objects.active = obj
for mod in obj.modifiers[:]:
    bpy.ops.object.modifier_apply(modifier=mod.name)


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
    filepath="C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/spider.stl",
    export_selected_objects=True,
    global_scale=1.0,
    ascii_format=False  # Binary STL is smaller and faster
)
print("Exported: C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/spider.stl")
