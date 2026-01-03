import bpy
import bmesh
import math
from mathutils import Vector, Matrix

# Clear default scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)


# Create metaball sphere: body_meta
bpy.ops.object.metaball_add(type='BALL', radius=0.18, location=(0, 0, 0.22))
obj = bpy.context.active_object
obj.name = "body_meta"


# Add metaball element to: body_meta
mball = bpy.data.metaballs[bpy.data.objects["body_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.14
elem.co = (0, 0.08, 0.25)


# Add metaball element to: body_meta
mball = bpy.data.metaballs[bpy.data.objects["body_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.12
elem.co = (0, -0.1, 0.2)


# Add metaball element to: body_meta
mball = bpy.data.metaballs[bpy.data.objects["body_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.1
elem.co = (0, 0.12, 0.18)


# Convert metaball to mesh: body_meta
obj = bpy.data.objects["body_meta"]
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
bpy.ops.object.convert(target='MESH')

bpy.context.active_object.name = "body"

# Create cylinder: neck_low_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.028, depth=0.12,
    vertices=32, location=(0.18, 0.0, 0.32))
obj = bpy.context.active_object
obj.name = "neck_low_0"


# Rotate: neck_low_0 (degrees)
import math
bpy.data.objects["neck_low_0"].rotation_euler = (
    math.radians(0.0),
    math.radians(-25.0),
    math.radians(0.0)
)


# Create cylinder: neck_high_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.1,
    vertices=32, location=(0.33599999999999997, 0.0, 0.44))
obj = bpy.context.active_object
obj.name = "neck_high_0"


# Rotate: neck_high_0 (degrees)
import math
bpy.data.objects["neck_high_0"].rotation_euler = (
    math.radians(0.0),
    math.radians(-35.0),
    math.radians(0.0)
)


# Create sphere: head_0
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.04, segments=32,
    ring_count=16, location=(0.48, 0.0, 0.54))
obj = bpy.context.active_object
obj.name = "head_0"


# Scale: head_0
bpy.data.objects["head_0"].scale = (1.4, 0.7, 0.85)


# Rotate: head_0 (degrees)
import math
bpy.data.objects["head_0"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(0.0)
)


# Create sphere: jaw_0
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.025, segments=32,
    ring_count=16, location=(0.5184, 0.0, 0.525))
obj = bpy.context.active_object
obj.name = "jaw_0"


# Scale: jaw_0
bpy.data.objects["jaw_0"].scale = (1.2, 0.6, 0.5)


# Create sphere: eye_0_-1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(0.48, -0.015, 0.555))
obj = bpy.context.active_object
obj.name = "eye_0_-1"


# Create sphere: eye_0_1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(0.48, 0.015, 0.555))
obj = bpy.context.active_object
obj.name = "eye_0_1"


# Create cylinder: neck_low_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.028, depth=0.12,
    vertices=32, location=(0.12727922061357855, 0.12727922061357855, 0.34992484959812165))
obj = bpy.context.active_object
obj.name = "neck_low_1"


# Rotate: neck_low_1 (degrees)
import math
bpy.data.objects["neck_low_1"].rotation_euler = (
    math.radians(17.67766952966369),
    math.radians(-17.67766952966369),
    math.radians(45.0)
)


# Create cylinder: neck_high_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.1,
    vertices=32, location=(0.23758787847867996, 0.23758787847867996, 0.4998496991962433))
obj = bpy.context.active_object
obj.name = "neck_high_1"


# Rotate: neck_high_1 (degrees)
import math
bpy.data.objects["neck_high_1"].rotation_euler = (
    math.radians(24.748737341529164),
    math.radians(-24.748737341529164),
    math.radians(45.0)
)


# Create sphere: head_1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.04, segments=32,
    ring_count=16, location=(0.33941125496954283, 0.33941125496954283, 0.6297745487943649))
obj = bpy.context.active_object
obj.name = "head_1"


# Scale: head_1
bpy.data.objects["head_1"].scale = (1.4, 0.7, 0.85)


# Rotate: head_1 (degrees)
import math
bpy.data.objects["head_1"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(45.0)
)


# Create sphere: jaw_1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.025, segments=32,
    ring_count=16, location=(0.3665641553671063, 0.3665641553671063, 0.6147745487943649))
obj = bpy.context.active_object
obj.name = "jaw_1"


# Scale: jaw_1
bpy.data.objects["jaw_1"].scale = (1.2, 0.6, 0.5)


# Create sphere: eye_1_-1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(0.35001785668734103, 0.3288046532517446, 0.6447745487943649))
obj = bpy.context.active_object
obj.name = "eye_1_-1"


# Create sphere: eye_1_1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(0.3288046532517446, 0.35001785668734103, 0.6447745487943649))
obj = bpy.context.active_object
obj.name = "eye_1_1"


# Create cylinder: neck_low_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.028, depth=0.12,
    vertices=32, location=(1.1021821192326178e-17, 0.18, 0.32423360024179604))
obj = bpy.context.active_object
obj.name = "neck_low_2"


# Rotate: neck_low_2 (degrees)
import math
bpy.data.objects["neck_low_2"].rotation_euler = (
    math.radians(25.0),
    math.radians(-1.5308084989341915e-15),
    math.radians(90.0)
)


# Create cylinder: neck_high_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.1,
    vertices=32, location=(2.057406622567553e-17, 0.33599999999999997, 0.44846720048359207))
obj = bpy.context.active_object
obj.name = "neck_high_2"


# Rotate: neck_high_2 (degrees)
import math
bpy.data.objects["neck_high_2"].rotation_euler = (
    math.radians(35.0),
    math.radians(-2.1431318985078682e-15),
    math.radians(90.0)
)


# Create sphere: head_2
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.04, segments=32,
    ring_count=16, location=(2.9391523179536474e-17, 0.48, 0.5527008007253881))
obj = bpy.context.active_object
obj.name = "head_2"


# Scale: head_2
bpy.data.objects["head_2"].scale = (1.4, 0.7, 0.85)


# Rotate: head_2 (degrees)
import math
bpy.data.objects["head_2"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(90.0)
)


# Create sphere: jaw_2
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.025, segments=32,
    ring_count=16, location=(3.174284503389939e-17, 0.5184, 0.5377008007253881))
obj = bpy.context.active_object
obj.name = "jaw_2"


# Scale: jaw_2
bpy.data.objects["jaw_2"].scale = (1.2, 0.6, 0.5)


# Create sphere: eye_2_-1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(0.015000000000000029, 0.48, 0.5677008007253881))
obj = bpy.context.active_object
obj.name = "eye_2_-1"


# Create sphere: eye_2_1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(-0.01499999999999997, 0.48, 0.5677008007253881))
obj = bpy.context.active_object
obj.name = "eye_2_1"


# Create cylinder: neck_low_3
bpy.ops.mesh.primitive_cylinder_add(radius=0.028, depth=0.12,
    vertices=32, location=(-0.12727922061357855, 0.12727922061357855, 0.2906740964700471))
obj = bpy.context.active_object
obj.name = "neck_low_3"


# Rotate: neck_low_3 (degrees)
import math
bpy.data.objects["neck_low_3"].rotation_euler = (
    math.radians(17.67766952966369),
    math.radians(17.677669529663685),
    math.radians(135.0)
)


# Create cylinder: neck_high_3
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.1,
    vertices=32, location=(-0.23758787847867993, 0.23758787847867996, 0.3813481929400942))
obj = bpy.context.active_object
obj.name = "neck_high_3"


# Rotate: neck_high_3 (degrees)
import math
bpy.data.objects["neck_high_3"].rotation_euler = (
    math.radians(24.748737341529164),
    math.radians(24.74873734152916),
    math.radians(135.0)
)


# Create sphere: head_3
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.04, segments=32,
    ring_count=16, location=(-0.3394112549695428, 0.33941125496954283, 0.45202228941014133))
obj = bpy.context.active_object
obj.name = "head_3"


# Scale: head_3
bpy.data.objects["head_3"].scale = (1.4, 0.7, 0.85)


# Rotate: head_3 (degrees)
import math
bpy.data.objects["head_3"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(135.0)
)


# Create sphere: jaw_3
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.025, segments=32,
    ring_count=16, location=(-0.36656415536710624, 0.3665641553671063, 0.4370222894101413))
obj = bpy.context.active_object
obj.name = "jaw_3"


# Scale: jaw_3
bpy.data.objects["jaw_3"].scale = (1.2, 0.6, 0.5)


# Create sphere: eye_3_-1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(-0.32880465325174457, 0.35001785668734103, 0.46702228941014134))
obj = bpy.context.active_object
obj.name = "eye_3_-1"


# Create sphere: eye_3_1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(-0.350017856687341, 0.3288046532517446, 0.46702228941014134))
obj = bpy.context.active_object
obj.name = "eye_3_1"


# Create cylinder: neck_low_4
bpy.ops.mesh.primitive_cylinder_add(radius=0.028, depth=0.12,
    vertices=32, location=(-0.18, 2.2043642384652355e-17, 0.3116175350540322))
obj = bpy.context.active_object
obj.name = "neck_low_4"


# Rotate: neck_low_4 (degrees)
import math
bpy.data.objects["neck_low_4"].rotation_euler = (
    math.radians(3.061616997868383e-15),
    math.radians(25.0),
    math.radians(180.0)
)


# Create cylinder: neck_high_4
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.1,
    vertices=32, location=(-0.33599999999999997, 4.114813245135106e-17, 0.42323507010806444))
obj = bpy.context.active_object
obj.name = "neck_high_4"


# Rotate: neck_high_4 (degrees)
import math
bpy.data.objects["neck_high_4"].rotation_euler = (
    math.radians(4.2862637970157365e-15),
    math.radians(35.0),
    math.radians(180.0)
)


# Create sphere: head_4
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.04, segments=32,
    ring_count=16, location=(-0.48, 5.878304635907295e-17, 0.5148526051620966))
obj = bpy.context.active_object
obj.name = "head_4"


# Scale: head_4
bpy.data.objects["head_4"].scale = (1.4, 0.7, 0.85)


# Rotate: head_4 (degrees)
import math
bpy.data.objects["head_4"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(180.0)
)


# Create sphere: jaw_4
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.025, segments=32,
    ring_count=16, location=(-0.5184, 6.348569006779878e-17, 0.4998526051620966))
obj = bpy.context.active_object
obj.name = "jaw_4"


# Scale: jaw_4
bpy.data.objects["jaw_4"].scale = (1.2, 0.6, 0.5)


# Create sphere: eye_4_-1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(-0.48, 0.015000000000000058, 0.5298526051620966))
obj = bpy.context.active_object
obj.name = "eye_4_-1"


# Create sphere: eye_4_1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(-0.48, -0.01499999999999994, 0.5298526051620966))
obj = bpy.context.active_object
obj.name = "eye_4_1"


# Create cylinder: neck_low_5
bpy.ops.mesh.primitive_cylinder_add(radius=0.028, depth=0.12,
    vertices=32, location=(-0.12727922061357858, -0.12727922061357855, 0.3481399993032422))
obj = bpy.context.active_object
obj.name = "neck_low_5"


# Rotate: neck_low_5 (degrees)
import math
bpy.data.objects["neck_low_5"].rotation_euler = (
    math.radians(-17.677669529663685),
    math.radians(17.677669529663692),
    math.radians(225.0)
)


# Create cylinder: neck_high_5
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.1,
    vertices=32, location=(-0.23758787847868001, -0.23758787847867993, 0.49627999860648436))
obj = bpy.context.active_object
obj.name = "neck_high_5"


# Rotate: neck_high_5 (degrees)
import math
bpy.data.objects["neck_high_5"].rotation_euler = (
    math.radians(-24.74873734152916),
    math.radians(24.748737341529168),
    math.radians(225.0)
)


# Create sphere: head_5
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.04, segments=32,
    ring_count=16, location=(-0.3394112549695429, -0.3394112549695428, 0.6244199979097266))
obj = bpy.context.active_object
obj.name = "head_5"


# Scale: head_5
bpy.data.objects["head_5"].scale = (1.4, 0.7, 0.85)


# Rotate: head_5 (degrees)
import math
bpy.data.objects["head_5"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(225.0)
)


# Create sphere: jaw_5
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.025, segments=32,
    ring_count=16, location=(-0.36656415536710635, -0.36656415536710624, 0.6094199979097266))
obj = bpy.context.active_object
obj.name = "jaw_5"


# Scale: jaw_5
bpy.data.objects["jaw_5"].scale = (1.2, 0.6, 0.5)


# Create sphere: eye_5_-1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(-0.3500178566873411, -0.32880465325174457, 0.6394199979097266))
obj = bpy.context.active_object
obj.name = "eye_5_-1"


# Create sphere: eye_5_1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(-0.3288046532517447, -0.350017856687341, 0.6394199979097266))
obj = bpy.context.active_object
obj.name = "eye_5_1"


# Create cylinder: neck_low_6
bpy.ops.mesh.primitive_cylinder_add(radius=0.028, depth=0.12,
    vertices=32, location=(-3.306546357697853e-17, -0.18, 0.3323635545572527))
obj = bpy.context.active_object
obj.name = "neck_low_6"


# Rotate: neck_low_6 (degrees)
import math
bpy.data.objects["neck_low_6"].rotation_euler = (
    math.radians(-25.0),
    math.radians(4.592425496802574e-15),
    math.radians(270.0)
)


# Create cylinder: neck_high_6
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.1,
    vertices=32, location=(-6.172219867702659e-17, -0.33599999999999997, 0.4647271091145054))
obj = bpy.context.active_object
obj.name = "neck_high_6"


# Rotate: neck_high_6 (degrees)
import math
bpy.data.objects["neck_high_6"].rotation_euler = (
    math.radians(-35.0),
    math.radians(6.429395695523604e-15),
    math.radians(270.0)
)


# Create sphere: head_6
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.04, segments=32,
    ring_count=16, location=(-8.817456953860942e-17, -0.48, 0.5770906636717581))
obj = bpy.context.active_object
obj.name = "head_6"


# Scale: head_6
bpy.data.objects["head_6"].scale = (1.4, 0.7, 0.85)


# Rotate: head_6 (degrees)
import math
bpy.data.objects["head_6"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(270.0)
)


# Create sphere: jaw_6
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.025, segments=32,
    ring_count=16, location=(-9.522853510169819e-17, -0.5184, 0.5620906636717581))
obj = bpy.context.active_object
obj.name = "jaw_6"


# Scale: jaw_6
bpy.data.objects["jaw_6"].scale = (1.2, 0.6, 0.5)


# Create sphere: eye_6_-1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(-0.015000000000000088, -0.48, 0.5920906636717581))
obj = bpy.context.active_object
obj.name = "eye_6_-1"


# Create sphere: eye_6_1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(0.014999999999999911, -0.48, 0.5920906636717581))
obj = bpy.context.active_object
obj.name = "eye_6_1"


# Create cylinder: neck_low_7
bpy.ops.mesh.primitive_cylinder_add(radius=0.028, depth=0.12,
    vertices=32, location=(0.12727922061357852, -0.12727922061357858, 0.2936091272008499))
obj = bpy.context.active_object
obj.name = "neck_low_7"


# Rotate: neck_low_7 (degrees)
import math
bpy.data.objects["neck_low_7"].rotation_euler = (
    math.radians(-17.677669529663692),
    math.radians(-17.677669529663685),
    math.radians(315.0)
)


# Create cylinder: neck_high_7
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.1,
    vertices=32, location=(0.23758787847867988, -0.23758787847868001, 0.3872182544016998))
obj = bpy.context.active_object
obj.name = "neck_high_7"


# Rotate: neck_high_7 (degrees)
import math
bpy.data.objects["neck_high_7"].rotation_euler = (
    math.radians(-24.748737341529168),
    math.radians(-24.748737341529157),
    math.radians(315.0)
)


# Create sphere: head_7
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.04, segments=32,
    ring_count=16, location=(0.3394112549695427, -0.3394112549695429, 0.46082738160254977))
obj = bpy.context.active_object
obj.name = "head_7"


# Scale: head_7
bpy.data.objects["head_7"].scale = (1.4, 0.7, 0.85)


# Rotate: head_7 (degrees)
import math
bpy.data.objects["head_7"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(315.0)
)


# Create sphere: jaw_7
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.025, segments=32,
    ring_count=16, location=(0.3665641553671062, -0.36656415536710635, 0.44582738160254975))
obj = bpy.context.active_object
obj.name = "jaw_7"


# Scale: jaw_7
bpy.data.objects["jaw_7"].scale = (1.2, 0.6, 0.5)


# Create sphere: eye_7_-1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(0.3288046532517445, -0.3500178566873411, 0.4758273816025498))
obj = bpy.context.active_object
obj.name = "eye_7_-1"


# Create sphere: eye_7_1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.008, segments=32,
    ring_count=16, location=(0.3500178566873409, -0.3288046532517447, 0.4758273816025498))
obj = bpy.context.active_object
obj.name = "eye_7_1"


# Create cone: tail_base
bpy.ops.mesh.primitive_cone_add(radius1=0.09, radius2=0.04,
    depth=0.18, vertices=32, location=(0, -0.22, 0.18))
obj = bpy.context.active_object
obj.name = "tail_base"


# Rotate: tail_base (degrees)
import math
bpy.data.objects["tail_base"].rotation_euler = (
    math.radians(65),
    math.radians(0),
    math.radians(0)
)


# Create cone: tail_mid
bpy.ops.mesh.primitive_cone_add(radius1=0.04, radius2=0.025,
    depth=0.14, vertices=32, location=(0, -0.36, 0.28))
obj = bpy.context.active_object
obj.name = "tail_mid"


# Rotate: tail_mid (degrees)
import math
bpy.data.objects["tail_mid"].rotation_euler = (
    math.radians(50),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: tail_end
bpy.ops.mesh.primitive_cylinder_add(radius=0.02, depth=0.1,
    vertices=32, location=(0, -0.46, 0.38))
obj = bpy.context.active_object
obj.name = "tail_end"


# Rotate: tail_end (degrees)
import math
bpy.data.objects["tail_end"].rotation_euler = (
    math.radians(35),
    math.radians(0),
    math.radians(0)
)


# Create cone: pincer_l
bpy.ops.mesh.primitive_cone_add(radius1=0.025, radius2=0.005,
    depth=0.1, vertices=32, location=(-0.04, -0.52, 0.45))
obj = bpy.context.active_object
obj.name = "pincer_l"


# Rotate: pincer_l (degrees)
import math
bpy.data.objects["pincer_l"].rotation_euler = (
    math.radians(25),
    math.radians(-25),
    math.radians(0)
)


# Create cone: pincer_r
bpy.ops.mesh.primitive_cone_add(radius1=0.025, radius2=0.005,
    depth=0.1, vertices=32, location=(0.04, -0.52, 0.45))
obj = bpy.context.active_object
obj.name = "pincer_r"


# Rotate: pincer_r (degrees)
import math
bpy.data.objects["pincer_r"].rotation_euler = (
    math.radians(25),
    math.radians(25),
    math.radians(0)
)


# Create cone: pincer_inner_l
bpy.ops.mesh.primitive_cone_add(radius1=0.012, radius2=0.003,
    depth=0.06, vertices=32, location=(-0.02, -0.52, 0.44))
obj = bpy.context.active_object
obj.name = "pincer_inner_l"


# Rotate: pincer_inner_l (degrees)
import math
bpy.data.objects["pincer_inner_l"].rotation_euler = (
    math.radians(35),
    math.radians(-40),
    math.radians(0)
)


# Create cone: pincer_inner_r
bpy.ops.mesh.primitive_cone_add(radius1=0.012, radius2=0.003,
    depth=0.06, vertices=32, location=(0.02, -0.52, 0.44))
obj = bpy.context.active_object
obj.name = "pincer_inner_r"


# Rotate: pincer_inner_r (degrees)
import math
bpy.data.objects["pincer_inner_r"].rotation_euler = (
    math.radians(35),
    math.radians(40),
    math.radians(0)
)


# Create cylinder: leg_up_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.1,
    vertices=32, location=(0.14, 0.08, 0.08))
obj = bpy.context.active_object
obj.name = "leg_up_0"


# Rotate: leg_up_0 (degrees)
import math
bpy.data.objects["leg_up_0"].rotation_euler = (
    math.radians(15),
    math.radians(30),
    math.radians(0)
)


# Create cylinder: leg_low_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=0.08,
    vertices=32, location=(0.22400000000000003, 0.08, 0.02))
obj = bpy.context.active_object
obj.name = "leg_low_0"


# Rotate: leg_low_0 (degrees)
import math
bpy.data.objects["leg_low_0"].rotation_euler = (
    math.radians(-10),
    math.radians(21.0),
    math.radians(0)
)


# Create cylinder: leg_up_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.1,
    vertices=32, location=(-0.14, 0.08, 0.08))
obj = bpy.context.active_object
obj.name = "leg_up_1"


# Rotate: leg_up_1 (degrees)
import math
bpy.data.objects["leg_up_1"].rotation_euler = (
    math.radians(15),
    math.radians(-30),
    math.radians(0)
)


# Create cylinder: leg_low_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=0.08,
    vertices=32, location=(-0.22400000000000003, 0.08, 0.02))
obj = bpy.context.active_object
obj.name = "leg_low_1"


# Rotate: leg_low_1 (degrees)
import math
bpy.data.objects["leg_low_1"].rotation_euler = (
    math.radians(-10),
    math.radians(-21.0),
    math.radians(0)
)


# Create cylinder: leg_up_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.1,
    vertices=32, location=(0.16, 0, 0.06))
obj = bpy.context.active_object
obj.name = "leg_up_2"


# Rotate: leg_up_2 (degrees)
import math
bpy.data.objects["leg_up_2"].rotation_euler = (
    math.radians(15),
    math.radians(50),
    math.radians(0)
)


# Create cylinder: leg_low_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=0.08,
    vertices=32, location=(0.256, 0, 0.02))
obj = bpy.context.active_object
obj.name = "leg_low_2"


# Rotate: leg_low_2 (degrees)
import math
bpy.data.objects["leg_low_2"].rotation_euler = (
    math.radians(-10),
    math.radians(35.0),
    math.radians(0)
)


# Create cylinder: leg_up_3
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.1,
    vertices=32, location=(-0.16, 0, 0.06))
obj = bpy.context.active_object
obj.name = "leg_up_3"


# Rotate: leg_up_3 (degrees)
import math
bpy.data.objects["leg_up_3"].rotation_euler = (
    math.radians(15),
    math.radians(-50),
    math.radians(0)
)


# Create cylinder: leg_low_3
bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=0.08,
    vertices=32, location=(-0.256, 0, 0.02))
obj = bpy.context.active_object
obj.name = "leg_low_3"


# Rotate: leg_low_3 (degrees)
import math
bpy.data.objects["leg_low_3"].rotation_euler = (
    math.radians(-10),
    math.radians(-35.0),
    math.radians(0)
)


# Create cylinder: leg_up_4
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.1,
    vertices=32, location=(0.13, -0.08, 0.06))
obj = bpy.context.active_object
obj.name = "leg_up_4"


# Rotate: leg_up_4 (degrees)
import math
bpy.data.objects["leg_up_4"].rotation_euler = (
    math.radians(15),
    math.radians(70),
    math.radians(0)
)


# Create cylinder: leg_low_4
bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=0.08,
    vertices=32, location=(0.20800000000000002, -0.08, 0.02))
obj = bpy.context.active_object
obj.name = "leg_low_4"


# Rotate: leg_low_4 (degrees)
import math
bpy.data.objects["leg_low_4"].rotation_euler = (
    math.radians(-10),
    math.radians(49.0),
    math.radians(0)
)


# Create cylinder: leg_up_5
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.1,
    vertices=32, location=(-0.13, -0.08, 0.06))
obj = bpy.context.active_object
obj.name = "leg_up_5"


# Rotate: leg_up_5 (degrees)
import math
bpy.data.objects["leg_up_5"].rotation_euler = (
    math.radians(15),
    math.radians(-70),
    math.radians(0)
)


# Create cylinder: leg_low_5
bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=0.08,
    vertices=32, location=(-0.20800000000000002, -0.08, 0.02))
obj = bpy.context.active_object
obj.name = "leg_low_5"


# Rotate: leg_low_5 (degrees)
import math
bpy.data.objects["leg_low_5"].rotation_euler = (
    math.radians(-10),
    math.radians(-49.0),
    math.radians(0)
)


# Union objects into: thessalhydra-8head
# Using boolean EXACT solver for watertight results
base_obj = bpy.data.objects["body"]
bpy.context.view_layer.objects.active = base_obj


# Boolean union: adding tail_base
tool_obj = bpy.data.objects["tail_base"]
mod = base_obj.modifiers.new(name="Boolean_0", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_0")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tail_mid
tool_obj = bpy.data.objects["tail_mid"]
mod = base_obj.modifiers.new(name="Boolean_1", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_1")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tail_end
tool_obj = bpy.data.objects["tail_end"]
mod = base_obj.modifiers.new(name="Boolean_2", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_2")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding pincer_l
tool_obj = bpy.data.objects["pincer_l"]
mod = base_obj.modifiers.new(name="Boolean_3", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_3")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding pincer_r
tool_obj = bpy.data.objects["pincer_r"]
mod = base_obj.modifiers.new(name="Boolean_4", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_4")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding pincer_inner_l
tool_obj = bpy.data.objects["pincer_inner_l"]
mod = base_obj.modifiers.new(name="Boolean_5", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_5")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding pincer_inner_r
tool_obj = bpy.data.objects["pincer_inner_r"]
mod = base_obj.modifiers.new(name="Boolean_6", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_6")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding neck_low_0
tool_obj = bpy.data.objects["neck_low_0"]
mod = base_obj.modifiers.new(name="Boolean_7", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_7")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding neck_high_0
tool_obj = bpy.data.objects["neck_high_0"]
mod = base_obj.modifiers.new(name="Boolean_8", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_8")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_0
tool_obj = bpy.data.objects["head_0"]
mod = base_obj.modifiers.new(name="Boolean_9", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_9")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding jaw_0
tool_obj = bpy.data.objects["jaw_0"]
mod = base_obj.modifiers.new(name="Boolean_10", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_10")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_0_-1
tool_obj = bpy.data.objects["eye_0_-1"]
mod = base_obj.modifiers.new(name="Boolean_11", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_11")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_0_1
tool_obj = bpy.data.objects["eye_0_1"]
mod = base_obj.modifiers.new(name="Boolean_12", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_12")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding neck_low_1
tool_obj = bpy.data.objects["neck_low_1"]
mod = base_obj.modifiers.new(name="Boolean_13", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_13")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding neck_high_1
tool_obj = bpy.data.objects["neck_high_1"]
mod = base_obj.modifiers.new(name="Boolean_14", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_14")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_1
tool_obj = bpy.data.objects["head_1"]
mod = base_obj.modifiers.new(name="Boolean_15", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_15")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding jaw_1
tool_obj = bpy.data.objects["jaw_1"]
mod = base_obj.modifiers.new(name="Boolean_16", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_16")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_1_-1
tool_obj = bpy.data.objects["eye_1_-1"]
mod = base_obj.modifiers.new(name="Boolean_17", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_17")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_1_1
tool_obj = bpy.data.objects["eye_1_1"]
mod = base_obj.modifiers.new(name="Boolean_18", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_18")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding neck_low_2
tool_obj = bpy.data.objects["neck_low_2"]
mod = base_obj.modifiers.new(name="Boolean_19", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_19")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding neck_high_2
tool_obj = bpy.data.objects["neck_high_2"]
mod = base_obj.modifiers.new(name="Boolean_20", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_20")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_2
tool_obj = bpy.data.objects["head_2"]
mod = base_obj.modifiers.new(name="Boolean_21", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_21")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding jaw_2
tool_obj = bpy.data.objects["jaw_2"]
mod = base_obj.modifiers.new(name="Boolean_22", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_22")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_2_-1
tool_obj = bpy.data.objects["eye_2_-1"]
mod = base_obj.modifiers.new(name="Boolean_23", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_23")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_2_1
tool_obj = bpy.data.objects["eye_2_1"]
mod = base_obj.modifiers.new(name="Boolean_24", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_24")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding neck_low_3
tool_obj = bpy.data.objects["neck_low_3"]
mod = base_obj.modifiers.new(name="Boolean_25", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_25")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding neck_high_3
tool_obj = bpy.data.objects["neck_high_3"]
mod = base_obj.modifiers.new(name="Boolean_26", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_26")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_3
tool_obj = bpy.data.objects["head_3"]
mod = base_obj.modifiers.new(name="Boolean_27", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_27")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding jaw_3
tool_obj = bpy.data.objects["jaw_3"]
mod = base_obj.modifiers.new(name="Boolean_28", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_28")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_3_-1
tool_obj = bpy.data.objects["eye_3_-1"]
mod = base_obj.modifiers.new(name="Boolean_29", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_29")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_3_1
tool_obj = bpy.data.objects["eye_3_1"]
mod = base_obj.modifiers.new(name="Boolean_30", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_30")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding neck_low_4
tool_obj = bpy.data.objects["neck_low_4"]
mod = base_obj.modifiers.new(name="Boolean_31", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_31")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding neck_high_4
tool_obj = bpy.data.objects["neck_high_4"]
mod = base_obj.modifiers.new(name="Boolean_32", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_32")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_4
tool_obj = bpy.data.objects["head_4"]
mod = base_obj.modifiers.new(name="Boolean_33", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_33")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding jaw_4
tool_obj = bpy.data.objects["jaw_4"]
mod = base_obj.modifiers.new(name="Boolean_34", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_34")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_4_-1
tool_obj = bpy.data.objects["eye_4_-1"]
mod = base_obj.modifiers.new(name="Boolean_35", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_35")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_4_1
tool_obj = bpy.data.objects["eye_4_1"]
mod = base_obj.modifiers.new(name="Boolean_36", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_36")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding neck_low_5
tool_obj = bpy.data.objects["neck_low_5"]
mod = base_obj.modifiers.new(name="Boolean_37", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_37")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding neck_high_5
tool_obj = bpy.data.objects["neck_high_5"]
mod = base_obj.modifiers.new(name="Boolean_38", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_38")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_5
tool_obj = bpy.data.objects["head_5"]
mod = base_obj.modifiers.new(name="Boolean_39", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_39")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding jaw_5
tool_obj = bpy.data.objects["jaw_5"]
mod = base_obj.modifiers.new(name="Boolean_40", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_40")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_5_-1
tool_obj = bpy.data.objects["eye_5_-1"]
mod = base_obj.modifiers.new(name="Boolean_41", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_41")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_5_1
tool_obj = bpy.data.objects["eye_5_1"]
mod = base_obj.modifiers.new(name="Boolean_42", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_42")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding neck_low_6
tool_obj = bpy.data.objects["neck_low_6"]
mod = base_obj.modifiers.new(name="Boolean_43", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_43")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding neck_high_6
tool_obj = bpy.data.objects["neck_high_6"]
mod = base_obj.modifiers.new(name="Boolean_44", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_44")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_6
tool_obj = bpy.data.objects["head_6"]
mod = base_obj.modifiers.new(name="Boolean_45", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_45")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding jaw_6
tool_obj = bpy.data.objects["jaw_6"]
mod = base_obj.modifiers.new(name="Boolean_46", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_46")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_6_-1
tool_obj = bpy.data.objects["eye_6_-1"]
mod = base_obj.modifiers.new(name="Boolean_47", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_47")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_6_1
tool_obj = bpy.data.objects["eye_6_1"]
mod = base_obj.modifiers.new(name="Boolean_48", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_48")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding neck_low_7
tool_obj = bpy.data.objects["neck_low_7"]
mod = base_obj.modifiers.new(name="Boolean_49", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_49")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding neck_high_7
tool_obj = bpy.data.objects["neck_high_7"]
mod = base_obj.modifiers.new(name="Boolean_50", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_50")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding head_7
tool_obj = bpy.data.objects["head_7"]
mod = base_obj.modifiers.new(name="Boolean_51", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_51")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding jaw_7
tool_obj = bpy.data.objects["jaw_7"]
mod = base_obj.modifiers.new(name="Boolean_52", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_52")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_7_-1
tool_obj = bpy.data.objects["eye_7_-1"]
mod = base_obj.modifiers.new(name="Boolean_53", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_53")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_7_1
tool_obj = bpy.data.objects["eye_7_1"]
mod = base_obj.modifiers.new(name="Boolean_54", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_54")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_up_0
tool_obj = bpy.data.objects["leg_up_0"]
mod = base_obj.modifiers.new(name="Boolean_55", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_55")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_low_0
tool_obj = bpy.data.objects["leg_low_0"]
mod = base_obj.modifiers.new(name="Boolean_56", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_56")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_up_1
tool_obj = bpy.data.objects["leg_up_1"]
mod = base_obj.modifiers.new(name="Boolean_57", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_57")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_low_1
tool_obj = bpy.data.objects["leg_low_1"]
mod = base_obj.modifiers.new(name="Boolean_58", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_58")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_up_2
tool_obj = bpy.data.objects["leg_up_2"]
mod = base_obj.modifiers.new(name="Boolean_59", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_59")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_low_2
tool_obj = bpy.data.objects["leg_low_2"]
mod = base_obj.modifiers.new(name="Boolean_60", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_60")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_up_3
tool_obj = bpy.data.objects["leg_up_3"]
mod = base_obj.modifiers.new(name="Boolean_61", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_61")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_low_3
tool_obj = bpy.data.objects["leg_low_3"]
mod = base_obj.modifiers.new(name="Boolean_62", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_62")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_up_4
tool_obj = bpy.data.objects["leg_up_4"]
mod = base_obj.modifiers.new(name="Boolean_63", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_63")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_low_4
tool_obj = bpy.data.objects["leg_low_4"]
mod = base_obj.modifiers.new(name="Boolean_64", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_64")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_up_5
tool_obj = bpy.data.objects["leg_up_5"]
mod = base_obj.modifiers.new(name="Boolean_65", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_65")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_low_5
tool_obj = bpy.data.objects["leg_low_5"]
mod = base_obj.modifiers.new(name="Boolean_66", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_66")
bpy.data.objects.remove(tool_obj, do_unlink=True)


base_obj.name = "thessalhydra-8head"


# Add subdivision surface: thessalhydra-8head
obj = bpy.data.objects["thessalhydra-8head"]
mod = obj.modifiers.new(name="Subdivision", type='SUBSURF')
mod.levels = 2
mod.render_levels = 2


# Add smooth: thessalhydra-8head
obj = bpy.data.objects["thessalhydra-8head"]
mod = obj.modifiers.new(name="Smooth", type='SMOOTH')
mod.factor = 0.25
mod.iterations = 1


# Apply all modifiers: thessalhydra-8head
obj = bpy.data.objects["thessalhydra-8head"]
bpy.context.view_layer.objects.active = obj
for mod in obj.modifiers[:]:
    bpy.ops.object.modifier_apply(modifier=mod.name)


# Create cylinder: thessalhydra-8head_base
bpy.ops.mesh.primitive_cylinder_add(radius=0.0375, depth=0.003,
    vertices=64, location=(0, 0, 0.0015))
obj = bpy.context.active_object
obj.name = "thessalhydra-8head_base"


# Add bevel: thessalhydra-8head_base
obj = bpy.data.objects["thessalhydra-8head_base"]
mod = obj.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.0005
mod.segments = 2


# Boolean union: thessalhydra-8head + thessalhydra-8head_base
target_obj = bpy.data.objects["thessalhydra-8head"]
tool_obj = bpy.data.objects["thessalhydra-8head_base"]
mod = target_obj.modifiers.new(name="Boolean", type='BOOLEAN')
mod.operation = 'UNION'
mod.object = tool_obj
bpy.context.view_layer.objects.active = target_obj
bpy.ops.object.modifier_apply(modifier='Boolean')
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Export to STL (Blender 4.0+ API)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.wm.stl_export(
    filepath="C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/thessalhydra-8head.stl",
    export_selected_objects=True,
    global_scale=1.0,
    ascii_format=False  # Binary STL is smaller and faster
)
print("Exported: C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/thessalhydra-8head.stl")
