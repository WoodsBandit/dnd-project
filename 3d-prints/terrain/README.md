# Terrain

Modular dungeon tiles, buildings, and landscape pieces for tabletop gaming.

## Modular Terrain Systems

### OpenLOCK
- **Grid:** 1" squares (25.4mm)
- **Tile Sizes:** 2x2, 2x4, 4x4 inches
- **Connector:** Clip-based locking system
- **Sources:** Printable Scenery, community designs
- **Pros:** Wide compatibility, huge library
- **Cons:** Clips can be fiddly

### Dragonlock
- **Grid:** 1" squares
- **Tile Sizes:** 2x2, 2x4 standard
- **Connector:** Peg and hole system
- **Sources:** Fat Dragon Games
- **Pros:** Very sturdy connection, good detail
- **Cons:** Proprietary system

### OpenForge
- **Grid:** 1" squares
- **Tile Sizes:** Various
- **Connector:** Multiple options (magnetic, clip, base)
- **Sources:** Devon Jones / Community
- **Pros:** Free, highly customizable
- **Cons:** Many versions can be confusing

### Rampage
- **Grid:** 1" squares
- **Tile Sizes:** Modular wall and floor system
- **Sources:** Printable Scenery
- **Pros:** Stackable, good for multi-level

### Custom/Standalone
- Non-modular terrain pieces
- One-off buildings and set pieces
- Scatter terrain

## Tile Sizing Standards

| Size | Grid Squares | Real Size (inches) | Common Use |
|------|--------------|-------------------|------------|
| 2x2 | 4 squares | 2" x 2" | Corridors, small rooms |
| 2x4 | 8 squares | 2" x 4" | Hallways |
| 4x4 | 16 squares | 4" x 4" | Standard room |
| 6x6 | 36 squares | 6" x 6" | Large room |
| 8x8 | 64 squares | 8" x 8" | Boss arena |

**Wall Heights:**
- Standard: 1.5" - 2" (fits most minis)
- Tall: 3"+ (multi-level dungeons)
- Half-height: 0.75" (line of sight blocking)

## Print Settings for Terrain

Terrain prioritizes speed over fine detail.

### Fast/Draft Quality
- **Layer Height:** 0.2mm - 0.28mm
- **Infill:** 10-15%
- **Walls:** 2-3 perimeters
- **Speed:** 60-80mm/s
- **Supports:** Minimal (design-dependent)

### Standard Quality
- **Layer Height:** 0.16mm - 0.2mm
- **Infill:** 15-20%
- **Walls:** 3 perimeters
- **Speed:** 50-60mm/s

### Tips for Faster Terrain Printing
- Use larger nozzle (0.6mm or 0.8mm) for big pieces
- Increase layer height proportionally
- Lower infill - terrain doesn't need strength
- Print multiple tiles at once (plate efficiency)
- Skip supports when possible (design floors to print face-down)

### Material Recommendations
- **PLA:** Standard choice, paints well
- **PLA+:** Slightly tougher
- **PETG:** More durable for heavy use
- Avoid ABS (warping on large flat pieces)

## Categories

### Dungeon
```
terrain/dungeon/
├── floors/           # Basic floor tiles
├── walls/            # Wall sections
├── corners/          # Corner pieces
├── doors/            # Door frames and doors
├── stairs/           # Stairs and ramps
├── pillars/          # Columns and pillars
├── traps/            # Trap tiles
└── set-pieces/       # Throne rooms, altars, etc.
```

### Forest/Outdoor
```
terrain/forest/
├── trees/            # Individual trees
├── forest-bases/     # Tree clusters
├── rocks/            # Boulders and rock formations
├── paths/            # Trail tiles
├── water/            # Rivers, ponds
├── bridges/          # Log bridges, stone bridges
└── camps/            # Campfire, tents
```

### Urban/Town
```
terrain/urban/
├── buildings/        # Houses, shops, taverns
├── streets/          # Road tiles
├── walls/            # Town walls, gates
├── market/           # Stalls, carts
├── docks/            # Piers, boats
└── fixtures/         # Fountains, wells, signs
```

### Cave/Underground
```
terrain/cave/
├── floors/           # Uneven cave floors
├── walls/            # Cave walls
├── formations/       # Stalagmites, crystals
├── water/            # Underground pools
└── mining/           # Mine cart rails, supports
```

### Specialty
```
terrain/specialty/
├── temple/           # Religious buildings
├── castle/           # Castle components
├── ship/             # Ship deck and parts
├── planar/           # Other planes (Feywild, etc.)
└── ruins/            # Destroyed/ancient versions
```

## Organization Tips

1. **Label storage bins** by system and type
2. **Keep connectors with tiles** (clips, magnets)
3. **Store flat** to prevent warping
4. **Batch similar tiles** for efficient printing
5. **Track inventory** to know what you have

## Companion Files

Each terrain set should have a settings file:
```
dungeon-floor-2x2-openlock.stl
dungeon-floor-2x2-openlock_settings.md
```

See `_print-settings-template.md` for the template.

## Build Plate Optimization

### Ender 3 / 220x220mm
- 4x 2x2 tiles per plate
- 2x 4x4 tiles per plate
- 1x 6x6 tile (tight fit)

### Larger Beds (300x300mm)
- 9x 2x2 tiles per plate
- 4x 4x4 tiles per plate
- 1x 8x8 tile

## Quick Reference: Print Time Estimates

| Piece | Layer Height | Approx Time |
|-------|-------------|-------------|
| 2x2 floor | 0.2mm | 30-45 min |
| 4x4 floor | 0.2mm | 1-2 hours |
| Wall section (2") | 0.2mm | 45-60 min |
| Full 4x4 room | 0.2mm | 3-5 hours |
