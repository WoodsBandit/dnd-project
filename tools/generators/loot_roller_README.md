# D&D 5e Loot Table Roller

A complete Python CLI tool for generating treasure following the Dungeon Master's Guide treasure tables. Supports themed loot generation for different encounter types.

## Features

- **DMG-Accurate Tables**: Follows official treasure tables from the Dungeon Master's Guide
- **Individual and Hoard Treasure**: Support for both treasure types
- **Themed Loot**: Dragon, Undead, Arcane, and Martial themes modify treasure distribution
- **All Treasure Tiers**: CR 0-4, 5-10, 11-16, and 17+
- **Complete Data**: Gems, art objects, and magic items from Tables A through I
- **Multiple Output Formats**: Text, Markdown, JSON, and compact single-line

## Installation

No external dependencies required. Uses only Python standard library.

```bash
# Ensure both files are in the same directory:
# - loot_roller.py
# - loot_data.json
```

## Usage

### Basic Usage

```bash
# Individual treasure for CR 5 encounter
python loot_roller.py --cr 5 --type individual

# Treasure hoard for CR 10 encounter
python loot_roller.py --cr 10 --type hoard

# Using tier directly instead of CR
python loot_roller.py --tier 5-10 --type hoard
```

### Themed Treasure

```bash
# Dragon hoard (more coins, gems, fire-themed magic items)
python loot_roller.py --cr 15 --type hoard --theme dragon

# Undead crypt treasure (ancient items, anti-undead weapons)
python loot_roller.py --cr 8 --type hoard --theme undead

# Wizard's tower cache (gems, scrolls, arcane items)
python loot_roller.py --cr 12 --type hoard --theme arcane

# Armory/war chest (weapons, armor, shields)
python loot_roller.py --cr 6 --type hoard --theme martial
```

### Output Formats

```bash
# Default text output
python loot_roller.py --cr 5 --type hoard

# Markdown output (great for notes)
python loot_roller.py --cr 5 --type hoard --format markdown

# JSON output (for programmatic use)
python loot_roller.py --cr 5 --type hoard --format json

# Compact one-line summary
python loot_roller.py --cr 5 --type hoard --compact
```

### Multiple Rolls

```bash
# Roll 5 individual treasures
python loot_roller.py --cr 3 --type individual --count 5

# Roll 3 hoards
python loot_roller.py --cr 10 --type hoard --count 3
```

### Reproducible Results

```bash
# Use a seed for reproducible results
python loot_roller.py --cr 5 --type hoard --seed 12345
```

## Command Line Options

| Option | Short | Description |
|--------|-------|-------------|
| `--cr` | | Challenge Rating (0-30). Converts to tier automatically. |
| `--tier` | | Treasure tier: 0-4, 5-10, 11-16, 17+ |
| `--type` | `-t` | Treasure type: individual or hoard (default: individual) |
| `--theme` | | Loot theme: standard, dragon, undead, arcane, martial |
| `--count` | `-c` | Number of rolls (default: 1) |
| `--format` | `-f` | Output format: text, json, markdown/md |
| `--compact` | | Single-line output |
| `--seed` | | Random seed for reproducibility |
| `--verbose` | `-v` | Show additional details |

## Treasure Tiers

| Tier | CR Range | Typical Encounters |
|------|----------|-------------------|
| 0-4 | CR 0-4 | Goblins, bandits, low-level undead |
| 5-10 | CR 5-10 | Young dragons, giants, demons |
| 11-16 | CR 11-16 | Adult dragons, liches, powerful fiends |
| 17+ | CR 17-30 | Ancient dragons, archdevils, demigods |

## Themes

### Standard
Default treasure distribution with no modifications.

### Dragon
- 2x coin multiplier
- 1.5x gem and art multiplier
- Prefers high-value gems (1000gp, 5000gp)
- Fire-themed magic items (Flame Tongue, Dragon Scale Mail)
- Extra items: charred adventurer gear, dragon scales

### Undead
- 0.8x coin multiplier
- 1.5x art multiplier (ancient treasures)
- Anti-undead magic items (Sun Blade, Mace of Disruption)
- Extra items: funeral masks, dusty spellbooks, burial shrouds

### Arcane
- 0.5x coin multiplier
- 2x gem multiplier (magical components)
- Spellcasting items (Staves, Wands, Robes)
- Extra items: spell components, arcane foci, torn spellbook pages

### Martial
- 1.2x coin multiplier
- Weapons and armor focus
- Magic weapons, shields, and armor
- Extra items: battle standards, military orders, veteran medals

## Example Output

### Text Format (default)
```
============================================================
  HOARD TREASURE (CR 5-10) - Dragon Theme
============================================================

Table Roll: 67

COINS: 42 pp, 2,100 gp, 1,400 sp, 800 cp

GEMS (12):
  - Fire Opal (1000 gp) x3
  - Star Ruby (1000 gp) x4
  - Emerald (1000 gp) x5
  Total: 12,000 gp

MAGIC ITEMS (3):
  - Flame Tongue (Rare) [THEMED] (Table G)
      +2d6 fire damage when ignited
  - Potion of Fire Breath (Uncommon) [THEMED]
      Exhale fire at a target within 30 feet three times
  - Ring of Fire Elemental Command (Legendary) [THEMED]
      Command fire elementals, various fire powers

THEMED EXTRAS:
  - Dragon scale (decorative)
  - Scorched banner

============================================================
TOTAL LIQUID VALUE: 14,750.0 gp
(Magic item values not included)
============================================================
```

### Compact Format
```
14,750gp in coins/valuables | 12 gems (12,000gp) | Magic: Flame Tongue, Potion of Fire Breath, Ring of Fire Elemental Command
```

## Data File Structure

The `loot_data.json` file contains:

- **coin_tables**: Individual and hoard coin tables by tier
- **gems**: 6 gem value tiers (10gp to 5000gp) with descriptions
- **art_objects**: 6 art value tiers (25gp to 7500gp) with descriptions
- **magic_item_tables**: Tables A through I with 20+ items each
- **themes**: Theme configurations with multipliers and item lists

## Magic Item Tables

| Table | Rarity | Typical Contents |
|-------|--------|------------------|
| A | Common | Potions of healing, cantrip scrolls |
| B | Uncommon | Better potions, low-level wondrous items |
| C | Rare | Superior potions, mid-level scrolls |
| D | Very Rare | Supreme healing, high-level consumables |
| E | Legendary | 9th level scrolls, legendary consumables |
| F | Uncommon | Permanent magic items (+1 weapons, cloaks) |
| G | Rare | Rare permanent items (+2 weapons, rings) |
| H | Very Rare | Very rare permanent items (+3 weapons) |
| I | Legendary | Legendary items (Vorpal Sword, Staff of the Magi) |

## Integration with Other Tools

This loot roller can be used alongside:
- `encounter_generator.py` - Generate encounters, then roll loot for defeated enemies
- `npc_generator.py` - Generate merchants with random inventory

## Troubleshooting

### "Could not find data file" Error
Ensure `loot_data.json` is in the same directory as `loot_roller.py`.

### Missing Magic Items
Some themed items may not be found in the data - they'll still appear with "unknown" rarity.

## License

This tool references content from the D&D 5e SRD. Dungeons & Dragons is a trademark of Wizards of the Coast.
