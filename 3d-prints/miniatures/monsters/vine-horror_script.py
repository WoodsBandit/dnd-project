import bpy
import bmesh
import math
from mathutils import Vector, Matrix

# Clear default scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)


# Create cylinder: rib_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.28,
    vertices=32, location=(0.08, 0.0, 0.6))
obj = bpy.context.active_object
obj.name = "rib_0"


# Create cylinder: rib_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.28,
    vertices=32, location=(0.05656854249492381, 0.042426406871192854, 0.6))
obj = bpy.context.active_object
obj.name = "rib_1"


# Create cylinder: rib_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.28,
    vertices=32, location=(4.898587196589413e-18, 0.06, 0.6))
obj = bpy.context.active_object
obj.name = "rib_2"


# Create cylinder: rib_3
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.28,
    vertices=32, location=(-0.056568542494923796, 0.042426406871192854, 0.6))
obj = bpy.context.active_object
obj.name = "rib_3"


# Create cylinder: rib_4
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.28,
    vertices=32, location=(-0.08, 7.347880794884118e-18, 0.6))
obj = bpy.context.active_object
obj.name = "rib_4"


# Create cylinder: rib_5
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.28,
    vertices=32, location=(-0.05656854249492382, -0.04242640687119285, 0.6))
obj = bpy.context.active_object
obj.name = "rib_5"


# Create cylinder: rib_6
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.28,
    vertices=32, location=(-1.4695761589768237e-17, -0.06, 0.6))
obj = bpy.context.active_object
obj.name = "rib_6"


# Create cylinder: rib_7
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.28,
    vertices=32, location=(0.05656854249492379, -0.04242640687119286, 0.6))
obj = bpy.context.active_object
obj.name = "rib_7"


# Create torus: ring_0
bpy.ops.mesh.primitive_torus_add(major_radius=0.065, minor_radius=0.008,
    major_segments=24, minor_segments=6, location=(0, 0, 0.5))
obj = bpy.context.active_object
obj.name = "ring_0"


# Create torus: ring_1
bpy.ops.mesh.primitive_torus_add(major_radius=0.075, minor_radius=0.008,
    major_segments=24, minor_segments=6, location=(0, 0, 0.58))
obj = bpy.context.active_object
obj.name = "ring_1"


# Create torus: ring_2
bpy.ops.mesh.primitive_torus_add(major_radius=0.075, minor_radius=0.008,
    major_segments=24, minor_segments=6, location=(0, 0, 0.66))
obj = bpy.context.active_object
obj.name = "ring_2"


# Create torus: ring_3
bpy.ops.mesh.primitive_torus_add(major_radius=0.065, minor_radius=0.008,
    major_segments=24, minor_segments=6, location=(0, 0, 0.74))
obj = bpy.context.active_object
obj.name = "ring_3"


# Create sphere: head_core
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.05, segments=32,
    ring_count=16, location=(0, 0, 0.82))
obj = bpy.context.active_object
obj.name = "head_core"


# Scale: head_core
bpy.data.objects["head_core"].scale = (0.85, 0.8, 1.0)


# Create cylinder: face_vine_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.006, depth=0.08,
    vertices=32, location=(1.8369701987210296e-18, -0.02, 0.82))
obj = bpy.context.active_object
obj.name = "face_vine_0"


# Rotate: face_vine_0 (degrees)
import math
bpy.data.objects["face_vine_0"].rotation_euler = (
    math.radians(-20.0),
    math.radians(0),
    math.radians(-45.0)
)


# Create cylinder: face_vine_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.006, depth=0.08,
    vertices=32, location=(0.017633557568774192, -0.012360679774997895, 0.82))
obj = bpy.context.active_object
obj.name = "face_vine_1"


# Rotate: face_vine_1 (degrees)
import math
bpy.data.objects["face_vine_1"].rotation_euler = (
    math.radians(-16.18033988749895),
    math.radians(0),
    math.radians(-27.0)
)


# Create cylinder: face_vine_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.006, depth=0.08,
    vertices=32, location=(0.028531695488854605, 0.0076393202250021035, 0.82))
obj = bpy.context.active_object
obj.name = "face_vine_2"


# Rotate: face_vine_2 (degrees)
import math
bpy.data.objects["face_vine_2"].rotation_euler = (
    math.radians(-6.180339887498948),
    math.radians(0),
    math.radians(-9.0)
)


# Create cylinder: face_vine_3
bpy.ops.mesh.primitive_cylinder_add(radius=0.006, depth=0.08,
    vertices=32, location=(0.028531695488854605, 0.032360679774997896, 0.82))
obj = bpy.context.active_object
obj.name = "face_vine_3"


# Rotate: face_vine_3 (degrees)
import math
bpy.data.objects["face_vine_3"].rotation_euler = (
    math.radians(6.180339887498948),
    math.radians(0),
    math.radians(9.0)
)


# Create cylinder: face_vine_4
bpy.ops.mesh.primitive_cylinder_add(radius=0.006, depth=0.08,
    vertices=32, location=(0.017633557568774192, 0.05236067977499789, 0.82))
obj = bpy.context.active_object
obj.name = "face_vine_4"


# Rotate: face_vine_4 (degrees)
import math
bpy.data.objects["face_vine_4"].rotation_euler = (
    math.radians(16.18033988749895),
    math.radians(0),
    math.radians(27.0)
)


# Create cylinder: face_vine_5
bpy.ops.mesh.primitive_cylinder_add(radius=0.006, depth=0.08,
    vertices=32, location=(1.8369701987210296e-18, 0.06, 0.82))
obj = bpy.context.active_object
obj.name = "face_vine_5"


# Rotate: face_vine_5 (degrees)
import math
bpy.data.objects["face_vine_5"].rotation_euler = (
    math.radians(20.0),
    math.radians(0),
    math.radians(45.0)
)


# Create sphere: eye_socket_r
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(0.02, 0.04, 0.83))
obj = bpy.context.active_object
obj.name = "eye_socket_r"


# Create sphere: eye_socket_l
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(-0.02, 0.04, 0.83))
obj = bpy.context.active_object
obj.name = "eye_socket_l"


# Create cylinder: mouth
bpy.ops.mesh.primitive_cylinder_add(radius=0.018, depth=0.02,
    vertices=32, location=(0, 0.045, 0.78))
obj = bpy.context.active_object
obj.name = "mouth"


# Rotate: mouth (degrees)
import math
bpy.data.objects["mouth"].rotation_euler = (
    math.radians(80),
    math.radians(0),
    math.radians(0)
)


# Create sphere: shoulder_r
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.025, segments=32,
    ring_count=16, location=(0.1, 0, 0.7))
obj = bpy.context.active_object
obj.name = "shoulder_r"


# Create cylinder: arm_vine_r_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.12,
    vertices=32, location=(0.16499999999999998, 0.0, 0.6))
obj = bpy.context.active_object
obj.name = "arm_vine_r_0"


# Rotate: arm_vine_r_0 (degrees)
import math
bpy.data.objects["arm_vine_r_0"].rotation_euler = (
    math.radians(15),
    math.radians(55),
    math.radians(0)
)


# Create cylinder: arm_vine_r_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.12,
    vertices=32, location=(0.1425, 0.01299038105676658, 0.6))
obj = bpy.context.active_object
obj.name = "arm_vine_r_1"


# Rotate: arm_vine_r_1 (degrees)
import math
bpy.data.objects["arm_vine_r_1"].rotation_euler = (
    math.radians(15),
    math.radians(55),
    math.radians(0)
)


# Create cylinder: arm_vine_r_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.12,
    vertices=32, location=(0.1425, -0.012990381056766576, 0.6))
obj = bpy.context.active_object
obj.name = "arm_vine_r_2"


# Rotate: arm_vine_r_2 (degrees)
import math
bpy.data.objects["arm_vine_r_2"].rotation_euler = (
    math.radians(15),
    math.radians(55),
    math.radians(0)
)


# Create cylinder: forearm_vine_r_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.006, depth=0.1,
    vertices=32, location=(0.24000000000000002, 0.0, 0.48))
obj = bpy.context.active_object
obj.name = "forearm_vine_r_0"


# Rotate: forearm_vine_r_0 (degrees)
import math
bpy.data.objects["forearm_vine_r_0"].rotation_euler = (
    math.radians(30),
    math.radians(35),
    math.radians(0)
)


# Create cylinder: forearm_vine_r_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.006, depth=0.1,
    vertices=32, location=(0.22, 1.2246467991473532e-18, 0.48))
obj = bpy.context.active_object
obj.name = "forearm_vine_r_1"


# Rotate: forearm_vine_r_1 (degrees)
import math
bpy.data.objects["forearm_vine_r_1"].rotation_euler = (
    math.radians(30),
    math.radians(35),
    math.radians(0)
)


# Create cone: finger_r_0
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.04, vertices=32, location=(0.28, 0.04, 0.38))
obj = bpy.context.active_object
obj.name = "finger_r_0"


# Rotate: finger_r_0 (degrees)
import math
bpy.data.objects["finger_r_0"].rotation_euler = (
    math.radians(50),
    math.radians(20),
    math.radians(0)
)


# Create cone: finger_r_1
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.04, vertices=32, location=(0.28800000000000003, 0.05, 0.38))
obj = bpy.context.active_object
obj.name = "finger_r_1"


# Rotate: finger_r_1 (degrees)
import math
bpy.data.objects["finger_r_1"].rotation_euler = (
    math.radians(60),
    math.radians(20),
    math.radians(0)
)


# Create cone: finger_r_2
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.04, vertices=32, location=(0.29600000000000004, 0.06, 0.38))
obj = bpy.context.active_object
obj.name = "finger_r_2"


# Rotate: finger_r_2 (degrees)
import math
bpy.data.objects["finger_r_2"].rotation_euler = (
    math.radians(70),
    math.radians(20),
    math.radians(0)
)


# Create cone: finger_r_3
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.04, vertices=32, location=(0.30400000000000005, 0.07, 0.38))
obj = bpy.context.active_object
obj.name = "finger_r_3"


# Rotate: finger_r_3 (degrees)
import math
bpy.data.objects["finger_r_3"].rotation_euler = (
    math.radians(80),
    math.radians(20),
    math.radians(0)
)


# Create sphere: shoulder_l
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.025, segments=32,
    ring_count=16, location=(-0.1, 0, 0.7))
obj = bpy.context.active_object
obj.name = "shoulder_l"


# Create cylinder: arm_vine_l_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.12,
    vertices=32, location=(-0.16499999999999998, 0.0, 0.6))
obj = bpy.context.active_object
obj.name = "arm_vine_l_0"


# Rotate: arm_vine_l_0 (degrees)
import math
bpy.data.objects["arm_vine_l_0"].rotation_euler = (
    math.radians(15),
    math.radians(-55),
    math.radians(0)
)


# Create cylinder: arm_vine_l_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.12,
    vertices=32, location=(-0.1425, 0.01299038105676658, 0.6))
obj = bpy.context.active_object
obj.name = "arm_vine_l_1"


# Rotate: arm_vine_l_1 (degrees)
import math
bpy.data.objects["arm_vine_l_1"].rotation_euler = (
    math.radians(15),
    math.radians(-55),
    math.radians(0)
)


# Create cylinder: arm_vine_l_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.12,
    vertices=32, location=(-0.1425, -0.012990381056766576, 0.6))
obj = bpy.context.active_object
obj.name = "arm_vine_l_2"


# Rotate: arm_vine_l_2 (degrees)
import math
bpy.data.objects["arm_vine_l_2"].rotation_euler = (
    math.radians(15),
    math.radians(-55),
    math.radians(0)
)


# Create cylinder: forearm_vine_l_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.006, depth=0.1,
    vertices=32, location=(-0.24000000000000002, 0.0, 0.48))
obj = bpy.context.active_object
obj.name = "forearm_vine_l_0"


# Rotate: forearm_vine_l_0 (degrees)
import math
bpy.data.objects["forearm_vine_l_0"].rotation_euler = (
    math.radians(30),
    math.radians(-35),
    math.radians(0)
)


# Create cylinder: forearm_vine_l_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.006, depth=0.1,
    vertices=32, location=(-0.22, 1.2246467991473532e-18, 0.48))
obj = bpy.context.active_object
obj.name = "forearm_vine_l_1"


# Rotate: forearm_vine_l_1 (degrees)
import math
bpy.data.objects["forearm_vine_l_1"].rotation_euler = (
    math.radians(30),
    math.radians(-35),
    math.radians(0)
)


# Create cone: finger_l_0
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.04, vertices=32, location=(-0.28, 0.04, 0.38))
obj = bpy.context.active_object
obj.name = "finger_l_0"


# Rotate: finger_l_0 (degrees)
import math
bpy.data.objects["finger_l_0"].rotation_euler = (
    math.radians(50),
    math.radians(-20),
    math.radians(0)
)


# Create cone: finger_l_1
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.04, vertices=32, location=(-0.28800000000000003, 0.05, 0.38))
obj = bpy.context.active_object
obj.name = "finger_l_1"


# Rotate: finger_l_1 (degrees)
import math
bpy.data.objects["finger_l_1"].rotation_euler = (
    math.radians(60),
    math.radians(-20),
    math.radians(0)
)


# Create cone: finger_l_2
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.04, vertices=32, location=(-0.29600000000000004, 0.06, 0.38))
obj = bpy.context.active_object
obj.name = "finger_l_2"


# Rotate: finger_l_2 (degrees)
import math
bpy.data.objects["finger_l_2"].rotation_euler = (
    math.radians(70),
    math.radians(-20),
    math.radians(0)
)


# Create cone: finger_l_3
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.04, vertices=32, location=(-0.30400000000000005, 0.07, 0.38))
obj = bpy.context.active_object
obj.name = "finger_l_3"


# Rotate: finger_l_3 (degrees)
import math
bpy.data.objects["finger_l_3"].rotation_euler = (
    math.radians(80),
    math.radians(-20),
    math.radians(0)
)


# Create cylinder: leg_vine_r_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.01, depth=0.16,
    vertices=32, location=(0.062, 0.0, 0.32))
obj = bpy.context.active_object
obj.name = "leg_vine_r_0"


# Rotate: leg_vine_r_0 (degrees)
import math
bpy.data.objects["leg_vine_r_0"].rotation_euler = (
    math.radians(5),
    math.radians(8),
    math.radians(0)
)


# Create cylinder: leg_vine_r_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.01, depth=0.16,
    vertices=32, location=(0.044000000000000004, 0.010392304845413265, 0.32))
obj = bpy.context.active_object
obj.name = "leg_vine_r_1"


# Rotate: leg_vine_r_1 (degrees)
import math
bpy.data.objects["leg_vine_r_1"].rotation_euler = (
    math.radians(5),
    math.radians(8),
    math.radians(0)
)


# Create cylinder: leg_vine_r_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.01, depth=0.16,
    vertices=32, location=(0.044, -0.010392304845413262, 0.32))
obj = bpy.context.active_object
obj.name = "leg_vine_r_2"


# Rotate: leg_vine_r_2 (degrees)
import math
bpy.data.objects["leg_vine_r_2"].rotation_euler = (
    math.radians(5),
    math.radians(8),
    math.radians(0)
)


# Create cylinder: shin_vine_r_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.007, depth=0.12,
    vertices=32, location=(0.06, 0.0, 0.1))
obj = bpy.context.active_object
obj.name = "shin_vine_r_0"


# Rotate: shin_vine_r_0 (degrees)
import math
bpy.data.objects["shin_vine_r_0"].rotation_euler = (
    math.radians(-5),
    math.radians(5),
    math.radians(0)
)


# Create cylinder: shin_vine_r_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.007, depth=0.12,
    vertices=32, location=(0.068, 0.01, 0.1))
obj = bpy.context.active_object
obj.name = "shin_vine_r_1"


# Rotate: shin_vine_r_1 (degrees)
import math
bpy.data.objects["shin_vine_r_1"].rotation_euler = (
    math.radians(-5),
    math.radians(5),
    math.radians(0)
)


# Create cone: root_r_0
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.003,
    depth=0.04, vertices=32, location=(0.05, 0.0, 0.02))
obj = bpy.context.active_object
obj.name = "root_r_0"


# Rotate: root_r_0 (degrees)
import math
bpy.data.objects["root_r_0"].rotation_euler = (
    math.radians(85),
    math.radians(0),
    math.radians(-15)
)


# Create cone: root_r_1
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.003,
    depth=0.04, vertices=32, location=(0.065, 0.02, 0.02))
obj = bpy.context.active_object
obj.name = "root_r_1"


# Rotate: root_r_1 (degrees)
import math
bpy.data.objects["root_r_1"].rotation_euler = (
    math.radians(85),
    math.radians(0),
    math.radians(0)
)


# Create cone: root_r_2
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.003,
    depth=0.04, vertices=32, location=(0.08, 0.04, 0.02))
obj = bpy.context.active_object
obj.name = "root_r_2"


# Rotate: root_r_2 (degrees)
import math
bpy.data.objects["root_r_2"].rotation_euler = (
    math.radians(85),
    math.radians(0),
    math.radians(15)
)


# Create cylinder: leg_vine_l_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.01, depth=0.16,
    vertices=32, location=(-0.062, 0.0, 0.32))
obj = bpy.context.active_object
obj.name = "leg_vine_l_0"


# Rotate: leg_vine_l_0 (degrees)
import math
bpy.data.objects["leg_vine_l_0"].rotation_euler = (
    math.radians(5),
    math.radians(-8),
    math.radians(0)
)


# Create cylinder: leg_vine_l_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.01, depth=0.16,
    vertices=32, location=(-0.044000000000000004, 0.010392304845413265, 0.32))
obj = bpy.context.active_object
obj.name = "leg_vine_l_1"


# Rotate: leg_vine_l_1 (degrees)
import math
bpy.data.objects["leg_vine_l_1"].rotation_euler = (
    math.radians(5),
    math.radians(-8),
    math.radians(0)
)


# Create cylinder: leg_vine_l_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.01, depth=0.16,
    vertices=32, location=(-0.044, -0.010392304845413262, 0.32))
obj = bpy.context.active_object
obj.name = "leg_vine_l_2"


# Rotate: leg_vine_l_2 (degrees)
import math
bpy.data.objects["leg_vine_l_2"].rotation_euler = (
    math.radians(5),
    math.radians(-8),
    math.radians(0)
)


# Create cylinder: shin_vine_l_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.007, depth=0.12,
    vertices=32, location=(-0.06, 0.0, 0.1))
obj = bpy.context.active_object
obj.name = "shin_vine_l_0"


# Rotate: shin_vine_l_0 (degrees)
import math
bpy.data.objects["shin_vine_l_0"].rotation_euler = (
    math.radians(-5),
    math.radians(-5),
    math.radians(0)
)


# Create cylinder: shin_vine_l_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.007, depth=0.12,
    vertices=32, location=(-0.068, 0.01, 0.1))
obj = bpy.context.active_object
obj.name = "shin_vine_l_1"


# Rotate: shin_vine_l_1 (degrees)
import math
bpy.data.objects["shin_vine_l_1"].rotation_euler = (
    math.radians(-5),
    math.radians(-5),
    math.radians(0)
)


# Create cone: root_l_0
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.003,
    depth=0.04, vertices=32, location=(-0.05, 0.0, 0.02))
obj = bpy.context.active_object
obj.name = "root_l_0"


# Rotate: root_l_0 (degrees)
import math
bpy.data.objects["root_l_0"].rotation_euler = (
    math.radians(85),
    math.radians(0),
    math.radians(-15)
)


# Create cone: root_l_1
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.003,
    depth=0.04, vertices=32, location=(-0.065, 0.02, 0.02))
obj = bpy.context.active_object
obj.name = "root_l_1"


# Rotate: root_l_1 (degrees)
import math
bpy.data.objects["root_l_1"].rotation_euler = (
    math.radians(85),
    math.radians(0),
    math.radians(0)
)


# Create cone: root_l_2
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.003,
    depth=0.04, vertices=32, location=(-0.08, 0.04, 0.02))
obj = bpy.context.active_object
obj.name = "root_l_2"


# Rotate: root_l_2 (degrees)
import math
bpy.data.objects["root_l_2"].rotation_euler = (
    math.radians(85),
    math.radians(0),
    math.radians(15)
)


# Create cylinder: tendril_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.005, depth=0.15,
    vertices=32, location=(0.07071067811865477, 0.07071067811865477, 0.45))
obj = bpy.context.active_object
obj.name = "tendril_0"


# Rotate: tendril_0 (degrees)
import math
bpy.data.objects["tendril_0"].rotation_euler = (
    math.radians(-30),
    math.radians(15.707963267948966),
    math.radians(45.0)
)


# Create cylinder: tendril_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.005, depth=0.15,
    vertices=32, location=(-0.07071067811865475, 0.07071067811865477, 0.45))
obj = bpy.context.active_object
obj.name = "tendril_1"


# Rotate: tendril_1 (degrees)
import math
bpy.data.objects["tendril_1"].rotation_euler = (
    math.radians(-15),
    math.radians(47.12388980384689),
    math.radians(135.0)
)


# Create cylinder: tendril_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.005, depth=0.15,
    vertices=32, location=(-0.07071067811865477, -0.07071067811865475, 0.45))
obj = bpy.context.active_object
obj.name = "tendril_2"


# Rotate: tendril_2 (degrees)
import math
bpy.data.objects["tendril_2"].rotation_euler = (
    math.radians(0),
    math.radians(78.53981633974483),
    math.radians(225.0)
)


# Create cylinder: tendril_3
bpy.ops.mesh.primitive_cylinder_add(radius=0.005, depth=0.15,
    vertices=32, location=(0.07071067811865474, -0.07071067811865477, 0.45))
obj = bpy.context.active_object
obj.name = "tendril_3"


# Rotate: tendril_3 (degrees)
import math
bpy.data.objects["tendril_3"].rotation_euler = (
    math.radians(15),
    math.radians(109.95574287564276),
    math.radians(315.0)
)


# Union objects into: vine-horror
# Using boolean EXACT solver for watertight results
base_obj = bpy.data.objects["head_core"]
bpy.context.view_layer.objects.active = base_obj


# Boolean union: adding mouth
tool_obj = bpy.data.objects["mouth"]
mod = base_obj.modifiers.new(name="Boolean_0", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_0")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_socket_r
tool_obj = bpy.data.objects["eye_socket_r"]
mod = base_obj.modifiers.new(name="Boolean_1", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_1")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_socket_l
tool_obj = bpy.data.objects["eye_socket_l"]
mod = base_obj.modifiers.new(name="Boolean_2", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_2")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding rib_0
tool_obj = bpy.data.objects["rib_0"]
mod = base_obj.modifiers.new(name="Boolean_3", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_3")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding rib_1
tool_obj = bpy.data.objects["rib_1"]
mod = base_obj.modifiers.new(name="Boolean_4", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_4")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding rib_2
tool_obj = bpy.data.objects["rib_2"]
mod = base_obj.modifiers.new(name="Boolean_5", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_5")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding rib_3
tool_obj = bpy.data.objects["rib_3"]
mod = base_obj.modifiers.new(name="Boolean_6", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_6")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding rib_4
tool_obj = bpy.data.objects["rib_4"]
mod = base_obj.modifiers.new(name="Boolean_7", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_7")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding rib_5
tool_obj = bpy.data.objects["rib_5"]
mod = base_obj.modifiers.new(name="Boolean_8", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_8")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding rib_6
tool_obj = bpy.data.objects["rib_6"]
mod = base_obj.modifiers.new(name="Boolean_9", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_9")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding rib_7
tool_obj = bpy.data.objects["rib_7"]
mod = base_obj.modifiers.new(name="Boolean_10", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_10")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding ring_0
tool_obj = bpy.data.objects["ring_0"]
mod = base_obj.modifiers.new(name="Boolean_11", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_11")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding ring_1
tool_obj = bpy.data.objects["ring_1"]
mod = base_obj.modifiers.new(name="Boolean_12", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_12")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding ring_2
tool_obj = bpy.data.objects["ring_2"]
mod = base_obj.modifiers.new(name="Boolean_13", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_13")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding ring_3
tool_obj = bpy.data.objects["ring_3"]
mod = base_obj.modifiers.new(name="Boolean_14", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_14")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding face_vine_0
tool_obj = bpy.data.objects["face_vine_0"]
mod = base_obj.modifiers.new(name="Boolean_15", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_15")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding face_vine_1
tool_obj = bpy.data.objects["face_vine_1"]
mod = base_obj.modifiers.new(name="Boolean_16", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_16")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding face_vine_2
tool_obj = bpy.data.objects["face_vine_2"]
mod = base_obj.modifiers.new(name="Boolean_17", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_17")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding face_vine_3
tool_obj = bpy.data.objects["face_vine_3"]
mod = base_obj.modifiers.new(name="Boolean_18", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_18")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding face_vine_4
tool_obj = bpy.data.objects["face_vine_4"]
mod = base_obj.modifiers.new(name="Boolean_19", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_19")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding face_vine_5
tool_obj = bpy.data.objects["face_vine_5"]
mod = base_obj.modifiers.new(name="Boolean_20", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_20")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding shoulder_r
tool_obj = bpy.data.objects["shoulder_r"]
mod = base_obj.modifiers.new(name="Boolean_21", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_21")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_vine_r_0
tool_obj = bpy.data.objects["arm_vine_r_0"]
mod = base_obj.modifiers.new(name="Boolean_22", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_22")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_vine_r_1
tool_obj = bpy.data.objects["arm_vine_r_1"]
mod = base_obj.modifiers.new(name="Boolean_23", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_23")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_vine_r_2
tool_obj = bpy.data.objects["arm_vine_r_2"]
mod = base_obj.modifiers.new(name="Boolean_24", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_24")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding forearm_vine_r_0
tool_obj = bpy.data.objects["forearm_vine_r_0"]
mod = base_obj.modifiers.new(name="Boolean_25", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_25")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding forearm_vine_r_1
tool_obj = bpy.data.objects["forearm_vine_r_1"]
mod = base_obj.modifiers.new(name="Boolean_26", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_26")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding finger_r_0
tool_obj = bpy.data.objects["finger_r_0"]
mod = base_obj.modifiers.new(name="Boolean_27", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_27")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding finger_r_1
tool_obj = bpy.data.objects["finger_r_1"]
mod = base_obj.modifiers.new(name="Boolean_28", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_28")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding finger_r_2
tool_obj = bpy.data.objects["finger_r_2"]
mod = base_obj.modifiers.new(name="Boolean_29", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_29")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding finger_r_3
tool_obj = bpy.data.objects["finger_r_3"]
mod = base_obj.modifiers.new(name="Boolean_30", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_30")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_vine_r_0
tool_obj = bpy.data.objects["leg_vine_r_0"]
mod = base_obj.modifiers.new(name="Boolean_31", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_31")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_vine_r_1
tool_obj = bpy.data.objects["leg_vine_r_1"]
mod = base_obj.modifiers.new(name="Boolean_32", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_32")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_vine_r_2
tool_obj = bpy.data.objects["leg_vine_r_2"]
mod = base_obj.modifiers.new(name="Boolean_33", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_33")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding shin_vine_r_0
tool_obj = bpy.data.objects["shin_vine_r_0"]
mod = base_obj.modifiers.new(name="Boolean_34", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_34")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding shin_vine_r_1
tool_obj = bpy.data.objects["shin_vine_r_1"]
mod = base_obj.modifiers.new(name="Boolean_35", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_35")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding root_r_0
tool_obj = bpy.data.objects["root_r_0"]
mod = base_obj.modifiers.new(name="Boolean_36", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_36")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding root_r_1
tool_obj = bpy.data.objects["root_r_1"]
mod = base_obj.modifiers.new(name="Boolean_37", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_37")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding root_r_2
tool_obj = bpy.data.objects["root_r_2"]
mod = base_obj.modifiers.new(name="Boolean_38", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_38")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding shoulder_l
tool_obj = bpy.data.objects["shoulder_l"]
mod = base_obj.modifiers.new(name="Boolean_39", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_39")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_vine_l_0
tool_obj = bpy.data.objects["arm_vine_l_0"]
mod = base_obj.modifiers.new(name="Boolean_40", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_40")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_vine_l_1
tool_obj = bpy.data.objects["arm_vine_l_1"]
mod = base_obj.modifiers.new(name="Boolean_41", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_41")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_vine_l_2
tool_obj = bpy.data.objects["arm_vine_l_2"]
mod = base_obj.modifiers.new(name="Boolean_42", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_42")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding forearm_vine_l_0
tool_obj = bpy.data.objects["forearm_vine_l_0"]
mod = base_obj.modifiers.new(name="Boolean_43", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_43")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding forearm_vine_l_1
tool_obj = bpy.data.objects["forearm_vine_l_1"]
mod = base_obj.modifiers.new(name="Boolean_44", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_44")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding finger_l_0
tool_obj = bpy.data.objects["finger_l_0"]
mod = base_obj.modifiers.new(name="Boolean_45", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_45")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding finger_l_1
tool_obj = bpy.data.objects["finger_l_1"]
mod = base_obj.modifiers.new(name="Boolean_46", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_46")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding finger_l_2
tool_obj = bpy.data.objects["finger_l_2"]
mod = base_obj.modifiers.new(name="Boolean_47", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_47")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding finger_l_3
tool_obj = bpy.data.objects["finger_l_3"]
mod = base_obj.modifiers.new(name="Boolean_48", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_48")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_vine_l_0
tool_obj = bpy.data.objects["leg_vine_l_0"]
mod = base_obj.modifiers.new(name="Boolean_49", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_49")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_vine_l_1
tool_obj = bpy.data.objects["leg_vine_l_1"]
mod = base_obj.modifiers.new(name="Boolean_50", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_50")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_vine_l_2
tool_obj = bpy.data.objects["leg_vine_l_2"]
mod = base_obj.modifiers.new(name="Boolean_51", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_51")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding shin_vine_l_0
tool_obj = bpy.data.objects["shin_vine_l_0"]
mod = base_obj.modifiers.new(name="Boolean_52", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_52")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding shin_vine_l_1
tool_obj = bpy.data.objects["shin_vine_l_1"]
mod = base_obj.modifiers.new(name="Boolean_53", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_53")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding root_l_0
tool_obj = bpy.data.objects["root_l_0"]
mod = base_obj.modifiers.new(name="Boolean_54", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_54")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding root_l_1
tool_obj = bpy.data.objects["root_l_1"]
mod = base_obj.modifiers.new(name="Boolean_55", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_55")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding root_l_2
tool_obj = bpy.data.objects["root_l_2"]
mod = base_obj.modifiers.new(name="Boolean_56", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_56")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tendril_0
tool_obj = bpy.data.objects["tendril_0"]
mod = base_obj.modifiers.new(name="Boolean_57", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_57")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tendril_1
tool_obj = bpy.data.objects["tendril_1"]
mod = base_obj.modifiers.new(name="Boolean_58", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_58")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tendril_2
tool_obj = bpy.data.objects["tendril_2"]
mod = base_obj.modifiers.new(name="Boolean_59", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_59")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tendril_3
tool_obj = bpy.data.objects["tendril_3"]
mod = base_obj.modifiers.new(name="Boolean_60", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_60")
bpy.data.objects.remove(tool_obj, do_unlink=True)


base_obj.name = "vine-horror"


# Add subdivision surface: vine-horror
obj = bpy.data.objects["vine-horror"]
mod = obj.modifiers.new(name="Subdivision", type='SUBSURF')
mod.levels = 1
mod.render_levels = 2


# Apply all modifiers: vine-horror
obj = bpy.data.objects["vine-horror"]
bpy.context.view_layer.objects.active = obj
for mod in obj.modifiers[:]:
    bpy.ops.object.modifier_apply(modifier=mod.name)


# Create cylinder: vine-horror_base
bpy.ops.mesh.primitive_cylinder_add(radius=0.02, depth=0.003,
    vertices=48, location=(0, 0, 0.0015))
obj = bpy.context.active_object
obj.name = "vine-horror_base"


# Add bevel: vine-horror_base
obj = bpy.data.objects["vine-horror_base"]
mod = obj.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.0004
mod.segments = 2


# Boolean union: vine-horror + vine-horror_base
target_obj = bpy.data.objects["vine-horror"]
tool_obj = bpy.data.objects["vine-horror_base"]
mod = target_obj.modifiers.new(name="Boolean", type='BOOLEAN')
mod.operation = 'UNION'
mod.object = tool_obj
bpy.context.view_layer.objects.active = target_obj
bpy.ops.object.modifier_apply(modifier='Boolean')
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Export to STL (Blender 4.0+ API)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.wm.stl_export(
    filepath="C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/vine-horror.stl",
    export_selected_objects=True,
    global_scale=1.0,
    ascii_format=False  # Binary STL is smaller and faster
)
print("Exported: C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/vine-horror.stl")
