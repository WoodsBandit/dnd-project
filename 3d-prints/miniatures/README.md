# Miniatures

Organized STL files and print documentation for D&D miniatures.

## File Naming Convention

```
[category]-[name]-[scale].[ext]
```

**Examples:**
- `hero-human-paladin-28mm.stl`
- `monster-beholder-32mm.stl`
- `npc-tavern-keeper-28mm.stl`
- `hero-dragonborn-barbarian-28mm.3mf`

**Categories:**
- `hero-` Player character miniatures
- `monster-` Enemy creatures
- `npc-` Non-player characters
- `mount-` Horses, wolves, griffons, etc.
- `boss-` Large boss monsters

## Scale Standards

| Scale | Use Case | Base Size |
|-------|----------|-----------|
| 28mm | Standard tabletop (most common) | 25mm round |
| 32mm | "Heroic" scale, slightly larger | 32mm round |
| 75mm | Display/painting pieces | 40mm+ |
| Custom | Huge/Gargantuan creatures | Varies |

**Scaling in Slicer:**
- 28mm to 32mm: Scale 114%
- 32mm to 28mm: Scale 87.5%
- Always scale uniformly (X/Y/Z locked)

## Print Settings Recommendations

### Standard Quality (Most Minis)
- **Layer Height:** 0.08mm (resin) / 0.12mm (FDM)
- **Infill:** 0-15% (small minis can be hollow)
- **Speed:** 30-40mm/s (FDM)
- **Walls:** 2-3 perimeters

### High Detail (Character Minis, Display)
- **Layer Height:** 0.04-0.05mm (resin) / 0.08mm (FDM)
- **Infill:** 10-20%
- **Speed:** 20-30mm/s (FDM)
- **Walls:** 3+ perimeters

### Quick Prints (Table Fodder)
- **Layer Height:** 0.1mm (resin) / 0.16mm (FDM)
- **Infill:** 5-10%
- **Speed:** 50mm/s+ (FDM)

## Support Settings for Detailed Prints

### Resin Printers
- **Support Type:** Light or Medium
- **Tip Diameter:** 0.3-0.4mm
- **Contact Depth:** 0.2-0.3mm
- **Density:** 50-70%
- **Angle Threshold:** 35-45 degrees

**Orientation Tips:**
- Tilt 15-30 degrees off vertical
- Face details point away from build plate
- Weapons/thin parts should not be lowest point
- Consider splitting for large minis

### FDM Printers
- **Support Type:** Tree supports preferred
- **Support Density:** 10-15%
- **Support Z Distance:** 0.2mm
- **Support Interface:** Yes, 2-3 layers
- **Overhang Angle:** 50-60 degrees

**FDM Orientation Tips:**
- Print face-up when possible
- Avoid supports on faces
- Consider pre-supported files or splitting

## Categories

### Heroes (Player Characters)
```
miniatures/heroes/
├── human/
├── elf/
├── dwarf/
├── halfling/
├── dragonborn/
├── tiefling/
└── [other-races]/
```

### Monsters
```
miniatures/monsters/
├── aberrations/
├── beasts/
├── celestials/
├── constructs/
├── dragons/
├── elementals/
├── fey/
├── fiends/
├── giants/
├── humanoids/
├── monstrosities/
├── oozes/
├── plants/
└── undead/
```

### NPCs
```
miniatures/npcs/
├── townsfolk/
├── merchants/
├── guards/
├── nobles/
├── adventurers/
└── villains/
```

### Mounts and Companions
```
miniatures/mounts/
├── horses/
├── exotic/
└── familiars/
```

## STL Sources

Track where files came from:
- **Patreon Creators:** Note creator and month released
- **MyMiniFactory:** Link to listing
- **Thingiverse/Printables:** Link + designer credit
- **Heroforge:** Custom character exports
- **Purchased STLs:** Note store and license

## Companion Files

Each printed mini should have a settings file:
```
hero-human-paladin-28mm.stl
hero-human-paladin-28mm_settings.md  <- Use template
```

See `_print-settings-template.md` for the template.
