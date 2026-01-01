# Resin Miniature Printing Settings

Complete resin printer settings for 28mm D&D miniatures.

## Overview

Resin printing produces the best detail for miniatures. These settings focus on capturing fine features while ensuring print success.

---

## Layer Height Profiles

### Ultra Fine (0.04mm) - Museum Quality

Maximum detail for display pieces and painting competition minis.

```
Layer Height:      0.04mm (40 microns)
Print Time Impact: ~50% longer than standard
```

**When to use:** Display pieces, hero minis, competition entries

### Fine (0.05mm) - High Quality

Best balance of detail and print time. Recommended for most minis.

```
Layer Height:      0.05mm (50 microns)
Print Time Impact: Baseline
```

**When to use:** Player characters, boss monsters, named NPCs

### Standard (0.08mm) - Gaming Quality

Faster printing with good detail at tabletop distance.

```
Layer Height:      0.08mm (80 microns)
Print Time Impact: ~35% faster than fine
```

**When to use:** Horde enemies, generic monsters, prototyping

---

## Exposure Settings

**Critical:** Exposure times vary significantly by printer, resin, and even room temperature. Use these as starting points only.

### Mono LCD Printers (Mars 3, Saturn, Photon Mono)

**Standard Grey Resin:**
```
Bottom Exposure:     25-35 seconds (5-8 layers)
Normal Exposure:     2.0-3.0 seconds
UV Wavelength:       405nm
```

**ABS-Like Resin:**
```
Bottom Exposure:     30-40 seconds
Normal Exposure:     2.5-3.5 seconds
```

**Water-Washable Resin:**
```
Bottom Exposure:     30-45 seconds
Normal Exposure:     2.5-4.0 seconds
Note: Tends to need longer exposure
```

### Older RGB LCD Printers

Approximately 3-4x longer exposure than mono printers.

```
Bottom Exposure:     60-90 seconds
Normal Exposure:     8-12 seconds
```

### Calibrating Exposure

1. Print an exposure test (XP2 validation matrix, Cones of Calibration)
2. Adjust in 0.2-0.3 second increments
3. Under-exposure: Details wash out, layers separate
4. Over-exposure: Details blob together, supports fused

---

## Lift Settings

Controls how the build plate rises between layers.

### Standard Settings

```
Lift Height:         6mm
Lift Speed:          60mm/min (1mm/s)
Retract Speed:       150mm/min (2.5mm/s)
Light-off Delay:     1-2 seconds
```

### Optimized Settings (After Tuning)

```
Lift Height:         5mm (can reduce to 4mm for small models)
Lift Speed:          90mm/min
Retract Speed:       180mm/min
Light-off Delay:     0.5-1 second
```

### Bottom Layer Settings

```
Bottom Lift Height:  8mm
Bottom Lift Speed:   40mm/min (slower for adhesion)
Bottom Layer Count:  5-8 layers
```

**Tips:**
- Slower lift = safer but longer print
- Higher lift height = more resin flow time
- Reduce lift height for small, low-suction prints
- Large flat surfaces need slower lifts

---

## Support Settings

### Light Supports (Recommended for Minis)

```
Contact Diameter:    0.30mm
Contact Depth:       0.30mm
Connection Shape:    Sphere
Upper Diameter:      0.40mm
Middle Diameter:     0.60mm
Lower Diameter:      0.80mm
Base Diameter:       3.0mm
Base Height:         3.0mm

Support Density:     50-70% auto-generated coverage
```

### Medium Supports (For Larger/Heavier Models)

```
Contact Diameter:    0.40mm
Contact Depth:       0.40mm
Connection Shape:    Cone
Upper Diameter:      0.60mm
Middle Diameter:     0.80mm
Lower Diameter:      1.00mm
Base Diameter:       4.0mm
Base Height:         4.0mm
```

### Heavy Supports (Large Models, Islands)

```
Contact Diameter:    0.50mm
Contact Depth:       0.50mm
Upper Diameter:      0.80mm
Middle Diameter:     1.20mm
Lower Diameter:      1.50mm
Base Diameter:       5.0mm
Base Height:         5.0mm
```

### Support Strategy

1. Start with auto-supports at 50% density
2. Check for unsupported islands (use slicer detection)
3. Add supports to:
   - Any island areas
   - Overhangs beyond 45 degrees
   - Thin protruding features (swords, fingers)
   - Bottom of weapons, capes, tails
4. Remove supports from:
   - Faces (when possible)
   - Detailed front surfaces
5. Increase support contact for:
   - Heavy overhangs
   - Parts with high suction
   - Known failure points

---

## Orientation Tips

Proper orientation is critical for resin printing success.

### Recommended Orientations

**Standard Humanoid:**
- Tilt back 25-35 degrees
- Slight rotation off-axis (5-10 degrees)
- Supports fall on back, not face

**Dynamic Poses:**
- Find angle that minimizes islands
- Support heavy extended limbs
- Consider splitting for complex poses

**Flat-Based Models:**
- Can print directly on base (skip supports)
- Requires perfectly level bed
- Risk: suction failure on large flat areas

**Flying/Mounted Models:**
- 30-45 degree angle
- Heavy support on mounting points
- Consider printing separately and gluing

### Orientation Goals

1. **Minimize islands** - Every layer needs connection
2. **Protect faces** - Orient so face is last to print
3. **Reduce suction** - Avoid large flat cross-sections
4. **Support accessibility** - Place supports where they're easy to remove
5. **Structural strength** - Print direction affects strength

### Cross-Section Analysis

Use slicer's layer preview to check:
- No sudden large cross-sections
- Gradual transitions between layers
- Islands are supported
- Faces print late (near top)

---

## Anti-Aliasing Settings

Smooths layer edges for better surface finish.

```
Anti-Aliasing:       Enabled
AA Level:            4-8 (higher = smoother, longer cure)
Grey Levels:         4-8
Image Blur:          2 pixels (if available)
```

**Note:** Higher AA needs slightly longer exposure.

---

## Printer-Specific Notes

### Elegoo Mars 3 / Mars 3 Pro

```
Layer Height:        0.05mm
Bottom Exposure:     25-30s
Normal Exposure:     2.0-2.5s
Bottom Layers:       6
Lift Height:         6mm
Lift Speed:          60mm/min
```

### Anycubic Photon Mono 4K / M3

```
Layer Height:        0.05mm
Bottom Exposure:     28-35s
Normal Exposure:     2.2-2.8s
Bottom Layers:       5
Lift Height:         6mm
Lift Speed:          60mm/min
```

### Elegoo Saturn 2 / Saturn 3

```
Layer Height:        0.05mm
Bottom Exposure:     25-30s
Normal Exposure:     2.0-2.5s
Bottom Layers:       6
Lift Height:         7mm (larger vat)
Lift Speed:          50mm/min
```

### Phrozen Sonic Mini / Mighty

```
Layer Height:        0.05mm
Bottom Exposure:     20-28s
Normal Exposure:     1.8-2.2s
Bottom Layers:       5
Lift Height:         6mm
Lift Speed:          60mm/min
```

---

## Complete Profile: Quality Mini (0.05mm)

Ready-to-use baseline settings:

```
# Layer Settings
layer_height = 0.05
bottom_layers = 6

# Exposure (ADJUST FOR YOUR RESIN)
bottom_exposure = 28
normal_exposure = 2.2

# Lift Settings
lift_height = 6
lift_speed = 60
retract_speed = 150
light_off_delay = 1

# Anti-Aliasing
anti_aliasing = enabled
aa_level = 4

# Support Settings (Light)
support_contact_diameter = 0.3
support_contact_depth = 0.3
support_top_diameter = 0.4
support_middle_diameter = 0.6
support_bottom_diameter = 0.8
```

---

## Post-Processing

### Washing

**IPA (Isopropyl Alcohol) Method:**
```
First wash:   2-3 minutes in dirty IPA (removes bulk resin)
Second wash:  2-3 minutes in clean IPA (final clean)
Air dry:      10-15 minutes before curing
```

**Water-Washable Resin:**
```
Wash:         2-4 minutes in water
Air dry:      15-20 minutes (water takes longer)
Note:         Don't pour resin water down drain - cure first
```

### Curing

```
UV Wavelength: 405nm
Cure Time:     3-6 minutes per side
Temperature:   40-50C helps (optional)
Turn/Rotate:   Ensure all surfaces get exposed
```

**Cure Station Tips:**
- Remove supports before curing (easier removal)
- Or cure with supports, then remove (stronger joints)
- Don't over-cure (becomes brittle, yellows)
- Water submersion cure for clear resins

### Support Removal

1. Let print drip excess resin
2. Light wash before removal (softens residue)
3. Use flush cutters for thick supports
4. Use hobby knife for stubborn nubs
5. Light sanding for cleanup (400-600 grit)
6. Fill any divots with UV resin, cure

---

## Troubleshooting

### Print Stuck to FEP, Not Building

- Increase bottom exposure (5-10s)
- Clean build plate with IPA
- Sand build plate lightly
- Check FEP for damage
- Ensure resin is mixed well

### Supports Failing Mid-Print

- Increase support density
- Add medium supports to heavy areas
- Check for unsupported islands
- Increase contact diameter
- Slow lift speed

### Details Mushy/Blobbed

- Decrease exposure time (0.2s increments)
- Check resin temperature (warm = faster cure)
- Ensure AA is enabled
- Check for light bleed

### Fine Details Missing

- Increase exposure slightly
- Check orientation (details at good angle?)
- Use finer layer height
- Verify supports aren't blocking

### Layer Separation / Delamination

- Increase exposure time
- Reduce lift speed
- Increase lift height
- Check resin expiration
- Shake/mix resin thoroughly

### Print Warping

- Add more supports to thin areas
- Cure in stages
- Don't over-cure
- Consider resin type (ABS-like less warpy)

### Cloudy/Rough Surface

- Replace dirty IPA
- Don't wash too long
- Ensure fully dry before curing
- Check FEP for scratches

---

## Safety Reminders

- **Always wear gloves** when handling uncured resin
- **Work in ventilated area** - resin fumes are harmful
- **UV protection** - don't expose skin/eyes to curing light
- **Dispose properly** - cure resin waste before trash
- **No drain disposal** - never pour liquid resin down drain
- **Keep away from pets/children** - resin is toxic
