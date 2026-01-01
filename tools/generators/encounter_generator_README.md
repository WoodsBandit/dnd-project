# D&D 5e Random Encounter Generator

A command-line tool for generating balanced D&D 5th Edition random encounters. Uses official DMG encounter building rules for accurate CR calculations and XP thresholds.

## Requirements

- Python 3.6+
- No external dependencies

## Quick Start

```bash
python encounter_generator.py --level 5 --size 4 --difficulty hard --environment forest
```

Short form:
```bash
python encounter_generator.py -l 5 -s 4 -d hard -e forest
```

## Command Line Arguments

| Argument | Short | Required | Description |
|----------|-------|----------|-------------|
| `--level` | `-l` | Yes | Party level (1-20) |
| `--size` | `-s` | Yes | Number of characters in party |
| `--difficulty` | `-d` | Yes | easy, medium, hard, or deadly |
| `--environment` | `-e` | Yes | Terrain/location type |
| `--format` | `-f` | No | Output format: text, json, markdown (default: text) |
| `--count` | `-c` | No | Number of encounters to generate (default: 1) |
| `--seed` | | No | Random seed for reproducible results |

## Supported Environments

- `forest` - Woodlands, jungles, groves
- `dungeon` - Underground complexes, caves, ruins
- `urban` - Cities, towns, settlements
- `mountain` - Peaks, cliffs, highlands
- `swamp` - Marshes, bogs, wetlands
- `desert` - Arid wastelands, dunes
- `arctic` - Tundra, glaciers, frozen wastes
- `coastal` - Beaches, shores, seaside
- `underdark` - Deep underground realms

## Difficulty Levels

| Difficulty | Description |
|------------|-------------|
| Easy | Little threat, resources barely taxed |
| Medium | Moderate challenge, some resource expenditure |
| Hard | Serious threat, risk of character death |
| Deadly | Potentially lethal, high chance of casualties |

## Encounter Composition Types

The generator creates five types of encounters:

1. **Solo** - A single powerful creature appropriate for the party
2. **Pack** - 2-6 identical creatures working together
3. **Leader + Minions** - One strong creature with weaker allies
4. **Horde** - 7+ weak creatures swarming the party
5. **Mixed Group** - 2-3 different creature types combined

## Output Formats

### Text (default)

```
============================================================
ENCOUNTER: Leader + Minions
============================================================

Party: 4 characters at level 5
Environment: Forest
Difficulty: HARD

XP Budget: 3,000 XP
Total XP: 650 XP
Adjusted XP: 1,625 XP (x2.5 multiplier)

------------------------------------------------------------
MONSTERS:
------------------------------------------------------------
  1x Bugbear
     CR 1 | 200 XP each | Type: humanoid
     Tactics: Surprise attacks for extra damage, uses reach with morningstar.

  4x Goblin
     CR 1/4 | 50 XP each | Type: humanoid
     Tactics: Uses Nimble Escape to disengage/hide. Sets ambushes.

------------------------------------------------------------
TACTICAL NOTES:
------------------------------------------------------------
  * Leader coordinates minions - take out the leader to disrupt tactics.
  * Minions can provide flanking bonuses and action economy advantage.
  * Trees provide cover. Creatures may ambush from foliage.

============================================================
```

### JSON

```bash
python encounter_generator.py -l 5 -s 4 -d hard -e forest --format json
```

Outputs structured JSON for integration with other tools.

### Markdown

```bash
python encounter_generator.py -l 5 -s 4 -d hard -e forest --format markdown
```

Outputs formatted Markdown for notes and documentation.

## Examples

### Basic Encounters

```bash
# Easy encounter for level 1 party
python encounter_generator.py -l 1 -s 4 -d easy -e dungeon

# Deadly boss fight for level 10 party
python encounter_generator.py -l 10 -s 5 -d deadly -e mountain

# Medium forest encounter
python encounter_generator.py -l 5 -s 4 -d medium -e forest
```

### Multiple Encounters

```bash
# Generate 5 encounter options
python encounter_generator.py -l 5 -s 4 -d hard -e forest --count 5

# Pre-generate session encounters as markdown
python encounter_generator.py -l 7 -s 4 -d medium -e dungeon -c 3 -f markdown > session_encounters.md
```

### Reproducible Results

```bash
# Same seed = same encounter
python encounter_generator.py -l 5 -s 4 -d hard -e forest --seed 12345
```

## XP Calculation

The tool uses official DMG encounter building rules:

1. **XP Thresholds**: Calculated per character based on level and difficulty
2. **Encounter Multipliers**: Applied based on number of monsters
3. **Party Size Adjustments**: Multipliers adjusted for small (<3) or large (6+) parties

### XP Thresholds by Level (Per Character)

| Level | Easy | Medium | Hard | Deadly |
|-------|------|--------|------|--------|
| 1 | 25 | 50 | 75 | 100 |
| 5 | 250 | 500 | 750 | 1,100 |
| 10 | 600 | 1,200 | 1,900 | 2,800 |
| 15 | 1,400 | 2,800 | 4,300 | 6,400 |
| 20 | 2,800 | 5,700 | 8,500 | 12,700 |

### Encounter Multipliers

| Monsters | Multiplier |
|----------|------------|
| 1 | x1.0 |
| 2 | x1.5 |
| 3-6 | x2.0 |
| 7-10 | x2.5 |
| 11-14 | x3.0 |
| 15+ | x4.0 |

## Data File

The `encounter_data.json` file contains:

- **monsters**: 120+ creatures with CR, XP, type, environments, and tactics
- **xp_thresholds_by_level**: DMG thresholds for levels 1-20
- **encounter_multipliers**: Multiplier table based on monster count

### Adding Custom Monsters

Edit `encounter_data.json` to add new creatures:

```json
{
  "name": "Custom Creature",
  "cr": "3",
  "xp": 700,
  "type": "monstrosity",
  "environments": ["forest", "swamp"],
  "tactics": "Description of combat behavior and special abilities."
}
```

## Tips for DMs

### Pre-Session Prep

Generate multiple encounters before the session:

```bash
python encounter_generator.py -l 5 -s 4 -d medium -e forest -c 5 -f markdown > forest_encounters.md
```

### Mid-Session Use

Quick generation with short flags:

```bash
python encounter_generator.py -l 5 -s 4 -d hard -e dungeon
```

### Adjusting Difficulty

- Start with **medium** for regular encounters
- Use **hard** for challenging fights
- Reserve **deadly** for boss encounters or climactic moments
- Use **easy** for resource drain encounters

### Tactical Notes

Each encounter includes tactical notes based on:
- Encounter composition (solo, pack, leader+minions, horde, mixed)
- Environment-specific considerations

## Troubleshooting

### "No suitable monsters found"

The combination of party level and environment may not have appropriate monsters. Try:
- Different environment
- Adjusting difficulty
- Higher or lower party level

### Encounter seems too easy/hard

The DMG XP system is a guideline. Adjust by:
- Changing difficulty level
- Adding/removing monsters manually
- Considering party composition and magic items

## License

Monster data derived from the D&D 5e SRD 5.1, released under the Open Gaming License.
