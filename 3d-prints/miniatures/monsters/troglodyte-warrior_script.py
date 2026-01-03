import bpy
import bmesh
import math
from mathutils import Vector, Matrix

# Clear default scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)


# Create sphere: torso
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.12, segments=32,
    ring_count=16, location=(0, 0.02, 0.55))
obj = bpy.context.active_object
obj.name = "torso"


# Scale: torso
bpy.data.objects["torso"].scale = (0.9, 0.7, 1.1)


# Create sphere: back_hunch
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.08, segments=32,
    ring_count=16, location=(0, -0.06, 0.62))
obj = bpy.context.active_object
obj.name = "back_hunch"


# Scale: back_hunch
bpy.data.objects["back_hunch"].scale = (0.8, 0.9, 0.7)


# Create sphere: belly
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.07, segments=32,
    ring_count=16, location=(0, 0.05, 0.45))
obj = bpy.context.active_object
obj.name = "belly"


# Scale: belly
bpy.data.objects["belly"].scale = (0.9, 0.8, 0.8)


# Create sphere: head
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.065, segments=32,
    ring_count=16, location=(0, 0.08, 0.72))
obj = bpy.context.active_object
obj.name = "head"


# Scale: head
bpy.data.objects["head"].scale = (0.85, 1.0, 0.9)


# Create cone: snout
bpy.ops.mesh.primitive_cone_add(radius1=0.04, radius2=0.02,
    depth=0.06, vertices=32, location=(0, 0.14, 0.7))
obj = bpy.context.active_object
obj.name = "snout"


# Rotate: snout (degrees)
import math
bpy.data.objects["snout"].rotation_euler = (
    math.radians(80),
    math.radians(0),
    math.radians(0)
)


# Create cylinder: brow_r
bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=0.03,
    vertices=32, location=(0.025, 0.1, 0.76))
obj = bpy.context.active_object
obj.name = "brow_r"


# Rotate: brow_r (degrees)
import math
bpy.data.objects["brow_r"].rotation_euler = (
    math.radians(70),
    math.radians(20),
    math.radians(0)
)


# Create cylinder: brow_l
bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=0.03,
    vertices=32, location=(-0.025, 0.1, 0.76))
obj = bpy.context.active_object
obj.name = "brow_l"


# Rotate: brow_l (degrees)
import math
bpy.data.objects["brow_l"].rotation_euler = (
    math.radians(70),
    math.radians(-20),
    math.radians(0)
)


# Create sphere: eye_r
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012, segments=32,
    ring_count=16, location=(0.03, 0.11, 0.74))
obj = bpy.context.active_object
obj.name = "eye_r"


# Create sphere: eye_l
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012, segments=32,
    ring_count=16, location=(-0.03, 0.11, 0.74))
obj = bpy.context.active_object
obj.name = "eye_l"


# Create cylinder: arm_r_up
bpy.ops.mesh.primitive_cylinder_add(radius=0.025, depth=0.12,
    vertices=32, location=(0.14, 0, 0.58))
obj = bpy.context.active_object
obj.name = "arm_r_up"


# Rotate: arm_r_up (degrees)
import math
bpy.data.objects["arm_r_up"].rotation_euler = (
    math.radians(-30),
    math.radians(60),
    math.radians(30)
)


# Create cylinder: arm_r_low
bpy.ops.mesh.primitive_cylinder_add(radius=0.02, depth=0.1,
    vertices=32, location=(0.22, 0.02, 0.68))
obj = bpy.context.active_object
obj.name = "arm_r_low"


# Rotate: arm_r_low (degrees)
import math
bpy.data.objects["arm_r_low"].rotation_euler = (
    math.radians(-60),
    math.radians(40),
    math.radians(0)
)


# Create cylinder: arm_l_up
bpy.ops.mesh.primitive_cylinder_add(radius=0.025, depth=0.12,
    vertices=32, location=(-0.14, 0.02, 0.55))
obj = bpy.context.active_object
obj.name = "arm_l_up"


# Rotate: arm_l_up (degrees)
import math
bpy.data.objects["arm_l_up"].rotation_euler = (
    math.radians(20),
    math.radians(-50),
    math.radians(0)
)


# Create cylinder: arm_l_low
bpy.ops.mesh.primitive_cylinder_add(radius=0.02, depth=0.1,
    vertices=32, location=(-0.22, 0.06, 0.45))
obj = bpy.context.active_object
obj.name = "arm_l_low"


# Rotate: arm_l_low (degrees)
import math
bpy.data.objects["arm_l_low"].rotation_euler = (
    math.radians(40),
    math.radians(-30),
    math.radians(0)
)


# Create cone: claw_r_0
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.025, vertices=32, location=(0.25, 0.06, 0.72))
obj = bpy.context.active_object
obj.name = "claw_r_0"


# Rotate: claw_r_0 (degrees)
import math
bpy.data.objects["claw_r_0"].rotation_euler = (
    math.radians(30),
    math.radians(15),
    math.radians(0)
)


# Create cone: claw_r_1
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.025, vertices=32, location=(0.26, 0.06, 0.71))
obj = bpy.context.active_object
obj.name = "claw_r_1"


# Rotate: claw_r_1 (degrees)
import math
bpy.data.objects["claw_r_1"].rotation_euler = (
    math.radians(30),
    math.radians(15),
    math.radians(0)
)


# Create cone: claw_r_2
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.025, vertices=32, location=(0.27, 0.06, 0.7))
obj = bpy.context.active_object
obj.name = "claw_r_2"


# Rotate: claw_r_2 (degrees)
import math
bpy.data.objects["claw_r_2"].rotation_euler = (
    math.radians(30),
    math.radians(15),
    math.radians(0)
)


# Create cone: claw_l_0
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.025, vertices=32, location=(-0.26, 0.1, 0.38))
obj = bpy.context.active_object
obj.name = "claw_l_0"


# Rotate: claw_l_0 (degrees)
import math
bpy.data.objects["claw_l_0"].rotation_euler = (
    math.radians(30),
    math.radians(-15),
    math.radians(0)
)


# Create cone: claw_l_1
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.025, vertices=32, location=(-0.27, 0.1, 0.37))
obj = bpy.context.active_object
obj.name = "claw_l_1"


# Rotate: claw_l_1 (degrees)
import math
bpy.data.objects["claw_l_1"].rotation_euler = (
    math.radians(30),
    math.radians(-15),
    math.radians(0)
)


# Create cone: claw_l_2
bpy.ops.mesh.primitive_cone_add(radius1=0.006, radius2=0.002,
    depth=0.025, vertices=32, location=(-0.28, 0.1, 0.36))
obj = bpy.context.active_object
obj.name = "claw_l_2"


# Rotate: claw_l_2 (degrees)
import math
bpy.data.objects["claw_l_2"].rotation_euler = (
    math.radians(30),
    math.radians(-15),
    math.radians(0)
)


# Create cylinder: club_handle
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.15,
    vertices=32, location=(0.28, 0.04, 0.78))
obj = bpy.context.active_object
obj.name = "club_handle"


# Rotate: club_handle (degrees)
import math
bpy.data.objects["club_handle"].rotation_euler = (
    math.radians(-50),
    math.radians(30),
    math.radians(0)
)


# Create sphere: club_head
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.035, segments=32,
    ring_count=16, location=(0.32, 0.06, 0.9))
obj = bpy.context.active_object
obj.name = "club_head"


# Scale: club_head
bpy.data.objects["club_head"].scale = (0.8, 0.8, 1.2)


# Create cone: club_spike_0
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.002,
    depth=0.02, vertices=32, location=(0.34500000000000003, 0.06, 0.9))
obj = bpy.context.active_object
obj.name = "club_spike_0"


# Rotate: club_spike_0 (degrees)
import math
bpy.data.objects["club_spike_0"].rotation_euler = (
    math.radians(0),
    math.radians(90),
    math.radians(0)
)


# Create cone: club_spike_1
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.002,
    depth=0.02, vertices=32, location=(0.32, 0.08499999999999999, 0.9))
obj = bpy.context.active_object
obj.name = "club_spike_1"


# Rotate: club_spike_1 (degrees)
import math
bpy.data.objects["club_spike_1"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(0)
)


# Create cone: club_spike_2
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.002,
    depth=0.02, vertices=32, location=(0.295, 0.06, 0.9))
obj = bpy.context.active_object
obj.name = "club_spike_2"


# Rotate: club_spike_2 (degrees)
import math
bpy.data.objects["club_spike_2"].rotation_euler = (
    math.radians(0),
    math.radians(-90),
    math.radians(0)
)


# Create cone: club_spike_3
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.002,
    depth=0.02, vertices=32, location=(0.32, 0.034999999999999996, 0.9))
obj = bpy.context.active_object
obj.name = "club_spike_3"


# Rotate: club_spike_3 (degrees)
import math
bpy.data.objects["club_spike_3"].rotation_euler = (
    math.radians(0),
    math.radians(-180),
    math.radians(0)
)


# Create cylinder: leg_r_up
bpy.ops.mesh.primitive_cylinder_add(radius=0.035, depth=0.15,
    vertices=32, location=(0.06, 0, 0.32))
obj = bpy.context.active_object
obj.name = "leg_r_up"


# Rotate: leg_r_up (degrees)
import math
bpy.data.objects["leg_r_up"].rotation_euler = (
    math.radians(10),
    math.radians(8),
    math.radians(0)
)


# Create cylinder: leg_l_up
bpy.ops.mesh.primitive_cylinder_add(radius=0.035, depth=0.15,
    vertices=32, location=(-0.06, 0, 0.32))
obj = bpy.context.active_object
obj.name = "leg_l_up"


# Rotate: leg_l_up (degrees)
import math
bpy.data.objects["leg_l_up"].rotation_euler = (
    math.radians(10),
    math.radians(-8),
    math.radians(0)
)


# Create cylinder: leg_r_low
bpy.ops.mesh.primitive_cylinder_add(radius=0.025, depth=0.12,
    vertices=32, location=(0.07, 0.02, 0.12))
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
bpy.ops.mesh.primitive_cylinder_add(radius=0.025, depth=0.12,
    vertices=32, location=(-0.07, 0.02, 0.12))
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
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.025, segments=32,
    ring_count=16, location=(0.07, 0.04, 0.02))
obj = bpy.context.active_object
obj.name = "foot_r"


# Scale: foot_r
bpy.data.objects["foot_r"].scale = (0.7, 1.3, 0.4)


# Create sphere: foot_l
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.025, segments=32,
    ring_count=16, location=(-0.07, 0.04, 0.02))
obj = bpy.context.active_object
obj.name = "foot_l"


# Scale: foot_l
bpy.data.objects["foot_l"].scale = (0.7, 1.3, 0.4)


# Create cone: tail
bpy.ops.mesh.primitive_cone_add(radius1=0.03, radius2=0.01,
    depth=0.15, vertices=32, location=(0, -0.12, 0.35))
obj = bpy.context.active_object
obj.name = "tail"


# Rotate: tail (degrees)
import math
bpy.data.objects["tail"].rotation_euler = (
    math.radians(120),
    math.radians(0),
    math.radians(0)
)


# Union objects into: troglodyte-warrior
# Using boolean EXACT solver for watertight results
base_obj = bpy.data.objects["torso"]
bpy.context.view_layer.objects.active = base_obj


# Boolean union: adding back_hunch
tool_obj = bpy.data.objects["back_hunch"]
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


# Boolean union: adding arm_r_up
tool_obj = bpy.data.objects["arm_r_up"]
mod = base_obj.modifiers.new(name="Boolean_8", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_8")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_r_low
tool_obj = bpy.data.objects["arm_r_low"]
mod = base_obj.modifiers.new(name="Boolean_9", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_9")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_l_up
tool_obj = bpy.data.objects["arm_l_up"]
mod = base_obj.modifiers.new(name="Boolean_10", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_10")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_l_low
tool_obj = bpy.data.objects["arm_l_low"]
mod = base_obj.modifiers.new(name="Boolean_11", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_11")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding club_handle
tool_obj = bpy.data.objects["club_handle"]
mod = base_obj.modifiers.new(name="Boolean_12", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_12")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding club_head
tool_obj = bpy.data.objects["club_head"]
mod = base_obj.modifiers.new(name="Boolean_13", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_13")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_r_up
tool_obj = bpy.data.objects["leg_r_up"]
mod = base_obj.modifiers.new(name="Boolean_14", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_14")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_l_up
tool_obj = bpy.data.objects["leg_l_up"]
mod = base_obj.modifiers.new(name="Boolean_15", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_15")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_r_low
tool_obj = bpy.data.objects["leg_r_low"]
mod = base_obj.modifiers.new(name="Boolean_16", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_16")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_l_low
tool_obj = bpy.data.objects["leg_l_low"]
mod = base_obj.modifiers.new(name="Boolean_17", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_17")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding foot_r
tool_obj = bpy.data.objects["foot_r"]
mod = base_obj.modifiers.new(name="Boolean_18", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_18")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding foot_l
tool_obj = bpy.data.objects["foot_l"]
mod = base_obj.modifiers.new(name="Boolean_19", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_19")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tail
tool_obj = bpy.data.objects["tail"]
mod = base_obj.modifiers.new(name="Boolean_20", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_20")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_r_0
tool_obj = bpy.data.objects["claw_r_0"]
mod = base_obj.modifiers.new(name="Boolean_21", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_21")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_r_1
tool_obj = bpy.data.objects["claw_r_1"]
mod = base_obj.modifiers.new(name="Boolean_22", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_22")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_r_2
tool_obj = bpy.data.objects["claw_r_2"]
mod = base_obj.modifiers.new(name="Boolean_23", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_23")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_l_0
tool_obj = bpy.data.objects["claw_l_0"]
mod = base_obj.modifiers.new(name="Boolean_24", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_24")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_l_1
tool_obj = bpy.data.objects["claw_l_1"]
mod = base_obj.modifiers.new(name="Boolean_25", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_25")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_l_2
tool_obj = bpy.data.objects["claw_l_2"]
mod = base_obj.modifiers.new(name="Boolean_26", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_26")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding club_spike_0
tool_obj = bpy.data.objects["club_spike_0"]
mod = base_obj.modifiers.new(name="Boolean_27", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_27")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding club_spike_1
tool_obj = bpy.data.objects["club_spike_1"]
mod = base_obj.modifiers.new(name="Boolean_28", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_28")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding club_spike_2
tool_obj = bpy.data.objects["club_spike_2"]
mod = base_obj.modifiers.new(name="Boolean_29", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_29")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding club_spike_3
tool_obj = bpy.data.objects["club_spike_3"]
mod = base_obj.modifiers.new(name="Boolean_30", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_30")
bpy.data.objects.remove(tool_obj, do_unlink=True)


base_obj.name = "troglodyte-warrior"


# Add subdivision surface: troglodyte-warrior
obj = bpy.data.objects["troglodyte-warrior"]
mod = obj.modifiers.new(name="Subdivision", type='SUBSURF')
mod.levels = 1
mod.render_levels = 2


# Add displacement: troglodyte-warrior
obj = bpy.data.objects["troglodyte-warrior"]
tex = bpy.data.textures.new("troglodyte-warrior_displace_tex", type='VORONOI')
mod = obj.modifiers.new(name="Displace", type='DISPLACE')
mod.texture = tex
mod.strength = 0.003


# Apply all modifiers: troglodyte-warrior
obj = bpy.data.objects["troglodyte-warrior"]
bpy.context.view_layer.objects.active = obj
for mod in obj.modifiers[:]:
    bpy.ops.object.modifier_apply(modifier=mod.name)


# Create cylinder: troglodyte-warrior_base
bpy.ops.mesh.primitive_cylinder_add(radius=0.0125, depth=0.003,
    vertices=48, location=(0, 0, 0.0015))
obj = bpy.context.active_object
obj.name = "troglodyte-warrior_base"


# Add bevel: troglodyte-warrior_base
obj = bpy.data.objects["troglodyte-warrior_base"]
mod = obj.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.0004
mod.segments = 2


# Boolean union: troglodyte-warrior + troglodyte-warrior_base
target_obj = bpy.data.objects["troglodyte-warrior"]
tool_obj = bpy.data.objects["troglodyte-warrior_base"]
mod = target_obj.modifiers.new(name="Boolean", type='BOOLEAN')
mod.operation = 'UNION'
mod.object = tool_obj
bpy.context.view_layer.objects.active = target_obj
bpy.ops.object.modifier_apply(modifier='Boolean')
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Export to STL (Blender 4.0+ API)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.wm.stl_export(
    filepath="C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/troglodyte-warrior.stl",
    export_selected_objects=True,
    global_scale=1.0,
    ascii_format=False  # Binary STL is smaller and faster
)
print("Exported: C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/troglodyte-warrior.stl")
