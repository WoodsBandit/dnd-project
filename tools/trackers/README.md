# D&D Campaign Trackers

Tools and templates for tracking your D&D campaigns, combat encounters, and session notes.

## Contents

| File | Purpose |
|------|---------|
| `initiative_tracker.py` | Real-time combat initiative and HP tracking |
| `conditions.json` | D&D 5e condition reference data |
| `session_template.md` | Template for documenting individual sessions |
| `campaign_template.md` | Template for starting and tracking a new campaign |

---

## Session Notes Template

**File:** `session_template.md`

A comprehensive template for documenting each game session. Copy this file and rename it for each session (e.g., `session-01.md`).

### Features

- **Player attendance tracking** - Who was there, who was absent
- **Recap section** - Quick summary of previous session for continuity
- **Event logging** - Key moments with optional timestamps
- **NPC tracker** - Everyone the party met and their dispositions
- **Location notes** - Places visited with map update reminders
- **Combat log** - Encounter details, tactics, and outcomes
- **Loot tracking** - Currency, items, and resource usage
- **Decision tracking** - Player choices and their consequences
- **DM reflection** - Private notes on what worked and what to improve
- **XP/Milestone tracking** - Experience and level progression

### How to Use

1. Copy `session_template.md` to your campaign folder
2. Rename to `session-XX-title.md` (e.g., `session-01-the-goblin-caves.md`)
3. Fill in sections during or after the session
4. Delete unused sections or mark them N/A
5. Review DM notes before next session for prep reminders

### Tips

- Fill in the "Previous Session Recap" at the START of next session while it's fresh
- Use the timestamp feature if recording sessions for reference
- The DM Notes section is for your eyes only - be honest about what worked
- Link to NPC files or maps where relevant

---

## Campaign Template

**File:** `campaign_template.md`

A comprehensive template for planning and tracking an entire campaign from Session 0 through completion.

### Features

- **Setting overview** - World, tone, themes, and content boundaries
- **Starting location** - Detailed breakdown of where the campaign begins
- **Plot structure** - Main hooks, underlying truths, and campaign arcs
- **Faction profiles** - Organizations, their goals, and relationships
- **Major NPC roster** - Allies, villains, and wildcards
- **Session 0 notes** - Player expectations, house rules, schedule
- **Character roster** - Full party documentation with DM notes
- **Progress tracking** - Session log, achievements, current status

### How to Use

1. Copy `campaign_template.md` to a new campaign folder
2. Rename to `campaign-overview.md` or similar
3. Fill in sections during Session 0 and campaign prep
4. Update the Session Log and Party Status after each session
5. Add new NPCs and factions as they emerge in play

### Tips

- The "DM Notes" under each character are secret - use for foreshadowing ideas
- Keep faction relationships updated as the party influences the world
- The "Prepared Content Not Yet Used" section saves wasted prep
- Review "Things to Prep" before each session

---

## Initiative Tracker

**File:** `initiative_tracker.py`

A command-line tool for managing combat encounters in real-time.

### Quick Start

```bash
python initiative_tracker.py
```

### Key Features

- Add combatants manually or roll initiative automatically
- Track HP, AC, and conditions
- Automatic condition duration countdown
- Save/load encounters to JSON

See the inline help (`help` command) or the initiative tracker section below for full documentation.

---

## Recommended Workflow

### Starting a New Campaign

1. Copy `campaign_template.md` to your campaign folder
2. Fill out during Session 0 with your players
3. Create character entries for each PC
4. Define your starting factions and NPCs

### Running Sessions

1. Copy `session_template.md` for each new session
2. Prep using the campaign template's "Things to Prep" section
3. Use `initiative_tracker.py` for combat
4. Fill in session notes during or immediately after play
5. Update the campaign template's Session Log

### Between Sessions

1. Review your DM notes from last session
2. Update faction standings and NPC relationships
3. Add any new plot threads or consequences
4. Prep for the next session

---

## File Organization

Recommended structure for your campaign folder:

```
campaigns/
└── my-campaign/
    ├── campaign-overview.md      # From campaign_template.md
    ├── sessions/
    │   ├── session-00-zero.md
    │   ├── session-01-beginning.md
    │   └── session-02-dungeon.md
    ├── npcs/
    │   ├── friendly/
    │   └── hostile/
    ├── locations/
    ├── maps/
    ├── handouts/
    └── encounters/
        └── saved-combat.json     # From initiative_tracker.py
```

---

## Integration with Other Tools

These templates work alongside other tools in the `dnd/tools/` directory:

- **Generators** (`../generators/`) - Create NPCs, loot, encounters to populate your notes
- **Calculators** (`../calculators/`) - Balance encounters, calculate XP

---

## D&D 5e Initiative Tracker

A command-line initiative tracker for D&D 5e combat encounters. Designed for fast, live play at the table.

### Quick Start

```bash
python initiative_tracker.py
```

### Commands Reference

#### Adding Combatants

| Command | Description |
|---------|-------------|
| `add <name> <init> <hp> <ac> [count]` | Add combatant(s) with set initiative |
| `roll <name> <dex> <hp> <ac> [count]` | Roll initiative (1d20 + dex mod) |

**Examples:**
```
>>> add Paladin 18 45 18
Added: Paladin

>>> roll Goblin 2 7 15 4
  Goblin 1: 14 (1d20+2)
  Goblin 2: 8 (1d20+2)
  Goblin 3: 19 (1d20+2)
  Goblin 4: 11 (1d20+2)
```

#### Turn Management

| Command | Description |
|---------|-------------|
| `start` | Begin combat at round 1 |
| `next` or `n` | Advance to next turn |
| `prev` or `p` | Go back one turn |

#### Damage and Healing

| Command | Description |
|---------|-------------|
| `damage <name> <amount>` | Apply damage (aliases: `dmg`, `d`) |
| `heal <name> <amount>` | Heal combatant (alias: `h`) |
| `kill <name>` | Mark as dead |
| `revive <name>` | Revive (restores to 1 HP) |

#### Conditions

| Command | Description |
|---------|-------------|
| `condition <name> <cond> [rounds]` | Add condition (alias: `cond`) |
| `uncondition <name> <cond>` | Remove condition (alias: `uncond`) |
| `info <condition>` | Show condition effects |

#### Management

| Command | Description |
|---------|-------------|
| `remove <name>` | Remove from combat (alias: `rm`) |
| `set <name> <stat> <value>` | Modify init/hp/maxhp/ac |
| `status` or `s` | Show current initiative order |
| `clear` | Reset tracker completely |

#### Save/Load

| Command | Description |
|---------|-------------|
| `save <filename>` | Save encounter to JSON |
| `load <filename>` | Load encounter from JSON |

### D&D 5e Conditions

The tracker includes a reference for all 15 official conditions:
Blinded, Charmed, Deafened, Exhaustion, Frightened, Grappled, Incapacitated, Invisible, Paralyzed, Petrified, Poisoned, Prone, Restrained, Stunned, Unconscious

Use `info <condition>` to see the full effects.
