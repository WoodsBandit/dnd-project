# FDM Terrain Printing Settings

Optimized settings for printing D&D terrain, dungeon tiles, and scenery.

## Overview

Terrain printing prioritizes speed and material efficiency over fine detail. These settings get you more terrain on the table faster.

---

## Layer Height Profiles

### Draft (0.20mm) - Standard Terrain

Good balance of speed and quality for most terrain.

```
Layer Height:      0.20mm
Initial Layer:     0.24mm
Line Width:        0.44mm (slightly wider = faster)
```

**Print time:** 40-60% faster than 0.12mm
**Best for:** Dungeon tiles, walls, floors, bases

### Fast (0.24mm) - Speed Printing

Maximize output, visible layers acceptable for rough terrain.

```
Layer Height:      0.24mm
Initial Layer:     0.28mm
Line Width:        0.48mm
```

**Print time:** 50-70% faster than 0.12mm
**Best for:** Cave terrain, rocks, rough surfaces, modular tiles

### Turbo (0.28mm with 0.6mm Nozzle) - Maximum Speed

For experienced printers with larger nozzles.

```
Layer Height:      0.28mm
Initial Layer:     0.32mm
Line Width:        0.64mm
Nozzle:            0.6mm required
```

**Print time:** 3-4x faster than mini settings
**Best for:** Large terrain, scatter, quick prototypes

### Quality (0.16mm) - Detailed Terrain

When terrain has important visible details.

```
Layer Height:      0.16mm
Initial Layer:     0.20mm
Line Width:        0.40mm
```

**Best for:** Buildings with details, statues, set pieces

---

## Speed Settings

### Draft Speed (0.20mm)

```
Print Speed:          60mm/s
Outer Wall Speed:     45mm/s
Inner Wall Speed:     70mm/s
Infill Speed:         80mm/s
Top/Bottom Speed:     50mm/s
Travel Speed:         180mm/s
Initial Layer Speed:  25mm/s

Acceleration:         800mm/s2
Jerk:                 10mm/s
```

### Fast Speed (0.24-0.28mm)

```
Print Speed:          80mm/s
Outer Wall Speed:     55mm/s
Inner Wall Speed:     90mm/s
Infill Speed:         100mm/s
Top/Bottom Speed:     60mm/s
Travel Speed:         200mm/s
Initial Layer Speed:  25mm/s

Acceleration:         1000mm/s2
Jerk:                 12mm/s
```

**Note:** Only use fast speeds if your printer is tuned and calibrated.

---

## Infill Patterns for Terrain

### Pattern Comparison

| Pattern | Speed | Strength | Best For |
|---------|-------|----------|----------|
| Lines | Fastest | Low | Flat tiles, bases |
| Grid | Fast | Medium | General terrain |
| Triangles | Medium | High | Stressed pieces |
| Gyroid | Medium | High | Load-bearing terrain |
| Lightning | Fastest | Low | Hollow shells |

### Infill Density by Terrain Type

**Dungeon Tiles (2x2, 4x4):**
```
Infill Density:    5-10%
Infill Pattern:    Lines or Lightning
Reason:            Tiles are flat, walls provide structure
```

**Walls and Pillars:**
```
Infill Density:    10-15%
Infill Pattern:    Grid
Reason:            Need some internal support
```

**Buildings and Towers:**
```
Infill Density:    10-15%
Infill Pattern:    Grid or Triangles
Reason:            Structural integrity matters
```

**Scatter Terrain (rocks, trees, barrels):**
```
Infill Density:    10%
Infill Pattern:    Gyroid
Reason:            Gets handled frequently
```

**Large Set Pieces:**
```
Infill Density:    5-10%
Infill Pattern:    Lightning or Lines
Reason:            Material savings on big prints
```

---

## Wall Settings

```
Wall Count:           2 (sufficient for terrain)
Wall Order:           Outside to Inside
Top Layers:           3 (4 if bridging issues)
Bottom Layers:        3

Top/Bottom Pattern:   Lines (fast)
Top Surface Skin:     Optional (disable for speed)
```

### When to Increase Walls

- Terrain that will be transported
- Pieces that interlock/connect
- Parts that bear weight
- Areas that will be glued

---

## Support Settings for Terrain

Most well-designed terrain shouldn't need supports.

### Minimal Supports

```
Support Enable:       Only when necessary
Support Overhang:     60 degrees (terrain tolerates more)
Support Density:      8-10%
Support Pattern:      Lines (fastest)
Support Interface:    Optional (terrain scars less visible)
Support Z Distance:   0.28mm (easier removal)
```

### Avoiding Supports

- Download "supportless" terrain models
- Orient for self-supporting overhangs
- Use support blockers aggressively
- Accept minor imperfections on undersides

### When Supports Are Worth It

- Arches and doorways (visible)
- Decorative overhangs
- Bridges and catwalks
- Flying buttresses

---

## Modularity Tips

### Modular Tile Systems

**OpenLOCK Clips:**
```
Print Speed:       50mm/s (slower for accuracy)
Layer Height:      0.16mm (tighter tolerances)
Horizontal Expansion: -0.1mm (snug fit)
```

**Dragonlock/Dragonbite:**
```
Similar to OpenLOCK
Test fit clips before batch printing
```

**Magnetic Systems:**
- Print holes slightly undersized
- 6x3mm magnets are common
- Glue in after printing

### Tile Size Recommendations

```
Standard tile:     50mm x 50mm (2" x 2")
Large tile:        100mm x 100mm (4" x 4")
Wall section:      50mm length
Room height:       ~50mm (2") for standard rooms
```

### Batch Printing Tiles

- Fill bed with same tile type
- Use identical settings for consistency
- Print overnight for efficiency
- Number tiles if variants exist

---

## Material Recommendations

### PLA (Best Choice)

```
Temperature:       195-210C
Bed:               55-60C
Cooling:           100%
```

**Pros:** Cheap, easy, low warp, paints well
**Cons:** Brittle if dropped, heat sensitive

### PLA+ (Recommended Upgrade)

```
Temperature:       205-220C
Bed:               60-65C
Cooling:           100%
```

**Pros:** Stronger, still easy to print
**Cons:** Slightly more expensive

### PETG (Durable Option)

```
Temperature:       235-250C
Bed:               70-80C
Cooling:           50-70%
Speed:             -10-15% from PLA speeds
```

**Pros:** Much stronger, heat resistant
**Cons:** Stringing, harder to tune, prints slower

---

## Special Terrain Types

### Dungeon Tiles (Floors)

```
Layer Height:      0.24mm
Infill:            5-10%, Lines
Walls:             2
Speed:             Fast settings
Orientation:       Texture side up
```

### Walls and Barriers

```
Layer Height:      0.20mm
Infill:            10-15%, Grid
Walls:             2
Speed:             Standard settings
Orientation:       Flat or on side
```

### Buildings and Structures

```
Layer Height:      0.16-0.20mm
Infill:            10-15%
Walls:             2-3
Speed:             Standard settings
Consider:          Printing in sections
```

### Natural Terrain (Rocks, Hills)

```
Layer Height:      0.24-0.28mm
Infill:            10%, Gyroid
Walls:             2
Speed:             Fast settings
Notes:             Layer lines add texture
```

### Trees and Vegetation

```
Layer Height:      0.16-0.20mm
Infill:            15%
Walls:             2-3
Supports:          Tree supports if needed
Notes:             Consider resin for small trees
```

### Water Features

```
Layer Height:      0.12-0.16mm (smoother = better)
Infill:            15%
Finish:            Apply gloss varnish or resin coat
Color:             Print in blue/clear PLA
```

---

## Complete Profile: Fast Terrain (0.24mm)

Ready-to-use settings for quick terrain:

```ini
# Quality
layer_height = 0.24
initial_layer_height = 0.28
line_width = 0.48

# Walls
wall_count = 2
wall_order = outside_to_inside
outer_wall_speed = 55
inner_wall_speed = 80

# Top/Bottom
top_layers = 3
bottom_layers = 3
top_bottom_pattern = lines

# Infill
infill_pattern = lines
infill_density = 10
infill_speed = 100

# Speed
print_speed = 70
travel_speed = 180
initial_layer_speed = 25
acceleration = 800

# Temperature
material_print_temperature = 210
material_bed_temperature = 60

# Retraction (Bowden)
retraction_distance = 6
retraction_speed = 45
z_hop_enabled = true
z_hop_height = 0.3

# Cooling
cool_fan_enabled = true
cool_fan_speed = 100

# Support
support_enable = false
# Enable manually when needed
```

---

## Large Format Tips

### Printing Big Terrain

- Split models at natural break points
- Use less infill (5-8%) for material savings
- Consider 0.6mm or 0.8mm nozzle
- Plan for multi-day prints

### Joining Large Pieces

- Pin with paper clips or brass rod
- Use CA glue (super glue) for quick bonds
- Epoxy for structural joints
- Sand mating surfaces for better adhesion
- Magnets for removable sections

### Print Time Estimation

| Terrain Type | Approximate Time (0.20mm) |
|--------------|---------------------------|
| 2x2 tile | 30-60 minutes |
| 4x4 tile | 2-4 hours |
| Wall section | 30-60 minutes |
| Small building | 4-8 hours |
| Large building | 12-24+ hours |
| Full dungeon room | 2-4 hours |

---

## Post-Processing Terrain

### Quick Prep

1. Remove from bed (flex plate helps)
2. Snap off supports (if any)
3. Quick sand any rough spots
4. Prime and paint

### For Better Finish

1. Light sanding (220 grit)
2. Fill layer lines with wood filler or primer
3. Sand again (400 grit)
4. Prime (grey primer shows imperfections)
5. Paint

### Painting Tips for FDM Terrain

- Heavy drybrush hides layer lines
- Washes settle in layer gaps (feature, not bug)
- Textured spray paint covers imperfections
- Matte varnish for final protection

---

## Troubleshooting

### Tiles Not Flat (Warping)

- Ensure bed is clean and level
- Use glue stick or hairspray
- Slow first layer
- Increase bed temperature 5C
- Use brim if needed

### Poor First Layer Adhesion

- Level bed carefully
- Clean with IPA
- Slow initial layer to 20mm/s
- Increase first layer width
- Squish first layer slightly

### Infill Showing Through Top

- Add more top layers (4-5)
- Slow top surface speed
- Increase infill density
- Use monotonic top fill

### Tiles Don't Fit Together

- Calibrate E-steps
- Check horizontal expansion
- Measure and adjust slicer compensation
- Sand if slightly tight

### Stringing on Travel

- Tune retraction
- Enable combing
- Reduce temperature 5C
- Enable Z-hop

### Layer Lines Too Visible

- Accept them (paint covers a lot)
- Reduce layer height to 0.16mm
- Apply filler primer
- Heavy drybrush painting technique
