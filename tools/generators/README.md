# D&D 5e NPC Generator

A fast, practical command-line tool for generating random NPCs during D&D 5e game sessions.

## Features

- Generate NPCs with names appropriate to their race and gender
- Weighted race distribution (common races appear more frequently)
- PHB-style personality traits, ideals, bonds, and flaws
- Motivations, mannerisms, and distinctive appearances
- Current mood for immediate roleplay cues
- Optional secrets for DM use
- Optional stat blocks based on NPC role
- Multiple output formats (text, JSON, Markdown)
- Quick reference mode for mid-session use

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Installation

1. Ensure both files are in the same directory:
   - `npc_generator.py`
   - `npc_data.json`

2. Make the script executable (Linux/Mac):
   ```bash
   chmod +x npc_generator.py
   ```

## Usage

### Basic Usage

```bash
# Generate one random NPC (quick format)
python npc_generator.py

# Generate one NPC with full details
python npc_generator.py --detailed

# Generate multiple NPCs
python npc_generator.py --count 5
```

### Specifying Options

```bash
# Generate an elf
python npc_generator.py --race elf

# Generate a merchant
python npc_generator.py --role merchant

# Generate a dwarf blacksmith with stats
python npc_generator.py --race dwarf --role commoner --stats --detailed

# Generate a noble with a higher-level stat block
python npc_generator.py --role noble --level 10 --stats
```

### Output Formats

```bash
# Default text output
python npc_generator.py

# JSON output (great for integrating with other tools)
python npc_generator.py --format json

# Markdown output (great for notes)
python npc_generator.py --format markdown
```

### All Options

| Option | Short | Description |
|--------|-------|-------------|
| `--race` | `-r` | Specify race (human, elf, dwarf, etc.) |
| `--role` | `-o` | Specify occupation type (merchant, guard, noble, etc.) |
| `--level` | `-l` | Level for stat block scaling |
| `--detailed` | `-d` | Show full detailed output |
| `--count` | `-c` | Number of NPCs to generate |
| `--format` | `-f` | Output format: text, json, markdown |
| `--stats` | `-s` | Include stat block |
| `--no-secret` | | Exclude the secret |
| `--seed` | | Random seed for reproducible results |
| `--data-file` | | Path to custom data JSON file |

## Available Races

- Human (most common)
- Half-Elf
- Halfling
- Dwarf
- Elf
- Gnome
- Half-Orc
- Tiefling
- Dragonborn

## Available Roles

- `commoner` - Farmers, craftspeople, laborers
- `merchant` - Shopkeepers, traders, vendors
- `guard` - City watch, bodyguards, sentries
- `noble` - Aristocrats, lords, knights
- `criminal` - Thieves, smugglers, assassins
- `entertainer` - Bards, actors, performers
- `religious` - Priests, monks, acolytes
- `scholar` - Sages, researchers, alchemists
- `military` - Soldiers, veterans, officers
- `adventurer_class` - Player character classes

## Example Outputs

### Quick Format (Default)

```
=== Aldric Thornton ===
Human Male | Blacksmith
Mood: Irritable and short-tempered
Trait: I judge people by their actions, not their words.
Wants: Wants to protect their home/family
Voice: Uses lots of hand gestures while talking
Look: Muscular and broad, Prominent scar
Secret: Is wanted for crimes in another region
```

### Detailed Format

```
==================================================
  Thia Siannodel
==================================================

Race: Elf
Gender: Female
Occupation: Herbalist
Current Mood: Curious and inquisitive

--- PERSONALITY ---
Traits:
  - I'm always polite and respectful, even to my enemies.
  - I connect everything that happens to me to a grand, cosmic plan.

Ideal: Nature (Neutral)
  "The natural world is more important than all the constructs of civilization."

Bond: An injury to the unspoiled wilderness of my home is an injury to me.

Flaw: I am dogmatic in my thoughts and philosophy.

Motivation: Seeks to create something beautiful

--- MANNERISMS ---
Speech: Speaks very slowly and deliberately
Physical: Tilts head when listening

--- APPEARANCE ---
Build: Thin and wiry
Hair: Long flowing hair
Face: Different colored eyes
Distinctive: Has an unusual smell (pleasant or not)

--- SECRET (DM ONLY) ---
Has a forbidden magical ability they hide
```

### JSON Format

```json
{
  "name": "Brottor Ironshield",
  "race": "Dwarf",
  "gender": "Male",
  "occupation": "Guard",
  "personality_traits": [
    "I blow up at the slightest insult.",
    "I am incredibly slow to trust."
  ],
  "ideal": {
    "ideal": "Honor",
    "description": "If I dishonor myself, I dishonor my whole family.",
    "alignment": "Lawful"
  },
  "bond": "My family, clan, or tribe is the most important thing in my life.",
  "flaw": "Violence is my answer to almost any challenge.",
  "motivation": "Seeks revenge against someone who wronged them",
  "mannerisms": {
    "speech": "Has a booming, loud voice",
    "physical": "Cracks knuckles frequently"
  },
  "appearance": {
    "build": "Short and stocky",
    "hair": "Impressive beard/mustache",
    "face": "Heavily scarred",
    "distinctive": "Missing finger(s)"
  },
  "mood": "Angry and hostile",
  "secret": "Is wanted for crimes in another region"
}
```

### Markdown Format

```markdown
# Merric Goodbarrel

**Race:** Halfling | **Gender:** Male | **Occupation:** Innkeeper

**Current Mood:** Friendly and welcoming

## Personality

**Traits:**
- I would rather make a new friend than a new enemy.
- I know a story relevant to almost every situation.

**Ideal:** Community (Lawful)
> It is the duty of all civilized people to strengthen the bonds of community.

**Bond:** My town or city is my home, and I'll fight to defend it.

**Flaw:** I am too enamored of ale, wine, and other intoxicants.

**Motivation:** Wants simple peace and quiet

## Mannerisms

- **Speech:** Has a distinctive laugh
- **Physical:** Bounces leg while seated

## Appearance

- **Build:** Petite
- **Hair:** Curly brown hair
- **Face:** Always smiling
- **Distinctive Feature:** Wears lots of jewelry

## Secret (DM Only)

*Has a gambling addiction with massive debts*
```

## Customization

You can customize the generator by editing `npc_data.json`:

- Add new names for races
- Expand personality trait pools
- Add new occupations
- Create custom mannerisms
- Add region-specific content

## Tips for DMs

1. **Mid-Session Use**: Use quick format (`python npc_generator.py`) for instant NPCs
2. **Session Prep**: Use `--detailed --count 10` to pre-generate a pool of NPCs
3. **Consistency**: Use `--seed` with a consistent value for reproducible campaigns
4. **Export**: Use `--format json` to save NPCs to files for later reference
5. **Combat NPCs**: Use `--stats --level X` when you need combat-ready NPCs

## License

Free to use and modify for personal and commercial use.
