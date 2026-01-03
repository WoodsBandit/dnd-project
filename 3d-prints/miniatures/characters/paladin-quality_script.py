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
    ring_count=8, location=(0.0014699999999999997, 0, 0.013640000000000003))
obj = bpy.context.active_object
obj.name = "leg_R_hip"


# Create cone: leg_R_thigh
bpy.ops.mesh.primitive_cone_add(radius1=0.000693, radius2=0.0008470000000000001,
    depth=0.005824000000000001, vertices=24, location=(0.0017009999999999998, 0.0004659200000000001, 0.010728000000000001))
obj = bpy.context.active_object
obj.name = "leg_R_thigh"


# Rotate: leg_R_thigh (degrees)
import math
bpy.data.objects["leg_R_thigh"].rotation_euler = (
    math.radians(15),
    math.radians(8),
    math.radians(0)
)


# Create sphere: leg_R_knee
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0006160000000000001, segments=16,
    ring_count=8, location=(0.0018164999999999998, 0.0006988800000000001, 0.007990720000000003))
obj = bpy.context.active_object
obj.name = "leg_R_knee"


# Create sphere: leg_R_kneecop
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.000693, segments=16,
    ring_count=8, location=(0.0018164999999999998, 0.0010068800000000001, 0.007990720000000003))
obj = bpy.context.active_object
obj.name = "leg_R_kneecop"


# Scale: leg_R_kneecop
bpy.data.objects["leg_R_kneecop"].scale = (0.9, 0.6, 0.7)


# Create cone: leg_R_shin
bpy.ops.mesh.primitive_cone_add(radius1=0.000462, radius2=0.0006468,
    depth=0.004816000000000001, vertices=24, location=(0.0018164999999999998, 0.0009396800000000002, 0.005582720000000003))
obj = bpy.context.active_object
obj.name = "leg_R_shin"


# Rotate: leg_R_shin (degrees)
import math
bpy.data.objects["leg_R_shin"].rotation_euler = (
    math.radians(-8),
    math.radians(0),
    math.radians(0)
)


# Create cube: leg_R_sabaton
bpy.ops.mesh.primitive_cube_add(size=0.0022400000000000002, location=(0.0018164999999999998, 0.0017236800000000004, 0.002950720000000002))
obj = bpy.context.active_object
obj.name = "leg_R_sabaton"


# Scale: leg_R_sabaton
bpy.data.objects["leg_R_sabaton"].scale = (0.55, 1.0, 0.35)


# Add bevel: leg_R_sabaton
obj = bpy.data.objects["leg_R_sabaton"]
mod = obj.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.0009599999999999999
mod.segments = 1


# Create sphere: leg_R_toe
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0005600000000000001, segments=16,
    ring_count=6, location=(0.0018164999999999998, 0.0025076800000000004, 0.0029059200000000024))
obj = bpy.context.active_object
obj.name = "leg_R_toe"


# Scale: leg_R_toe
bpy.data.objects["leg_R_toe"].scale = (0.9, 0.9, 0.5)


# Create sphere: leg_L_hip
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0008470000000000001, segments=16,
    ring_count=8, location=(-0.0014699999999999997, 0, 0.013640000000000003))
obj = bpy.context.active_object
obj.name = "leg_L_hip"


# Create cone: leg_L_thigh
bpy.ops.mesh.primitive_cone_add(radius1=0.000693, radius2=0.0008470000000000001,
    depth=0.005824000000000001, vertices=24, location=(-0.0017009999999999998, 0.0004659200000000001, 0.010728000000000001))
obj = bpy.context.active_object
obj.name = "leg_L_thigh"


# Rotate: leg_L_thigh (degrees)
import math
bpy.data.objects["leg_L_thigh"].rotation_euler = (
    math.radians(-10),
    math.radians(-8),
    math.radians(0)
)


# Create sphere: leg_L_knee
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0006160000000000001, segments=16,
    ring_count=8, location=(-0.0018164999999999998, 0.0006988800000000001, 0.007990720000000003))
obj = bpy.context.active_object
obj.name = "leg_L_knee"


# Create sphere: leg_L_kneecop
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.000693, segments=16,
    ring_count=8, location=(-0.0018164999999999998, 0.0010068800000000001, 0.007990720000000003))
obj = bpy.context.active_object
obj.name = "leg_L_kneecop"


# Scale: leg_L_kneecop
bpy.data.objects["leg_L_kneecop"].scale = (0.9, 0.6, 0.7)


# Create cone: leg_L_shin
bpy.ops.mesh.primitive_cone_add(radius1=0.000462, radius2=0.0006468,
    depth=0.004816000000000001, vertices=24, location=(-0.0018164999999999998, 0.0009396800000000002, 0.005582720000000003))
obj = bpy.context.active_object
obj.name = "leg_L_shin"


# Rotate: leg_L_shin (degrees)
import math
bpy.data.objects["leg_L_shin"].rotation_euler = (
    math.radians(-8),
    math.radians(0),
    math.radians(0)
)


# Create cube: leg_L_sabaton
bpy.ops.mesh.primitive_cube_add(size=0.0022400000000000002, location=(-0.0018164999999999998, 0.0017236800000000004, 0.002950720000000002))
obj = bpy.context.active_object
obj.name = "leg_L_sabaton"


# Scale: leg_L_sabaton
bpy.data.objects["leg_L_sabaton"].scale = (0.55, 1.0, 0.35)


# Add bevel: leg_L_sabaton
obj = bpy.data.objects["leg_L_sabaton"]
mod = obj.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.0009599999999999999
mod.segments = 1


# Create sphere: leg_L_toe
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0005600000000000001, segments=16,
    ring_count=6, location=(-0.0018164999999999998, 0.0025076800000000004, 0.0029059200000000024))
obj = bpy.context.active_object
obj.name = "leg_L_toe"


# Scale: leg_L_toe
bpy.data.objects["leg_L_toe"].scale = (0.9, 0.9, 0.5)


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


# Create cube: torso_breastplate
bpy.ops.mesh.primitive_cube_add(size=0.005488000000000001, location=(0, 0.0013720000000000002, 0.019380000000000005))
obj = bpy.context.active_object
obj.name = "torso_breastplate"


# Scale: torso_breastplate
bpy.data.objects["torso_breastplate"].scale = (1.0, 0.2, 0.75)


# Add bevel: torso_breastplate
obj = bpy.data.objects["torso_breastplate"]
mod = obj.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.0012
mod.segments = 2


# Create sphere: torso_pec_L
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0011760000000000002, segments=24,
    ring_count=8, location=(-0.0011760000000000002, 0.0015680000000000004, 0.019968000000000003))
obj = bpy.context.active_object
obj.name = "torso_pec_L"


# Scale: torso_pec_L
bpy.data.objects["torso_pec_L"].scale = (1.1, 0.4, 0.7)


# Create sphere: torso_pec_R
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0011760000000000002, segments=24,
    ring_count=8, location=(0.0011760000000000002, 0.0015680000000000004, 0.019968000000000003))
obj = bpy.context.active_object
obj.name = "torso_pec_R"


# Scale: torso_pec_R
bpy.data.objects["torso_pec_R"].scale = (1.1, 0.4, 0.7)


# Create sphere: torso_pauldron_L
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0015680000000000004, segments=24,
    ring_count=8, location=(-0.0035280000000000008, 0, 0.021480000000000006))
obj = bpy.context.active_object
obj.name = "torso_pauldron_L"


# Scale: torso_pauldron_L
bpy.data.objects["torso_pauldron_L"].scale = (1.0, 0.7, 0.55)


# Create torus: torso_pauldron_rim_L
bpy.ops.mesh.primitive_torus_add(major_radius=0.0013328000000000003, minor_radius=0.0018,
    major_segments=24, minor_segments=8, location=(-0.0035280000000000008, 0, 0.020808000000000004))
obj = bpy.context.active_object
obj.name = "torso_pauldron_rim_L"


# Create sphere: torso_pauldron_R
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0015680000000000004, segments=24,
    ring_count=8, location=(0.0035280000000000008, 0, 0.021480000000000006))
obj = bpy.context.active_object
obj.name = "torso_pauldron_R"


# Scale: torso_pauldron_R
bpy.data.objects["torso_pauldron_R"].scale = (1.0, 0.7, 0.55)


# Create torus: torso_pauldron_rim_R
bpy.ops.mesh.primitive_torus_add(major_radius=0.0013328000000000003, minor_radius=0.0018,
    major_segments=24, minor_segments=8, location=(0.0035280000000000008, 0, 0.020808000000000004))
obj = bpy.context.active_object
obj.name = "torso_pauldron_rim_R"


# Create cylinder: torso_faulds
bpy.ops.mesh.primitive_cylinder_add(radius=0.0025199999999999997, depth=0.0018479999999999998,
    vertices=32, location=(0, 0, 0.014340000000000004))
obj = bpy.context.active_object
obj.name = "torso_faulds"


# Scale: torso_faulds
bpy.data.objects["torso_faulds"].scale = (1.0, 0.65, 1.0)


# Create torus: torso_belt
bpy.ops.mesh.primitive_torus_add(major_radius=0.00231, minor_radius=0.0024,
    major_segments=24, minor_segments=8, location=(0, 0, 0.015180000000000004))
obj = bpy.context.active_object
obj.name = "torso_belt"


# Create cube: torso_buckle
bpy.ops.mesh.primitive_cube_add(size=0.0006299999999999999, location=(0, 0.0014699999999999997, 0.015180000000000004))
obj = bpy.context.active_object
obj.name = "torso_buckle"


# Scale: torso_buckle
bpy.data.objects["torso_buckle"].scale = (1.0, 0.4, 0.8)


# Create cylinder: head_helm
bpy.ops.mesh.primitive_cylinder_add(radius=0.0030800000000000007, depth=0.005040000000000001,
    vertices=32, location=(0, 0, 0.02414))
obj = bpy.context.active_object
obj.name = "head_helm"


# Scale: head_helm
bpy.data.objects["head_helm"].scale = (0.9, 0.85, 1.0)


# Create cylinder: head_top
bpy.ops.mesh.primitive_cylinder_add(radius=0.0026880000000000003, depth=0.0006720000000000001,
    vertices=32, location=(0, 0, 0.026660000000000003))
obj = bpy.context.active_object
obj.name = "head_top"


# Create cube: head_visor
bpy.ops.mesh.primitive_cube_add(size=0.00044800000000000005, location=(0, 0.0019600000000000004, 0.024700000000000003))
obj = bpy.context.active_object
obj.name = "head_visor"


# Scale: head_visor
bpy.data.objects["head_visor"].scale = (5.5, 0.6, 0.5)


# Create cylinder: head_hole_0_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.00014000000000000001, depth=0.0005600000000000001,
    vertices=8, location=(-0.0008400000000000001, 0.0028000000000000004, 0.022852))
obj = bpy.context.active_object
obj.name = "head_hole_0_0"


# Rotate: head_hole_0_0 (degrees)
import math
bpy.data.objects["head_hole_0_0"].rotation_euler = (
    math.radians(90),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: head_hole_0_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.00014000000000000001, depth=0.0005600000000000001,
    vertices=8, location=(-0.0008400000000000001, 0.0028000000000000004, 0.0233))
obj = bpy.context.active_object
obj.name = "head_hole_0_1"


# Rotate: head_hole_0_1 (degrees)
import math
bpy.data.objects["head_hole_0_1"].rotation_euler = (
    math.radians(90),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: head_hole_0_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.00014000000000000001, depth=0.0005600000000000001,
    vertices=8, location=(-0.0008400000000000001, 0.0028000000000000004, 0.023748000000000002))
obj = bpy.context.active_object
obj.name = "head_hole_0_2"


# Rotate: head_hole_0_2 (degrees)
import math
bpy.data.objects["head_hole_0_2"].rotation_euler = (
    math.radians(90),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: head_hole_1_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.00014000000000000001, depth=0.0005600000000000001,
    vertices=8, location=(0.0, 0.0028000000000000004, 0.022852))
obj = bpy.context.active_object
obj.name = "head_hole_1_0"


# Rotate: head_hole_1_0 (degrees)
import math
bpy.data.objects["head_hole_1_0"].rotation_euler = (
    math.radians(90),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: head_hole_1_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.00014000000000000001, depth=0.0005600000000000001,
    vertices=8, location=(0.0, 0.0028000000000000004, 0.0233))
obj = bpy.context.active_object
obj.name = "head_hole_1_1"


# Rotate: head_hole_1_1 (degrees)
import math
bpy.data.objects["head_hole_1_1"].rotation_euler = (
    math.radians(90),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: head_hole_1_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.00014000000000000001, depth=0.0005600000000000001,
    vertices=8, location=(0.0, 0.0028000000000000004, 0.023748000000000002))
obj = bpy.context.active_object
obj.name = "head_hole_1_2"


# Rotate: head_hole_1_2 (degrees)
import math
bpy.data.objects["head_hole_1_2"].rotation_euler = (
    math.radians(90),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: head_hole_2_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.00014000000000000001, depth=0.0005600000000000001,
    vertices=8, location=(0.0008400000000000001, 0.0028000000000000004, 0.022852))
obj = bpy.context.active_object
obj.name = "head_hole_2_0"


# Rotate: head_hole_2_0 (degrees)
import math
bpy.data.objects["head_hole_2_0"].rotation_euler = (
    math.radians(90),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: head_hole_2_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.00014000000000000001, depth=0.0005600000000000001,
    vertices=8, location=(0.0008400000000000001, 0.0028000000000000004, 0.0233))
obj = bpy.context.active_object
obj.name = "head_hole_2_1"


# Rotate: head_hole_2_1 (degrees)
import math
bpy.data.objects["head_hole_2_1"].rotation_euler = (
    math.radians(90),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: head_hole_2_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.00014000000000000001, depth=0.0005600000000000001,
    vertices=8, location=(0.0008400000000000001, 0.0028000000000000004, 0.023748000000000002))
obj = bpy.context.active_object
obj.name = "head_hole_2_2"


# Rotate: head_hole_2_2 (degrees)
import math
bpy.data.objects["head_hole_2_2"].rotation_euler = (
    math.radians(90),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: head_crest_base
bpy.ops.mesh.primitive_cylinder_add(radius=0.00044800000000000005, depth=0.00028000000000000003,
    vertices=16, location=(0, -0.0005600000000000001, 0.026940000000000002))
obj = bpy.context.active_object
obj.name = "head_crest_base"


# Create sphere: arm_R_shoulder
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0006720000000000001, segments=16,
    ring_count=8, location=(0.0032928000000000007, 0, 0.021060000000000002))
obj = bpy.context.active_object
obj.name = "arm_R_shoulder"


# Create cone: arm_R_upper
bpy.ops.mesh.primitive_cone_add(radius1=0.00039200000000000004, radius2=0.0005040000000000001,
    depth=0.0051072, vertices=24, location=(0.0036288000000000006, 0.00051072, 0.01927248))
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
    ring_count=8, location=(0.003852800000000001, 0.0007660799999999999, 0.01748496))
obj = bpy.context.active_object
obj.name = "arm_R_elbow"


# Create sphere: arm_R_elbow_cop
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0005600000000000001, segments=16,
    ring_count=8, location=(0.003852800000000001, 0.0007660799999999999, 0.01748496))
obj = bpy.context.active_object
obj.name = "arm_R_elbow_cop"


# Scale: arm_R_elbow_cop
bpy.data.objects["arm_R_elbow_cop"].scale = (0.8, 0.6, 0.6)


# Create cone: arm_R_lower
bpy.ops.mesh.primitive_cone_add(radius1=0.0003136000000000001, radius2=0.00039200000000000004,
    depth=0.004788000000000001, vertices=24, location=(0.004076800000000001, 0.0014842800000000001, 0.01509096))
obj = bpy.context.active_object
obj.name = "arm_R_lower"


# Rotate: arm_R_lower (degrees)
import math
bpy.data.objects["arm_R_lower"].rotation_euler = (
    math.radians(-50),
    math.radians(0),
    math.radians(0)
)


# Create cube: arm_R_gauntlet
bpy.ops.mesh.primitive_cube_add(size=0.0015680000000000004, location=(0.004188800000000001, 0.00205884, 0.012936360000000001))
obj = bpy.context.active_object
obj.name = "arm_R_gauntlet"


# Scale: arm_R_gauntlet
bpy.data.objects["arm_R_gauntlet"].scale = (0.65, 0.45, 1.0)


# Add bevel: arm_R_gauntlet
obj = bpy.data.objects["arm_R_gauntlet"]
mod = obj.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.0009599999999999999
mod.segments = 1


# Create cylinder: arm_R_finger_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.00015680000000000004, depth=0.0007840000000000002,
    vertices=6, location=(0.0037478000000000012, 0.00254884, 0.01225036))
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
    vertices=6, location=(0.004041800000000001, 0.00254884, 0.01225036))
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
    vertices=6, location=(0.004335800000000002, 0.00254884, 0.01225036))
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
    vertices=6, location=(0.004629800000000002, 0.00254884, 0.01225036))
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
    vertices=6, location=(0.004776800000000001, 0.00225484, 0.012740360000000001))
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
    ring_count=8, location=(-0.0032928000000000007, 0, 0.021060000000000002))
obj = bpy.context.active_object
obj.name = "arm_L_shoulder"


# Create cone: arm_L_upper
bpy.ops.mesh.primitive_cone_add(radius1=0.00039200000000000004, radius2=0.0005040000000000001,
    depth=0.0051072, vertices=24, location=(-0.0036288000000000006, 0.00076608, 0.018761760000000002))
obj = bpy.context.active_object
obj.name = "arm_L_upper"


# Rotate: arm_L_upper (degrees)
import math
bpy.data.objects["arm_L_upper"].rotation_euler = (
    math.radians(-40),
    math.radians(0),
    math.radians(15)
)


# Create sphere: arm_L_elbow
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.00044800000000000005, segments=16,
    ring_count=8, location=(-0.003852800000000001, 0.00114912, 0.016463520000000002))
obj = bpy.context.active_object
obj.name = "arm_L_elbow"


# Create sphere: arm_L_elbow_cop
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0005600000000000001, segments=16,
    ring_count=8, location=(-0.003852800000000001, 0.00114912, 0.016463520000000002))
obj = bpy.context.active_object
obj.name = "arm_L_elbow_cop"


# Scale: arm_L_elbow_cop
bpy.data.objects["arm_L_elbow_cop"].scale = (0.8, 0.6, 0.6)


# Create cone: arm_L_lower
bpy.ops.mesh.primitive_cone_add(radius1=0.0003136000000000001, radius2=0.00039200000000000004,
    depth=0.004788000000000001, vertices=24, location=(-0.004076800000000001, 0.00234612, 0.014069520000000002))
obj = bpy.context.active_object
obj.name = "arm_L_lower"


# Rotate: arm_L_lower (degrees)
import math
bpy.data.objects["arm_L_lower"].rotation_euler = (
    math.radians(-80),
    math.radians(0),
    math.radians(0)
)


# Create cube: arm_L_gauntlet
bpy.ops.mesh.primitive_cube_add(size=0.0015680000000000004, location=(-0.004188800000000001, 0.0033037200000000004, 0.011914920000000002))
obj = bpy.context.active_object
obj.name = "arm_L_gauntlet"


# Scale: arm_L_gauntlet
bpy.data.objects["arm_L_gauntlet"].scale = (0.65, 0.45, 1.0)


# Add bevel: arm_L_gauntlet
obj = bpy.data.objects["arm_L_gauntlet"]
mod = obj.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.0009599999999999999
mod.segments = 1


# Create cylinder: arm_L_finger_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.00015680000000000004, depth=0.0007840000000000002,
    vertices=6, location=(-0.0037478000000000012, 0.0037937200000000004, 0.011228920000000002))
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
    vertices=6, location=(-0.004041800000000001, 0.0037937200000000004, 0.011228920000000002))
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
    vertices=6, location=(-0.004335800000000002, 0.0037937200000000004, 0.011228920000000002))
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
    vertices=6, location=(-0.004629800000000002, 0.0037937200000000004, 0.011228920000000002))
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
    vertices=6, location=(-0.004776800000000001, 0.0034997200000000004, 0.011718920000000002))
obj = bpy.context.active_object
obj.name = "arm_L_thumb"


# Rotate: arm_L_thumb (degrees)
import math
bpy.data.objects["arm_L_thumb"].rotation_euler = (
    math.radians(30),
    math.radians(-25),
    math.radians(0)
)


# Create cube: sword_blade
bpy.ops.mesh.primitive_cube_add(size=0.0105, location=(0.004312000000000002, 0.015, 0.031070000000000004))
obj = bpy.context.active_object
obj.name = "sword_blade"


# Scale: sword_blade
bpy.data.objects["sword_blade"].scale = (0.14, 0.048999999999999995, 1.0)


# Create cone: sword_tip
bpy.ops.mesh.primitive_cone_add(radius1=0.0007350000000000001, radius2=0,
    depth=0.00252, vertices=4, location=(0.004312000000000002, 0.015, 0.040100000000000004))
obj = bpy.context.active_object
obj.name = "sword_tip"


# Scale: sword_tip
bpy.data.objects["sword_tip"].scale = (1.0, 0.35, 1.0)


# Create cube: sword_guard
bpy.ops.mesh.primitive_cube_add(size=0.007350000000000001, location=(0.004312000000000002, 0.015, 0.021620000000000004))
obj = bpy.context.active_object
obj.name = "sword_guard"


# Scale: sword_guard
bpy.data.objects["sword_guard"].scale = (1.0, 0.35, 0.25)


# Add bevel: sword_guard
obj = bpy.data.objects["sword_guard"]
mod = obj.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.0006
mod.segments = 1


# Create cylinder: sword_handle
bpy.ops.mesh.primitive_cylinder_add(radius=0.0008820000000000001, depth=0.00462,
    vertices=8, location=(0.004312000000000002, 0.015, 0.019310000000000004))
obj = bpy.context.active_object
obj.name = "sword_handle"


# Create sphere: sword_pommel
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0016170000000000004, segments=16,
    ring_count=8, location=(0.004312000000000002, 0.015, 0.017000000000000005))
obj = bpy.context.active_object
obj.name = "sword_pommel"


# Scale: sword_pommel
bpy.data.objects["sword_pommel"].scale = (1.0, 0.55, 0.75)


# Rotate: sword_blade (degrees)
import math
bpy.data.objects["sword_blade"].rotation_euler = (
    math.radians(-25),
    math.radians(15),
    math.radians(0)
)


# Rotate: sword_tip (degrees)
import math
bpy.data.objects["sword_tip"].rotation_euler = (
    math.radians(-25),
    math.radians(15),
    math.radians(0)
)


# Rotate: sword_guard (degrees)
import math
bpy.data.objects["sword_guard"].rotation_euler = (
    math.radians(-25),
    math.radians(15),
    math.radians(0)
)


# Rotate: sword_handle (degrees)
import math
bpy.data.objects["sword_handle"].rotation_euler = (
    math.radians(-25),
    math.radians(15),
    math.radians(0)
)


# Rotate: sword_pommel (degrees)
import math
bpy.data.objects["sword_pommel"].rotation_euler = (
    math.radians(-25),
    math.radians(15),
    math.radians(0)
)


# Create cylinder: shield_body
bpy.ops.mesh.primitive_cylinder_add(radius=0.007056, depth=0.001029,
    vertices=32, location=(-0.003920000000000001, 0.012, 0.020780000000000003))
obj = bpy.context.active_object
obj.name = "shield_body"


# Rotate: shield_body (degrees)
import math
bpy.data.objects["shield_body"].rotation_euler = (
    math.radians(90),
    math.radians(0),
    math.radians(0)
)


# Scale: shield_body
bpy.data.objects["shield_body"].scale = (1.0, 1.0, 1.35)


# Create sphere: shield_boss
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.002058, segments=24,
    ring_count=8, location=(-0.003920000000000001, 0.012735, 0.020780000000000003))
obj = bpy.context.active_object
obj.name = "shield_boss"


# Scale: shield_boss
bpy.data.objects["shield_boss"].scale = (1.0, 0.45, 1.0)


# Create torus: shield_rim
bpy.ops.mesh.primitive_torus_add(major_radius=0.006762, minor_radius=0.0003675,
    major_segments=32, minor_segments=8, location=(-0.003920000000000001, 0.012, 0.020780000000000003))
obj = bpy.context.active_object
obj.name = "shield_rim"


# Rotate: shield_rim (degrees)
import math
bpy.data.objects["shield_rim"].rotation_euler = (
    math.radians(90),
    math.radians(0),
    math.radians(0)
)


# Scale: shield_rim
bpy.data.objects["shield_rim"].scale = (1.0, 1.0, 1.35)


# Create cube: shield_cross_v
bpy.ops.mesh.primitive_cube_add(size=0.00147, location=(-0.003920000000000001, 0.012588, 0.020780000000000003))
obj = bpy.context.active_object
obj.name = "shield_cross_v"


# Scale: shield_cross_v
bpy.data.objects["shield_cross_v"].scale = (0.3, 0.4, 3.5)


# Create cube: shield_cross_h
bpy.ops.mesh.primitive_cube_add(size=0.00147, location=(-0.003920000000000001, 0.012588, 0.022985000000000002))
obj = bpy.context.active_object
obj.name = "shield_cross_h"


# Scale: shield_cross_h
bpy.data.objects["shield_cross_h"].scale = (2.5, 0.4, 0.3)


# Union objects into: paladin
# Using boolean EXACT solver for watertight results
base_obj = bpy.data.objects["base"]
bpy.context.view_layer.objects.active = base_obj


# Boolean union: adding leg_R_hip
tool_obj = bpy.data.objects["leg_R_hip"]
mod = base_obj.modifiers.new(name="Boolean_0", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_0")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_R_thigh
tool_obj = bpy.data.objects["leg_R_thigh"]
mod = base_obj.modifiers.new(name="Boolean_1", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_1")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_R_knee
tool_obj = bpy.data.objects["leg_R_knee"]
mod = base_obj.modifiers.new(name="Boolean_2", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_2")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_R_kneecop
tool_obj = bpy.data.objects["leg_R_kneecop"]
mod = base_obj.modifiers.new(name="Boolean_3", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_3")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_R_shin
tool_obj = bpy.data.objects["leg_R_shin"]
mod = base_obj.modifiers.new(name="Boolean_4", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_4")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_R_sabaton
tool_obj = bpy.data.objects["leg_R_sabaton"]
mod = base_obj.modifiers.new(name="Boolean_5", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_5")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_R_toe
tool_obj = bpy.data.objects["leg_R_toe"]
mod = base_obj.modifiers.new(name="Boolean_6", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_6")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_L_hip
tool_obj = bpy.data.objects["leg_L_hip"]
mod = base_obj.modifiers.new(name="Boolean_7", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_7")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_L_thigh
tool_obj = bpy.data.objects["leg_L_thigh"]
mod = base_obj.modifiers.new(name="Boolean_8", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_8")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_L_knee
tool_obj = bpy.data.objects["leg_L_knee"]
mod = base_obj.modifiers.new(name="Boolean_9", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_9")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_L_kneecop
tool_obj = bpy.data.objects["leg_L_kneecop"]
mod = base_obj.modifiers.new(name="Boolean_10", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_10")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_L_shin
tool_obj = bpy.data.objects["leg_L_shin"]
mod = base_obj.modifiers.new(name="Boolean_11", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_11")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_L_sabaton
tool_obj = bpy.data.objects["leg_L_sabaton"]
mod = base_obj.modifiers.new(name="Boolean_12", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_12")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_L_toe
tool_obj = bpy.data.objects["leg_L_toe"]
mod = base_obj.modifiers.new(name="Boolean_13", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_13")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding torso_body
tool_obj = bpy.data.objects["torso_body"]
mod = base_obj.modifiers.new(name="Boolean_14", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_14")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding torso_shoulder_L
tool_obj = bpy.data.objects["torso_shoulder_L"]
mod = base_obj.modifiers.new(name="Boolean_15", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_15")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding torso_shoulder_R
tool_obj = bpy.data.objects["torso_shoulder_R"]
mod = base_obj.modifiers.new(name="Boolean_16", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_16")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding torso_breastplate
tool_obj = bpy.data.objects["torso_breastplate"]
mod = base_obj.modifiers.new(name="Boolean_17", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_17")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding torso_pec_L
tool_obj = bpy.data.objects["torso_pec_L"]
mod = base_obj.modifiers.new(name="Boolean_18", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_18")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding torso_pec_R
tool_obj = bpy.data.objects["torso_pec_R"]
mod = base_obj.modifiers.new(name="Boolean_19", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_19")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding torso_pauldron_L
tool_obj = bpy.data.objects["torso_pauldron_L"]
mod = base_obj.modifiers.new(name="Boolean_20", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_20")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding torso_pauldron_R
tool_obj = bpy.data.objects["torso_pauldron_R"]
mod = base_obj.modifiers.new(name="Boolean_21", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_21")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding torso_pauldron_rim_L
tool_obj = bpy.data.objects["torso_pauldron_rim_L"]
mod = base_obj.modifiers.new(name="Boolean_22", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_22")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding torso_pauldron_rim_R
tool_obj = bpy.data.objects["torso_pauldron_rim_R"]
mod = base_obj.modifiers.new(name="Boolean_23", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_23")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding torso_faulds
tool_obj = bpy.data.objects["torso_faulds"]
mod = base_obj.modifiers.new(name="Boolean_24", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_24")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding torso_belt
tool_obj = bpy.data.objects["torso_belt"]
mod = base_obj.modifiers.new(name="Boolean_25", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_25")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding torso_buckle
tool_obj = bpy.data.objects["torso_buckle"]
mod = base_obj.modifiers.new(name="Boolean_26", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_26")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_helm
tool_obj = bpy.data.objects["head_helm"]
mod = base_obj.modifiers.new(name="Boolean_27", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_27")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_top
tool_obj = bpy.data.objects["head_top"]
mod = base_obj.modifiers.new(name="Boolean_28", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_28")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_visor
tool_obj = bpy.data.objects["head_visor"]
mod = base_obj.modifiers.new(name="Boolean_29", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_29")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_crest_base
tool_obj = bpy.data.objects["head_crest_base"]
mod = base_obj.modifiers.new(name="Boolean_30", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_30")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_hole_0_0
tool_obj = bpy.data.objects["head_hole_0_0"]
mod = base_obj.modifiers.new(name="Boolean_31", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_31")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_hole_0_1
tool_obj = bpy.data.objects["head_hole_0_1"]
mod = base_obj.modifiers.new(name="Boolean_32", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_32")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_hole_0_2
tool_obj = bpy.data.objects["head_hole_0_2"]
mod = base_obj.modifiers.new(name="Boolean_33", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_33")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_hole_1_0
tool_obj = bpy.data.objects["head_hole_1_0"]
mod = base_obj.modifiers.new(name="Boolean_34", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_34")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_hole_1_1
tool_obj = bpy.data.objects["head_hole_1_1"]
mod = base_obj.modifiers.new(name="Boolean_35", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_35")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_hole_1_2
tool_obj = bpy.data.objects["head_hole_1_2"]
mod = base_obj.modifiers.new(name="Boolean_36", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_36")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_hole_2_0
tool_obj = bpy.data.objects["head_hole_2_0"]
mod = base_obj.modifiers.new(name="Boolean_37", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_37")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_hole_2_1
tool_obj = bpy.data.objects["head_hole_2_1"]
mod = base_obj.modifiers.new(name="Boolean_38", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_38")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_hole_2_2
tool_obj = bpy.data.objects["head_hole_2_2"]
mod = base_obj.modifiers.new(name="Boolean_39", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_39")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_shoulder
tool_obj = bpy.data.objects["arm_R_shoulder"]
mod = base_obj.modifiers.new(name="Boolean_40", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_40")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_upper
tool_obj = bpy.data.objects["arm_R_upper"]
mod = base_obj.modifiers.new(name="Boolean_41", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_41")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_elbow
tool_obj = bpy.data.objects["arm_R_elbow"]
mod = base_obj.modifiers.new(name="Boolean_42", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_42")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_elbow_cop
tool_obj = bpy.data.objects["arm_R_elbow_cop"]
mod = base_obj.modifiers.new(name="Boolean_43", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_43")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_lower
tool_obj = bpy.data.objects["arm_R_lower"]
mod = base_obj.modifiers.new(name="Boolean_44", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_44")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_gauntlet
tool_obj = bpy.data.objects["arm_R_gauntlet"]
mod = base_obj.modifiers.new(name="Boolean_45", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_45")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_thumb
tool_obj = bpy.data.objects["arm_R_thumb"]
mod = base_obj.modifiers.new(name="Boolean_46", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_46")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_finger_0
tool_obj = bpy.data.objects["arm_R_finger_0"]
mod = base_obj.modifiers.new(name="Boolean_47", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_47")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_finger_1
tool_obj = bpy.data.objects["arm_R_finger_1"]
mod = base_obj.modifiers.new(name="Boolean_48", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_48")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_finger_2
tool_obj = bpy.data.objects["arm_R_finger_2"]
mod = base_obj.modifiers.new(name="Boolean_49", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_49")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_R_finger_3
tool_obj = bpy.data.objects["arm_R_finger_3"]
mod = base_obj.modifiers.new(name="Boolean_50", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_50")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_shoulder
tool_obj = bpy.data.objects["arm_L_shoulder"]
mod = base_obj.modifiers.new(name="Boolean_51", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_51")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_upper
tool_obj = bpy.data.objects["arm_L_upper"]
mod = base_obj.modifiers.new(name="Boolean_52", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_52")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_elbow
tool_obj = bpy.data.objects["arm_L_elbow"]
mod = base_obj.modifiers.new(name="Boolean_53", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_53")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_elbow_cop
tool_obj = bpy.data.objects["arm_L_elbow_cop"]
mod = base_obj.modifiers.new(name="Boolean_54", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_54")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_lower
tool_obj = bpy.data.objects["arm_L_lower"]
mod = base_obj.modifiers.new(name="Boolean_55", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_55")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_gauntlet
tool_obj = bpy.data.objects["arm_L_gauntlet"]
mod = base_obj.modifiers.new(name="Boolean_56", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_56")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_thumb
tool_obj = bpy.data.objects["arm_L_thumb"]
mod = base_obj.modifiers.new(name="Boolean_57", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_57")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_finger_0
tool_obj = bpy.data.objects["arm_L_finger_0"]
mod = base_obj.modifiers.new(name="Boolean_58", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_58")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_finger_1
tool_obj = bpy.data.objects["arm_L_finger_1"]
mod = base_obj.modifiers.new(name="Boolean_59", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_59")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_finger_2
tool_obj = bpy.data.objects["arm_L_finger_2"]
mod = base_obj.modifiers.new(name="Boolean_60", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_60")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_L_finger_3
tool_obj = bpy.data.objects["arm_L_finger_3"]
mod = base_obj.modifiers.new(name="Boolean_61", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_61")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding sword_blade
tool_obj = bpy.data.objects["sword_blade"]
mod = base_obj.modifiers.new(name="Boolean_62", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_62")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding sword_tip
tool_obj = bpy.data.objects["sword_tip"]
mod = base_obj.modifiers.new(name="Boolean_63", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_63")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding sword_guard
tool_obj = bpy.data.objects["sword_guard"]
mod = base_obj.modifiers.new(name="Boolean_64", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_64")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding sword_handle
tool_obj = bpy.data.objects["sword_handle"]
mod = base_obj.modifiers.new(name="Boolean_65", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_65")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding sword_pommel
tool_obj = bpy.data.objects["sword_pommel"]
mod = base_obj.modifiers.new(name="Boolean_66", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_66")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding shield_body
tool_obj = bpy.data.objects["shield_body"]
mod = base_obj.modifiers.new(name="Boolean_67", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_67")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding shield_boss
tool_obj = bpy.data.objects["shield_boss"]
mod = base_obj.modifiers.new(name="Boolean_68", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_68")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding shield_rim
tool_obj = bpy.data.objects["shield_rim"]
mod = base_obj.modifiers.new(name="Boolean_69", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_69")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding shield_cross_v
tool_obj = bpy.data.objects["shield_cross_v"]
mod = base_obj.modifiers.new(name="Boolean_70", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_70")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding shield_cross_h
tool_obj = bpy.data.objects["shield_cross_h"]
mod = base_obj.modifiers.new(name="Boolean_71", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_71")
bpy.data.objects.remove(tool_obj, do_unlink=True)


base_obj.name = "paladin"


# Clean mesh for printing: paladin
obj = bpy.data.objects["paladin"]
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
print(f"Mesh cleaned: paladin")


# Add subdivision surface: paladin
obj = bpy.data.objects["paladin"]
mod = obj.modifiers.new(name="Subdivision", type='SUBSURF')
mod.levels = 2
mod.render_levels = 2


# Apply all modifiers: paladin
obj = bpy.data.objects["paladin"]
bpy.context.view_layer.objects.active = obj
for mod in obj.modifiers[:]:
    bpy.ops.object.modifier_apply(modifier=mod.name)


# Export to STL (Blender 4.0+ API)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.wm.stl_export(
    filepath="C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/characters/paladin-quality.stl",
    export_selected_objects=True,
    global_scale=1.0,
    ascii_format=False  # Binary STL is smaller and faster
)
print("Exported: C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/characters/paladin-quality.stl")
