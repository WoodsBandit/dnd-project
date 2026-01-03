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


# Create cube: pelvis
bpy.ops.mesh.primitive_cube_add(size=0.006, location=(0, 0, 0.008))
obj = bpy.context.active_object
obj.name = "pelvis"


# Scale: pelvis
bpy.data.objects["pelvis"].scale = (1.2, 0.6, 0.5)


# Create cylinder: spine_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.001, depth=0.003,
    vertices=8, location=(0, 0, 0.012))
obj = bpy.context.active_object
obj.name = "spine_0"


# Create cylinder: spine_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.001, depth=0.003,
    vertices=8, location=(0, 0, 0.015))
obj = bpy.context.active_object
obj.name = "spine_1"


# Create cylinder: spine_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.001, depth=0.003,
    vertices=8, location=(0, 0, 0.018000000000000002))
obj = bpy.context.active_object
obj.name = "spine_2"


# Create cylinder: spine_3
bpy.ops.mesh.primitive_cylinder_add(radius=0.001, depth=0.003,
    vertices=8, location=(0, 0, 0.021))
obj = bpy.context.active_object
obj.name = "spine_3"


# Create cube: ribcage
bpy.ops.mesh.primitive_cube_add(size=0.008, location=(0, 0, 0.022))
obj = bpy.context.active_object
obj.name = "ribcage"


# Scale: ribcage
bpy.data.objects["ribcage"].scale = (1.0, 0.5, 0.8)


# Create cylinder: rib_l_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.0005, depth=0.006,
    vertices=6, location=(-0.003, 0.001, 0.019))
obj = bpy.context.active_object
obj.name = "rib_l_0"


# Rotate: rib_l_0 (degrees)
import math
bpy.data.objects["rib_l_0"].rotation_euler = (
    math.radians(0),
    math.radians(-70),
    math.radians(0)
)


# Create cylinder: rib_r_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.0005, depth=0.006,
    vertices=6, location=(0.003, 0.001, 0.019))
obj = bpy.context.active_object
obj.name = "rib_r_0"


# Rotate: rib_r_0 (degrees)
import math
bpy.data.objects["rib_r_0"].rotation_euler = (
    math.radians(0),
    math.radians(70),
    math.radians(0)
)


# Create cylinder: rib_l_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.0005, depth=0.006,
    vertices=6, location=(-0.003, 0.001, 0.022))
obj = bpy.context.active_object
obj.name = "rib_l_1"


# Rotate: rib_l_1 (degrees)
import math
bpy.data.objects["rib_l_1"].rotation_euler = (
    math.radians(0),
    math.radians(-70),
    math.radians(0)
)


# Create cylinder: rib_r_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.0005, depth=0.006,
    vertices=6, location=(0.003, 0.001, 0.022))
obj = bpy.context.active_object
obj.name = "rib_r_1"


# Rotate: rib_r_1 (degrees)
import math
bpy.data.objects["rib_r_1"].rotation_euler = (
    math.radians(0),
    math.radians(70),
    math.radians(0)
)


# Create cylinder: rib_l_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.0005, depth=0.006,
    vertices=6, location=(-0.003, 0.001, 0.025))
obj = bpy.context.active_object
obj.name = "rib_l_2"


# Rotate: rib_l_2 (degrees)
import math
bpy.data.objects["rib_l_2"].rotation_euler = (
    math.radians(0),
    math.radians(-70),
    math.radians(0)
)


# Create cylinder: rib_r_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.0005, depth=0.006,
    vertices=6, location=(0.003, 0.001, 0.025))
obj = bpy.context.active_object
obj.name = "rib_r_2"


# Rotate: rib_r_2 (degrees)
import math
bpy.data.objects["rib_r_2"].rotation_euler = (
    math.radians(0),
    math.radians(70),
    math.radians(0)
)


# Create cylinder: clavicle_l
bpy.ops.mesh.primitive_cylinder_add(radius=0.0006, depth=0.005,
    vertices=6, location=(-0.003, 0, 0.027))
obj = bpy.context.active_object
obj.name = "clavicle_l"


# Rotate: clavicle_l (degrees)
import math
bpy.data.objects["clavicle_l"].rotation_euler = (
    math.radians(0),
    math.radians(90),
    math.radians(0)
)


# Create cylinder: clavicle_r
bpy.ops.mesh.primitive_cylinder_add(radius=0.0006, depth=0.005,
    vertices=6, location=(0.003, 0, 0.027))
obj = bpy.context.active_object
obj.name = "clavicle_r"


# Rotate: clavicle_r (degrees)
import math
bpy.data.objects["clavicle_r"].rotation_euler = (
    math.radians(0),
    math.radians(90),
    math.radians(0)
)


# Create cylinder: upper_arm_l
bpy.ops.mesh.primitive_cylinder_add(radius=0.001, depth=0.008,
    vertices=8, location=(-0.006, 0, 0.022))
obj = bpy.context.active_object
obj.name = "upper_arm_l"


# Create cylinder: lower_arm_l
bpy.ops.mesh.primitive_cylinder_add(radius=0.0008, depth=0.007,
    vertices=8, location=(-0.006, 0, 0.013))
obj = bpy.context.active_object
obj.name = "lower_arm_l"


# Create sphere: hand_l
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0015, segments=8,
    ring_count=6, location=(-0.006, 0, 0.008))
obj = bpy.context.active_object
obj.name = "hand_l"


# Create cylinder: upper_arm_r
bpy.ops.mesh.primitive_cylinder_add(radius=0.001, depth=0.008,
    vertices=8, location=(0.006, 0, 0.022))
obj = bpy.context.active_object
obj.name = "upper_arm_r"


# Rotate: upper_arm_r (degrees)
import math
bpy.data.objects["upper_arm_r"].rotation_euler = (
    math.radians(30),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: lower_arm_r
bpy.ops.mesh.primitive_cylinder_add(radius=0.0008, depth=0.007,
    vertices=8, location=(0.006, 0.005, 0.016))
obj = bpy.context.active_object
obj.name = "lower_arm_r"


# Rotate: lower_arm_r (degrees)
import math
bpy.data.objects["lower_arm_r"].rotation_euler = (
    math.radians(60),
    math.radians(0),
    math.radians(0)
)


# Create sphere: hand_r
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0015, segments=8,
    ring_count=6, location=(0.006, 0.01, 0.012))
obj = bpy.context.active_object
obj.name = "hand_r"


# Create sphere: skull
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.004, segments=16,
    ring_count=12, location=(0, 0, 0.033))
obj = bpy.context.active_object
obj.name = "skull"


# Scale: skull
bpy.data.objects["skull"].scale = (0.9, 1.0, 1.1)


# Create cube: jaw
bpy.ops.mesh.primitive_cube_add(size=0.004, location=(0, 0.002, 0.028))
obj = bpy.context.active_object
obj.name = "jaw"


# Scale: jaw
bpy.data.objects["jaw"].scale = (0.7, 0.5, 0.3)


# Rotate: jaw (degrees)
import math
bpy.data.objects["jaw"].rotation_euler = (
    math.radians(-10),
    math.radians(0),
    math.radians(0)
)


# Create sphere: eye_socket_l
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.001, segments=8,
    ring_count=6, location=(-0.0015, 0.003, 0.033))
obj = bpy.context.active_object
obj.name = "eye_socket_l"


# Create sphere: eye_socket_r
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.001, segments=8,
    ring_count=6, location=(0.0015, 0.003, 0.033))
obj = bpy.context.active_object
obj.name = "eye_socket_r"


# Create cylinder: femur_l
bpy.ops.mesh.primitive_cylinder_add(radius=0.0012, depth=0.009,
    vertices=8, location=(-0.003, 0, 0.005))
obj = bpy.context.active_object
obj.name = "femur_l"


# Create cylinder: tibia_l
bpy.ops.mesh.primitive_cylinder_add(radius=0.001, depth=0.008,
    vertices=8, location=(-0.003, 0, -0.003))
obj = bpy.context.active_object
obj.name = "tibia_l"


# Create cube: foot_l
bpy.ops.mesh.primitive_cube_add(size=0.003, location=(-0.003, 0.002, -0.006))
obj = bpy.context.active_object
obj.name = "foot_l"


# Scale: foot_l
bpy.data.objects["foot_l"].scale = (0.5, 1.2, 0.3)


# Create cylinder: femur_r
bpy.ops.mesh.primitive_cylinder_add(radius=0.0012, depth=0.009,
    vertices=8, location=(0.003, 0, 0.005))
obj = bpy.context.active_object
obj.name = "femur_r"


# Create cylinder: tibia_r
bpy.ops.mesh.primitive_cylinder_add(radius=0.001, depth=0.008,
    vertices=8, location=(0.003, 0, -0.003))
obj = bpy.context.active_object
obj.name = "tibia_r"


# Create cube: foot_r
bpy.ops.mesh.primitive_cube_add(size=0.003, location=(0.003, 0.002, -0.006))
obj = bpy.context.active_object
obj.name = "foot_r"


# Scale: foot_r
bpy.data.objects["foot_r"].scale = (0.5, 1.2, 0.3)


# Create cube: blade
bpy.ops.mesh.primitive_cube_add(size=0.002, location=(0.006, 0.015, 0.018))
obj = bpy.context.active_object
obj.name = "blade"


# Scale: blade
bpy.data.objects["blade"].scale = (0.2, 0.15, 6.0)


# Rotate: blade (degrees)
import math
bpy.data.objects["blade"].rotation_euler = (
    math.radians(30),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: handle
bpy.ops.mesh.primitive_cylinder_add(radius=0.0008, depth=0.006,
    vertices=8, location=(0.006, 0.011, 0.01))
obj = bpy.context.active_object
obj.name = "handle"


# Rotate: handle (degrees)
import math
bpy.data.objects["handle"].rotation_euler = (
    math.radians(60),
    math.radians(0),
    math.radians(0)
)


# Create cube: crossguard
bpy.ops.mesh.primitive_cube_add(size=0.002, location=(0.006, 0.012, 0.013))
obj = bpy.context.active_object
obj.name = "crossguard"


# Scale: crossguard
bpy.data.objects["crossguard"].scale = (1.5, 0.3, 0.3)


# Rotate: crossguard (degrees)
import math
bpy.data.objects["crossguard"].rotation_euler = (
    math.radians(60),
    math.radians(0),
    math.radians(0)
)


# Union objects into: skeleton-simple
# Using boolean EXACT solver for watertight results
base_obj = bpy.data.objects["base"]
bpy.context.view_layer.objects.active = base_obj


# Boolean union: adding pelvis
tool_obj = bpy.data.objects["pelvis"]
mod = base_obj.modifiers.new(name="Boolean_0", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_0")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding ribcage
tool_obj = bpy.data.objects["ribcage"]
mod = base_obj.modifiers.new(name="Boolean_1", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_1")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding skull
tool_obj = bpy.data.objects["skull"]
mod = base_obj.modifiers.new(name="Boolean_2", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_2")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding jaw
tool_obj = bpy.data.objects["jaw"]
mod = base_obj.modifiers.new(name="Boolean_3", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_3")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding clavicle_l
tool_obj = bpy.data.objects["clavicle_l"]
mod = base_obj.modifiers.new(name="Boolean_4", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_4")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding clavicle_r
tool_obj = bpy.data.objects["clavicle_r"]
mod = base_obj.modifiers.new(name="Boolean_5", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_5")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding upper_arm_l
tool_obj = bpy.data.objects["upper_arm_l"]
mod = base_obj.modifiers.new(name="Boolean_6", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_6")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding lower_arm_l
tool_obj = bpy.data.objects["lower_arm_l"]
mod = base_obj.modifiers.new(name="Boolean_7", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_7")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding hand_l
tool_obj = bpy.data.objects["hand_l"]
mod = base_obj.modifiers.new(name="Boolean_8", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_8")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding upper_arm_r
tool_obj = bpy.data.objects["upper_arm_r"]
mod = base_obj.modifiers.new(name="Boolean_9", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_9")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding lower_arm_r
tool_obj = bpy.data.objects["lower_arm_r"]
mod = base_obj.modifiers.new(name="Boolean_10", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_10")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding hand_r
tool_obj = bpy.data.objects["hand_r"]
mod = base_obj.modifiers.new(name="Boolean_11", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_11")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding femur_l
tool_obj = bpy.data.objects["femur_l"]
mod = base_obj.modifiers.new(name="Boolean_12", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_12")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tibia_l
tool_obj = bpy.data.objects["tibia_l"]
mod = base_obj.modifiers.new(name="Boolean_13", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_13")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding foot_l
tool_obj = bpy.data.objects["foot_l"]
mod = base_obj.modifiers.new(name="Boolean_14", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_14")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding femur_r
tool_obj = bpy.data.objects["femur_r"]
mod = base_obj.modifiers.new(name="Boolean_15", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_15")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tibia_r
tool_obj = bpy.data.objects["tibia_r"]
mod = base_obj.modifiers.new(name="Boolean_16", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_16")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding foot_r
tool_obj = bpy.data.objects["foot_r"]
mod = base_obj.modifiers.new(name="Boolean_17", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_17")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_socket_l
tool_obj = bpy.data.objects["eye_socket_l"]
mod = base_obj.modifiers.new(name="Boolean_18", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_18")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_socket_r
tool_obj = bpy.data.objects["eye_socket_r"]
mod = base_obj.modifiers.new(name="Boolean_19", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_19")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding blade
tool_obj = bpy.data.objects["blade"]
mod = base_obj.modifiers.new(name="Boolean_20", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_20")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding handle
tool_obj = bpy.data.objects["handle"]
mod = base_obj.modifiers.new(name="Boolean_21", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_21")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding crossguard
tool_obj = bpy.data.objects["crossguard"]
mod = base_obj.modifiers.new(name="Boolean_22", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_22")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding spine_0
tool_obj = bpy.data.objects["spine_0"]
mod = base_obj.modifiers.new(name="Boolean_23", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_23")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding spine_1
tool_obj = bpy.data.objects["spine_1"]
mod = base_obj.modifiers.new(name="Boolean_24", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_24")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding spine_2
tool_obj = bpy.data.objects["spine_2"]
mod = base_obj.modifiers.new(name="Boolean_25", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_25")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding spine_3
tool_obj = bpy.data.objects["spine_3"]
mod = base_obj.modifiers.new(name="Boolean_26", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_26")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding rib_l_0
tool_obj = bpy.data.objects["rib_l_0"]
mod = base_obj.modifiers.new(name="Boolean_27", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_27")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding rib_r_0
tool_obj = bpy.data.objects["rib_r_0"]
mod = base_obj.modifiers.new(name="Boolean_28", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_28")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding rib_l_1
tool_obj = bpy.data.objects["rib_l_1"]
mod = base_obj.modifiers.new(name="Boolean_29", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_29")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding rib_r_1
tool_obj = bpy.data.objects["rib_r_1"]
mod = base_obj.modifiers.new(name="Boolean_30", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_30")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding rib_l_2
tool_obj = bpy.data.objects["rib_l_2"]
mod = base_obj.modifiers.new(name="Boolean_31", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_31")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding rib_r_2
tool_obj = bpy.data.objects["rib_r_2"]
mod = base_obj.modifiers.new(name="Boolean_32", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_32")
bpy.data.objects.remove(tool_obj, do_unlink=True)


base_obj.name = "skeleton-simple"


# Clean mesh for printing: skeleton-simple
obj = bpy.data.objects["skeleton-simple"]
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
print(f"Mesh cleaned: skeleton-simple")


# Add subdivision surface: skeleton-simple
obj = bpy.data.objects["skeleton-simple"]
mod = obj.modifiers.new(name="Subdivision", type='SUBSURF')
mod.levels = 2
mod.render_levels = 2


# Apply all modifiers: skeleton-simple
obj = bpy.data.objects["skeleton-simple"]
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
    filepath="C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/skeleton-simple.stl",
    export_selected_objects=True,
    global_scale=1.0,
    ascii_format=False  # Binary STL is smaller and faster
)
print("Exported: C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/skeleton-simple.stl")
