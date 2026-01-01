# Props

Small items, scatter terrain, furniture, and accessories for tabletop gaming.

## Categories

### Scatter Terrain
Small items placed on terrain tiles to add detail and visual interest.

```
props/scatter/
├── barrels/          # Barrels, crates, boxes
├── debris/           # Rubble, bones, broken items
├── vegetation/       # Bushes, grass tufts, mushrooms
├── dungeon/          # Chains, torture items, skulls
├── camp/             # Bedrolls, campfires, cooking gear
├── magic/            # Crystals, runes, arcane circles
└── misc/             # Books, scrolls, candles, misc items
```

**Common Scatter Sets:**
- Barrel and crate sets (5-10 pieces)
- Dungeon dressing (chains, skulls, rats)
- Tavern accessories (mugs, plates, bottles)
- Market goods (baskets, cloth, produce)

### Furniture
Interior furnishings for buildings and dungeons.

```
props/furniture/
├── tavern/           # Tables, chairs, bar, kegs
├── bedroom/          # Beds, wardrobes, nightstands
├── throne/           # Thrones, pedestals, banners
├── library/          # Bookshelves, desks, lecterns
├── kitchen/          # Stoves, counters, pantry
├── workshop/         # Workbenches, anvils, forges
├── temple/           # Altars, pews, shrines
└── prison/           # Cages, stocks, cells
```

**Furniture Scale Notes:**
- Chairs: ~12-15mm seat height at 28mm scale
- Tables: ~15-18mm height
- Beds: ~10mm mattress height
- Doors: ~35-40mm tall

### Treasure and Loot
Items players might find or fight over.

```
props/treasure/
├── chests/           # Treasure chests (open/closed)
├── coins/            # Coin piles, coin stacks
├── gems/             # Crystal formations, gem piles
├── artifacts/        # Magic items, relics
├── hoards/           # Dragon hoard piles
└── containers/       # Urns, vases, bags
```

**Treasure Chest Variants:**
- Closed (standard)
- Open (empty)
- Open (with treasure visible)
- Mimic version

### Vehicles
Transportation for adventures.

```
props/vehicles/
├── carts/            # Wagons, carts, wheelbarrows
├── boats/            # Rowboats, canoes, rafts
├── ships/            # Ship components, small vessels
├── carriages/        # Noble carriages, prison wagons
└── fantasy/          # Flying carpets, magic vehicles
```

### Objective Markers
Game-specific functional items.

```
props/markers/
├── objectives/       # Quest markers, capture points
├── tokens/           # Condition markers, spell effects
├── doors/            # Standalone door pieces
└── traps/            # Trap indicators, hazard markers
```

### Weapons and Equipment
Oversized weapon props and equipment displays.

```
props/equipment/
├── weapon-racks/     # Sword racks, weapon displays
├── armor-stands/     # Armor on stands
├── shields/          # Shield displays
└── tools/            # Adventuring gear
```

## Print Settings for Props

Props are small and detailed - settings between minis and terrain.

### Standard Quality
- **Layer Height:** 0.12mm - 0.16mm
- **Infill:** 15-20%
- **Walls:** 2-3 perimeters
- **Speed:** 40-50mm/s
- **Supports:** As needed (many props can print without)

### Quick/Batch Quality
- **Layer Height:** 0.16mm - 0.2mm
- **Infill:** 10-15%
- **Speed:** 50-60mm/s

### Small Detailed Props (gems, coins)
- **Layer Height:** 0.08mm - 0.12mm
- **Infill:** 20%
- **Speed:** 30-40mm/s

## Batch Printing Tips

Props are ideal for batch printing:
- Fill the build plate with multiple props
- Group similar items (all barrels, all crates)
- Print sets together for consistent color
- Consider using a draft profile for playtest pieces

**Typical Batch Sizes (220x220 bed):**
- 10-20 barrels/crates
- 4-8 chairs
- 2-4 tables
- 20-40 small scatter items

## File Naming Convention

```
[category]-[item]-[variant].[ext]
```

**Examples:**
- `scatter-barrel-small.stl`
- `scatter-barrel-large.stl`
- `furniture-chair-tavern.stl`
- `treasure-chest-open.stl`
- `treasure-chest-mimic.stl`
- `vehicle-cart-merchant.stl`

## Organization Tips

### Physical Storage
- Small compartment boxes for tiny items
- Separate painted from unpainted
- Group by location type (tavern set, dungeon set)
- Keep multiples together (all barrels in one spot)

### Quick-Grab Sets
Pre-assembled prop collections:
- **Tavern Kit:** Tables, chairs, bar, mugs, kegs
- **Dungeon Kit:** Chains, skulls, crates, debris
- **Camp Kit:** Bedrolls, fire, cooking gear
- **Market Kit:** Stalls, goods, crates

## Painting Props

### Speed Painting Method
1. Prime (gray or black)
2. Heavy drybrush base color
3. Wash
4. Light drybrush highlight
5. Done

### Color Schemes by Type
- **Wood:** Brown base, Agrax wash, bone drybrush
- **Stone:** Gray base, Nuln wash, light gray drybrush
- **Metal:** Metallic base, Nuln wash, silver edge
- **Cloth:** Base color, wash, light drybrush

### Batch Painting
- Attach to paint sticks (10-20 items)
- Assembly line each step
- All barrels brown > all barrels washed > all barrels drybrushed

## Companion Files

Each prop or prop set should have settings documented:
```
scatter-barrel-set.stl
scatter-barrel-set_settings.md
```

See `_print-settings-template.md` for the template.

## Sources for Props

### Free Sources
- Thingiverse (search "DnD scatter")
- Printables (search "tabletop props")
- MyMiniFactory (free section)

### Paid/Patreon
- Many mini creators include props
- Dedicated scatter terrain creators
- Monthly releases often include prop packs

## Quantity Guidelines

Suggested quantities for a well-stocked prop collection:

| Item | Quantity | Notes |
|------|----------|-------|
| Barrels | 10-20 | Various sizes |
| Crates | 10-15 | Different types |
| Chairs | 8-12 | For tavern scenes |
| Tables | 4-6 | Various sizes |
| Beds | 4-6 | Inn rooms |
| Treasure chests | 4-8 | Open and closed |
| Bookshelves | 4-6 | Library/wizard tower |
| Debris piles | 6-10 | Dungeon dressing |
| Campfire | 2-3 | Different sizes |
