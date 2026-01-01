# Slicer Profiles Guide

Complete guide to slicer profiles for D&D miniatures, terrain, and props.

## Quick Reference

| Print Type | Layer Height | Speed | Infill | Time Factor |
|------------|--------------|-------|--------|-------------|
| Display Mini | 0.04-0.08mm | 30-40mm/s | 15% | Slowest |
| Gaming Mini | 0.08-0.12mm | 40-50mm/s | 10-15% | Medium |
| Terrain | 0.16-0.20mm | 50-70mm/s | 10% | Fast |
| Props | 0.12-0.16mm | 45-55mm/s | 10-15% | Medium |
| Large Dragons | 0.12-0.16mm | 40-50mm/s | 5-10% | Long |

## Profile Files

- [miniatures-fdm.md](miniatures-fdm.md) - FDM settings for minis
- [miniatures-resin.md](miniatures-resin.md) - Resin settings for minis
- [terrain-fdm.md](terrain-fdm.md) - Terrain printing settings

---

## Recommended Settings by Category

### 28mm Miniatures

Miniatures are the most demanding prints due to fine details and small features.

**FDM Printing:**
- Layer height: 0.08mm (fine) to 0.12mm (gaming quality)
- Nozzle: 0.4mm standard, 0.2mm for extreme detail
- Speed: 30-45mm/s (slower = better detail)
- Walls: 3 minimum for strength
- Supports: Tree supports work best for organic shapes
- Orientation: Print standing upright for best detail on faces

**Resin Printing (Recommended for Minis):**
- Layer height: 0.04-0.05mm
- Exposure: Resin and printer dependent
- Supports: Light supports with 0.3mm contact points
- Orientation: 30-45 degree angle for best results

### Terrain Pieces

Terrain is more forgiving and benefits from faster print speeds.

**Dungeon Tiles:**
- Layer height: 0.20-0.28mm
- Speed: 60-80mm/s
- Infill: 10% (tiles are mostly solid anyway)
- No supports if designed properly
- Consider 0.6mm nozzle for faster prints

**Buildings and Structures:**
- Layer height: 0.16-0.20mm
- Speed: 50-60mm/s
- Infill: 10-15%
- Minimal supports

**Scatter Terrain (rocks, trees, barrels):**
- Layer height: 0.12-0.16mm
- Treat more like minis if detailed
- Use supports sparingly

### Props and Accessories

**Small Props (coins, keys, potions):**
- Layer height: 0.08-0.12mm
- Consider resin for best results
- Light supports

**Larger Props (chests, furniture, doors):**
- Layer height: 0.12-0.16mm
- FDM works well
- 10-15% infill

**Weapons and Items (for display):**
- Layer height: 0.08mm
- Print flat when possible
- Sand and prime for best finish

---

## Material Recommendations

### FDM Materials

**PLA (Recommended for Most Prints)**
- Easy to print, low warping
- Good detail retention
- Temperature: 190-215C nozzle, 60C bed
- Best for: Minis, terrain, props
- Downsides: Brittle, heat sensitive

**PLA+ (Premium PLA)**
- Stronger than regular PLA
- Slightly better heat resistance
- Temperature: 205-220C nozzle, 60-65C bed
- Best for: Gaming pieces that get handled
- Worth the extra cost for minis

**PETG**
- Stronger and more flexible than PLA
- Temperature: 230-250C nozzle, 70-80C bed
- Best for: Durable terrain, game boards
- Downsides: More stringing, harder to dial in

**ABS (Not Recommended)**
- Requires enclosure
- Fumes are unpleasant
- Warping issues
- Skip unless you have specific needs

### Resin Materials

**Standard Grey/White Resin**
- Best for general mini printing
- Easy to cure, good detail
- Brittle when thin
- Most cost effective

**ABS-Like Resin**
- More durable than standard
- Good for gaming pieces
- Slightly less detail
- Worth it for tabletop use

**Water-Washable Resin**
- Easier cleanup (no IPA needed)
- Slightly softer
- Good for beginners

**Plant-Based/Eco Resin**
- Lower odor
- Variable quality by brand
- Good option if ventilation is limited

---

## Support Settings

### FDM Supports

**Tree Supports (Preferred for Minis)**
```
Type: Tree
Branch Angle: 40-45 degrees
Branch Diameter: 2.5mm
Support Density: 10-15%
Z Distance: 0.2mm
XY Distance: 0.7mm
```

**Normal Supports (Good for Terrain)**
```
Type: Normal
Pattern: Zig Zag or Lines
Density: 10-15%
Z Distance: 0.2mm
XY Distance: 0.8mm
Support Interface: Yes, 2 layers
```

**Tips:**
- Enable support interface for easier removal
- Paint-on supports in slicer for problem areas
- Angle model to minimize support needs
- Supports on build plate only when possible

### Resin Supports

**Light Supports (Preferred for Minis)**
```
Contact Diameter: 0.3mm
Connection Shape: Sphere
Upper Diameter: 0.5mm
Lower Diameter: 0.8mm
Base Height: 5mm
```

**Medium Supports (Large Models)**
```
Contact Diameter: 0.4-0.5mm
Connection Shape: Cone
Upper Diameter: 0.6mm
Lower Diameter: 1.0mm
Base Height: 5mm
```

**Tips:**
- Place supports on hidden areas (back, underarms, bases)
- Ensure island areas are supported
- Use auto-supports then manually adjust
- More supports = safer but more cleanup

---

## Layer Height Guidelines

| Layer Height | Use Case | Print Time | Detail Level |
|--------------|----------|------------|--------------|
| 0.04mm | Display minis (resin) | Very slow | Exceptional |
| 0.05mm | Quality minis (resin) | Slow | Excellent |
| 0.08mm | Fine minis (FDM/resin) | Slow | Very good |
| 0.10mm | Balanced minis | Medium | Good |
| 0.12mm | Gaming minis | Medium | Good |
| 0.16mm | Large models, props | Faster | Acceptable |
| 0.20mm | Terrain, bases | Fast | Visible layers |
| 0.24mm | Quick terrain | Very fast | Obvious layers |
| 0.28mm | Draft/test prints | Fastest | Rough |

**Rule of Thumb:**
- Faces and hands: Use finest layer height
- Bodies and armor: Standard layer height is fine
- Bases and terrain: Thicker layers save time

---

## Infill Recommendations

### Infill Patterns

| Pattern | Strength | Speed | Use Case |
|---------|----------|-------|----------|
| Grid | Good | Fast | General use |
| Gyroid | Excellent | Medium | Minis, stressed parts |
| Cubic | Very good | Medium | Large models |
| Lines | Low | Fastest | Terrain, bases |
| Lightning | Low | Fastest | Hollow terrain |

### Infill Percentages

| Infill % | Use Case |
|----------|----------|
| 0-5% | Hollow terrain pieces |
| 10% | Standard terrain, large models |
| 15% | Minis, props |
| 20% | Gaming pieces that get handled |
| 100% | Thin parts, weapon props |

**Tips:**
- Minis don't need high infill (they're small)
- Terrain can often be nearly hollow
- Increase infill for pieces that will be glued
- Weight can be added with sand in hollow bases

---

## Print Orientation

### Miniatures
- **Standard pose:** Print upright on feet/base
- **Dynamic pose:** Slight tilt (10-15 degrees)
- **Flying models:** 45 degree angle on supports
- **Large monsters:** Consider splitting

### Terrain
- **Tiles:** Print flat, texture side up
- **Walls:** Print flat or on side
- **Towers:** Print upright in sections
- **Rocks/trees:** Orientation depends on detail

### Props
- **Weapons:** Print flat for strength
- **Furniture:** Upright usually works
- **Containers:** Might need rotation for overhangs

---

## Print Speed by Feature

```
First Layer: 20mm/s (always slow)
Outer Walls: 30-40mm/s (visible surface)
Inner Walls: 40-60mm/s (hidden)
Infill: 50-80mm/s (interior)
Top/Bottom: 35-50mm/s (solid layers)
Supports: 50-80mm/s (not visible)
Travel: 150-200mm/s (non-printing moves)
```

**Note:** These are conservative speeds. Tune for your printer.

---

## File Organization

Save profiles with consistent naming:

```
[printer]-[material]-[quality]-[purpose].ini
```

Examples:
- `ender3-pla-fine-minis.ini`
- `ender3-pla-draft-terrain.ini`
- `mars3-standard-mini.lys`

See individual profile files for complete settings.
