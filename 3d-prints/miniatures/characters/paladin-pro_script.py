import bpy
import bmesh
import math
from mathutils import Vector, Matrix, Euler

# Clear default scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Helper function for tapered cylinders
def create_tapered_cylinder(name, radius_top, radius_bottom, height, location, segments=16):
    bpy.ops.mesh.primitive_cone_add(
        radius1=radius_bottom, radius2=radius_top,
        depth=height, vertices=segments,
        location=location
    )
    obj = bpy.context.active_object
    obj.name = name
    return obj

# Helper for smooth joint spheres
def create_joint(name, radius, location):
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=radius, segments=12, ring_count=8,
        location=location
    )
    obj = bpy.context.active_object
    obj.name = name
    return obj


# Create base: base (25mm beveled)
bpy.ops.mesh.primitive_cylinder_add(
    radius=0.0125, depth=0.003, vertices=64,
    location=(0, 0, 0.0015)
)
base = bpy.context.active_object
base.name = "base"

# Add bevel for finished edge
mod = base.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 0.0006
mod.segments = 2
bpy.ops.object.modifier_apply(modifier="Bevel")


# Create heroic leg: leg_R (R side, combat_stance pose)
x_mult = 1

# Hip joint
create_joint("leg_R_hip_joint", 0.0007000000000000001, (0.0013440000000000001, 0, 0.014759999999999999))

# Upper leg - tapered and muscular
upper_center = (
    0.0013440000000000001,
    0 + 0.0006160000000000001 * math.sin(math.radians(20)),
    0.014759999999999999 - 0.0030800000000000003
)
create_tapered_cylinder(
    "leg_R_upper",
    radius_top=0.0007700000000000002,
    radius_bottom=0.0005600000000000001,
    height=0.0061600000000000005,
    location=upper_center,
    segments=12
)
upper = bpy.data.objects["leg_R_upper"]
upper.rotation_euler = (
    math.radians(20),
    math.radians(15),
    0
)

# Knee position
knee_pos = (
    0.0013440000000000001 + 0.000924 * math.sin(math.radians(15)) * x_mult,
    0 + 0.0012320000000000002 * math.sin(math.radians(20)),
    0.014759999999999999 - 0.005852
)

# Knee joint
create_joint("leg_R_knee_joint", 0.0004900000000000001, knee_pos)

# Knee cap
bpy.ops.mesh.primitive_uv_sphere_add(
    radius=0.00035000000000000005, segments=8, ring_count=6,
    location=(knee_pos[0], knee_pos[1] + 0.00028000000000000003, knee_pos[2])
)
kneecap = bpy.context.active_object
kneecap.name = "leg_R_kneecap"
kneecap.scale = (0.8, 0.5, 0.8)

# Lower leg
lower_center = (
    knee_pos[0],
    knee_pos[1] + 0.000252,
    knee_pos[2] - 0.00252
)
create_tapered_cylinder(
    "leg_R_lower",
    radius_top=0.0005600000000000001,
    radius_bottom=0.00035000000000000005,
    height=0.00504,
    location=lower_center,
    segments=12
)
lower = bpy.data.objects["leg_R_lower"]
lower.rotation_euler = (
    math.radians(-10),
    0,
    0
)

# Ankle position
ankle_pos = (
    knee_pos[0],
    knee_pos[1],
    knee_pos[2] - 0.00504
)

# Foot - chunky heroic style
bpy.ops.mesh.primitive_cube_add(
    size=0.0022400000000000002,
    location=(ankle_pos[0], ankle_pos[1] + 0.0006720000000000001, ankle_pos[2] - 0.00033600000000000004)
)
foot = bpy.context.active_object
foot.name = "leg_R_foot"
foot.scale = (0.5, 1.0, 0.3)

# Toe cap
bpy.ops.mesh.primitive_uv_sphere_add(
    radius=0.0005600000000000001, segments=8, ring_count=6,
    location=(ankle_pos[0], ankle_pos[1] + 0.0015680000000000002, ankle_pos[2] - 0.00033600000000000004)
)
toe = bpy.context.active_object
toe.name = "leg_R_toe"
toe.scale = (0.8, 0.8, 0.5)

# Join leg parts
bpy.ops.object.select_all(action='DESELECT')
for obj in bpy.data.objects:
    if obj.name.startswith("leg_R_"):
        obj.select_set(True)
bpy.context.view_layer.objects.active = upper
bpy.ops.object.join()
upper.name = "leg_R"

mod = upper.modifiers.new(name="Subsurf", type='SUBSURF')
mod.levels = 1
bpy.ops.object.modifier_apply(modifier="Subsurf")


# Create heroic leg: leg_L (L side, combat_stance pose)
x_mult = -1

# Hip joint
create_joint("leg_L_hip_joint", 0.0007000000000000001, (-0.0013440000000000001, 0, 0.014759999999999999))

# Upper leg - tapered and muscular
upper_center = (
    -0.0013440000000000001,
    0 + 0.0006160000000000001 * math.sin(math.radians(10)),
    0.014759999999999999 - 0.0030800000000000003
)
create_tapered_cylinder(
    "leg_L_upper",
    radius_top=0.0007700000000000002,
    radius_bottom=0.0005600000000000001,
    height=0.0061600000000000005,
    location=upper_center,
    segments=12
)
upper = bpy.data.objects["leg_L_upper"]
upper.rotation_euler = (
    math.radians(10),
    math.radians(-15),
    0
)

# Knee position
knee_pos = (
    -0.0013440000000000001 + 0.000924 * math.sin(math.radians(-15)) * x_mult,
    0 + 0.0012320000000000002 * math.sin(math.radians(10)),
    0.014759999999999999 - 0.005852
)

# Knee joint
create_joint("leg_L_knee_joint", 0.0004900000000000001, knee_pos)

# Knee cap
bpy.ops.mesh.primitive_uv_sphere_add(
    radius=0.00035000000000000005, segments=8, ring_count=6,
    location=(knee_pos[0], knee_pos[1] + 0.00028000000000000003, knee_pos[2])
)
kneecap = bpy.context.active_object
kneecap.name = "leg_L_kneecap"
kneecap.scale = (0.8, 0.5, 0.8)

# Lower leg
lower_center = (
    knee_pos[0],
    knee_pos[1] + 0.000252,
    knee_pos[2] - 0.00252
)
create_tapered_cylinder(
    "leg_L_lower",
    radius_top=0.0005600000000000001,
    radius_bottom=0.00035000000000000005,
    height=0.00504,
    location=lower_center,
    segments=12
)
lower = bpy.data.objects["leg_L_lower"]
lower.rotation_euler = (
    math.radians(-10),
    0,
    0
)

# Ankle position
ankle_pos = (
    knee_pos[0],
    knee_pos[1],
    knee_pos[2] - 0.00504
)

# Foot - chunky heroic style
bpy.ops.mesh.primitive_cube_add(
    size=0.0022400000000000002,
    location=(ankle_pos[0], ankle_pos[1] + 0.0006720000000000001, ankle_pos[2] - 0.00033600000000000004)
)
foot = bpy.context.active_object
foot.name = "leg_L_foot"
foot.scale = (0.5, 1.0, 0.3)

# Toe cap
bpy.ops.mesh.primitive_uv_sphere_add(
    radius=0.0005600000000000001, segments=8, ring_count=6,
    location=(ankle_pos[0], ankle_pos[1] + 0.0015680000000000002, ankle_pos[2] - 0.00033600000000000004)
)
toe = bpy.context.active_object
toe.name = "leg_L_toe"
toe.scale = (0.8, 0.8, 0.5)

# Join leg parts
bpy.ops.object.select_all(action='DESELECT')
for obj in bpy.data.objects:
    if obj.name.startswith("leg_L_"):
        obj.select_set(True)
bpy.context.view_layer.objects.active = upper
bpy.ops.object.join()
upper.name = "leg_L"

mod = upper.modifiers.new(name="Subsurf", type='SUBSURF')
mod.levels = 1
bpy.ops.object.modifier_apply(modifier="Subsurf")


# Create heroic torso: torso
# Main chest - tapered for V-shape
create_tapered_cylinder(
    "torso_chest",
    radius_top=0.00336,
    radius_bottom=0.002156000000000001,
    height=0.007840000000000001,
    location=(0, 0, 0.020679999999999997),
    segments=12
)
chest = bpy.data.objects["torso_chest"]
chest.scale = (1.0, 0.5, 1.0)

# Pectorals - add heroic muscle definition
for side, x_mult in [("L", -1), ("R", 1)]:
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=0.0012096, segments=12, ring_count=8,
        location=(
            0 + 0.0012096 * x_mult,
            0 + 0.001176,
            0.020679999999999997 + 0.0019600000000000004
        )
    )
    pec = bpy.context.active_object
    pec.name = f"torso_pec_{side}"
    pec.scale = (1.2, 0.5, 0.8)

# Shoulders - rounded caps
for side, x_mult in [("L", -1), ("R", 1)]:
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=0.001008, segments=10, ring_count=8,
        location=(
            0 + 0.003024 * x_mult,
            0,
            0.020679999999999997 + 0.0031360000000000008
        )
    )
    shoulder = bpy.context.active_object
    shoulder.name = f"torso_shoulder_{side}"


# Plate armor: breastplate
bpy.ops.mesh.primitive_cube_add(
    size=0.005376000000000001,
    location=(
        0,
        0 + 0.001512,
        0.020679999999999997 + 0.0011760000000000002
    )
)
breastplate = bpy.context.active_object
breastplate.name = "torso_breastplate"
breastplate.scale = (1.0, 0.15, 0.8)

# Add bevel for armor edge
mod = breastplate.modifiers.new(name="Bevel", type='BEVEL')
mod.width = 5.039999999999999e-05
mod.segments = 2
bpy.ops.object.modifier_apply(modifier="Bevel")

# Pauldrons (shoulder plates)
for side, x_mult in [("L", -1), ("R", 1)]:
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=0.0013440000000000001, segments=12, ring_count=8,
        location=(
            0 + 0.0032256 * x_mult,
            0,
            0.020679999999999997 + 0.0035280000000000008
        )
    )
    pauldron = bpy.context.active_object
    pauldron.name = f"torso_pauldron_{side}"
    pauldron.scale = (1.0, 0.8, 0.6)

    # Pauldron rim
    bpy.ops.mesh.primitive_torus_add(
        major_radius=0.0012096,
        minor_radius=5.039999999999999e-05,
        major_segments=16, minor_segments=8,
        location=(
            0 + 0.0032256 * x_mult,
            0,
            0.020679999999999997 + 0.0029792000000000004
        )
    )
    rim = bpy.context.active_object
    rim.name = f"torso_pauldron_rim_{side}"
    rim.rotation_euler = (0, 0, 0)

# Faulds (waist armor)
bpy.ops.mesh.primitive_cylinder_add(
    radius=0.0028224, depth=0.0019600000000000004, vertices=12,
    location=(
        0,
        0,
        0.020679999999999997 - 0.003920000000000001
    )
)
faulds = bpy.context.active_object
faulds.name = "torso_faulds"
faulds.scale = (1.0, 0.7, 1.0)


# Join torso parts
bpy.ops.object.select_all(action='DESELECT')
for obj in bpy.data.objects:
    if obj.name.startswith("torso_"):
        obj.select_set(True)
chest.select_set(True)
bpy.context.view_layer.objects.active = chest
bpy.ops.object.join()
chest.name = "torso"


# Great Helm - full face coverage
bpy.ops.mesh.primitive_cylinder_add(
    radius=0.002772, depth=0.004536, vertices=16,
    location=(0, 0, 0.02712)
)
helm = bpy.context.active_object
helm.name = "head"
helm.scale = (0.9, 0.85, 1.0)

# Flat top
bpy.ops.mesh.primitive_cylinder_add(
    radius=0.00252, depth=0.000756, vertices=16,
    location=(0, 0, 0.029387999999999997)
)
top = bpy.context.active_object
top.name = "head_top"

# Eye slit - carved out detail
bpy.ops.mesh.primitive_cube_add(
    size=0.003024,
    location=(0, 0.002016, 0.027624)
)
slit = bpy.context.active_object
slit.name = "head_slit"
slit.scale = (0.9, 0.2, 0.15)

# Breathing holes
hole_h = 0.00504
hole_loc = (0, 0, 0.02712)
for i, x_off in enumerate([-0.15, 0, 0.15]):
    for j, z_off in enumerate([-0.2, -0.1, 0]):
        bpy.ops.mesh.primitive_cylinder_add(
            radius=hole_h * 0.02, depth=hole_h * 0.3, vertices=8,
            location=(hole_loc[0] + x_off * hole_h, hole_loc[1] + hole_h * 0.5, hole_loc[2] + z_off * hole_h)
        )
        hole = bpy.context.active_object
        hole.name = f"head_hole_{i}_{j}"
        hole.rotation_euler = (math.radians(90), 0, 0)

# Join helmet parts
bpy.ops.object.select_all(action='DESELECT')
for obj in bpy.data.objects:
    if obj.name.startswith("head"):
        obj.select_set(True)
bpy.context.view_layer.objects.active = helm
bpy.ops.object.join()
helm.name = "head"


# Create heroic arm: arm_R (R side, raised pose)
x_mult = 1

# Shoulder joint
create_joint("arm_R_shoulder_joint", 0.0006720000000000001, (0.003024, 0, 0.024599999999999997))

# Upper arm - tapered
upper_arm_center = (
    0.003024 + 0.00252 * math.sin(math.radians(-120)) * x_mult,
    0 + 0.00252 * math.cos(math.radians(-120)) * math.cos(math.radians(0)),
    0.024599999999999997 - 0.00252 * math.cos(math.radians(-120))
)
create_tapered_cylinder(
    "arm_R_upper",
    radius_top=0.0005040000000000001,
    radius_bottom=0.00039200000000000004,
    height=0.00504,
    location=upper_arm_center,
    segments=10
)
upper = bpy.data.objects["arm_R_upper"]
upper.rotation_euler = (
    math.radians(-120),
    math.radians(0) * x_mult,
    math.radians(-30)
)

# Elbow position
elbow_pos = (
    0.003024 + 0.00504 * math.sin(math.radians(-120)) * x_mult * 0.7,
    0 + 0.001512,
    0.024599999999999997 - 0.0042840000000000005
)

# Elbow joint
create_joint("arm_R_elbow_joint", 0.00044800000000000005, elbow_pos)

# Lower arm
lower_arm_center = (
    elbow_pos[0] + 0.0022400000000000002 * math.sin(math.radians(-45)) * x_mult * 0.5,
    elbow_pos[1] + 0.0017920000000000002,
    elbow_pos[2] - 0.0022400000000000002
)
create_tapered_cylinder(
    "arm_R_lower",
    radius_top=0.00039200000000000004,
    radius_bottom=0.00028000000000000003,
    height=0.0044800000000000005,
    location=lower_arm_center,
    segments=10
)
lower = bpy.data.objects["arm_R_lower"]
lower.rotation_euler = (
    math.radians(-45),
    math.radians(0),
    0
)

# Wrist position
wrist_pos = (
    elbow_pos[0] + 0.004032000000000001 * math.sin(math.radians(-45)) * x_mult * 0.3,
    elbow_pos[1] + 0.0026880000000000003,
    elbow_pos[2] - 0.004032000000000001
)

# Hand - oversized for heroic look
bpy.ops.mesh.primitive_cube_add(
    size=0.00168,
    location=wrist_pos
)
hand = bpy.context.active_object
hand.name = "arm_R_hand"
hand.scale = (0.6, 0.4, 1.0)
hand.rotation_euler = (math.radians(-20), 0, 0)

# Fingers - simplified chunky style
for i, offset in enumerate([-0.3, -0.1, 0.1, 0.3]):
    bpy.ops.mesh.primitive_cylinder_add(
        radius=0.0002016, depth=0.00084, vertices=6,
        location=(
            wrist_pos[0] + offset * 0.00168,
            wrist_pos[1] + 0.000504,
            wrist_pos[2] - 0.0006720000000000001
        )
    )
    finger = bpy.context.active_object
    finger.name = f"arm_R_finger_{i}"
    finger.rotation_euler = (math.radians(30), 0, 0)

# Thumb
bpy.ops.mesh.primitive_cylinder_add(
    radius=0.0002016, depth=0.000588, vertices=6,
    location=(
        wrist_pos[0] + 0.4 * 0.00168 * x_mult,
        wrist_pos[1] + 0.00016800000000000002,
        wrist_pos[2] - 0.00016800000000000002
    )
)
thumb = bpy.context.active_object
thumb.name = "arm_R_thumb"
thumb.rotation_euler = (math.radians(45), math.radians(30) * x_mult, 0)

# Join arm parts
bpy.ops.object.select_all(action='DESELECT')
for obj in bpy.data.objects:
    if obj.name.startswith("arm_R_"):
        obj.select_set(True)
bpy.context.view_layer.objects.active = upper
bpy.ops.object.join()
upper.name = "arm_R"

# Add subdivision for smoother result
mod = upper.modifiers.new(name="Subsurf", type='SUBSURF')
mod.levels = 1
bpy.ops.object.modifier_apply(modifier="Subsurf")


# Create heroic arm: arm_L (L side, holding pose)
x_mult = -1

# Shoulder joint
create_joint("arm_L_shoulder_joint", 0.0006720000000000001, (-0.003024, 0, 0.024599999999999997))

# Upper arm - tapered
upper_arm_center = (
    -0.003024 + 0.00252 * math.sin(math.radians(-45)) * x_mult,
    0 + 0.00252 * math.cos(math.radians(-45)) * math.cos(math.radians(0)),
    0.024599999999999997 - 0.00252 * math.cos(math.radians(-45))
)
create_tapered_cylinder(
    "arm_L_upper",
    radius_top=0.0005040000000000001,
    radius_bottom=0.00039200000000000004,
    height=0.00504,
    location=upper_arm_center,
    segments=10
)
upper = bpy.data.objects["arm_L_upper"]
upper.rotation_euler = (
    math.radians(-45),
    math.radians(0) * x_mult,
    math.radians(15)
)

# Elbow position
elbow_pos = (
    -0.003024 + 0.00504 * math.sin(math.radians(-45)) * x_mult * 0.7,
    0 + 0.001512,
    0.024599999999999997 - 0.0042840000000000005
)

# Elbow joint
create_joint("arm_L_elbow_joint", 0.00044800000000000005, elbow_pos)

# Lower arm
lower_arm_center = (
    elbow_pos[0] + 0.0022400000000000002 * math.sin(math.radians(-90)) * x_mult * 0.5,
    elbow_pos[1] + 0.0017920000000000002,
    elbow_pos[2] - 0.0022400000000000002
)
create_tapered_cylinder(
    "arm_L_lower",
    radius_top=0.00039200000000000004,
    radius_bottom=0.00028000000000000003,
    height=0.0044800000000000005,
    location=lower_arm_center,
    segments=10
)
lower = bpy.data.objects["arm_L_lower"]
lower.rotation_euler = (
    math.radians(-90),
    math.radians(0),
    0
)

# Wrist position
wrist_pos = (
    elbow_pos[0] + 0.004032000000000001 * math.sin(math.radians(-90)) * x_mult * 0.3,
    elbow_pos[1] + 0.0026880000000000003,
    elbow_pos[2] - 0.004032000000000001
)

# Hand - oversized for heroic look
bpy.ops.mesh.primitive_cube_add(
    size=0.00168,
    location=wrist_pos
)
hand = bpy.context.active_object
hand.name = "arm_L_hand"
hand.scale = (0.6, 0.4, 1.0)
hand.rotation_euler = (math.radians(-20), 0, 0)

# Fingers - simplified chunky style
for i, offset in enumerate([-0.3, -0.1, 0.1, 0.3]):
    bpy.ops.mesh.primitive_cylinder_add(
        radius=0.0002016, depth=0.00084, vertices=6,
        location=(
            wrist_pos[0] + offset * 0.00168,
            wrist_pos[1] + 0.000504,
            wrist_pos[2] - 0.0006720000000000001
        )
    )
    finger = bpy.context.active_object
    finger.name = f"arm_L_finger_{i}"
    finger.rotation_euler = (math.radians(30), 0, 0)

# Thumb
bpy.ops.mesh.primitive_cylinder_add(
    radius=0.0002016, depth=0.000588, vertices=6,
    location=(
        wrist_pos[0] + 0.4 * 0.00168 * x_mult,
        wrist_pos[1] + 0.00016800000000000002,
        wrist_pos[2] - 0.00016800000000000002
    )
)
thumb = bpy.context.active_object
thumb.name = "arm_L_thumb"
thumb.rotation_euler = (math.radians(45), math.radians(30) * x_mult, 0)

# Join arm parts
bpy.ops.object.select_all(action='DESELECT')
for obj in bpy.data.objects:
    if obj.name.startswith("arm_L_"):
        obj.select_set(True)
bpy.context.view_layer.objects.active = upper
bpy.ops.object.join()
upper.name = "arm_L"

# Add subdivision for smoother result
mod = upper.modifiers.new(name="Subsurf", type='SUBSURF')
mod.levels = 1
bpy.ops.object.modifier_apply(modifier="Subsurf")


# Create sword: sword (longsword)
blade_length = 0.0196
blade_width = 0.001568
handle_length = 0.0049

# Blade
bpy.ops.mesh.primitive_cube_add(size=1, location=(0.004032, 0.01, 0.039599999999999996))
blade = bpy.context.active_object
blade.name = "sword_blade"
blade.scale = (blade_width, blade_width * 0.3, blade_length * 0.5)
blade.location.z += blade_length * 0.5

# Blade taper (using lattice or manual edit)
# Simplified: add point at tip
bpy.ops.mesh.primitive_cone_add(
    radius1=blade_width, radius2=0,
    depth=blade_length * 0.15, vertices=4,
    location=(0.004032, 0.01, 0.039599999999999996 + blade_length * 0.9)
)
tip = bpy.context.active_object
tip.name = "sword_tip"
tip.scale = (1.0, 0.3, 1.0)

# Crossguard
bpy.ops.mesh.primitive_cube_add(
    size=blade_width * 6,
    location=(0.004032, 0.01, 0.039599999999999996)
)
guard = bpy.context.active_object
guard.name = "sword_guard"
guard.scale = (1.0, 0.3, 0.2)

# Handle/grip
bpy.ops.mesh.primitive_cylinder_add(
    radius=blade_width * 0.7, depth=handle_length, vertices=8,
    location=(0.004032, 0.01, 0.039599999999999996 - handle_length * 0.5)
)
handle = bpy.context.active_object
handle.name = "sword_handle"

# Pommel
bpy.ops.mesh.primitive_uv_sphere_add(
    radius=blade_width * 1.2, segments=8, ring_count=6,
    location=(0.004032, 0.01, 0.039599999999999996 - handle_length)
)
pommel = bpy.context.active_object
pommel.name = "sword_pommel"
pommel.scale = (1.0, 0.6, 0.8)

# Join sword parts
bpy.ops.object.select_all(action='DESELECT')
blade.select_set(True)
tip.select_set(True)
guard.select_set(True)
handle.select_set(True)
pommel.select_set(True)
bpy.context.view_layer.objects.active = blade
bpy.ops.object.join()
blade.name = "sword"


# Create shield: shield (heater)
shield_size = 0.013719999999999998

# Main shield body
bpy.ops.mesh.primitive_cylinder_add(
    radius=shield_size * 0.5, depth=shield_size * 0.08, vertices=32,
    location=(-0.0036960000000000005, 0.01, 0.019599999999999996)
)
shield = bpy.context.active_object
shield.name = "shield"
shield.rotation_euler = (math.radians(90), 0, 0)
shield.scale = (1.0, 1.0, 1.3)  # Elongate for heater shape

# Shield boss (center dome)
bpy.ops.mesh.primitive_uv_sphere_add(
    radius=shield_size * 0.15, segments=12, ring_count=8,
    location=(-0.0036960000000000005, 0.01 + shield_size * 0.05, 0.019599999999999996)
)
boss = bpy.context.active_object
boss.name = "shield_boss"
boss.scale = (1.0, 0.5, 1.0)

# Shield rim
bpy.ops.mesh.primitive_torus_add(
    major_radius=shield_size * 0.48,
    minor_radius=shield_size * 0.03,
    major_segments=32, minor_segments=8,
    location=(-0.0036960000000000005, 0.01, 0.019599999999999996)
)
rim = bpy.context.active_object
rim.name = "shield_rim"
rim.rotation_euler = (math.radians(90), 0, 0)
rim.scale = (1.0, 1.0, 1.3)

# Join shield parts
bpy.ops.object.select_all(action='DESELECT')
shield.select_set(True)
boss.select_set(True)
rim.select_set(True)
bpy.context.view_layer.objects.active = shield
bpy.ops.object.join()
shield.name = "shield"


# Union all parts into: paladin
base_obj = bpy.data.objects["base"]
bpy.context.view_layer.objects.active = base_obj


# Boolean union: leg_R
tool_obj = bpy.data.objects["leg_R"]
mod = base_obj.modifiers.new(name="Bool_0", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Bool_0")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: leg_L
tool_obj = bpy.data.objects["leg_L"]
mod = base_obj.modifiers.new(name="Bool_1", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Bool_1")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: torso
tool_obj = bpy.data.objects["torso"]
mod = base_obj.modifiers.new(name="Bool_2", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Bool_2")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: head
tool_obj = bpy.data.objects["head"]
mod = base_obj.modifiers.new(name="Bool_3", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Bool_3")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: arm_R
tool_obj = bpy.data.objects["arm_R"]
mod = base_obj.modifiers.new(name="Bool_4", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Bool_4")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: arm_L
tool_obj = bpy.data.objects["arm_L"]
mod = base_obj.modifiers.new(name="Bool_5", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Bool_5")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: sword
tool_obj = bpy.data.objects["sword"]
mod = base_obj.modifiers.new(name="Bool_6", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Bool_6")
bpy.data.objects.remove(tool_obj, do_unlink=True)


# Boolean union: shield
tool_obj = bpy.data.objects["shield"]
mod = base_obj.modifiers.new(name="Bool_7", type='BOOLEAN')
mod.operation = 'UNION'
mod.solver = 'EXACT'
mod.object = tool_obj
bpy.ops.object.modifier_apply(modifier="Bool_7")
bpy.data.objects.remove(tool_obj, do_unlink=True)


base_obj.name = "paladin"


# Clean mesh for printing: paladin
obj = bpy.data.objects["paladin"]
bpy.context.view_layer.objects.active = obj
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.remove_doubles(threshold=0.0001)
bpy.ops.mesh.delete_loose()
bpy.ops.mesh.normals_make_consistent(inside=False)
bpy.ops.mesh.select_non_manifold()
try:
    bpy.ops.mesh.fill_holes(sides=4)
except:
    pass
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.mode_set(mode='OBJECT')
print(f"Cleaned: paladin")


# Export STL
bpy.ops.object.select_all(action='SELECT')
bpy.ops.wm.stl_export(
    filepath="C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/characters/paladin-pro.stl",
    export_selected_objects=True,
    global_scale=1.0,
    ascii_format=False
)
print("Exported: C:/Users/Xx LilMan xX/Documents/Claude Docs/dnd/3d-prints/miniatures/characters/paladin-pro.stl")
