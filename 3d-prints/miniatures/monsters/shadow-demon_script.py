import bpy
import bmesh
import math
from mathutils import Vector, Matrix

# Clear default scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)


# Create metaball sphere: shadow_meta
bpy.ops.object.metaball_add(type='BALL', radius=0.06, location=(0, 0, 0.45))
obj = bpy.context.active_object
obj.name = "shadow_meta"


# Add metaball element to: shadow_meta
mball = bpy.data.metaballs[bpy.data.objects["shadow_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.055
elem.co = (0, 0, 0.55)


# Add metaball element to: shadow_meta
mball = bpy.data.metaballs[bpy.data.objects["shadow_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.045
elem.co = (0, 0.02, 0.65)


# Add metaball element to: shadow_meta
mball = bpy.data.metaballs[bpy.data.objects["shadow_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.04
elem.co = (0, 0.01, 0.72)


# Add metaball element to: shadow_meta
mball = bpy.data.metaballs[bpy.data.objects["shadow_meta"].data.name]
elem = mball.elements.new(type='BALL')
elem.radius = 0.05
elem.co = (0, -0.02, 0.35)


# Add metaball element to: shadow_meta
mball = bpy.data.metaballs[bpy.data.objects["shadow_meta"].data.name]
elem = mball.elements.new(type='ELLIPSOID')
elem.radius = 0.04
elem.co = (0, 0, 0.25)


# Add metaball element to: shadow_meta
mball = bpy.data.metaballs[bpy.data.objects["shadow_meta"].data.name]
elem = mball.elements.new(type='ELLIPSOID')
elem.radius = 0.035
elem.co = (0.02, 0.02, 0.15)


# Add metaball element to: shadow_meta
mball = bpy.data.metaballs[bpy.data.objects["shadow_meta"].data.name]
elem = mball.elements.new(type='ELLIPSOID')
elem.radius = 0.03
elem.co = (-0.02, -0.02, 0.1)


# Convert metaball to mesh: shadow_meta
obj = bpy.data.objects["shadow_meta"]
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
bpy.ops.object.convert(target='MESH')

bpy.context.active_object.name = "shadow_body"

# Create sphere: head
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.045, segments=32,
    ring_count=16, location=(0, 0.02, 0.78))
obj = bpy.context.active_object
obj.name = "head"


# Scale: head
bpy.data.objects["head"].scale = (0.9, 0.85, 1.1)


# Create sphere: eye_r
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012, segments=32,
    ring_count=16, location=(0.018, 0.04, 0.8))
obj = bpy.context.active_object
obj.name = "eye_r"


# Scale: eye_r
bpy.data.objects["eye_r"].scale = (0.6, 0.8, 1.0)


# Create sphere: eye_l
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012, segments=32,
    ring_count=16, location=(-0.018, 0.04, 0.8))
obj = bpy.context.active_object
obj.name = "eye_l"


# Scale: eye_l
bpy.data.objects["eye_l"].scale = (0.6, 0.8, 1.0)


# Create sphere: mouth
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.02, segments=32,
    ring_count=16, location=(0, 0.04, 0.74))
obj = bpy.context.active_object
obj.name = "mouth"


# Scale: mouth
bpy.data.objects["mouth"].scale = (1.2, 0.6, 0.8)


# Create cone: horn_r
bpy.ops.mesh.primitive_cone_add(radius1=0.012, radius2=0.003,
    depth=0.06, vertices=32, location=(0.03, -0.01, 0.85))
obj = bpy.context.active_object
obj.name = "horn_r"


# Rotate: horn_r (degrees)
import math
bpy.data.objects["horn_r"].rotation_euler = (
    math.radians(-30),
    math.radians(25),
    math.radians(15)
)


# Create cone: horn_l
bpy.ops.mesh.primitive_cone_add(radius1=0.012, radius2=0.003,
    depth=0.06, vertices=32, location=(-0.03, -0.01, 0.85))
obj = bpy.context.active_object
obj.name = "horn_l"


# Rotate: horn_l (degrees)
import math
bpy.data.objects["horn_l"].rotation_euler = (
    math.radians(-30),
    math.radians(-25),
    math.radians(-15)
)


# Create cylinder: arm_upper_r
bpy.ops.mesh.primitive_cylinder_add(radius=0.018, depth=0.12,
    vertices=32, location=(0.08, 0, 0.6))
obj = bpy.context.active_object
obj.name = "arm_upper_r"


# Rotate: arm_upper_r (degrees)
import math
bpy.data.objects["arm_upper_r"].rotation_euler = (
    math.radians(20),
    math.radians(60),
    math.radians(20)
)


# Create cone: arm_lower_r
bpy.ops.mesh.primitive_cone_add(radius1=0.015, radius2=0.008,
    depth=0.1, vertices=32, location=(0.16, 0.04, 0.5))
obj = bpy.context.active_object
obj.name = "arm_lower_r"


# Rotate: arm_lower_r (degrees)
import math
bpy.data.objects["arm_lower_r"].rotation_euler = (
    math.radians(40),
    math.radians(45),
    math.radians(0)
)


# Create cone: claw_r_0
bpy.ops.mesh.primitive_cone_add(radius1=0.005, radius2=0.001,
    depth=0.035, vertices=32, location=(0.2, 0.08, 0.42))
obj = bpy.context.active_object
obj.name = "claw_r_0"


# Rotate: claw_r_0 (degrees)
import math
bpy.data.objects["claw_r_0"].rotation_euler = (
    math.radians(60),
    math.radians(15),
    math.radians(0)
)


# Create cone: claw_r_1
bpy.ops.mesh.primitive_cone_add(radius1=0.005, radius2=0.001,
    depth=0.035, vertices=32, location=(0.21000000000000002, 0.095, 0.39999999999999997))
obj = bpy.context.active_object
obj.name = "claw_r_1"


# Rotate: claw_r_1 (degrees)
import math
bpy.data.objects["claw_r_1"].rotation_euler = (
    math.radians(60),
    math.radians(23),
    math.radians(0)
)


# Create cone: claw_r_2
bpy.ops.mesh.primitive_cone_add(radius1=0.005, radius2=0.001,
    depth=0.035, vertices=32, location=(0.22, 0.11, 0.38))
obj = bpy.context.active_object
obj.name = "claw_r_2"


# Rotate: claw_r_2 (degrees)
import math
bpy.data.objects["claw_r_2"].rotation_euler = (
    math.radians(60),
    math.radians(31),
    math.radians(0)
)


# Create cone: claw_r_3
bpy.ops.mesh.primitive_cone_add(radius1=0.005, radius2=0.001,
    depth=0.035, vertices=32, location=(0.23, 0.125, 0.36))
obj = bpy.context.active_object
obj.name = "claw_r_3"


# Rotate: claw_r_3 (degrees)
import math
bpy.data.objects["claw_r_3"].rotation_euler = (
    math.radians(60),
    math.radians(39),
    math.radians(0)
)


# Create cylinder: arm_upper_l
bpy.ops.mesh.primitive_cylinder_add(radius=0.018, depth=0.12,
    vertices=32, location=(-0.08, 0, 0.6))
obj = bpy.context.active_object
obj.name = "arm_upper_l"


# Rotate: arm_upper_l (degrees)
import math
bpy.data.objects["arm_upper_l"].rotation_euler = (
    math.radians(20),
    math.radians(-60),
    math.radians(-20)
)


# Create cone: arm_lower_l
bpy.ops.mesh.primitive_cone_add(radius1=0.015, radius2=0.008,
    depth=0.1, vertices=32, location=(-0.16, 0.04, 0.5))
obj = bpy.context.active_object
obj.name = "arm_lower_l"


# Rotate: arm_lower_l (degrees)
import math
bpy.data.objects["arm_lower_l"].rotation_euler = (
    math.radians(40),
    math.radians(-45),
    math.radians(0)
)


# Create cone: claw_l_0
bpy.ops.mesh.primitive_cone_add(radius1=0.005, radius2=0.001,
    depth=0.035, vertices=32, location=(-0.2, 0.08, 0.42))
obj = bpy.context.active_object
obj.name = "claw_l_0"


# Rotate: claw_l_0 (degrees)
import math
bpy.data.objects["claw_l_0"].rotation_euler = (
    math.radians(60),
    math.radians(-15),
    math.radians(0)
)


# Create cone: claw_l_1
bpy.ops.mesh.primitive_cone_add(radius1=0.005, radius2=0.001,
    depth=0.035, vertices=32, location=(-0.21000000000000002, 0.095, 0.39999999999999997))
obj = bpy.context.active_object
obj.name = "claw_l_1"


# Rotate: claw_l_1 (degrees)
import math
bpy.data.objects["claw_l_1"].rotation_euler = (
    math.radians(60),
    math.radians(-23),
    math.radians(0)
)


# Create cone: claw_l_2
bpy.ops.mesh.primitive_cone_add(radius1=0.005, radius2=0.001,
    depth=0.035, vertices=32, location=(-0.22, 0.11, 0.38))
obj = bpy.context.active_object
obj.name = "claw_l_2"


# Rotate: claw_l_2 (degrees)
import math
bpy.data.objects["claw_l_2"].rotation_euler = (
    math.radians(60),
    math.radians(-31),
    math.radians(0)
)


# Create cone: claw_l_3
bpy.ops.mesh.primitive_cone_add(radius1=0.005, radius2=0.001,
    depth=0.035, vertices=32, location=(-0.23, 0.125, 0.36))
obj = bpy.context.active_object
obj.name = "claw_l_3"


# Rotate: claw_l_3 (degrees)
import math
bpy.data.objects["claw_l_3"].rotation_euler = (
    math.radians(60),
    math.radians(-39),
    math.radians(0)
)


# Create cone: tendril_0
bpy.ops.mesh.primitive_cone_add(radius1=0.02, radius2=0.005,
    depth=0.13, vertices=32, location=(0.04, 0.03, 0.04))
obj = bpy.context.active_object
obj.name = "tendril_0"


# Rotate: tendril_0 (degrees)
import math
bpy.data.objects["tendril_0"].rotation_euler = (
    math.radians(15),
    math.radians(20),
    math.radians(0)
)


# Create cone: tendril_1
bpy.ops.mesh.primitive_cone_add(radius1=0.02, radius2=0.005,
    depth=0.11, vertices=32, location=(-0.03, 0.04, 0.03))
obj = bpy.context.active_object
obj.name = "tendril_1"


# Rotate: tendril_1 (degrees)
import math
bpy.data.objects["tendril_1"].rotation_euler = (
    math.radians(10),
    math.radians(-15),
    math.radians(45)
)


# Create cone: tendril_2
bpy.ops.mesh.primitive_cone_add(radius1=0.02, radius2=0.005,
    depth=0.15000000000000002, vertices=32, location=(0.05, -0.02, 0.05))
obj = bpy.context.active_object
obj.name = "tendril_2"


# Rotate: tendril_2 (degrees)
import math
bpy.data.objects["tendril_2"].rotation_euler = (
    math.radians(-10),
    math.radians(30),
    math.radians(90)
)


# Create cone: tendril_3
bpy.ops.mesh.primitive_cone_add(radius1=0.02, radius2=0.005,
    depth=0.12000000000000001, vertices=32, location=(-0.04, -0.03, 0.035))
obj = bpy.context.active_object
obj.name = "tendril_3"


# Rotate: tendril_3 (degrees)
import math
bpy.data.objects["tendril_3"].rotation_euler = (
    math.radians(-15),
    math.radians(-25),
    math.radians(135)
)


# Create cone: tendril_4
bpy.ops.mesh.primitive_cone_add(radius1=0.02, radius2=0.005,
    depth=0.1, vertices=32, location=(0.02, 0.05, 0.025))
obj = bpy.context.active_object
obj.name = "tendril_4"


# Rotate: tendril_4 (degrees)
import math
bpy.data.objects["tendril_4"].rotation_euler = (
    math.radians(20),
    math.radians(10),
    math.radians(180)
)


# Create cone: tendril_5
bpy.ops.mesh.primitive_cone_add(radius1=0.02, radius2=0.005,
    depth=0.09, vertices=32, location=(-0.02, -0.05, 0.02))
obj = bpy.context.active_object
obj.name = "tendril_5"


# Rotate: tendril_5 (degrees)
import math
bpy.data.objects["tendril_5"].rotation_euler = (
    math.radians(-20),
    math.radians(-10),
    math.radians(225)
)


# Create cone: tendril_6
bpy.ops.mesh.primitive_cone_add(radius1=0.02, radius2=0.005,
    depth=0.16999999999999998, vertices=32, location=(0, 0.04, 0.06))
obj = bpy.context.active_object
obj.name = "tendril_6"


# Rotate: tendril_6 (degrees)
import math
bpy.data.objects["tendril_6"].rotation_euler = (
    math.radians(25),
    math.radians(0),
    math.radians(270)
)


# Create cone: tendril_7
bpy.ops.mesh.primitive_cone_add(radius1=0.02, radius2=0.005,
    depth=0.08, vertices=32, location=(0.06, 0, 0.015))
obj = bpy.context.active_object
obj.name = "tendril_7"


# Rotate: tendril_7 (degrees)
import math
bpy.data.objects["tendril_7"].rotation_euler = (
    math.radians(5),
    math.radians(35),
    math.radians(315)
)


# Create sphere: wisp_0
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(0.1, 0.0, 0.4))
obj = bpy.context.active_object
obj.name = "wisp_0"


# Scale: wisp_0
bpy.data.objects["wisp_0"].scale = (0.6, 0.8, 1.0)


# Create sphere: wisp_1
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(0.06363946140238524, 0.11022678051524973, 0.5496242479906082))
obj = bpy.context.active_object
obj.name = "wisp_1"


# Scale: wisp_1
bpy.data.objects["wisp_1"].scale = (0.7682941969615793, 0.708060461173628, 1.0)


# Create sphere: wisp_2
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(-0.03864796257038107, 0.0669402347809203, 0.4211680012089801))
obj = bpy.context.active_object
obj.name = "wisp_2"


# Scale: wisp_2
bpy.data.objects["wisp_2"].scale = (0.7818594853651364, 0.5167706326905714, 1.0)


# Create sphere: wisp_3
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(-0.09161753505403222, 1.1219912104969099e-17, 0.2533704823502355))
obj = bpy.context.active_object
obj.name = "wisp_3"


# Scale: wisp_3
bpy.data.objects["wisp_3"].scale = (0.6282240016119734, 0.4020015006799109, 1.0)


# Create sphere: wisp_4
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(-0.06484037369935078, -0.11230682162902819, 0.35808767527016117))
obj = bpy.context.active_object
obj.name = "wisp_4"


# Scale: wisp_4
bpy.data.objects["wisp_4"].scale = (0.4486395009384143, 0.46927127582727757, 1.0)


# Create sphere: wisp_5
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015, segments=32,
    ring_count=16, location=(0.04183968333665946, -0.07246845731168709, 0.5406999965162108))
obj = bpy.context.active_object
obj.name = "wisp_5"


# Scale: wisp_5
bpy.data.objects["wisp_5"].scale = (0.4082151450673723, 0.6567324370926453, 1.0)


# Union objects into: shadow-demon
# Using boolean EXACT solver for watertight results
base_obj = bpy.data.objects["shadow_body"]
bpy.context.view_layer.objects.active = base_obj


# Boolean union: adding head
tool_obj = bpy.data.objects["head"]
mod = base_obj.modifiers.new(name="Boolean_0", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_0")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_r
tool_obj = bpy.data.objects["eye_r"]
mod = base_obj.modifiers.new(name="Boolean_1", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_1")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_l
tool_obj = bpy.data.objects["eye_l"]
mod = base_obj.modifiers.new(name="Boolean_2", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_2")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding mouth
tool_obj = bpy.data.objects["mouth"]
mod = base_obj.modifiers.new(name="Boolean_3", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_3")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding horn_r
tool_obj = bpy.data.objects["horn_r"]
mod = base_obj.modifiers.new(name="Boolean_4", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_4")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding horn_l
tool_obj = bpy.data.objects["horn_l"]
mod = base_obj.modifiers.new(name="Boolean_5", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_5")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_upper_r
tool_obj = bpy.data.objects["arm_upper_r"]
mod = base_obj.modifiers.new(name="Boolean_6", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_6")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_lower_r
tool_obj = bpy.data.objects["arm_lower_r"]
mod = base_obj.modifiers.new(name="Boolean_7", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_7")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_r_0
tool_obj = bpy.data.objects["claw_r_0"]
mod = base_obj.modifiers.new(name="Boolean_8", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_8")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_r_1
tool_obj = bpy.data.objects["claw_r_1"]
mod = base_obj.modifiers.new(name="Boolean_9", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_9")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_r_2
tool_obj = bpy.data.objects["claw_r_2"]
mod = base_obj.modifiers.new(name="Boolean_10", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_10")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_r_3
tool_obj = bpy.data.objects["claw_r_3"]
mod = base_obj.modifiers.new(name="Boolean_11", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_11")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_upper_l
tool_obj = bpy.data.objects["arm_upper_l"]
mod = base_obj.modifiers.new(name="Boolean_12", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_12")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_lower_l
tool_obj = bpy.data.objects["arm_lower_l"]
mod = base_obj.modifiers.new(name="Boolean_13", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_13")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_l_0
tool_obj = bpy.data.objects["claw_l_0"]
mod = base_obj.modifiers.new(name="Boolean_14", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_14")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_l_1
tool_obj = bpy.data.objects["claw_l_1"]
mod = base_obj.modifiers.new(name="Boolean_15", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_15")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_l_2
tool_obj = bpy.data.objects["claw_l_2"]
mod = base_obj.modifiers.new(name="Boolean_16", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_16")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_l_3
tool_obj = bpy.data.objects["claw_l_3"]
mod = base_obj.modifiers.new(name="Boolean_17", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_17")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tendril_0
tool_obj = bpy.data.objects["tendril_0"]
mod = base_obj.modifiers.new(name="Boolean_18", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_18")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tendril_1
tool_obj = bpy.data.objects["tendril_1"]
mod = base_obj.modifiers.new(name="Boolean_19", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_19")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tendril_2
tool_obj = bpy.data.objects["tendril_2"]
mod = base_obj.modifiers.new(name="Boolean_20", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_20")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tendril_3
tool_obj = bpy.data.objects["tendril_3"]
mod = base_obj.modifiers.new(name="Boolean_21", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_21")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tendril_4
tool_obj = bpy.data.objects["tendril_4"]
mod = base_obj.modifiers.new(name="Boolean_22", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_22")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tendril_5
tool_obj = bpy.data.objects["tendril_5"]
mod = base_obj.modifiers.new(name="Boolean_23", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_23")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tendril_6
tool_obj = bpy.data.objects["tendril_6"]
mod = base_obj.modifiers.new(name="Boolean_24", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_24")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tendril_7
tool_obj = bpy.data.objects["tendril_7"]
mod = base_obj.modifiers.new(name="Boolean_25", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_25")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding wisp_0
tool_obj = bpy.data.objects["wisp_0"]
mod = base_obj.modifiers.new(name="Boolean_26", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_26")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding wisp_1
tool_obj = bpy.data.objects["wisp_1"]
mod = base_obj.modifiers.new(name="Boolean_27", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_27")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding wisp_2
tool_obj = bpy.data.objects["wisp_2"]
mod = base_obj.modifiers.new(name="Boolean_28", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_28")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding wisp_3
tool_obj = bpy.data.objects["wisp_3"]
mod = base_obj.modifiers.new(name="Boolean_29", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_29")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding wisp_4
tool_obj = bpy.data.objects["wisp_4"]
mod = base_obj.modifiers.new(name="Boolean_30", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_30")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding wisp_5
tool_obj = bpy.data.objects["wisp_5"]
mod = base_obj.modifiers.new(name="Boolean_31", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_31")
bpy.data.objects.remove(tool_obj, do_unlink=True)


base_obj.name = "shadow-demon"


# Add subdivision surface: shadow-demon
obj = bpy.data.objects["shadow-demon"]
mod = obj.modifiers.new(name="Subdivision", type='SUBSURF')
mod.levels = 2
mod.render_levels = 2


# Add smooth: shadow-demon
obj = bpy.data.objects["shadow-demon"]
mod = obj.modifiers.new(name="Smooth", type='SMOOTH')
mod.factor = 0.5
mod.iterations = 2


# Apply all modifiers: shadow-demon
obj = bpy.data.objects["shadow-demon"]
bpy.context.view_layer.objects.active = obj
for mod in obj.modifiers[:]:
    bpy.ops.object.modifier_apply(modifier=mod.name)


# Create cylinder: shadow-demon_base
bpy.ops.mesh.primitive_cylinder_add(radius=0.0125, depth=0.003,
    vertices=48, location=(0, 0, 0.0015))
obj = bpy.context.active_object
obj.name = "shadow-demon_base"


# Add bevel: shadow-demon_base
obj = bpy.data.objects["shadow-demon_base"]
mod = obj.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.0004
mod.segments = 2


# Boolean union: shadow-demon + shadow-demon_base
target_obj = bpy.data.objects["shadow-demon"]
tool_obj = bpy.data.objects["shadow-demon_base"]
mod = target_obj.modifiers.new(name="Boolean", type='BOOLEAN')
mod.operation = 'UNION'
mod.object = tool_obj
bpy.context.view_layer.objects.active = target_obj
bpy.ops.object.modifier_apply(modifier='Boolean')
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Export to STL (Blender 4.0+ API)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.wm.stl_export(
    filepath="C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/shadow-demon.stl",
    export_selected_objects=True,
    global_scale=1.0,
    ascii_format=False  # Binary STL is smaller and faster
)
print("Exported: C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/shadow-demon.stl")
