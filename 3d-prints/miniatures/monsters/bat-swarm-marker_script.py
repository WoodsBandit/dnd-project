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


# Create cylinder: stand_0
bpy.ops.mesh.primitive_cylinder_add(radius=0.0004, depth=0.012,
    vertices=8, location=(0, 0, 0.009000000000000001))
obj = bpy.context.active_object
obj.name = "stand_0"


# Create cylinder: stand_1
bpy.ops.mesh.primitive_cylinder_add(radius=0.0004, depth=0.019,
    vertices=8, location=(-0.005, 0.004, 0.0125))
obj = bpy.context.active_object
obj.name = "stand_1"


# Create cylinder: stand_2
bpy.ops.mesh.primitive_cylinder_add(radius=0.0004, depth=0.015,
    vertices=8, location=(0.005, 0.003, 0.010499999999999999))
obj = bpy.context.active_object
obj.name = "stand_2"


# Create cylinder: stand_3
bpy.ops.mesh.primitive_cylinder_add(radius=0.0004, depth=0.009000000000000001,
    vertices=8, location=(0.002, -0.005, 0.007500000000000001))
obj = bpy.context.active_object
obj.name = "stand_3"


# Create sphere: bat_0_body
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.002, segments=12,
    ring_count=8, location=(0, 0, 0.018))
obj = bpy.context.active_object
obj.name = "bat_0_body"


# Scale: bat_0_body
bpy.data.objects["bat_0_body"].scale = (0.5, 1.0, 0.6)


# Rotate: bat_0_body (degrees)
import math
bpy.data.objects["bat_0_body"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(15)
)


# Create sphere: bat_0_head
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0012, segments=10,
    ring_count=6, location=(0.0007764571353075623, 0.002897777478867205, 0.0185))
obj = bpy.context.active_object
obj.name = "bat_0_head"


# Create cone: bat_0_ear_l
bpy.ops.mesh.primitive_cone_add(radius1=0.0006, radius2=0,
    depth=0.002, vertices=6, location=(-0.00022354286469243774, 0.002897777478867205, 0.019999999999999997))
obj = bpy.context.active_object
obj.name = "bat_0_ear_l"


# Create cone: bat_0_ear_r
bpy.ops.mesh.primitive_cone_add(radius1=0.0006, radius2=0,
    depth=0.002, vertices=6, location=(0.0017764571353075624, 0.002897777478867205, 0.019999999999999997))
obj = bpy.context.active_object
obj.name = "bat_0_ear_r"


# Create plane: bat_0_wing_l
bpy.ops.mesh.primitive_plane_add(size=0.008, location=(-0.004, 0, 0.018))
obj = bpy.context.active_object
obj.name = "bat_0_wing_l"


# Scale: bat_0_wing_l
bpy.data.objects["bat_0_wing_l"].scale = (1.0, 0.4, 1.0)


# Rotate: bat_0_wing_l (degrees)
import math
bpy.data.objects["bat_0_wing_l"].rotation_euler = (
    math.radians(0),
    math.radians(-25),
    math.radians(15)
)


# Add solidify: bat_0_wing_l
obj = bpy.data.objects["bat_0_wing_l"]
mod = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
mod.thickness = 0.0003


# Create plane: bat_0_wing_r
bpy.ops.mesh.primitive_plane_add(size=0.008, location=(0.004, 0, 0.018))
obj = bpy.context.active_object
obj.name = "bat_0_wing_r"


# Scale: bat_0_wing_r
bpy.data.objects["bat_0_wing_r"].scale = (1.0, 0.4, 1.0)


# Rotate: bat_0_wing_r (degrees)
import math
bpy.data.objects["bat_0_wing_r"].rotation_euler = (
    math.radians(0),
    math.radians(25),
    math.radians(15)
)


# Add solidify: bat_0_wing_r
obj = bpy.data.objects["bat_0_wing_r"]
mod = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
mod.thickness = 0.0003


# Create sphere: bat_1_body
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.002, segments=12,
    ring_count=8, location=(-0.005, 0.004, 0.025))
obj = bpy.context.active_object
obj.name = "bat_1_body"


# Scale: bat_1_body
bpy.data.objects["bat_1_body"].scale = (0.5, 1.0, 0.6)


# Rotate: bat_1_body (degrees)
import math
bpy.data.objects["bat_1_body"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(-30)
)


# Create sphere: bat_1_head
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0012, segments=10,
    ring_count=6, location=(-0.0065, 0.006598076211353316, 0.025500000000000002))
obj = bpy.context.active_object
obj.name = "bat_1_head"


# Create cone: bat_1_ear_l
bpy.ops.mesh.primitive_cone_add(radius1=0.0006, radius2=0,
    depth=0.002, vertices=6, location=(-0.0075, 0.006598076211353316, 0.027000000000000003))
obj = bpy.context.active_object
obj.name = "bat_1_ear_l"


# Create cone: bat_1_ear_r
bpy.ops.mesh.primitive_cone_add(radius1=0.0006, radius2=0,
    depth=0.002, vertices=6, location=(-0.0055, 0.006598076211353316, 0.027000000000000003))
obj = bpy.context.active_object
obj.name = "bat_1_ear_r"


# Create plane: bat_1_wing_l
bpy.ops.mesh.primitive_plane_add(size=0.008, location=(-0.009000000000000001, 0.004, 0.025))
obj = bpy.context.active_object
obj.name = "bat_1_wing_l"


# Scale: bat_1_wing_l
bpy.data.objects["bat_1_wing_l"].scale = (1.0, 0.4, 1.0)


# Rotate: bat_1_wing_l (degrees)
import math
bpy.data.objects["bat_1_wing_l"].rotation_euler = (
    math.radians(0),
    math.radians(20),
    math.radians(-30)
)


# Add solidify: bat_1_wing_l
obj = bpy.data.objects["bat_1_wing_l"]
mod = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
mod.thickness = 0.0003


# Create plane: bat_1_wing_r
bpy.ops.mesh.primitive_plane_add(size=0.008, location=(-0.001, 0.004, 0.025))
obj = bpy.context.active_object
obj.name = "bat_1_wing_r"


# Scale: bat_1_wing_r
bpy.data.objects["bat_1_wing_r"].scale = (1.0, 0.4, 1.0)


# Rotate: bat_1_wing_r (degrees)
import math
bpy.data.objects["bat_1_wing_r"].rotation_euler = (
    math.radians(0),
    math.radians(-20),
    math.radians(-30)
)


# Add solidify: bat_1_wing_r
obj = bpy.data.objects["bat_1_wing_r"]
mod = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
mod.thickness = 0.0003


# Create sphere: bat_2_body
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.002, segments=12,
    ring_count=8, location=(0.005, 0.003, 0.021))
obj = bpy.context.active_object
obj.name = "bat_2_body"


# Scale: bat_2_body
bpy.data.objects["bat_2_body"].scale = (0.5, 1.0, 0.6)


# Rotate: bat_2_body (degrees)
import math
bpy.data.objects["bat_2_body"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(45)
)


# Create sphere: bat_2_head
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0012, segments=10,
    ring_count=6, location=(0.007121320343559643, 0.005121320343559643, 0.021500000000000002))
obj = bpy.context.active_object
obj.name = "bat_2_head"


# Create cone: bat_2_ear_l
bpy.ops.mesh.primitive_cone_add(radius1=0.0006, radius2=0,
    depth=0.002, vertices=6, location=(0.006121320343559643, 0.005121320343559643, 0.023))
obj = bpy.context.active_object
obj.name = "bat_2_ear_l"


# Create cone: bat_2_ear_r
bpy.ops.mesh.primitive_cone_add(radius1=0.0006, radius2=0,
    depth=0.002, vertices=6, location=(0.008121320343559644, 0.005121320343559643, 0.023))
obj = bpy.context.active_object
obj.name = "bat_2_ear_r"


# Create plane: bat_2_wing_l
bpy.ops.mesh.primitive_plane_add(size=0.008, location=(0.001, 0.003, 0.021))
obj = bpy.context.active_object
obj.name = "bat_2_wing_l"


# Scale: bat_2_wing_l
bpy.data.objects["bat_2_wing_l"].scale = (1.0, 0.4, 1.0)


# Rotate: bat_2_wing_l (degrees)
import math
bpy.data.objects["bat_2_wing_l"].rotation_euler = (
    math.radians(0),
    math.radians(-35),
    math.radians(45)
)


# Add solidify: bat_2_wing_l
obj = bpy.data.objects["bat_2_wing_l"]
mod = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
mod.thickness = 0.0003


# Create plane: bat_2_wing_r
bpy.ops.mesh.primitive_plane_add(size=0.008, location=(0.009000000000000001, 0.003, 0.021))
obj = bpy.context.active_object
obj.name = "bat_2_wing_r"


# Scale: bat_2_wing_r
bpy.data.objects["bat_2_wing_r"].scale = (1.0, 0.4, 1.0)


# Rotate: bat_2_wing_r (degrees)
import math
bpy.data.objects["bat_2_wing_r"].rotation_euler = (
    math.radians(0),
    math.radians(35),
    math.radians(45)
)


# Add solidify: bat_2_wing_r
obj = bpy.data.objects["bat_2_wing_r"]
mod = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
mod.thickness = 0.0003


# Create sphere: bat_3_body
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.002, segments=12,
    ring_count=8, location=(0.002, -0.005, 0.015))
obj = bpy.context.active_object
obj.name = "bat_3_body"


# Scale: bat_3_body
bpy.data.objects["bat_3_body"].scale = (0.5, 1.0, 0.6)


# Rotate: bat_3_body (degrees)
import math
bpy.data.objects["bat_3_body"].rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(180)
)


# Create sphere: bat_3_head
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0012, segments=10,
    ring_count=6, location=(0.0020000000000000005, -0.008, 0.0155))
obj = bpy.context.active_object
obj.name = "bat_3_head"


# Create cone: bat_3_ear_l
bpy.ops.mesh.primitive_cone_add(radius1=0.0006, radius2=0,
    depth=0.002, vertices=6, location=(0.0010000000000000005, -0.008, 0.017))
obj = bpy.context.active_object
obj.name = "bat_3_ear_l"


# Create cone: bat_3_ear_r
bpy.ops.mesh.primitive_cone_add(radius1=0.0006, radius2=0,
    depth=0.002, vertices=6, location=(0.0030000000000000005, -0.008, 0.017))
obj = bpy.context.active_object
obj.name = "bat_3_ear_r"


# Create plane: bat_3_wing_l
bpy.ops.mesh.primitive_plane_add(size=0.008, location=(-0.002, -0.005, 0.015))
obj = bpy.context.active_object
obj.name = "bat_3_wing_l"


# Scale: bat_3_wing_l
bpy.data.objects["bat_3_wing_l"].scale = (1.0, 0.4, 1.0)


# Rotate: bat_3_wing_l (degrees)
import math
bpy.data.objects["bat_3_wing_l"].rotation_euler = (
    math.radians(0),
    math.radians(15),
    math.radians(180)
)


# Add solidify: bat_3_wing_l
obj = bpy.data.objects["bat_3_wing_l"]
mod = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
mod.thickness = 0.0003


# Create plane: bat_3_wing_r
bpy.ops.mesh.primitive_plane_add(size=0.008, location=(0.006, -0.005, 0.015))
obj = bpy.context.active_object
obj.name = "bat_3_wing_r"


# Scale: bat_3_wing_r
bpy.data.objects["bat_3_wing_r"].scale = (1.0, 0.4, 1.0)


# Rotate: bat_3_wing_r (degrees)
import math
bpy.data.objects["bat_3_wing_r"].rotation_euler = (
    math.radians(0),
    math.radians(-15),
    math.radians(180)
)


# Add solidify: bat_3_wing_r
obj = bpy.data.objects["bat_3_wing_r"]
mod = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
mod.thickness = 0.0003


# Union objects into: bat-swarm-marker
# Using boolean EXACT solver for watertight results
base_obj = bpy.data.objects["base"]
bpy.context.view_layer.objects.active = base_obj


# Boolean union: adding stand_0
tool_obj = bpy.data.objects["stand_0"]
mod = base_obj.modifiers.new(name="Boolean_0", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_0")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding stand_1
tool_obj = bpy.data.objects["stand_1"]
mod = base_obj.modifiers.new(name="Boolean_1", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_1")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding stand_2
tool_obj = bpy.data.objects["stand_2"]
mod = base_obj.modifiers.new(name="Boolean_2", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_2")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding stand_3
tool_obj = bpy.data.objects["stand_3"]
mod = base_obj.modifiers.new(name="Boolean_3", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_3")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_0_body
tool_obj = bpy.data.objects["bat_0_body"]
mod = base_obj.modifiers.new(name="Boolean_4", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_4")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_0_head
tool_obj = bpy.data.objects["bat_0_head"]
mod = base_obj.modifiers.new(name="Boolean_5", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_5")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_0_ear_l
tool_obj = bpy.data.objects["bat_0_ear_l"]
mod = base_obj.modifiers.new(name="Boolean_6", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_6")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_0_ear_r
tool_obj = bpy.data.objects["bat_0_ear_r"]
mod = base_obj.modifiers.new(name="Boolean_7", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_7")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_0_wing_l
tool_obj = bpy.data.objects["bat_0_wing_l"]
mod = base_obj.modifiers.new(name="Boolean_8", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_8")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_0_wing_r
tool_obj = bpy.data.objects["bat_0_wing_r"]
mod = base_obj.modifiers.new(name="Boolean_9", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_9")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_1_body
tool_obj = bpy.data.objects["bat_1_body"]
mod = base_obj.modifiers.new(name="Boolean_10", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_10")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_1_head
tool_obj = bpy.data.objects["bat_1_head"]
mod = base_obj.modifiers.new(name="Boolean_11", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_11")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_1_ear_l
tool_obj = bpy.data.objects["bat_1_ear_l"]
mod = base_obj.modifiers.new(name="Boolean_12", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_12")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_1_ear_r
tool_obj = bpy.data.objects["bat_1_ear_r"]
mod = base_obj.modifiers.new(name="Boolean_13", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_13")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_1_wing_l
tool_obj = bpy.data.objects["bat_1_wing_l"]
mod = base_obj.modifiers.new(name="Boolean_14", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_14")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_1_wing_r
tool_obj = bpy.data.objects["bat_1_wing_r"]
mod = base_obj.modifiers.new(name="Boolean_15", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_15")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_2_body
tool_obj = bpy.data.objects["bat_2_body"]
mod = base_obj.modifiers.new(name="Boolean_16", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_16")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_2_head
tool_obj = bpy.data.objects["bat_2_head"]
mod = base_obj.modifiers.new(name="Boolean_17", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_17")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_2_ear_l
tool_obj = bpy.data.objects["bat_2_ear_l"]
mod = base_obj.modifiers.new(name="Boolean_18", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_18")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_2_ear_r
tool_obj = bpy.data.objects["bat_2_ear_r"]
mod = base_obj.modifiers.new(name="Boolean_19", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_19")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_2_wing_l
tool_obj = bpy.data.objects["bat_2_wing_l"]
mod = base_obj.modifiers.new(name="Boolean_20", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_20")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_2_wing_r
tool_obj = bpy.data.objects["bat_2_wing_r"]
mod = base_obj.modifiers.new(name="Boolean_21", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_21")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_3_body
tool_obj = bpy.data.objects["bat_3_body"]
mod = base_obj.modifiers.new(name="Boolean_22", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_22")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_3_head
tool_obj = bpy.data.objects["bat_3_head"]
mod = base_obj.modifiers.new(name="Boolean_23", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_23")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_3_ear_l
tool_obj = bpy.data.objects["bat_3_ear_l"]
mod = base_obj.modifiers.new(name="Boolean_24", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_24")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_3_ear_r
tool_obj = bpy.data.objects["bat_3_ear_r"]
mod = base_obj.modifiers.new(name="Boolean_25", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_25")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_3_wing_l
tool_obj = bpy.data.objects["bat_3_wing_l"]
mod = base_obj.modifiers.new(name="Boolean_26", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_26")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: adding bat_3_wing_r
tool_obj = bpy.data.objects["bat_3_wing_r"]
mod = base_obj.modifiers.new(name="Boolean_27", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'  # EXACT solver is more reliable for watertight results
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Boolean_27")
bpy.data.objects.remove(tool_obj, do_unlink=True)


base_obj.name = "bat-swarm-marker"


# Clean mesh for printing: bat-swarm-marker
obj = bpy.data.objects["bat-swarm-marker"]
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
print(f"Mesh cleaned: bat-swarm-marker")


# Add subdivision surface: bat-swarm-marker
obj = bpy.data.objects["bat-swarm-marker"]
mod = obj.modifiers.new(name="Subdivision", type='SUBSURF')
mod.levels = 2
mod.render_levels = 2


# Apply all modifiers: bat-swarm-marker
obj = bpy.data.objects["bat-swarm-marker"]
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
    filepath="C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/bat-swarm-marker.stl",
    export_selected_objects=True,
    global_scale=1.0,
    ascii_format=False  # Binary STL is smaller and faster
)
print("Exported: C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/monsters/bat-swarm-marker.stl")
