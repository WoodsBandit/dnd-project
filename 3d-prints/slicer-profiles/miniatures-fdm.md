# FDM Miniature Printing Settings

Complete FDM slicer settings for 28mm D&D miniatures.

## Overview

FDM printing minis requires careful tuning. These settings prioritize detail over speed.

---

## Layer Height Profiles

### Ultra Fine (0.08mm) - Display Quality

Best for hero minis, display pieces, and high-detail characters.

```
Layer Height:      0.08mm
Initial Layer:     0.12mm
Line Width:        0.40mm
Initial Line Width: 0.42mm
```

**Print time:** ~3-6 hours for standard mini
**When to use:** Player characters, boss monsters, display pieces

### Fine (0.10mm) - High Quality

Good balance of detail and time for important minis.

```
Layer Height:      0.10mm
Initial Layer:     0.16mm
Line Width:        0.40mm
Initial Line Width: 0.42mm
```

**Print time:** ~2-4 hours for standard mini
**When to use:** Named NPCs, recurring monsters

### Standard (0.12mm) - Gaming Quality

Acceptable detail for tabletop distance, faster printing.

```
Layer Height:      0.12mm
Initial Layer:     0.20mm
Line Width:        0.40mm
Initial Line Width: 0.44mm
```

**Print time:** ~1.5-3 hours for standard mini
**When to use:** Generic monsters, horde enemies, testing

---

## Nozzle Recommendations

### 0.4mm Nozzle (Standard)

Works for most minis with proper tuning.

```
Line Width: 0.40mm
Minimum Wall Width: 0.35mm
Enable Thin Walls: Yes
```

**Good for:** Most miniatures, terrain, general printing

### 0.2mm Nozzle (Detail)

Maximum detail for small features.

```
Line Width: 0.20mm (can go to 0.25mm)
Minimum Wall Width: 0.18mm
Layer Height: 0.04-0.08mm
Print Speed: 20-30mm/s
```

**Good for:** Faces, hands, weapons, jewelry, tiny details
**Note:** Much slower, clogs more easily, requires patience

### 0.3mm Nozzle (Balanced)

Good compromise between 0.4mm and 0.2mm.

```
Line Width: 0.30mm
Minimum Wall Width: 0.25mm
Layer Height: 0.06-0.10mm
```

**Good for:** Detailed minis without extreme slowdown

---

## Wall and Shell Settings

```
Wall Count:           3 (minimum for strength)
Wall Order:           Outside to Inside (better surface)
Outer Wall Speed:     35mm/s
Inner Wall Speed:     50mm/s

Top Layers:           4
Bottom Layers:        4
Top/Bottom Pattern:   Lines
Top Surface Skin:     Enabled (0.08mm if available)

Horizontal Expansion: -0.02mm (compensate for bulge)
```

---

## Temperature Settings

### PLA

```
Nozzle Temperature:   200-210C (start at 205C)
Build Plate:          60C
Build Plate Initial:  65C (better adhesion)
Standby Temperature:  160C
```

### PLA+

```
Nozzle Temperature:   210-220C (start at 215C)
Build Plate:          60-65C
Build Plate Initial:  70C
```

**Tips:**
- Run a temperature tower for your specific filament
- Lower temps = slightly better detail, higher stringing risk
- Higher temps = better layer adhesion, more oozing

---

## Speed Settings

Conservative speeds for maximum detail:

```
Print Speed:          40mm/s (general)
Outer Wall Speed:     30mm/s (most visible)
Inner Wall Speed:     50mm/s
Top/Bottom Speed:     35mm/s
Infill Speed:         60mm/s
Support Speed:        50mm/s
Travel Speed:         150mm/s
Initial Layer Speed:  20mm/s

Acceleration:         500mm/s2 (reduce if ringing occurs)
Jerk:                 8mm/s
```

### Speed Adjustments by Quality

| Setting | Ultra (0.08mm) | Fine (0.10mm) | Standard (0.12mm) |
|---------|----------------|---------------|-------------------|
| Outer Wall | 25mm/s | 30mm/s | 40mm/s |
| Inner Wall | 40mm/s | 50mm/s | 60mm/s |
| Infill | 50mm/s | 60mm/s | 80mm/s |
| Overall | 35mm/s | 40mm/s | 50mm/s |

---

## Infill Settings

```
Infill Density:       15%
Infill Pattern:       Gyroid (or Grid)
Infill Line Width:    0.40mm
Infill Speed:         60mm/s
Connect Infill Lines: Yes
```

**Pattern Comparison:**
- **Gyroid:** Strongest, best for minis, slightly slower
- **Grid:** Fast, adequate strength
- **Cubic:** Good all-around, moderate speed

---

## Support Settings

### Tree Supports (Recommended)

```
Support Structure:    Tree
Support Placement:    Everywhere (or Touching Buildplate)
Support Overhang Angle: 50 degrees
Support Density:      12-15%

Tree Support Branch Angle:    40 degrees
Tree Support Branch Diameter: 2.5mm
Tree Support Branch Distance: 1mm
Tree Support Trunk Diameter:  3mm
```

### Regular Supports (Alternative)

```
Support Structure:    Normal
Support Pattern:      Zig Zag
Support Density:      15%
Support Z Distance:   0.2mm
Support X/Y Distance: 0.7mm
Support Interface:    Enabled
Interface Density:    80%
Interface Layers:     2
```

### Support Tips

- **Tree supports** leave less scarring on organic shapes
- Enable **Support Interface** for easier removal
- Use **Paint-on supports** in slicer for problem areas
- Consider **Support Blocker** to prevent supports on faces
- Angle model slightly to reduce support needs

---

## Retraction Settings

### Bowden Setup (Ender 3, etc.)

```
Retraction Distance:       6mm (5-7mm range)
Retraction Speed:          45mm/s
Retraction Extra Prime:    0mm
Retraction Minimum Travel: 1.5mm
Maximum Retraction Count:  100
Minimum Extrusion Window:  6mm
```

### Direct Drive Setup

```
Retraction Distance:       1-2mm
Retraction Speed:          35mm/s
Retraction Extra Prime:    0mm
Retraction Minimum Travel: 1mm
Maximum Retraction Count:  100
```

### Anti-Stringing Settings

```
Combing Mode:              All (or Not in Skin)
Z Hop When Retracted:      Yes
Z Hop Height:              0.2mm
Z Hop After Extruder Switch: Yes
```

---

## Cooling Settings

```
Enable Print Cooling: Yes
Fan Speed:            100%
Initial Fan Speed:    0%
Regular Fan at Layer: 3
Regular/Maximum Fan Threshold: 10s

Minimum Layer Time:   10s
Minimum Speed:        15mm/s
Lift Head:            No
```

**Tips:**
- Minis need maximum cooling for small features
- Point cooling fan at nozzle area, not bed
- Consider part cooling duct upgrades (Hero Me, Satsana)

---

## Special Settings

### Thin Feature Handling

```
Enable Thin Walls:    Yes
Minimum Wall Width:   0.35mm (0.4mm nozzle)
Fill Gaps Between Walls: Everywhere
Filter Out Tiny Gaps: Yes
```

### Ironing (Optional for Flat Surfaces)

```
Enable Ironing:       Yes (only for flat tops)
Ironing Pattern:      Zig Zag
Ironing Line Spacing: 0.1mm
Ironing Flow:         10%
Ironing Speed:        16.6mm/s
```

**Note:** Only use ironing on models with flat top surfaces.

---

## Adhesion Settings

```
Build Plate Adhesion: Skirt (or Brim)
Skirt Line Count:     3
Skirt Distance:       5mm

# If using Brim (better adhesion)
Brim Width:           3mm
Brim Only on Outside: Yes
```

**When to use Brim:**
- Small contact area with bed
- Tall, narrow minis
- Models that tend to lift

---

## Complete Profile: Gaming Mini (0.12mm)

Ready-to-use settings for standard gaming miniatures:

```ini
# Quality
layer_height = 0.12
initial_layer_height = 0.20
line_width = 0.4

# Walls
wall_count = 3
wall_order = outside_to_inside
outer_wall_speed = 35
inner_wall_speed = 50

# Top/Bottom
top_layers = 4
bottom_layers = 4
top_bottom_pattern = lines

# Infill
infill_pattern = gyroid
infill_density = 15
infill_speed = 60

# Speed
print_speed = 45
travel_speed = 150
initial_layer_speed = 20
acceleration = 500

# Temperature (adjust for your filament)
material_print_temperature = 205
material_bed_temperature = 60
material_initial_print_temperature = 210

# Retraction (Bowden)
retraction_distance = 6
retraction_speed = 45
retraction_combing = all
z_hop_enabled = true
z_hop_height = 0.2

# Cooling
cool_fan_enabled = true
cool_fan_speed = 100
cool_min_layer_time = 10

# Support
support_enable = true
support_structure = tree
support_angle = 50
support_density = 15
```

---

## Troubleshooting

### Stringing Between Parts
- Increase retraction distance (0.5mm increments)
- Enable coasting (0.04-0.08mm)
- Lower temperature 5C
- Enable Z-hop

### Layer Lines Too Visible
- Reduce layer height
- Slow outer wall speed
- Enable ironing for flat surfaces
- Orient model for best visible angle

### Small Features Breaking
- Print slower
- Increase wall count
- Check thin wall settings
- Consider 0.2mm nozzle

### Supports Hard to Remove
- Increase Z distance (0.24mm)
- Enable support interface
- Reduce support density
- Use tree supports instead

### Elephant Foot (First Layer Bulge)
- Level bed properly
- Reduce initial layer flow (95-98%)
- Increase initial layer height
- Set horizontal expansion to -0.1mm for first layer

### Rough Top Surfaces
- Add top layers (5-6)
- Enable ironing
- Reduce top surface speed
- Check for cooling issues
