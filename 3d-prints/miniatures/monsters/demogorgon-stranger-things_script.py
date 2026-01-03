import bpy
import bmesh
import math
from mathutils import Vector, Matrix

# Clear default scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)


# Create cube: torso
bpy.ops.mesh.primitive_cube_add(size=0.4, location=(0, 0, 0.9))
obj = bpy.context.active_object
obj.name = "torso"


# Scale: torso
bpy.data.objects["torso"].scale = (0.9, 0.5, 1.6)


# Create cube: chest
bpy.ops.mesh.primitive_cube_add(size=0.35, location=(0, 0, 1.1))
obj = bpy.context.active_object
obj.name = "chest"


# Scale: chest
bpy.data.objects["chest"].scale = (1.0, 0.55, 0.8)


# Create cube: hips
bpy.ops.mesh.primitive_cube_add(size=0.3, location=(0, 0, 0.55))
obj = bpy.context.active_object
obj.name = "hips"


# Scale: hips
bpy.data.objects["hips"].scale = (1.1, 0.6, 0.7)


# Create cylinder: arm_upper_r
bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=0.45,
    vertices=32, location=(0.28, 0.05, 1.1))
obj = bpy.context.active_object
obj.name = "arm_upper_r"


# Rotate: arm_upper_r (degrees)
import math
bpy.data.objects["arm_upper_r"].rotation_euler = (
    math.radians(15),
    math.radians(55),
    math.radians(10)
)


# Create cylinder: arm_upper_l
bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=0.45,
    vertices=32, location=(-0.28, 0.05, 1.1))
obj = bpy.context.active_object
obj.name = "arm_upper_l"


# Rotate: arm_upper_l (degrees)
import math
bpy.data.objects["arm_upper_l"].rotation_euler = (
    math.radians(15),
    math.radians(-55),
    math.radians(-10)
)


# Create cylinder: arm_lower_r
bpy.ops.mesh.primitive_cylinder_add(radius=0.032, depth=0.5,
    vertices=32, location=(0.55, 0.15, 0.95))
obj = bpy.context.active_object
obj.name = "arm_lower_r"


# Rotate: arm_lower_r (degrees)
import math
bpy.data.objects["arm_lower_r"].rotation_euler = (
    math.radians(25),
    math.radians(45),
    math.radians(5)
)


# Create cylinder: arm_lower_l
bpy.ops.mesh.primitive_cylinder_add(radius=0.032, depth=0.5,
    vertices=32, location=(-0.55, 0.15, 0.95))
obj = bpy.context.active_object
obj.name = "arm_lower_l"


# Rotate: arm_lower_l (degrees)
import math
bpy.data.objects["arm_lower_l"].rotation_euler = (
    math.radians(25),
    math.radians(-45),
    math.radians(-5)
)


# Create cone: claw_r_0
bpy.ops.mesh.primitive_cone_add(radius1=0.015, radius2=0.003,
    depth=0.08, vertices=32, location=(0.78, 0.25, 0.75))
obj = bpy.context.active_object
obj.name = "claw_r_0"


# Rotate: claw_r_0 (degrees)
import math
bpy.data.objects["claw_r_0"].rotation_euler = (
    math.radians(60),
    math.radians(-30),
    math.radians(0)
)


# Create cone: claw_r_1
bpy.ops.mesh.primitive_cone_add(radius1=0.015, radius2=0.003,
    depth=0.08, vertices=32, location=(0.8, 0.26, 0.75))
obj = bpy.context.active_object
obj.name = "claw_r_1"


# Rotate: claw_r_1 (degrees)
import math
bpy.data.objects["claw_r_1"].rotation_euler = (
    math.radians(60),
    math.radians(-10),
    math.radians(0)
)


# Create cone: claw_r_2
bpy.ops.mesh.primitive_cone_add(radius1=0.015, radius2=0.003,
    depth=0.08, vertices=32, location=(0.8200000000000001, 0.27, 0.75))
obj = bpy.context.active_object
obj.name = "claw_r_2"


# Rotate: claw_r_2 (degrees)
import math
bpy.data.objects["claw_r_2"].rotation_euler = (
    math.radians(60),
    math.radians(10),
    math.radians(0)
)


# Create cone: claw_r_3
bpy.ops.mesh.primitive_cone_add(radius1=0.015, radius2=0.003,
    depth=0.08, vertices=32, location=(0.8400000000000001, 0.28, 0.75))
obj = bpy.context.active_object
obj.name = "claw_r_3"


# Rotate: claw_r_3 (degrees)
import math
bpy.data.objects["claw_r_3"].rotation_euler = (
    math.radians(60),
    math.radians(30),
    math.radians(0)
)


# Create cone: claw_l_0
bpy.ops.mesh.primitive_cone_add(radius1=0.015, radius2=0.003,
    depth=0.08, vertices=32, location=(-0.78, 0.25, 0.75))
obj = bpy.context.active_object
obj.name = "claw_l_0"


# Rotate: claw_l_0 (degrees)
import math
bpy.data.objects["claw_l_0"].rotation_euler = (
    math.radians(60),
    math.radians(30),
    math.radians(0)
)


# Create cone: claw_l_1
bpy.ops.mesh.primitive_cone_add(radius1=0.015, radius2=0.003,
    depth=0.08, vertices=32, location=(-0.8, 0.26, 0.75))
obj = bpy.context.active_object
obj.name = "claw_l_1"


# Rotate: claw_l_1 (degrees)
import math
bpy.data.objects["claw_l_1"].rotation_euler = (
    math.radians(60),
    math.radians(10),
    math.radians(0)
)


# Create cone: claw_l_2
bpy.ops.mesh.primitive_cone_add(radius1=0.015, radius2=0.003,
    depth=0.08, vertices=32, location=(-0.8200000000000001, 0.27, 0.75))
obj = bpy.context.active_object
obj.name = "claw_l_2"


# Rotate: claw_l_2 (degrees)
import math
bpy.data.objects["claw_l_2"].rotation_euler = (
    math.radians(60),
    math.radians(-10),
    math.radians(0)
)


# Create cone: claw_l_3
bpy.ops.mesh.primitive_cone_add(radius1=0.015, radius2=0.003,
    depth=0.08, vertices=32, location=(-0.8400000000000001, 0.28, 0.75))
obj = bpy.context.active_object
obj.name = "claw_l_3"


# Rotate: claw_l_3 (degrees)
import math
bpy.data.objects["claw_l_3"].rotation_euler = (
    math.radians(60),
    math.radians(-30),
    math.radians(0)
)


# Create cylinder: leg_upper_r
bpy.ops.mesh.primitive_cylinder_add(radius=0.055, depth=0.4,
    vertices=32, location=(0.1, 0, 0.35))
obj = bpy.context.active_object
obj.name = "leg_upper_r"


# Rotate: leg_upper_r (degrees)
import math
bpy.data.objects["leg_upper_r"].rotation_euler = (
    math.radians(5),
    math.radians(5),
    math.radians(0)
)


# Create cylinder: leg_upper_l
bpy.ops.mesh.primitive_cylinder_add(radius=0.055, depth=0.4,
    vertices=32, location=(-0.1, 0, 0.35))
obj = bpy.context.active_object
obj.name = "leg_upper_l"


# Rotate: leg_upper_l (degrees)
import math
bpy.data.objects["leg_upper_l"].rotation_euler = (
    math.radians(5),
    math.radians(-5),
    math.radians(0)
)


# Create cylinder: leg_lower_r
bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=0.35,
    vertices=32, location=(0.12, 0.03, 0.08))
obj = bpy.context.active_object
obj.name = "leg_lower_r"


# Rotate: leg_lower_r (degrees)
import math
bpy.data.objects["leg_lower_r"].rotation_euler = (
    math.radians(-5),
    math.radians(3),
    math.radians(0)
)


# Create cylinder: leg_lower_l
bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=0.35,
    vertices=32, location=(-0.12, 0.03, 0.08))
obj = bpy.context.active_object
obj.name = "leg_lower_l"


# Rotate: leg_lower_l (degrees)
import math
bpy.data.objects["leg_lower_l"].rotation_euler = (
    math.radians(-5),
    math.radians(-3),
    math.radians(0)
)


# Create sphere: foot_r
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.045, segments=32,
    ring_count=16, location=(0.13, 0.04, 0.02))
obj = bpy.context.active_object
obj.name = "foot_r"


# Scale: foot_r
bpy.data.objects["foot_r"].scale = (0.8, 1.5, 0.5)


# Create sphere: foot_l
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.045, segments=32,
    ring_count=16, location=(-0.13, 0.04, 0.02))
obj = bpy.context.active_object
obj.name = "foot_l"


# Scale: foot_l
bpy.data.objects["foot_l"].scale = (0.8, 1.5, 0.5)


# Create cylinder: neck
bpy.ops.mesh.primitive_cylinder_add(radius=0.06, depth=0.12,
    vertices=32, location=(0, 0, 1.4))
obj = bpy.context.active_object
obj.name = "neck"


# Create cylinder: maw
bpy.ops.mesh.primitive_cylinder_add(radius=0.045, depth=0.08,
    vertices=32, location=(0, 0, 1.5))
obj = bpy.context.active_object
obj.name = "maw"


# Create cone: petal_0
bpy.ops.mesh.primitive_cone_add(radius1=0.055, radius2=0.015,
    depth=0.13, vertices=32, location=(0.09100000000000001, 0.0, 1.52))
obj = bpy.context.active_object
obj.name = "petal_0"


# Rotate: petal_0 (degrees)
import math
bpy.data.objects["petal_0"].rotation_euler = (
    math.radians(0.0),
    math.radians(-40.0),
    math.radians(0.0)
)


# Create cone: petal_inner_0
bpy.ops.mesh.primitive_cone_add(radius1=0.03, radius2=0.01,
    depth=0.08, vertices=32, location=(0.06300000000000001, 0.0, 1.48))
obj = bpy.context.active_object
obj.name = "petal_inner_0"


# Rotate: petal_inner_0 (degrees)
import math
bpy.data.objects["petal_inner_0"].rotation_euler = (
    math.radians(0.0),
    math.radians(-24.0),
    math.radians(0.0)
)


# Create cone: petal_1
bpy.ops.mesh.primitive_cone_add(radius1=0.055, radius2=0.015,
    depth=0.13, vertices=32, location=(0.02812054648812022, 0.08654614298285898, 1.52))
obj = bpy.context.active_object
obj.name = "petal_1"


# Rotate: petal_1 (degrees)
import math
bpy.data.objects["petal_1"].rotation_euler = (
    math.radians(38.04226065180614),
    math.radians(-12.360679774997898),
    math.radians(72.0)
)


# Create cone: petal_inner_1
bpy.ops.mesh.primitive_cone_add(radius1=0.03, radius2=0.01,
    depth=0.08, vertices=32, location=(0.019468070645621692, 0.05991656052659468, 1.48))
obj = bpy.context.active_object
obj.name = "petal_inner_1"


# Rotate: petal_inner_1 (degrees)
import math
bpy.data.objects["petal_inner_1"].rotation_euler = (
    math.radians(22.825356391083684),
    math.radians(-7.416407864998739),
    math.radians(72.0)
)


# Create cone: petal_2
bpy.ops.mesh.primitive_cone_add(radius1=0.055, radius2=0.015,
    depth=0.13, vertices=32, location=(-0.07362054648812022, 0.05348845795861507, 1.52))
obj = bpy.context.active_object
obj.name = "petal_2"


# Rotate: petal_2 (degrees)
import math
bpy.data.objects["petal_2"].rotation_euler = (
    math.radians(23.51141009169893),
    math.radians(32.36067977499789),
    math.radians(144.0)
)


# Create cone: petal_inner_2
bpy.ops.mesh.primitive_cone_add(radius1=0.03, radius2=0.01,
    depth=0.08, vertices=32, location=(-0.05096807064562169, 0.03703047089442582, 1.48))
obj = bpy.context.active_object
obj.name = "petal_inner_2"


# Rotate: petal_inner_2 (degrees)
import math
bpy.data.objects["petal_inner_2"].rotation_euler = (
    math.radians(14.106846055019359),
    math.radians(19.416407864998735),
    math.radians(144.0)
)


# Create cone: petal_3
bpy.ops.mesh.primitive_cone_add(radius1=0.055, radius2=0.015,
    depth=0.13, vertices=32, location=(-0.07362054648812023, -0.05348845795861506, 1.52))
obj = bpy.context.active_object
obj.name = "petal_3"


# Rotate: petal_3 (degrees)
import math
bpy.data.objects["petal_3"].rotation_euler = (
    math.radians(-23.51141009169892),
    math.radians(32.3606797749979),
    math.radians(216.0)
)


# Create cone: petal_inner_3
bpy.ops.mesh.primitive_cone_add(radius1=0.03, radius2=0.01,
    depth=0.08, vertices=32, location=(-0.0509680706456217, -0.03703047089442581, 1.48))
obj = bpy.context.active_object
obj.name = "petal_inner_3"


# Rotate: petal_inner_3 (degrees)
import math
bpy.data.objects["petal_inner_3"].rotation_euler = (
    math.radians(-14.106846055019352),
    math.radians(19.41640786499874),
    math.radians(216.0)
)


# Create cone: petal_4
bpy.ops.mesh.primitive_cone_add(radius1=0.055, radius2=0.015,
    depth=0.13, vertices=32, location=(0.028120546488120204, -0.086546142982859, 1.52))
obj = bpy.context.active_object
obj.name = "petal_4"


# Rotate: petal_4 (degrees)
import math
bpy.data.objects["petal_4"].rotation_euler = (
    math.radians(-38.042260651806146),
    math.radians(-12.36067977499789),
    math.radians(288.0)
)


# Create cone: petal_inner_4
bpy.ops.mesh.primitive_cone_add(radius1=0.03, radius2=0.01,
    depth=0.08, vertices=32, location=(0.019468070645621678, -0.05991656052659469, 1.48))
obj = bpy.context.active_object
obj.name = "petal_inner_4"


# Rotate: petal_inner_4 (degrees)
import math
bpy.data.objects["petal_inner_4"].rotation_euler = (
    math.radians(-22.825356391083687),
    math.radians(-7.4164078649987335),
    math.radians(288.0)
)


# Create cone: tooth_0
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.002,
    depth=0.04, vertices=32, location=(0.035, 0.0, 1.5))
obj = bpy.context.active_object
obj.name = "tooth_0"


# Rotate: tooth_0 (degrees)
import math
bpy.data.objects["tooth_0"].rotation_euler = (
    math.radians(0.0),
    math.radians(-15.0),
    math.radians(0)
)


# Create cone: tooth_1
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.002,
    depth=0.04, vertices=32, location=(0.024748737341529166, 0.024748737341529166, 1.5))
obj = bpy.context.active_object
obj.name = "tooth_1"


# Rotate: tooth_1 (degrees)
import math
bpy.data.objects["tooth_1"].rotation_euler = (
    math.radians(10.606601717798213),
    math.radians(-10.606601717798213),
    math.radians(0)
)


# Create cone: tooth_2
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.002,
    depth=0.04, vertices=32, location=(2.1431318985078684e-18, 0.035, 1.5))
obj = bpy.context.active_object
obj.name = "tooth_2"


# Rotate: tooth_2 (degrees)
import math
bpy.data.objects["tooth_2"].rotation_euler = (
    math.radians(15.0),
    math.radians(-9.18485099360515e-16),
    math.radians(0)
)


# Create cone: tooth_3
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.002,
    depth=0.04, vertices=32, location=(-0.024748737341529162, 0.024748737341529166, 1.5))
obj = bpy.context.active_object
obj.name = "tooth_3"


# Rotate: tooth_3 (degrees)
import math
bpy.data.objects["tooth_3"].rotation_euler = (
    math.radians(10.606601717798213),
    math.radians(10.606601717798211),
    math.radians(0)
)


# Create cone: tooth_4
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.002,
    depth=0.04, vertices=32, location=(-0.035, 4.286263797015737e-18, 1.5))
obj = bpy.context.active_object
obj.name = "tooth_4"


# Rotate: tooth_4 (degrees)
import math
bpy.data.objects["tooth_4"].rotation_euler = (
    math.radians(1.83697019872103e-15),
    math.radians(15.0),
    math.radians(0)
)


# Create cone: tooth_5
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.002,
    depth=0.04, vertices=32, location=(-0.024748737341529173, -0.024748737341529162, 1.5))
obj = bpy.context.active_object
obj.name = "tooth_5"


# Rotate: tooth_5 (degrees)
import math
bpy.data.objects["tooth_5"].rotation_euler = (
    math.radians(-10.606601717798211),
    math.radians(10.606601717798215),
    math.radians(0)
)


# Create cone: tooth_6
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.002,
    depth=0.04, vertices=32, location=(-6.429395695523605e-18, -0.035, 1.5))
obj = bpy.context.active_object
obj.name = "tooth_6"


# Rotate: tooth_6 (degrees)
import math
bpy.data.objects["tooth_6"].rotation_euler = (
    math.radians(-15.0),
    math.radians(2.7554552980815444e-15),
    math.radians(0)
)


# Create cone: tooth_7
bpy.ops.mesh.primitive_cone_add(radius1=0.008, radius2=0.002,
    depth=0.04, vertices=32, location=(0.02474873734152916, -0.024748737341529173, 1.5))
obj = bpy.context.active_object
obj.name = "tooth_7"


# Rotate: tooth_7 (degrees)
import math
bpy.data.objects["tooth_7"].rotation_euler = (
    math.radians(-10.606601717798215),
    math.radians(-10.60660171779821),
    math.radians(0)
)


# Union objects into: demogorgon-stranger-things
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


# Boolean union: adding hips
tool_obj = bpy.data.objects["hips"]
mod = base_obj.modifiers.new(name="Boolean_1", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_1")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding neck
tool_obj = bpy.data.objects["neck"]
mod = base_obj.modifiers.new(name="Boolean_2", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_2")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding maw
tool_obj = bpy.data.objects["maw"]
mod = base_obj.modifiers.new(name="Boolean_3", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_3")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_upper_r
tool_obj = bpy.data.objects["arm_upper_r"]
mod = base_obj.modifiers.new(name="Boolean_4", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_4")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_upper_l
tool_obj = bpy.data.objects["arm_upper_l"]
mod = base_obj.modifiers.new(name="Boolean_5", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_5")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_lower_r
tool_obj = bpy.data.objects["arm_lower_r"]
mod = base_obj.modifiers.new(name="Boolean_6", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_6")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_lower_l
tool_obj = bpy.data.objects["arm_lower_l"]
mod = base_obj.modifiers.new(name="Boolean_7", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_7")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_upper_r
tool_obj = bpy.data.objects["leg_upper_r"]
mod = base_obj.modifiers.new(name="Boolean_8", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_8")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_upper_l
tool_obj = bpy.data.objects["leg_upper_l"]
mod = base_obj.modifiers.new(name="Boolean_9", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_9")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_lower_r
tool_obj = bpy.data.objects["leg_lower_r"]
mod = base_obj.modifiers.new(name="Boolean_10", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_10")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_lower_l
tool_obj = bpy.data.objects["leg_lower_l"]
mod = base_obj.modifiers.new(name="Boolean_11", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_11")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding foot_r
tool_obj = bpy.data.objects["foot_r"]
mod = base_obj.modifiers.new(name="Boolean_12", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_12")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding foot_l
tool_obj = bpy.data.objects["foot_l"]
mod = base_obj.modifiers.new(name="Boolean_13", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_13")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding petal_0
tool_obj = bpy.data.objects["petal_0"]
mod = base_obj.modifiers.new(name="Boolean_14", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_14")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding petal_1
tool_obj = bpy.data.objects["petal_1"]
mod = base_obj.modifiers.new(name="Boolean_15", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_15")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding petal_2
tool_obj = bpy.data.objects["petal_2"]
mod = base_obj.modifiers.new(name="Boolean_16", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_16")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding petal_3
tool_obj = bpy.data.objects["petal_3"]
mod = base_obj.modifiers.new(name="Boolean_17", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_17")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding petal_4
tool_obj = bpy.data.objects["petal_4"]
mod = base_obj.modifiers.new(name="Boolean_18", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_18")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding petal_inner_0
tool_obj = bpy.data.objects["petal_inner_0"]
mod = base_obj.modifiers.new(name="Boolean_19", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_19")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding petal_inner_1
tool_obj = bpy.data.objects["petal_inner_1"]
mod = base_obj.modifiers.new(name="Boolean_20", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_20")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding petal_inner_2
tool_obj = bpy.data.objects["petal_inner_2"]
mod = base_obj.modifiers.new(name="Boolean_21", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_21")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding petal_inner_3
tool_obj = bpy.data.objects["petal_inner_3"]
mod = base_obj.modifiers.new(name="Boolean_22", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_22")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding petal_inner_4
tool_obj = bpy.data.objects["petal_inner_4"]
mod = base_obj.modifiers.new(name="Boolean_23", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_23")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tooth_0
tool_obj = bpy.data.objects["tooth_0"]
mod = base_obj.modifiers.new(name="Boolean_24", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_24")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tooth_1
tool_obj = bpy.data.objects["tooth_1"]
mod = base_obj.modifiers.new(name="Boolean_25", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_25")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tooth_2
tool_obj = bpy.data.objects["tooth_2"]
mod = base_obj.modifiers.new(name="Boolean_26", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_26")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tooth_3
tool_obj = bpy.data.objects["tooth_3"]
mod = base_obj.modifiers.new(name="Boolean_27", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_27")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tooth_4
tool_obj = bpy.data.objects["tooth_4"]
mod = base_obj.modifiers.new(name="Boolean_28", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_28")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tooth_5
tool_obj = bpy.data.objects["tooth_5"]
mod = base_obj.modifiers.new(name="Boolean_29", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_29")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tooth_6
tool_obj = bpy.data.objects["tooth_6"]
mod = base_obj.modifiers.new(name="Boolean_30", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_30")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tooth_7
tool_obj = bpy.data.objects["tooth_7"]
mod = base_obj.modifiers.new(name="Boolean_31", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_31")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_r_0
tool_obj = bpy.data.objects["claw_r_0"]
mod = base_obj.modifiers.new(name="Boolean_32", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_32")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_r_1
tool_obj = bpy.data.objects["claw_r_1"]
mod = base_obj.modifiers.new(name="Boolean_33", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_33")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_r_2
tool_obj = bpy.data.objects["claw_r_2"]
mod = base_obj.modifiers.new(name="Boolean_34", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_34")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_r_3
tool_obj = bpy.data.objects["claw_r_3"]
mod = base_obj.modifiers.new(name="Boolean_35", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_35")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_l_0
tool_obj = bpy.data.objects["claw_l_0"]
mod = base_obj.modifiers.new(name="Boolean_36", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_36")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_l_1
tool_obj = bpy.data.objects["claw_l_1"]
mod = base_obj.modifiers.new(name="Boolean_37", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_37")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_l_2
tool_obj = bpy.data.objects["claw_l_2"]
mod = base_obj.modifiers.new(name="Boolean_38", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_38")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding claw_l_3
tool_obj = bpy.data.objects["claw_l_3"]
mod = base_obj.modifiers.new(name="Boolean_39", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_39")
bpy.data.objects.remove(tool_obj, do_unlink=True)


base_obj.name = "demogorgon-stranger-things"


# Add subdivision surface: demogorgon-stranger-things
obj = bpy.data.objects["demogorgon-stranger-things"]
mod = obj.modifiers.new(name="Subdivision", type='SUBSURF')
mod.levels = 2
mod.render_levels = 2


# Add smooth: demogorgon-stranger-things
obj = bpy.data.objects["demogorgon-stranger-things"]
mod = obj.modifiers.new(name="Smooth", type='SMOOTH')
mod.factor = 0.3
mod.iterations = 1


# Apply all modifiers: demogorgon-stranger-things
obj = bpy.data.objects["demogorgon-stranger-things"]
bpy.context.view_layer.objects.active = obj
for mod in obj.modifiers[:]:
    bpy.ops.object.modifier_apply(modifier=mod.name)


# Create cylinder: demogorgon-stranger-things_base
bpy.ops.mesh.primitive_cylinder_add(radius=0.025, depth=0.003,
    vertices=64, location=(0, 0, 0.0015))
obj = bpy.context.active_object
obj.name = "demogorgon-stranger-things_base"


# Add bevel: demogorgon-stranger-things_base
obj = bpy.data.objects["demogorgon-stranger-things_base"]
mod = obj.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.0005
mod.segments = 2


# Boolean union: demogorgon-stranger-things + demogorgon-stranger-things_base
target_obj = bpy.data.objects["demogorgon-stranger-things"]
tool_obj = bpy.data.objects["demogorgon-stranger-things_base"]
mod = target_obj.modifiers.new(name="Boolean", type='BOOLEAN')
mod.operation = 'UNION'
mod.object = tool_obj
bpy.context.view_layer.objects.active = target_obj
bpy.ops.object.modifier_apply(modifier='Boolean')
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Export to STL (Blender 4.0+ API)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.wm.stl_export(
    filepath="C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/demogorgon-stranger-things.stl",
    export_selected_objects=True,
    global_scale=1.0,
    ascii_format=False  # Binary STL is smaller and faster
)
print("Exported: C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/demogorgon-stranger-things.stl")
