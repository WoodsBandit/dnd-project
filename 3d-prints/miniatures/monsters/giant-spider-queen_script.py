import bpy
import bmesh
import math
from mathutils import Vector, Matrix

# Clear default scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)


# Create sphere: abdomen
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.12, segments=32,
    ring_count=16, location=(0, -0.1, 0.14))
obj = bpy.context.active_object
obj.name = "abdomen"


# Scale: abdomen
bpy.data.objects["abdomen"].scale = (1.0, 1.4, 0.9)


# Create sphere: egg_sac
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.08, segments=32,
    ring_count=16, location=(0, -0.15, 0.08))
obj = bpy.context.active_object
obj.name = "egg_sac"


# Scale: egg_sac
bpy.data.objects["egg_sac"].scale = (0.9, 1.1, 0.7)


# Create sphere: egg_0
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(0.05, -0.15, 0.06))
obj = bpy.context.active_object
obj.name = "egg_0"


# Create sphere: egg_1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(0.03535533905932738, -0.10757359312880714, 0.06))
obj = bpy.context.active_object
obj.name = "egg_1"


# Create sphere: egg_2
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(3.061616997868383e-18, -0.09, 0.06))
obj = bpy.context.active_object
obj.name = "egg_2"


# Create sphere: egg_3
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(-0.035355339059327376, -0.10757359312880714, 0.06))
obj = bpy.context.active_object
obj.name = "egg_3"


# Create sphere: egg_4
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(-0.05, -0.15, 0.06))
obj = bpy.context.active_object
obj.name = "egg_4"


# Create sphere: egg_5
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(-0.03535533905932738, -0.19242640687119283, 0.06))
obj = bpy.context.active_object
obj.name = "egg_5"


# Create sphere: egg_6
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(-9.184850993605149e-18, -0.21, 0.06))
obj = bpy.context.active_object
obj.name = "egg_6"


# Create sphere: egg_7
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(0.03535533905932737, -0.19242640687119286, 0.06))
obj = bpy.context.active_object
obj.name = "egg_7"


# Create sphere: cephalothorax
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.08, segments=32,
    ring_count=16, location=(0, 0.08, 0.14))
obj = bpy.context.active_object
obj.name = "cephalothorax"


# Scale: cephalothorax
bpy.data.objects["cephalothorax"].scale = (1.0, 1.2, 0.85)


# Create sphere: head
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.045, segments=32,
    ring_count=16, location=(0, 0.18, 0.16))
obj = bpy.context.active_object
obj.name = "head"


# Scale: head
bpy.data.objects["head"].scale = (0.9, 1.0, 0.85)


# Create sphere: eye_0
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(0.015, 0.22, 0.19))
obj = bpy.context.active_object
obj.name = "eye_0"


# Create sphere: eye_1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(-0.015, 0.22, 0.19))
obj = bpy.context.active_object
obj.name = "eye_1"


# Create sphere: eye_2
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(0.025, 0.21, 0.18))
obj = bpy.context.active_object
obj.name = "eye_2"


# Create sphere: eye_3
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(-0.025, 0.21, 0.18))
obj = bpy.context.active_object
obj.name = "eye_3"


# Create sphere: eye_4
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(0.02, 0.19, 0.2))
obj = bpy.context.active_object
obj.name = "eye_4"


# Create sphere: eye_5
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(-0.02, 0.19, 0.2))
obj = bpy.context.active_object
obj.name = "eye_5"


# Create sphere: eye_6
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(0.03, 0.17, 0.17))
obj = bpy.context.active_object
obj.name = "eye_6"


# Create sphere: eye_7
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(-0.03, 0.17, 0.17))
obj = bpy.context.active_object
obj.name = "eye_7"


# Create cone: fang_r
bpy.ops.mesh.primitive_cone_add(radius1=0.012, radius2=0.003,
    depth=0.04, vertices=32, location=(0.015, 0.23, 0.12))
obj = bpy.context.active_object
obj.name = "fang_r"


# Rotate: fang_r (degrees)
import math
bpy.data.objects["fang_r"].rotation_euler = (
    math.radians(120),
    math.radians(10),
    math.radians(0)
)


# Create cone: fang_l
bpy.ops.mesh.primitive_cone_add(radius1=0.012, radius2=0.003,
    depth=0.04, vertices=32, location=(-0.015, 0.23, 0.12))
obj = bpy.context.active_object
obj.name = "fang_l"


# Rotate: fang_l (degrees)
import math
bpy.data.objects["fang_l"].rotation_euler = (
    math.radians(120),
    math.radians(-10),
    math.radians(0)
)


# Create cylinder: palp_r
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.04,
    vertices=32, location=(0.03, 0.2, 0.14))
obj = bpy.context.active_object
obj.name = "palp_r"


# Rotate: palp_r (degrees)
import math
bpy.data.objects["palp_r"].rotation_euler = (
    math.radians(60),
    math.radians(30),
    math.radians(0)
)


# Create cylinder: palp_l
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.04,
    vertices=32, location=(-0.03, 0.2, 0.14))
obj = bpy.context.active_object
obj.name = "palp_l"


# Rotate: palp_l (degrees)
import math
bpy.data.objects["palp_l"].rotation_euler = (
    math.radians(60),
    math.radians(-30),
    math.radians(0)
)


# Create sphere: leg_coxa_0
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(0.08, 0.12, 0.14))
obj = bpy.context.active_object
obj.name = "leg_coxa_0"


# Create cylinder: leg_femur_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.1,
    vertices=32, location=(0.12, 0.12, 0.18000000000000002))
obj = bpy.context.active_object
obj.name = "leg_femur_0"


# Rotate: leg_femur_0 (degrees)
import math
bpy.data.objects["leg_femur_0"].rotation_euler = (
    math.radians(30),
    math.radians(50),
    math.radians(30)
)


# Create cylinder: leg_tibia_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.09,
    vertices=32, location=(0.2, 0.16999999999999998, 0.26))
obj = bpy.context.active_object
obj.name = "leg_tibia_0"


# Rotate: leg_tibia_0 (degrees)
import math
bpy.data.objects["leg_tibia_0"].rotation_euler = (
    math.radians(-60),
    math.radians(30),
    math.radians(0)
)


# Create cone: leg_tarsus_0
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.03, vertices=32, location=(0.256, 0.2, 0.2))
obj = bpy.context.active_object
obj.name = "leg_tarsus_0"


# Rotate: leg_tarsus_0 (degrees)
import math
bpy.data.objects["leg_tarsus_0"].rotation_euler = (
    math.radians(45),
    math.radians(20),
    math.radians(0)
)


# Create sphere: leg_coxa_1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(-0.08, 0.12, 0.14))
obj = bpy.context.active_object
obj.name = "leg_coxa_1"


# Create cylinder: leg_femur_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.1,
    vertices=32, location=(-0.12, 0.12, 0.18000000000000002))
obj = bpy.context.active_object
obj.name = "leg_femur_1"


# Rotate: leg_femur_1 (degrees)
import math
bpy.data.objects["leg_femur_1"].rotation_euler = (
    math.radians(30),
    math.radians(-50),
    math.radians(-30)
)


# Create cylinder: leg_tibia_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.09,
    vertices=32, location=(-0.2, 0.16999999999999998, 0.26))
obj = bpy.context.active_object
obj.name = "leg_tibia_1"


# Rotate: leg_tibia_1 (degrees)
import math
bpy.data.objects["leg_tibia_1"].rotation_euler = (
    math.radians(-60),
    math.radians(-30),
    math.radians(0)
)


# Create cone: leg_tarsus_1
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.03, vertices=32, location=(-0.256, 0.2, 0.2))
obj = bpy.context.active_object
obj.name = "leg_tarsus_1"


# Rotate: leg_tarsus_1 (degrees)
import math
bpy.data.objects["leg_tarsus_1"].rotation_euler = (
    math.radians(45),
    math.radians(-20),
    math.radians(0)
)


# Create sphere: leg_coxa_2
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(0.1, 0.06, 0.13))
obj = bpy.context.active_object
obj.name = "leg_coxa_2"


# Create cylinder: leg_femur_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.08,
    vertices=32, location=(0.15000000000000002, 0.06, 0.13))
obj = bpy.context.active_object
obj.name = "leg_femur_2"


# Rotate: leg_femur_2 (degrees)
import math
bpy.data.objects["leg_femur_2"].rotation_euler = (
    math.radians(10),
    math.radians(70),
    math.radians(20)
)


# Create cylinder: leg_tibia_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.09,
    vertices=32, location=(0.22000000000000003, 0.08, 0.15))
obj = bpy.context.active_object
obj.name = "leg_tibia_2"


# Rotate: leg_tibia_2 (degrees)
import math
bpy.data.objects["leg_tibia_2"].rotation_euler = (
    math.radians(-20),
    math.radians(50),
    math.radians(0)
)


# Create cone: leg_tarsus_2
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.03, vertices=32, location=(0.27999999999999997, 0.1, 0.02))
obj = bpy.context.active_object
obj.name = "leg_tarsus_2"


# Rotate: leg_tarsus_2 (degrees)
import math
bpy.data.objects["leg_tarsus_2"].rotation_euler = (
    math.radians(90),
    math.radians(20),
    math.radians(0)
)


# Create sphere: leg_coxa_3
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(-0.1, 0.06, 0.13))
obj = bpy.context.active_object
obj.name = "leg_coxa_3"


# Create cylinder: leg_femur_3
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.08,
    vertices=32, location=(-0.15000000000000002, 0.06, 0.13))
obj = bpy.context.active_object
obj.name = "leg_femur_3"


# Rotate: leg_femur_3 (degrees)
import math
bpy.data.objects["leg_femur_3"].rotation_euler = (
    math.radians(10),
    math.radians(-70),
    math.radians(-20)
)


# Create cylinder: leg_tibia_3
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.09,
    vertices=32, location=(-0.22000000000000003, 0.08, 0.15))
obj = bpy.context.active_object
obj.name = "leg_tibia_3"


# Rotate: leg_tibia_3 (degrees)
import math
bpy.data.objects["leg_tibia_3"].rotation_euler = (
    math.radians(-20),
    math.radians(-50),
    math.radians(0)
)


# Create cone: leg_tarsus_3
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.03, vertices=32, location=(-0.27999999999999997, 0.1, 0.02))
obj = bpy.context.active_object
obj.name = "leg_tarsus_3"


# Rotate: leg_tarsus_3 (degrees)
import math
bpy.data.objects["leg_tarsus_3"].rotation_euler = (
    math.radians(90),
    math.radians(-20),
    math.radians(0)
)


# Create sphere: leg_coxa_4
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(0.1, -0.02, 0.12))
obj = bpy.context.active_object
obj.name = "leg_coxa_4"


# Create cylinder: leg_femur_4
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.08,
    vertices=32, location=(0.15000000000000002, -0.02, 0.12))
obj = bpy.context.active_object
obj.name = "leg_femur_4"


# Rotate: leg_femur_4 (degrees)
import math
bpy.data.objects["leg_femur_4"].rotation_euler = (
    math.radians(-10),
    math.radians(80),
    math.radians(10)
)


# Create cylinder: leg_tibia_4
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.09,
    vertices=32, location=(0.22000000000000003, -0.04, 0.13999999999999999))
obj = bpy.context.active_object
obj.name = "leg_tibia_4"


# Rotate: leg_tibia_4 (degrees)
import math
bpy.data.objects["leg_tibia_4"].rotation_euler = (
    math.radians(10),
    math.radians(60),
    math.radians(0)
)


# Create cone: leg_tarsus_4
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.03, vertices=32, location=(0.27999999999999997, -0.06, 0.02))
obj = bpy.context.active_object
obj.name = "leg_tarsus_4"


# Rotate: leg_tarsus_4 (degrees)
import math
bpy.data.objects["leg_tarsus_4"].rotation_euler = (
    math.radians(90),
    math.radians(20),
    math.radians(0)
)


# Create sphere: leg_coxa_5
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(-0.1, -0.02, 0.12))
obj = bpy.context.active_object
obj.name = "leg_coxa_5"


# Create cylinder: leg_femur_5
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.08,
    vertices=32, location=(-0.15000000000000002, -0.02, 0.12))
obj = bpy.context.active_object
obj.name = "leg_femur_5"


# Rotate: leg_femur_5 (degrees)
import math
bpy.data.objects["leg_femur_5"].rotation_euler = (
    math.radians(-10),
    math.radians(-80),
    math.radians(-10)
)


# Create cylinder: leg_tibia_5
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.09,
    vertices=32, location=(-0.22000000000000003, -0.04, 0.13999999999999999))
obj = bpy.context.active_object
obj.name = "leg_tibia_5"


# Rotate: leg_tibia_5 (degrees)
import math
bpy.data.objects["leg_tibia_5"].rotation_euler = (
    math.radians(10),
    math.radians(-60),
    math.radians(0)
)


# Create cone: leg_tarsus_5
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.03, vertices=32, location=(-0.27999999999999997, -0.06, 0.02))
obj = bpy.context.active_object
obj.name = "leg_tarsus_5"


# Rotate: leg_tarsus_5 (degrees)
import math
bpy.data.objects["leg_tarsus_5"].rotation_euler = (
    math.radians(90),
    math.radians(-20),
    math.radians(0)
)


# Create sphere: leg_coxa_6
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(0.08, -0.08, 0.12))
obj = bpy.context.active_object
obj.name = "leg_coxa_6"


# Create cylinder: leg_femur_6
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.08,
    vertices=32, location=(0.12, -0.08, 0.12))
obj = bpy.context.active_object
obj.name = "leg_femur_6"


# Rotate: leg_femur_6 (degrees)
import math
bpy.data.objects["leg_femur_6"].rotation_euler = (
    math.radians(-30),
    math.radians(70),
    math.radians(0)
)


# Create cylinder: leg_tibia_6
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.09,
    vertices=32, location=(0.17600000000000002, -0.1, 0.13999999999999999))
obj = bpy.context.active_object
obj.name = "leg_tibia_6"


# Rotate: leg_tibia_6 (degrees)
import math
bpy.data.objects["leg_tibia_6"].rotation_euler = (
    math.radians(20),
    math.radians(50),
    math.radians(0)
)


# Create cone: leg_tarsus_6
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.03, vertices=32, location=(0.22399999999999998, -0.12, 0.02))
obj = bpy.context.active_object
obj.name = "leg_tarsus_6"


# Rotate: leg_tarsus_6 (degrees)
import math
bpy.data.objects["leg_tarsus_6"].rotation_euler = (
    math.radians(90),
    math.radians(20),
    math.radians(0)
)


# Create sphere: leg_coxa_7
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(-0.08, -0.08, 0.12))
obj = bpy.context.active_object
obj.name = "leg_coxa_7"


# Create cylinder: leg_femur_7
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.08,
    vertices=32, location=(-0.12, -0.08, 0.12))
obj = bpy.context.active_object
obj.name = "leg_femur_7"


# Rotate: leg_femur_7 (degrees)
import math
bpy.data.objects["leg_femur_7"].rotation_euler = (
    math.radians(-30),
    math.radians(-70),
    math.radians(0)
)


# Create cylinder: leg_tibia_7
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.09,
    vertices=32, location=(-0.17600000000000002, -0.1, 0.13999999999999999))
obj = bpy.context.active_object
obj.name = "leg_tibia_7"


# Rotate: leg_tibia_7 (degrees)
import math
bpy.data.objects["leg_tibia_7"].rotation_euler = (
    math.radians(20),
    math.radians(-50),
    math.radians(0)
)


# Create cone: leg_tarsus_7
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.03, vertices=32, location=(-0.22399999999999998, -0.12, 0.02))
obj = bpy.context.active_object
obj.name = "leg_tarsus_7"


# Rotate: leg_tarsus_7 (degrees)
import math
bpy.data.objects["leg_tarsus_7"].rotation_euler = (
    math.radians(90),
    math.radians(-20),
    math.radians(0)
)


# Create cone: spinneret
bpy.ops.mesh.primitive_cone_add(radius1=0.02, radius2=0.008,
    depth=0.03, vertices=32, location=(0, -0.25, 0.1))
obj = bpy.context.active_object
obj.name = "spinneret"


# Rotate: spinneret (degrees)
import math
bpy.data.objects["spinneret"].rotation_euler = (
    math.radians(100),
    math.radians(0),
    math.radians(0)
)


# Union objects into: giant-spider-queen
# Using boolean EXACT solver for watertight results
base_obj = bpy.data.objects["abdomen"]
bpy.context.view_layer.objects.active = base_obj


# Boolean union: adding egg_sac
tool_obj = bpy.data.objects["egg_sac"]
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


# Boolean union: adding fang_r
tool_obj = bpy.data.objects["fang_r"]
mod = base_obj.modifiers.new(name="Boolean_3", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_3")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding fang_l
tool_obj = bpy.data.objects["fang_l"]
mod = base_obj.modifiers.new(name="Boolean_4", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_4")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding palp_r
tool_obj = bpy.data.objects["palp_r"]
mod = base_obj.modifiers.new(name="Boolean_5", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_5")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding palp_l
tool_obj = bpy.data.objects["palp_l"]
mod = base_obj.modifiers.new(name="Boolean_6", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_6")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding spinneret
tool_obj = bpy.data.objects["spinneret"]
mod = base_obj.modifiers.new(name="Boolean_7", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_7")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding egg_0
tool_obj = bpy.data.objects["egg_0"]
mod = base_obj.modifiers.new(name="Boolean_8", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_8")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding egg_1
tool_obj = bpy.data.objects["egg_1"]
mod = base_obj.modifiers.new(name="Boolean_9", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_9")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding egg_2
tool_obj = bpy.data.objects["egg_2"]
mod = base_obj.modifiers.new(name="Boolean_10", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_10")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding egg_3
tool_obj = bpy.data.objects["egg_3"]
mod = base_obj.modifiers.new(name="Boolean_11", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_11")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding egg_4
tool_obj = bpy.data.objects["egg_4"]
mod = base_obj.modifiers.new(name="Boolean_12", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_12")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding egg_5
tool_obj = bpy.data.objects["egg_5"]
mod = base_obj.modifiers.new(name="Boolean_13", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_13")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding egg_6
tool_obj = bpy.data.objects["egg_6"]
mod = base_obj.modifiers.new(name="Boolean_14", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_14")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding egg_7
tool_obj = bpy.data.objects["egg_7"]
mod = base_obj.modifiers.new(name="Boolean_15", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_15")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_0
tool_obj = bpy.data.objects["eye_0"]
mod = base_obj.modifiers.new(name="Boolean_16", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_16")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_1
tool_obj = bpy.data.objects["eye_1"]
mod = base_obj.modifiers.new(name="Boolean_17", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_17")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_2
tool_obj = bpy.data.objects["eye_2"]
mod = base_obj.modifiers.new(name="Boolean_18", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_18")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_3
tool_obj = bpy.data.objects["eye_3"]
mod = base_obj.modifiers.new(name="Boolean_19", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_19")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_4
tool_obj = bpy.data.objects["eye_4"]
mod = base_obj.modifiers.new(name="Boolean_20", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_20")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_5
tool_obj = bpy.data.objects["eye_5"]
mod = base_obj.modifiers.new(name="Boolean_21", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_21")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_6
tool_obj = bpy.data.objects["eye_6"]
mod = base_obj.modifiers.new(name="Boolean_22", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_22")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_7
tool_obj = bpy.data.objects["eye_7"]
mod = base_obj.modifiers.new(name="Boolean_23", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_23")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_coxa_0
tool_obj = bpy.data.objects["leg_coxa_0"]
mod = base_obj.modifiers.new(name="Boolean_24", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_24")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_femur_0
tool_obj = bpy.data.objects["leg_femur_0"]
mod = base_obj.modifiers.new(name="Boolean_25", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_25")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_tibia_0
tool_obj = bpy.data.objects["leg_tibia_0"]
mod = base_obj.modifiers.new(name="Boolean_26", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_26")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_tarsus_0
tool_obj = bpy.data.objects["leg_tarsus_0"]
mod = base_obj.modifiers.new(name="Boolean_27", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_27")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_coxa_1
tool_obj = bpy.data.objects["leg_coxa_1"]
mod = base_obj.modifiers.new(name="Boolean_28", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_28")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_femur_1
tool_obj = bpy.data.objects["leg_femur_1"]
mod = base_obj.modifiers.new(name="Boolean_29", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_29")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_tibia_1
tool_obj = bpy.data.objects["leg_tibia_1"]
mod = base_obj.modifiers.new(name="Boolean_30", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_30")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_tarsus_1
tool_obj = bpy.data.objects["leg_tarsus_1"]
mod = base_obj.modifiers.new(name="Boolean_31", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_31")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_coxa_2
tool_obj = bpy.data.objects["leg_coxa_2"]
mod = base_obj.modifiers.new(name="Boolean_32", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_32")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_femur_2
tool_obj = bpy.data.objects["leg_femur_2"]
mod = base_obj.modifiers.new(name="Boolean_33", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_33")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_tibia_2
tool_obj = bpy.data.objects["leg_tibia_2"]
mod = base_obj.modifiers.new(name="Boolean_34", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_34")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_tarsus_2
tool_obj = bpy.data.objects["leg_tarsus_2"]
mod = base_obj.modifiers.new(name="Boolean_35", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_35")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_coxa_3
tool_obj = bpy.data.objects["leg_coxa_3"]
mod = base_obj.modifiers.new(name="Boolean_36", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_36")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_femur_3
tool_obj = bpy.data.objects["leg_femur_3"]
mod = base_obj.modifiers.new(name="Boolean_37", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_37")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_tibia_3
tool_obj = bpy.data.objects["leg_tibia_3"]
mod = base_obj.modifiers.new(name="Boolean_38", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_38")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_tarsus_3
tool_obj = bpy.data.objects["leg_tarsus_3"]
mod = base_obj.modifiers.new(name="Boolean_39", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_39")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_coxa_4
tool_obj = bpy.data.objects["leg_coxa_4"]
mod = base_obj.modifiers.new(name="Boolean_40", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_40")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_femur_4
tool_obj = bpy.data.objects["leg_femur_4"]
mod = base_obj.modifiers.new(name="Boolean_41", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_41")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_tibia_4
tool_obj = bpy.data.objects["leg_tibia_4"]
mod = base_obj.modifiers.new(name="Boolean_42", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_42")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_tarsus_4
tool_obj = bpy.data.objects["leg_tarsus_4"]
mod = base_obj.modifiers.new(name="Boolean_43", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_43")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_coxa_5
tool_obj = bpy.data.objects["leg_coxa_5"]
mod = base_obj.modifiers.new(name="Boolean_44", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_44")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_femur_5
tool_obj = bpy.data.objects["leg_femur_5"]
mod = base_obj.modifiers.new(name="Boolean_45", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_45")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_tibia_5
tool_obj = bpy.data.objects["leg_tibia_5"]
mod = base_obj.modifiers.new(name="Boolean_46", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_46")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_tarsus_5
tool_obj = bpy.data.objects["leg_tarsus_5"]
mod = base_obj.modifiers.new(name="Boolean_47", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_47")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_coxa_6
tool_obj = bpy.data.objects["leg_coxa_6"]
mod = base_obj.modifiers.new(name="Boolean_48", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_48")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_femur_6
tool_obj = bpy.data.objects["leg_femur_6"]
mod = base_obj.modifiers.new(name="Boolean_49", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_49")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_tibia_6
tool_obj = bpy.data.objects["leg_tibia_6"]
mod = base_obj.modifiers.new(name="Boolean_50", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_50")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_tarsus_6
tool_obj = bpy.data.objects["leg_tarsus_6"]
mod = base_obj.modifiers.new(name="Boolean_51", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_51")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_coxa_7
tool_obj = bpy.data.objects["leg_coxa_7"]
mod = base_obj.modifiers.new(name="Boolean_52", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_52")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_femur_7
tool_obj = bpy.data.objects["leg_femur_7"]
mod = base_obj.modifiers.new(name="Boolean_53", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_53")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_tibia_7
tool_obj = bpy.data.objects["leg_tibia_7"]
mod = base_obj.modifiers.new(name="Boolean_54", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_54")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_tarsus_7
tool_obj = bpy.data.objects["leg_tarsus_7"]
mod = base_obj.modifiers.new(name="Boolean_55", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_55")
bpy.data.objects.remove(tool_obj, do_unlink=True)


base_obj.name = "giant-spider-queen"


# Add subdivision surface: giant-spider-queen
obj = bpy.data.objects["giant-spider-queen"]
mod = obj.modifiers.new(name="Subdivision", type='SUBSURF')
mod.levels = 1
mod.render_levels = 2


# Apply all modifiers: giant-spider-queen
obj = bpy.data.objects["giant-spider-queen"]
bpy.context.view_layer.objects.active = obj
for mod in obj.modifiers[:]:
    bpy.ops.object.modifier_apply(modifier=mod.name)


# Create cylinder: giant-spider-queen_base
bpy.ops.mesh.primitive_cylinder_add(radius=0.025, depth=0.003,
    vertices=64, location=(0, 0, 0.0015))
obj = bpy.context.active_object
obj.name = "giant-spider-queen_base"


# Add bevel: giant-spider-queen_base
obj = bpy.data.objects["giant-spider-queen_base"]
mod = obj.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.0005
mod.segments = 2


# Boolean union: giant-spider-queen + giant-spider-queen_base
target_obj = bpy.data.objects["giant-spider-queen"]
tool_obj = bpy.data.objects["giant-spider-queen_base"]
mod = target_obj.modifiers.new(name="Boolean", type='BOOLEAN')
mod.operation = 'UNION'
mod.object = tool_obj
bpy.context.view_layer.objects.active = target_obj
bpy.ops.object.modifier_apply(modifier='Boolean')
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Export to STL (Blender 4.0+ API)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.wm.stl_export(
    filepath="C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/giant-spider-queen.stl",
    export_selected_objects=True,
    global_scale=1.0,
    ascii_format=False  # Binary STL is smaller and faster
)
print("Exported: C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/giant-spider-queen.stl")
