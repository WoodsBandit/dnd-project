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
mod.width = 0.0005
mod.segments = 2


# Create sphere: leg_R_hip
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0008470000000000001, segments=16,
    ring_count=8, location=(0.0012599999999999998, 0, 0.013640000000000003))
obj = bpy.context.active_object
obj.name = "leg_R_hip"


# Create cone: leg_R_thigh
bpy.ops.mesh.primitive_cone_add(radius1=0.000693, radius2=0.0008470000000000001,
    depth=0.005824000000000001, vertices=24, location=(0.0012599999999999998, 0.0004659200000000001, 0.010728000000000001))
obj = bpy.context.active_object
obj.name = "leg_R_thigh"


# Rotate: leg_R_thigh (degrees)
import math
bpy.data.objects["leg_R_thigh"].rotation_euler = (
    math.radians(5),
    math.radians(8),
    math.radians(0)
)


# Create sphere: leg_R_knee
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0006160000000000001, segments=16,
    ring_count=8, location=(0.0012599999999999998, 0.0006988800000000001, 0.007990720000000003))
obj = bpy.context.active_object
obj.name = "leg_R_knee"


# Create cone: leg_R_shin
bpy.ops.mesh.primitive_cone_add(radius1=0.000462, radius2=0.0006468,
    depth=0.004816000000000001, vertices=24, location=(0.0012599999999999998, 0.0009396800000000002, 0.005582720000000003))
obj = bpy.context.active_object
obj.name = "leg_R_shin"


# Rotate: leg_R_shin (degrees)
import math
bpy.data.objects["leg_R_shin"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(0)
)


# Create cube: leg_R_foot
bpy.ops.mesh.primitive_cube_add(size=0.0022400000000000002, location=(0.0012599999999999998, 0.0016116800000000003, 0.0028387200000000025))
obj = bpy.context.active_object
obj.name = "leg_R_foot"


# Scale: leg_R_foot
bpy.data.objects["leg_R_foot"].scale = (0.5, 1.0, 0.3)


# Create sphere: leg_L_hip
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0008470000000000001, segments=16,
    ring_count=8, location=(-0.0012599999999999998, 0, 0.013640000000000003))
obj = bpy.context.active_object
obj.name = "leg_L_hip"


# Create cone: leg_L_thigh
bpy.ops.mesh.primitive_cone_add(radius1=0.000693, radius2=0.0008470000000000001,
    depth=0.005824000000000001, vertices=24, location=(-0.0012599999999999998, 0.0004659200000000001, 0.010728000000000001))
obj = bpy.context.active_object
obj.name = "leg_L_thigh"


# Rotate: leg_L_thigh (degrees)
import math
bpy.data.objects["leg_L_thigh"].rotation_euler = (
    math.radians(5),
    math.radians(-8),
    math.radians(0)
)


# Create sphere: leg_L_knee
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0006160000000000001, segments=16,
    ring_count=8, location=(-0.0012599999999999998, 0.0006988800000000001, 0.007990720000000003))
obj = bpy.context.active_object
obj.name = "leg_L_knee"


# Create cone: leg_L_shin
bpy.ops.mesh.primitive_cone_add(radius1=0.000462, radius2=0.0006468,
    depth=0.004816000000000001, vertices=24, location=(-0.0012599999999999998, 0.0009396800000000002, 0.005582720000000003))
obj = bpy.context.active_object
obj.name = "leg_L_shin"


# Rotate: leg_L_shin (degrees)
import math
bpy.data.objects["leg_L_shin"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(0)
)


# Create cube: leg_L_foot
bpy.ops.mesh.primitive_cube_add(size=0.0022400000000000002, location=(-0.0012599999999999998, 0.0016116800000000003, 0.0028387200000000025))
obj = bpy.context.active_object
obj.name = "leg_L_foot"


# Scale: leg_L_foot
bpy.data.objects["leg_L_foot"].scale = (0.5, 1.0, 0.3)


# Create cone: torso_body
bpy.ops.mesh.primitive_cone_add(radius1=0.00231, radius2=0.003920000000000001,
    depth=0.0084, vertices=32, location=(0, 0, 0.018120000000000004))
obj = bpy.context.active_object
obj.name = "torso_body"


# Scale: torso_body
bpy.data.objects["torso_body"].scale = (1.0, 0.55, 1.0)


# Create sphere: torso_shoulder_L
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0012544000000000003, segments=24,
    ring_count=10, location=(-0.0032928000000000007, 0, 0.021648000000000004))
obj = bpy.context.active_object
obj.name = "torso_shoulder_L"


# Create sphere: torso_shoulder_R
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0012544000000000003, segments=24,
    ring_count=10, location=(0.0032928000000000007, 0, 0.021648000000000004))
obj = bpy.context.active_object
obj.name = "torso_shoulder_R"


# Create sphere: head_skull
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0026880000000000003, segments=32,
    ring_count=12, location=(0, 0, 0.02414))
obj = bpy.context.active_object
obj.name = "head_skull"


# Scale: head_skull
bpy.data.objects["head_skull"].scale = (0.9, 0.95, 1.05)


# Create cube: head_jaw
bpy.ops.mesh.primitive_cube_add(size=0.0019600000000000004, location=(0, 0.00044800000000000005, 0.022908))
obj = bpy.context.active_object
obj.name = "head_jaw"


# Scale: head_jaw
bpy.data.objects["head_jaw"].scale = (0.85, 0.55, 0.45)


# Add bevel: head_jaw
obj = bpy.data.objects["head_jaw"]
mod = obj.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.00028000000000000003
mod.segments = 2


# Create cylinder: head_brow
bpy.ops.mesh.primitive_cylinder_add(radius=0.00033600000000000004, depth=0.002856,
    vertices=16, location=(0, 0.0010080000000000002, 0.024980000000000002))
obj = bpy.context.active_object
obj.name = "head_brow"


# Rotate: head_brow (degrees)
import math
bpy.data.objects["head_brow"].rotation_euler = (
    math.radians(0),
    math.radians(90),
    math.radians(0)
)


# Create cone: head_nose
bpy.ops.mesh.primitive_cone_add(radius1=0.00028000000000000003, radius2=0.00011200000000000001,
    depth=0.0006720000000000001, vertices=8, location=(0, 0.0017920000000000002, 0.023860000000000003))
obj = bpy.context.active_object
obj.name = "head_nose"


# Rotate: head_nose (degrees)
import math
bpy.data.objects["head_nose"].rotation_euler = (
    math.radians(-70),
    math.radians(0),
    math.radians(0)
)


# Create sphere: head_ear_L
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.00044800000000000005, segments=16,
    ring_count=8, location=(-0.0021420000000000002, 0, 0.02414))
obj = bpy.context.active_object
obj.name = "head_ear_L"


# Scale: head_ear_L
bpy.data.objects["head_ear_L"].scale = (0.3, 0.5, 0.8)


# Create sphere: head_ear_R
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.00044800000000000005, segments=16,
    ring_count=8, location=(0.0021420000000000002, 0, 0.02414))
obj = bpy.context.active_object
obj.name = "head_ear_R"


# Scale: head_ear_R
bpy.data.objects["head_ear_R"].scale = (0.3, 0.5, 0.8)


# Create cone: elf_ear_L
bpy.ops.mesh.primitive_cone_add(radius1=0.00033600000000000004, radius2=0,
    depth=0.0011200000000000001, vertices=8, location=(-0.0022400000000000002, 0, 0.024700000000000003))
obj = bpy.context.active_object
obj.name = "elf_ear_L"


# Rotate: elf_ear_L (degrees)
import math
bpy.data.objects["elf_ear_L"].rotation_euler = (
    math.radians(0),
    math.radians(-30),
    math.radians(0)
)


# Create cone: elf_ear_R
bpy.ops.mesh.primitive_cone_add(radius1=0.00033600000000000004, radius2=0,
    depth=0.0011200000000000001, vertices=8, location=(0.0022400000000000002, 0, 0.024700000000000003))
obj = bpy.context.active_object
obj.name = "elf_ear_R"


# Rotate: elf_ear_R (degrees)
import math
bpy.data.objects["elf_ear_R"].rotation_euler = (
    math.radians(0),
    math.radians(30),
    math.radians(0)
)


# Create sphere: arm_R_shoulder
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0006720000000000001, segments=16,
    ring_count=8, location=(0.0029792000000000004, 0, 0.021060000000000002))
obj = bpy.context.active_object
obj.name = "arm_R_shoulder"


# Create cone: arm_R_upper
bpy.ops.mesh.primitive_cone_add(radius1=0.00039200000000000004, radius2=0.0005040000000000001,
    depth=0.0051072, vertices=24, location=(0.0033152000000000004, 0.00051072, 0.01927248))
obj = bpy.context.active_object
obj.name = "arm_R_upper"


# Rotate: arm_R_upper (degrees)
import math
bpy.data.objects["arm_R_upper"].rotation_euler = (
    math.radians(-110),
    math.radians(0),
    math.radians(-15)
)


# Create sphere: arm_R_elbow
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.00044800000000000005, segments=16,
    ring_count=8, location=(0.0035392000000000006, 0.0007660799999999999, 0.01748496))
obj = bpy.context.active_object
obj.name = "arm_R_elbow"


# Create cone: arm_R_lower
bpy.ops.mesh.primitive_cone_add(radius1=0.0003136000000000001, radius2=0.00039200000000000004,
    depth=0.004788000000000001, vertices=24, location=(0.0037632000000000004, 0.0014842800000000001, 0.01509096))
obj = bpy.context.active_object
obj.name = "arm_R_lower"


# Rotate: arm_R_lower (degrees)
import math
bpy.data.objects["arm_R_lower"].rotation_euler = (
    math.radians(-50),
    math.radians(0),
    math.radians(0)
)


# Create cube: arm_R_hand
bpy.ops.mesh.primitive_cube_add(size=0.0019600000000000004, location=(0.0038752000000000005, 0.00205884, 0.012936360000000001))
obj = bpy.context.active_object
obj.name = "arm_R_hand"


# Scale: arm_R_hand
bpy.data.objects["arm_R_hand"].scale = (0.55, 0.4, 0.9)


# Create cylinder: arm_R_finger_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.00015680000000000004, depth=0.0007840000000000002,
    vertices=6, location=(0.0034342000000000005, 0.00254884, 0.01225036))
obj = bpy.context.active_object
obj.name = "arm_R_finger_0"


# Rotate: arm_R_finger_0 (degrees)
import math
bpy.data.objects["arm_R_finger_0"].rotation_euler = (
    math.radians(25),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: arm_R_finger_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.00015680000000000004, depth=0.0007840000000000002,
    vertices=6, location=(0.0037282000000000005, 0.00254884, 0.01225036))
obj = bpy.context.active_object
obj.name = "arm_R_finger_1"


# Rotate: arm_R_finger_1 (degrees)
import math
bpy.data.objects["arm_R_finger_1"].rotation_euler = (
    math.radians(25),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: arm_R_finger_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.00015680000000000004, depth=0.0007840000000000002,
    vertices=6, location=(0.004022200000000001, 0.00254884, 0.01225036))
obj = bpy.context.active_object
obj.name = "arm_R_finger_2"


# Rotate: arm_R_finger_2 (degrees)
import math
bpy.data.objects["arm_R_finger_2"].rotation_euler = (
    math.radians(25),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: arm_R_finger_3
bpy.ops.mesh.primitive_cylinder_add(radius=0.00015680000000000004, depth=0.0007840000000000002,
    vertices=6, location=(0.004316200000000001, 0.00254884, 0.01225036))
obj = bpy.context.active_object
obj.name = "arm_R_finger_3"


# Rotate: arm_R_finger_3 (degrees)
import math
bpy.data.objects["arm_R_finger_3"].rotation_euler = (
    math.radians(25),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: arm_R_thumb
bpy.ops.mesh.primitive_cylinder_add(radius=0.00017640000000000003, depth=0.0005880000000000001,
    vertices=6, location=(0.0044632000000000005, 0.00225484, 0.012740360000000001))
obj = bpy.context.active_object
obj.name = "arm_R_thumb"


# Rotate: arm_R_thumb (degrees)
import math
bpy.data.objects["arm_R_thumb"].rotation_euler = (
    math.radians(30),
    math.radians(25),
    math.radians(0)
)


# Create sphere: arm_L_shoulder
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0006720000000000001, segments=16,
    ring_count=8, location=(-0.0029792000000000004, 0, 0.021060000000000002))
obj = bpy.context.active_object
obj.name = "arm_L_shoulder"


# Create cone: arm_L_upper
bpy.ops.mesh.primitive_cone_add(radius1=0.00039200000000000004, radius2=0.0005040000000000001,
    depth=0.0051072, vertices=24, location=(-0.0033152000000000004, 0.0012768, 0.01888944))
obj = bpy.context.active_object
obj.name = "arm_L_upper"


# Rotate: arm_L_upper (degrees)
import math
bpy.data.objects["arm_L_upper"].rotation_euler = (
    math.radians(-60),
    math.radians(0),
    math.radians(15)
)


# Create sphere: arm_L_elbow
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.00044800000000000005, segments=16,
    ring_count=8, location=(-0.0035392000000000006, 0.0019152000000000001, 0.016718880000000002))
obj = bpy.context.active_object
obj.name = "arm_L_elbow"


# Create cone: arm_L_lower
bpy.ops.mesh.primitive_cone_add(radius1=0.0003136000000000001, radius2=0.00039200000000000004,
    depth=0.004788000000000001, vertices=24, location=(-0.0037632000000000004, 0.0033516000000000006, 0.014324880000000002))
obj = bpy.context.active_object
obj.name = "arm_L_lower"


# Rotate: arm_L_lower (degrees)
import math
bpy.data.objects["arm_L_lower"].rotation_euler = (
    math.radians(-30),
    math.radians(0),
    math.radians(0)
)


# Create cube: arm_L_hand
bpy.ops.mesh.primitive_cube_add(size=0.0019600000000000004, location=(-0.0038752000000000005, 0.004500720000000001, 0.012170280000000002))
obj = bpy.context.active_object
obj.name = "arm_L_hand"


# Scale: arm_L_hand
bpy.data.objects["arm_L_hand"].scale = (0.55, 0.4, 0.9)


# Create cylinder: arm_L_finger_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.00015680000000000004, depth=0.0007840000000000002,
    vertices=6, location=(-0.0034342000000000005, 0.004990720000000001, 0.011484280000000001))
obj = bpy.context.active_object
obj.name = "arm_L_finger_0"


# Rotate: arm_L_finger_0 (degrees)
import math
bpy.data.objects["arm_L_finger_0"].rotation_euler = (
    math.radians(25),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: arm_L_finger_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.00015680000000000004, depth=0.0007840000000000002,
    vertices=6, location=(-0.0037282000000000005, 0.004990720000000001, 0.011484280000000001))
obj = bpy.context.active_object
obj.name = "arm_L_finger_1"


# Rotate: arm_L_finger_1 (degrees)
import math
bpy.data.objects["arm_L_finger_1"].rotation_euler = (
    math.radians(25),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: arm_L_finger_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.00015680000000000004, depth=0.0007840000000000002,
    vertices=6, location=(-0.004022200000000001, 0.004990720000000001, 0.011484280000000001))
obj = bpy.context.active_object
obj.name = "arm_L_finger_2"


# Rotate: arm_L_finger_2 (degrees)
import math
bpy.data.objects["arm_L_finger_2"].rotation_euler = (
    math.radians(25),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: arm_L_finger_3
bpy.ops.mesh.primitive_cylinder_add(radius=0.00015680000000000004, depth=0.0007840000000000002,
    vertices=6, location=(-0.004316200000000001, 0.004990720000000001, 0.011484280000000001))
obj = bpy.context.active_object
obj.name = "arm_L_finger_3"


# Rotate: arm_L_finger_3 (degrees)
import math
bpy.data.objects["arm_L_finger_3"].rotation_euler = (
    math.radians(25),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: arm_L_thumb
bpy.ops.mesh.primitive_cylinder_add(radius=0.00017640000000000003, depth=0.0005880000000000001,
    vertices=6, location=(-0.0044632000000000005, 0.004696720000000001, 0.011974280000000002))
obj = bpy.context.active_object
obj.name = "arm_L_thumb"


# Rotate: arm_L_thumb (degrees)
import math
bpy.data.objects["arm_L_thumb"].rotation_euler = (
    math.radians(30),
    math.radians(-25),
    math.radians(0)
)


# Create cylinder: mace_handle
bpy.ops.mesh.primitive_cylinder_add(radius=0.0004410000000000001, depth=0.007560000000000001,
    vertices=16, location=(0.003920000000000001, 0.015, 0.021060000000000002))
obj = bpy.context.active_object
obj.name = "mace_handle"


# Create sphere: mace_head
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0014700000000000004, segments=24,
    ring_count=10, location=(0.003920000000000001, 0.015, 0.026016))
obj = bpy.context.active_object
obj.name = "mace_head"


# Create cube: mace_flange_0
bpy.ops.mesh.primitive_cube_add(size=0.0011760000000000004, location=(0.003920000000000001, 0.015, 0.026016))
obj = bpy.context.active_object
obj.name = "mace_flange_0"


# Scale: mace_flange_0
bpy.data.objects["mace_flange_0"].scale = (0.2, 0.2, 0.8)


# Rotate: mace_flange_0 (degrees)
import math
bpy.data.objects["mace_flange_0"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(0)
)


# Create cube: mace_flange_1
bpy.ops.mesh.primitive_cube_add(size=0.0011760000000000004, location=(0.003920000000000001, 0.015, 0.026016))
obj = bpy.context.active_object
obj.name = "mace_flange_1"


# Scale: mace_flange_1
bpy.data.objects["mace_flange_1"].scale = (0.2, 0.2, 0.8)


# Rotate: mace_flange_1 (degrees)
import math
bpy.data.objects["mace_flange_1"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(60)
)


# Create cube: mace_flange_2
bpy.ops.mesh.primitive_cube_add(size=0.0011760000000000004, location=(0.003920000000000001, 0.015, 0.026016))
obj = bpy.context.active_object
obj.name = "mace_flange_2"


# Scale: mace_flange_2
bpy.data.objects["mace_flange_2"].scale = (0.2, 0.2, 0.8)


# Rotate: mace_flange_2 (degrees)
import math
bpy.data.objects["mace_flange_2"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(120)
)


# Create cube: mace_flange_3
bpy.ops.mesh.primitive_cube_add(size=0.0011760000000000004, location=(0.003920000000000001, 0.015, 0.026016))
obj = bpy.context.active_object
obj.name = "mace_flange_3"


# Scale: mace_flange_3
bpy.data.objects["mace_flange_3"].scale = (0.2, 0.2, 0.8)


# Rotate: mace_flange_3 (degrees)
import math
bpy.data.objects["mace_flange_3"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(180)
)


# Create cube: mace_flange_4
bpy.ops.mesh.primitive_cube_add(size=0.0011760000000000004, location=(0.003920000000000001, 0.015, 0.026016))
obj = bpy.context.active_object
obj.name = "mace_flange_4"


# Scale: mace_flange_4
bpy.data.objects["mace_flange_4"].scale = (0.2, 0.2, 0.8)


# Rotate: mace_flange_4 (degrees)
import math
bpy.data.objects["mace_flange_4"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(240)
)


# Create cube: mace_flange_5
bpy.ops.mesh.primitive_cube_add(size=0.0011760000000000004, location=(0.003920000000000001, 0.015, 0.026016))
obj = bpy.context.active_object
obj.name = "mace_flange_5"


# Scale: mace_flange_5
bpy.data.objects["mace_flange_5"].scale = (0.2, 0.2, 0.8)


# Rotate: mace_flange_5 (degrees)
import math
bpy.data.objects["mace_flange_5"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(300)
)


# Create cylinder: symbol_shaft
bpy.ops.mesh.primitive_cylinder_add(radius=0.00014000000000000001, depth=0.0022400000000000002,
    vertices=8, location=(-0.0031360000000000008, 0.02, 0.020220000000000002))
obj = bpy.context.active_object
obj.name = "symbol_shaft"


# Create cube: symbol_cross_v
bpy.ops.mesh.primitive_cube_add(size=0.00042, location=(-0.0031360000000000008, 0.02, 0.02162))
obj = bpy.context.active_object
obj.name = "symbol_cross_v"


# Scale: symbol_cross_v
bpy.data.objects["symbol_cross_v"].scale = (0.3, 0.3, 2.0)


# Create cube: symbol_cross_h
bpy.ops.mesh.primitive_cube_add(size=0.00042, location=(-0.0031360000000000008, 0.02, 0.02176))
obj = bpy.context.active_object
obj.name = "symbol_cross_h"


# Scale: symbol_cross_h
bpy.data.objects["symbol_cross_h"].scale = (1.5, 0.3, 0.3)


# Create cone: robe_skirt
bpy.ops.mesh.primitive_cone_add(radius1=0.00357, radius2=0.00168,
    depth=0.00336, vertices=32, location=(0, 0, 0.012520000000000003))
obj = bpy.context.active_object
obj.name = "robe_skirt"


# Union objects into: cleric
# Using boolean EXACT solver for watertight results
base_obj = bpy.data.objects["base"]
bpy.context.view_layer.objects.active = base_obj


# Boolean union: adding elf_ear_L
tool_obj = bpy.data.objects["elf_ear_L"]
mod = base_obj.modifiers.new(name="Boolean_0", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_0")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding elf_ear_R
tool_obj = bpy.data.objects["elf_ear_R"]
mod = base_obj.modifiers.new(name="Boolean_1", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_1")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding robe_skirt
tool_obj = bpy.data.objects["robe_skirt"]
mod = base_obj.modifiers.new(name="Boolean_2", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_2")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding symbol_shaft
tool_obj = bpy.data.objects["symbol_shaft"]
mod = base_obj.modifiers.new(name="Boolean_3", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_3")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding symbol_cross_v
tool_obj = bpy.data.objects["symbol_cross_v"]
mod = base_obj.modifiers.new(name="Boolean_4", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_4")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding symbol_cross_h
tool_obj = bpy.data.objects["symbol_cross_h"]
mod = base_obj.modifiers.new(name="Boolean_5", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_5")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_R_hip
tool_obj = bpy.data.objects["leg_R_hip"]
mod = base_obj.modifiers.new(name="Boolean_6", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_6")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_R_thigh
tool_obj = bpy.data.objects["leg_R_thigh"]
mod = base_obj.modifiers.new(name="Boolean_7", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_7")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_R_knee
tool_obj = bpy.data.objects["leg_R_knee"]
mod = base_obj.modifiers.new(name="Boolean_8", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_8")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_R_shin
tool_obj = bpy.data.objects["leg_R_shin"]
mod = base_obj.modifiers.new(name="Boolean_9", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_9")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_R_foot
tool_obj = bpy.data.objects["leg_R_foot"]
mod = base_obj.modifiers.new(name="Boolean_10", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_10")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_L_hip
tool_obj = bpy.data.objects["leg_L_hip"]
mod = base_obj.modifiers.new(name="Boolean_11", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_11")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_L_thigh
tool_obj = bpy.data.objects["leg_L_thigh"]
mod = base_obj.modifiers.new(name="Boolean_12", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_12")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_L_knee
tool_obj = bpy.data.objects["leg_L_knee"]
mod = base_obj.modifiers.new(name="Boolean_13", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_13")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_L_shin
tool_obj = bpy.data.objects["leg_L_shin"]
mod = base_obj.modifiers.new(name="Boolean_14", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_14")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_L_foot
tool_obj = bpy.data.objects["leg_L_foot"]
mod = base_obj.modifiers.new(name="Boolean_15", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_15")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding torso_body
tool_obj = bpy.data.objects["torso_body"]
mod = base_obj.modifiers.new(name="Boolean_16", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_16")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding torso_shoulder_L
tool_obj = bpy.data.objects["torso_shoulder_L"]
mod = base_obj.modifiers.new(name="Boolean_17", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_17")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding torso_shoulder_R
tool_obj = bpy.data.objects["torso_shoulder_R"]
mod = base_obj.modifiers.new(name="Boolean_18", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_18")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_skull
tool_obj = bpy.data.objects["head_skull"]
mod = base_obj.modifiers.new(name="Boolean_19", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_19")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_jaw
tool_obj = bpy.data.objects["head_jaw"]
mod = base_obj.modifiers.new(name="Boolean_20", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_20")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_brow
tool_obj = bpy.data.objects["head_brow"]
mod = base_obj.modifiers.new(name="Boolean_21", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_21")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_nose
tool_obj = bpy.data.objects["head_nose"]
mod = base_obj.modifiers.new(name="Boolean_22", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_22")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_ear_L
tool_obj = bpy.data.objects["head_ear_L"]
mod = base_obj.modifiers.new(name="Boolean_23", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_23")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_ear_R
tool_obj = bpy.data.objects["head_ear_R"]
mod = base_obj.modifiers.new(name="Boolean_24", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_24")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_shoulder
tool_obj = bpy.data.objects["arm_R_shoulder"]
mod = base_obj.modifiers.new(name="Boolean_25", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_25")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_upper
tool_obj = bpy.data.objects["arm_R_upper"]
mod = base_obj.modifiers.new(name="Boolean_26", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_26")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_elbow
tool_obj = bpy.data.objects["arm_R_elbow"]
mod = base_obj.modifiers.new(name="Boolean_27", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_27")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_lower
tool_obj = bpy.data.objects["arm_R_lower"]
mod = base_obj.modifiers.new(name="Boolean_28", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_28")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_hand
tool_obj = bpy.data.objects["arm_R_hand"]
mod = base_obj.modifiers.new(name="Boolean_29", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_29")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_thumb
tool_obj = bpy.data.objects["arm_R_thumb"]
mod = base_obj.modifiers.new(name="Boolean_30", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_30")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_finger_0
tool_obj = bpy.data.objects["arm_R_finger_0"]
mod = base_obj.modifiers.new(name="Boolean_31", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_31")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_finger_1
tool_obj = bpy.data.objects["arm_R_finger_1"]
mod = base_obj.modifiers.new(name="Boolean_32", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_32")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_finger_2
tool_obj = bpy.data.objects["arm_R_finger_2"]
mod = base_obj.modifiers.new(name="Boolean_33", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_33")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_finger_3
tool_obj = bpy.data.objects["arm_R_finger_3"]
mod = base_obj.modifiers.new(name="Boolean_34", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_34")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_shoulder
tool_obj = bpy.data.objects["arm_L_shoulder"]
mod = base_obj.modifiers.new(name="Boolean_35", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_35")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_upper
tool_obj = bpy.data.objects["arm_L_upper"]
mod = base_obj.modifiers.new(name="Boolean_36", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_36")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_elbow
tool_obj = bpy.data.objects["arm_L_elbow"]
mod = base_obj.modifiers.new(name="Boolean_37", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_37")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_lower
tool_obj = bpy.data.objects["arm_L_lower"]
mod = base_obj.modifiers.new(name="Boolean_38", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_38")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_hand
tool_obj = bpy.data.objects["arm_L_hand"]
mod = base_obj.modifiers.new(name="Boolean_39", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_39")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_thumb
tool_obj = bpy.data.objects["arm_L_thumb"]
mod = base_obj.modifiers.new(name="Boolean_40", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_40")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_finger_0
tool_obj = bpy.data.objects["arm_L_finger_0"]
mod = base_obj.modifiers.new(name="Boolean_41", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_41")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_finger_1
tool_obj = bpy.data.objects["arm_L_finger_1"]
mod = base_obj.modifiers.new(name="Boolean_42", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_42")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_finger_2
tool_obj = bpy.data.objects["arm_L_finger_2"]
mod = base_obj.modifiers.new(name="Boolean_43", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_43")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_finger_3
tool_obj = bpy.data.objects["arm_L_finger_3"]
mod = base_obj.modifiers.new(name="Boolean_44", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_44")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding mace_handle
tool_obj = bpy.data.objects["mace_handle"]
mod = base_obj.modifiers.new(name="Boolean_45", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_45")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding mace_head
tool_obj = bpy.data.objects["mace_head"]
mod = base_obj.modifiers.new(name="Boolean_46", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_46")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding mace_flange_0
tool_obj = bpy.data.objects["mace_flange_0"]
mod = base_obj.modifiers.new(name="Boolean_47", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_47")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding mace_flange_1
tool_obj = bpy.data.objects["mace_flange_1"]
mod = base_obj.modifiers.new(name="Boolean_48", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_48")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding mace_flange_2
tool_obj = bpy.data.objects["mace_flange_2"]
mod = base_obj.modifiers.new(name="Boolean_49", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_49")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding mace_flange_3
tool_obj = bpy.data.objects["mace_flange_3"]
mod = base_obj.modifiers.new(name="Boolean_50", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_50")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding mace_flange_4
tool_obj = bpy.data.objects["mace_flange_4"]
mod = base_obj.modifiers.new(name="Boolean_51", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_51")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding mace_flange_5
tool_obj = bpy.data.objects["mace_flange_5"]
mod = base_obj.modifiers.new(name="Boolean_52", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_52")
bpy.data.objects.remove(tool_obj, do_unlink=True)


base_obj.name = "cleric"


# Clean mesh for printing: cleric
obj = bpy.data.objects["cleric"]
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
print(f"Mesh cleaned: cleric")


# Add subdivision surface: cleric
obj = bpy.data.objects["cleric"]
mod = obj.modifiers.new(name="Subdivision", type='SUBSURF')
mod.levels = 2
mod.render_levels = 2


# Apply all modifiers: cleric
obj = bpy.data.objects["cleric"]
bpy.context.view_layer.objects.active = obj
for mod in obj.modifiers[:]:
    bpy.ops.object.modifier_apply(modifier=mod.name)


# Export to STL (Blender 4.0+ API)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.wm.stl_export(
    filepath="C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/characters/cleric-quality.stl",
    export_selected_objects=True,
    global_scale=1.0,
    ascii_format=False  # Binary STL is smaller and faster
)
print("Exported: C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/characters/cleric-quality.stl")
