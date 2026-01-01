# D&D 5e Calculator Tools

Command-line calculators for encounter XP management and custom monster CR estimation, based on Dungeon Master's Guide (DMG) guidelines.

## Files

| File | Description |
|------|-------------|
| `xp_calculator.py` | Calculate encounter XP, difficulty, and awards |
| `cr_calculator.py` | Estimate CR for custom/homebrew monsters |
| `calculator_data.json` | Reference tables for both calculators |

---

## XP Calculator

Calculate XP thresholds for a party, adjusted XP for encounters, determine encounter difficulty, and calculate XP awards per player.

### Quick Start

```bash
python xp_calculator.py --party 5,5,5,4 --monsters "2xCR2,1xCR3"
```

### Usage

```bash
python xp_calculator.py --party LEVELS --monsters MONSTERS [options]
```

### Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `--party` | Party member levels (comma-separated) | `5,5,5,4` |
| `--monsters` | Monsters in format `NxCR` | `"2xCR2,1xCR3"` |
| `--thresholds` | Show XP threshold table by level | |
| `--level` | Show thresholds for specific level | `5` |
| `--cr-table` | Show CR to XP conversion table | |
| `--multipliers` | Show encounter multiplier reference | |
| `--json` | Output results as JSON | |

### Monster String Format

The `--monsters` argument accepts flexible formats:

```
2xCR2      - 2 monsters of CR 2
1xCR3      - 1 monster of CR 3
4xCR1/4    - 4 monsters of CR 1/4
3x1/2      - 3 monsters of CR 1/2 (CR prefix optional)
2xcr5      - Case insensitive
```

Combine multiple monster types with commas:
```
"2xCR2,1xCR3"
"4xCR1/4,1xCR2"
"1xCR5,2xCR3,4xCR1"
```

### Examples

#### Basic Encounter Calculation

```bash
python xp_calculator.py --party 5,5,5,4 --monsters "2xCR2,1xCR3"
```

Output includes:
- Party XP thresholds (easy/medium/hard/deadly)
- Monster XP breakdown
- Adjusted XP with multiplier
- Encounter difficulty rating
- XP award per player

#### Mixed Party Levels

```bash
python xp_calculator.py --party 3,3,3,3,3 --monsters "4xCR1/4,1xCR2"
```

#### Large Encounter

```bash
python xp_calculator.py --party 8,8,7,7 --monsters "1xCR5,2xCR3,4xCR1"
```

#### View Reference Tables

```bash
# XP thresholds by level
python xp_calculator.py --thresholds

# Thresholds for specific level
python xp_calculator.py --thresholds --level 5

# CR to XP conversion
python xp_calculator.py --cr-table

# Encounter multipliers
python xp_calculator.py --multipliers
```

#### JSON Output

```bash
python xp_calculator.py --party 5,5,5,4 --monsters "2xCR2,1xCR3" --json
```

### How It Works

1. **Party Thresholds**: Sum individual XP thresholds for each party member at their level

2. **Base XP**: Sum XP values for all monsters

3. **Encounter Multiplier**: Applied based on monster count:
   | Monsters | Multiplier |
   |----------|------------|
   | 1 | x1.0 |
   | 2 | x1.5 |
   | 3-6 | x2.0 |
   | 7-10 | x2.5 |
   | 11-14 | x3.0 |
   | 15+ | x4.0 |

   Adjusted by party size:
   - Party of 1-2: Use next higher multiplier
   - Party of 3-5: Use standard multiplier
   - Party of 6+: Use next lower multiplier

4. **Difficulty**: Compare adjusted XP to party thresholds
   - Trivial: Below easy threshold
   - Easy/Medium/Hard/Deadly: Between respective thresholds
   - Beyond Deadly: Above 1.5x deadly threshold

5. **XP Award**: Divide BASE XP (not adjusted) evenly among party members

---

## CR Calculator

Estimate Challenge Rating for custom/homebrew monsters using DMG guidelines. Calculates offensive CR, defensive CR, and final CR with XP value.

### Quick Start

```bash
python cr_calculator.py --hp 135 --ac 18 --attack 8 --damage 50
```

### Usage

```bash
python cr_calculator.py --hp HP --ac AC --attack BONUS --damage DPR [options]
```

### Required Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `--hp` | Monster hit points | `135` |
| `--ac` | Armor class | `18` |
| `--attack` | Attack bonus (number only) | `8` (for +8) |
| `--damage` | Average damage per round | `50` |

### Optional Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `--save-dc` | Save DC for abilities | `16` |
| `--special` | Special abilities/adjustments | `pack_tactics magic_resistance` |
| `--stats` | Show monster statistics table | |
| `--abilities` | Show special ability adjustments | |
| `--xp` | Show CR to XP table | |
| `--json` | Output as JSON | |

### Examples

#### Basic CR Calculation

```bash
python cr_calculator.py --hp 135 --ac 18 --attack 8 --damage 50
```

#### With Save DC

```bash
python cr_calculator.py --hp 200 --ac 17 --attack 10 --damage 80 --save-dc 16
```

The calculator uses whichever gives a higher adjustment (attack bonus or save DC).

#### With Special Abilities

```bash
python cr_calculator.py --hp 150 --ac 16 --attack 7 --damage 45 \
    --special pack_tactics magic_resistance
```

#### Custom Adjustments

```bash
# Add +2 CR for powerful homebrew abilities
python cr_calculator.py --hp 100 --ac 15 --attack 6 --damage 30 --special +2

# Mix named abilities and custom adjustments
python cr_calculator.py --hp 150 --ac 16 --attack 7 --damage 45 \
    --special pack_tactics +1 -1
```

#### View Reference Tables

```bash
# Monster statistics by CR
python cr_calculator.py --stats

# Special ability adjustments
python cr_calculator.py --abilities

# CR to XP conversion
python cr_calculator.py --xp
```

### How CR is Calculated

#### Step 1: Defensive CR (HP + AC)

1. Find base CR from HP range in DMG table
2. Compare actual AC to expected AC for that CR
3. Adjust CR by +/- 1 for every 2 AC difference

Example:
- 135 HP -> Base CR 5
- Expected AC for CR 5: 15
- Actual AC: 18 (+3 difference)
- AC adjustment: +1 CR
- Defensive CR: 6

#### Step 2: Offensive CR (Damage + Attack/DC)

1. Find base CR from damage per round in DMG table
2. Compare attack bonus AND save DC to expected values
3. Use whichever gives higher adjustment
4. Adjust CR by +/- 1 for every 2 points difference

Example:
- 50 DPR -> Base CR 7
- Expected Attack for CR 7: +6
- Actual Attack: +8 (+2 difference)
- Attack adjustment: +1 CR
- Offensive CR: 8

#### Step 3: Final CR

1. Average defensive and offensive CRs
2. Apply special ability adjustments

Example:
- Defensive CR 6, Offensive CR 8
- Average: (6 + 8) / 2 = CR 7
- Final CR: 7 (XP: 2,900)

### Special Abilities

| Ability | CR Mod | Notes |
|---------|--------|-------|
| `flying` | +0 | Tactical advantage, no direct CR change |
| `resistances` | +0 | Effectively doubles HP vs common damage |
| `immunities` | +0 | Consider common damage types |
| `spellcasting` | +0 | Calculate DPR using highest damage spell |
| `legendary_actions` | +0 | Add legendary action damage to DPR |
| `legendary_resistances` | +0 | Increases effective survivability |
| `regeneration` | +0 | Add (regen x 3 rounds) to effective HP |
| `pack_tactics` | +1 | Consistent advantage on attacks |
| `magic_resistance` | +2 | Advantage on saves vs spells |
| `frightful_presence` | +1 | Area fear effect |
| `multiattack_3plus` | +1 | 3+ attacks per round |
| `swallow` | +1 | Swallow/engulf abilities |
| `at_will_spells` | +1 | Unlimited use damaging spells |
| `innate_teleport` | +1 | At-will teleportation |

### Tips for Accurate CR

#### Calculating Damage Per Round (DPR)

1. **Melee/Ranged**: Sum average damage from all attacks
   - Example: 2 attacks at 2d6+4 = 2 x 11 = 22 DPR

2. **Spellcasters**: Use highest expected damage spell
   - Consider realistic spell usage per combat
   - Fireball: 8d6 = 28 average (single target equivalent)

3. **Legendary Actions**: Add legendary action damage to DPR
   - 3 legendary attacks at 1d8+5 each = 28.5 added to DPR

#### Effective HP Adjustments

Before using the calculator, adjust HP for:

| Ability | HP Adjustment |
|---------|---------------|
| Resistances (common damage) | Double HP |
| Immunities (common damage) | Double HP |
| Regeneration | Add (regen x 3) to HP |
| High save bonuses | Consider as survivability |

#### When Results Seem Off

- Very high AC + low HP = higher CR than pure HP suggests
- Area damage (Fireball, breath weapons) may warrant +1 CR
- Control abilities (stun, paralyze) may warrant +1-2 CR
- Lair actions add approximately +1 CR
- Unusual mobility (teleport, burrow) may warrant +1 CR

---

## Reference Data (calculator_data.json)

The JSON file contains all reference tables used by both calculators:

| Key | Description |
|-----|-------------|
| `xp_by_cr` | XP values for each CR (0 to 30) |
| `xp_thresholds_by_level` | Easy/medium/hard/deadly thresholds per level |
| `encounter_multipliers` | Multiplier tiers by monster count |
| `monster_statistics_by_cr` | HP, AC, attack, damage, save DC by CR |
| `special_ability_adjustments` | CR modifiers for special abilities |
| `cr_order` | Ordered list of CRs (0, 1/8, 1/4, 1/2, 1-30) |
| `level_xp_requirements` | XP needed to reach each level |

---

## Integration with Other Tools

These calculators can be used alongside:
- **Encounter Generator** (`../generators/`) - Generate balanced encounters
- **Initiative Tracker** (`../trackers/`) - Track combat with XP awards
- **Monster Database** - Store custom monsters with calculated CRs

---

## Examples in Practice

### Planning a Session

```bash
# What can a level 5 party handle?
python xp_calculator.py --thresholds --level 5

# Test a planned encounter
python xp_calculator.py --party 5,5,5,5 --monsters "1xCR4,2xCR1"
```

### Creating a Custom Monster

```bash
# Draft stats for a homebrew creature
python cr_calculator.py --hp 120 --ac 16 --attack 7 --damage 35

# It has pack tactics and magic resistance
python cr_calculator.py --hp 120 --ac 16 --attack 7 --damage 35 \
    --special pack_tactics magic_resistance

# Verify it fits the intended encounter
python xp_calculator.py --party 5,5,5,5 --monsters "1xCR6"
```

### Quick Reference During Play

```bash
# How much XP for beating that dragon?
python xp_calculator.py --party 10,10,9,9,9 --monsters "1xCR13"

# What CR should this improvised monster be?
python cr_calculator.py --hp 85 --ac 14 --attack 5 --damage 22
```
