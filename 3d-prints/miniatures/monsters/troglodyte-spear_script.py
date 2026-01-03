import bpy
import bmesh
import math
from mathutils import Vector, Matrix

# Clear default scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)


# Create sphere: torso
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.11, segments=32,
    ring_count=16, location=(0, 0.04, 0.52))
obj = bpy.context.active_object
obj.name = "torso"


# Scale: torso
bpy.data.objects["torso"].scale = (0.85, 0.75, 1.0)


# Rotate: torso (degrees)
import math
bpy.data.objects["torso"].rotation_euler = (
    math.radians(15),
    math.radians(0),
    math.radians(0)
)


# Create sphere: back_hunch
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.07, segments=32,
    ring_count=16, location=(0, -0.04, 0.58))
obj = bpy.context.active_object
obj.name = "back_hunch"


# Scale: back_hunch
bpy.data.objects["back_hunch"].scale = (0.75, 0.85, 0.65)


# Create sphere: head
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.06, segments=32,
    ring_count=16, location=(0, 0.12, 0.68))
obj = bpy.context.active_object
obj.name = "head"


# Scale: head
bpy.data.objects["head"].scale = (0.8, 1.0, 0.85)


# Rotate: head (degrees)
import math
bpy.data.objects["head"].rotation_euler = (
    math.radians(10),
    math.radians(0),
    math.radians(0)
)


# Create cone: snout
bpy.ops.mesh.primitive_cone_add(radius1=0.035, radius2=0.018,
    depth=0.055, vertices=32, location=(0, 0.18, 0.66))
obj = bpy.context.active_object
obj.name = "snout"


# Rotate: snout (degrees)
import math
bpy.data.objects["snout"].rotation_euler = (
    math.radians(75),
    math.radians(0),
    math.radians(0)
)


# Create sphere: eye_r
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.01, segments=32,
    ring_count=16, location=(0.025, 0.14, 0.7))
obj = bpy.context.active_object
obj.name = "eye_r"


# Create sphere: eye_l
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.01, segments=32,
    ring_count=16, location=(-0.025, 0.14, 0.7))
obj = bpy.context.active_object
obj.name = "eye_l"


# Create cylinder: arm_r_up
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.11,
    vertices=32, location=(0.12, 0.08, 0.52))
obj = bpy.context.active_object
obj.name = "arm_r_up"


# Rotate: arm_r_up (degrees)
import math
bpy.data.objects["arm_r_up"].rotation_euler = (
    math.radians(45),
    math.radians(40),
    math.radians(20)
)


# Create cylinder: arm_r_low
bpy.ops.mesh.primitive_cylinder_add(radius=0.018, depth=0.09,
    vertices=32, location=(0.18, 0.16, 0.48))
obj = bpy.context.active_object
obj.name = "arm_r_low"


# Rotate: arm_r_low (degrees)
import math
bpy.data.objects["arm_r_low"].rotation_euler = (
    math.radians(70),
    math.radians(20),
    math.radians(0)
)


# Create cylinder: arm_l_up
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.11,
    vertices=32, location=(-0.1, -0.02, 0.54))
obj = bpy.context.active_object
obj.name = "arm_l_up"


# Rotate: arm_l_up (degrees)
import math
bpy.data.objects["arm_l_up"].rotation_euler = (
    math.radians(-20),
    math.radians(-45),
    math.radians(-10)
)


# Create cylinder: arm_l_low
bpy.ops.mesh.primitive_cylinder_add(radius=0.018, depth=0.09,
    vertices=32, location=(-0.16, -0.06, 0.5))
obj = bpy.context.active_object
obj.name = "arm_l_low"


# Rotate: arm_l_low (degrees)
import math
bpy.data.objects["arm_l_low"].rotation_euler = (
    math.radians(-30),
    math.radians(-30),
    math.radians(0)
)


# Create cylinder: spear_shaft
bpy.ops.mesh.primitive_cylinder_add(radius=0.008, depth=0.55,
    vertices=32, location=(0.05, 0.2, 0.42))
obj = bpy.context.active_object
obj.name = "spear_shaft"


# Rotate: spear_shaft (degrees)
import math
bpy.data.objects["spear_shaft"].rotation_euler = (
    math.radians(70),
    math.radians(10),
    math.radians(0)
)


# Create cone: spear_point
bpy.ops.mesh.primitive_cone_add(radius1=0.018, radius2=0.003,
    depth=0.06, vertices=32, location=(0.12, 0.42, 0.52))
obj = bpy.context.active_object
obj.name = "spear_point"


# Rotate: spear_point (degrees)
import math
bpy.data.objects["spear_point"].rotation_euler = (
    math.radians(70),
    math.radians(10),
    math.radians(0)
)


# Create sphere: spear_butt
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012, segments=32,
    ring_count=16, location=(-0.08, -0.12, 0.28))
obj = bpy.context.active_object
obj.name = "spear_butt"


# Create cylinder: leg_r_up
bpy.ops.mesh.primitive_cylinder_add(radius=0.032, depth=0.14,
    vertices=32, location=(0.05, 0.06, 0.3))
obj = bpy.context.active_object
obj.name = "leg_r_up"


# Rotate: leg_r_up (degrees)
import math
bpy.data.objects["leg_r_up"].rotation_euler = (
    math.radians(25),
    math.radians(10),
    math.radians(0)
)


# Create cylinder: leg_r_low
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.11,
    vertices=32, location=(0.06, 0.12, 0.1))
obj = bpy.context.active_object
obj.name = "leg_r_low"


# Rotate: leg_r_low (degrees)
import math
bpy.data.objects["leg_r_low"].rotation_euler = (
    math.radians(-15),
    math.radians(5),
    math.radians(0)
)


# Create cylinder: leg_l_up
bpy.ops.mesh.primitive_cylinder_add(radius=0.032, depth=0.14,
    vertices=32, location=(-0.05, -0.04, 0.32))
obj = bpy.context.active_object
obj.name = "leg_l_up"


# Rotate: leg_l_up (degrees)
import math
bpy.data.objects["leg_l_up"].rotation_euler = (
    math.radians(-15),
    math.radians(-10),
    math.radians(0)
)


# Create cylinder: leg_l_low
bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.11,
    vertices=32, location=(-0.06, -0.08, 0.12))
obj = bpy.context.active_object
obj.name = "leg_l_low"


# Rotate: leg_l_low (degrees)
import math
bpy.data.objects["leg_l_low"].rotation_euler = (
    math.radians(10),
    math.radians(-5),
    math.radians(0)
)


# Create sphere: foot_r
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.022, segments=32,
    ring_count=16, location=(0.06, 0.14, 0.02))
obj = bpy.context.active_object
obj.name = "foot_r"


# Scale: foot_r
bpy.data.objects["foot_r"].scale = (0.65, 1.2, 0.35)


# Create sphere: foot_l
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.022, segments=32,
    ring_count=16, location=(-0.06, -0.08, 0.02))
obj = bpy.context.active_object
obj.name = "foot_l"


# Scale: foot_l
bpy.data.objects["foot_l"].scale = (0.65, 1.2, 0.35)


# Create cone: tail
bpy.ops.mesh.primitive_cone_add(radius1=0.025, radius2=0.008,
    depth=0.12, vertices=32, location=(0, -0.1, 0.38))
obj = bpy.context.active_object
obj.name = "tail"


# Rotate: tail (degrees)
import math
bpy.data.objects["tail"].rotation_euler = (
    math.radians(110),
    math.radians(0),
    math.radians(0)
)


# Union objects into: troglodyte-spear
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


# Boolean union: adding head
tool_obj = bpy.data.objects["head"]
mod = base_obj.modifiers.new(name="Boolean_1", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_1")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding snout
tool_obj = bpy.data.objects["snout"]
mod = base_obj.modifiers.new(name="Boolean_2", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_2")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_r
tool_obj = bpy.data.objects["eye_r"]
mod = base_obj.modifiers.new(name="Boolean_3", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_3")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding eye_l
tool_obj = bpy.data.objects["eye_l"]
mod = base_obj.modifiers.new(name="Boolean_4", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_4")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_r_up
tool_obj = bpy.data.objects["arm_r_up"]
mod = base_obj.modifiers.new(name="Boolean_5", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_5")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_r_low
tool_obj = bpy.data.objects["arm_r_low"]
mod = base_obj.modifiers.new(name="Boolean_6", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_6")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_l_up
tool_obj = bpy.data.objects["arm_l_up"]
mod = base_obj.modifiers.new(name="Boolean_7", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_7")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding arm_l_low
tool_obj = bpy.data.objects["arm_l_low"]
mod = base_obj.modifiers.new(name="Boolean_8", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_8")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding spear_shaft
tool_obj = bpy.data.objects["spear_shaft"]
mod = base_obj.modifiers.new(name="Boolean_9", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_9")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding spear_point
tool_obj = bpy.data.objects["spear_point"]
mod = base_obj.modifiers.new(name="Boolean_10", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_10")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding spear_butt
tool_obj = bpy.data.objects["spear_butt"]
mod = base_obj.modifiers.new(name="Boolean_11", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_11")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_r_up
tool_obj = bpy.data.objects["leg_r_up"]
mod = base_obj.modifiers.new(name="Boolean_12", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_12")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_r_low
tool_obj = bpy.data.objects["leg_r_low"]
mod = base_obj.modifiers.new(name="Boolean_13", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_13")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_l_up
tool_obj = bpy.data.objects["leg_l_up"]
mod = base_obj.modifiers.new(name="Boolean_14", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_14")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding leg_l_low
tool_obj = bpy.data.objects["leg_l_low"]
mod = base_obj.modifiers.new(name="Boolean_15", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_15")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding foot_r
tool_obj = bpy.data.objects["foot_r"]
mod = base_obj.modifiers.new(name="Boolean_16", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_16")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding foot_l
tool_obj = bpy.data.objects["foot_l"]
mod = base_obj.modifiers.new(name="Boolean_17", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_17")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding tail
tool_obj = bpy.data.objects["tail"]
mod = base_obj.modifiers.new(name="Boolean_18", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_18")
bpy.data.objects.remove(tool_obj, do_unlink=True)


base_obj.name = "troglodyte-spear"


# Add subdivision surface: troglodyte-spear
obj = bpy.data.objects["troglodyte-spear"]
mod = obj.modifiers.new(name="Subdivision", type='SUBSURF')
mod.levels = 1
mod.render_levels = 2


# Add displacement: troglodyte-spear
obj = bpy.data.objects["troglodyte-spear"]
tex = bpy.data.textures.new("troglodyte-spear_displace_tex", type='VORONOI')
mod = obj.modifiers.new(name="Displace", type='DISPLACE')
mod.texture = tex
mod.strength = 0.002


# Apply all modifiers: troglodyte-spear
obj = bpy.data.objects["troglodyte-spear"]
bpy.context.view_layer.objects.active = obj
for mod in obj.modifiers[:]:
    bpy.ops.object.modifier_apply(modifier=mod.name)


# Create cylinder: troglodyte-spear_base
bpy.ops.mesh.primitive_cylinder_add(radius=0.0125, depth=0.003,
    vertices=48, location=(0, 0, 0.0015))
obj = bpy.context.active_object
obj.name = "troglodyte-spear_base"


# Add bevel: troglodyte-spear_base
obj = bpy.data.objects["troglodyte-spear_base"]
mod = obj.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.0004
mod.segments = 2


# Boolean union: troglodyte-spear + troglodyte-spear_base
target_obj = bpy.data.objects["troglodyte-spear"]
tool_obj = bpy.data.objects["troglodyte-spear_base"]
mod = target_obj.modifiers.new(name="Boolean", type='BOOLEAN')
mod.operation = 'UNION'
mod.object = tool_obj
bpy.context.view_layer.objects.active = target_obj
bpy.ops.object.modifier_apply(modifier='Boolean')
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Export to STL (Blender 4.0+ API)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.wm.stl_export(
    filepath="C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/troglodyte-spear.stl",
    export_selected_objects=True,
    global_scale=1.0,
    ascii_format=False  # Binary STL is smaller and faster
)
print("Exported: C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/troglodyte-spear.stl")
