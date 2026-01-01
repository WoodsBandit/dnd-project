# D&D Project - Claude Instructions

## Project Overview

This is a Dungeons & Dragons project workspace focused on:
- **3D Printing**: Designing .stl and .gcode files for miniatures, terrain, and props
- **Campaign Tools**: Helper utilities for DMs and players
- **AI Agents**: Claude-powered agents for real-time game enhancement

## Directory Structure

```
dnd/
├── 3d-prints/           # STL and GCODE files
│   ├── miniatures/      # Character and monster minis
│   ├── terrain/         # Dungeon tiles, buildings, landscapes
│   └── props/           # Items, weapons, accessories
├── campaigns/           # Campaign-specific content
│   └── [campaign-name]/ # Each campaign gets its own folder
├── tools/               # Campaign helper tools
│   ├── generators/      # Random generators (NPCs, loot, encounters)
│   ├── trackers/        # Initiative, HP, inventory trackers
│   └── calculators/     # CR, XP, encounter balance tools
├── agents/              # AI agent configurations
│   ├── dm-assistant/    # DM support agent
│   ├── npc-roleplay/    # NPC voice and personality agent
│   └── rules-lookup/    # Quick rules reference agent
├── CLAUDE.md            # This file
├── index.md             # Project navigation
└── log.md               # Session and development log
```

## Working Guidelines

### 3D Print Files
- Use descriptive filenames: `goblin-archer-28mm.stl`
- Include print settings in companion `.md` files
- Track slicer profiles for consistent GCODE generation
- Note scale (typically 28mm for minis)

### Campaign Management
- Each campaign folder should contain: notes, maps, NPCs, session logs
- Use consistent naming: `session-01.md`, `npc-tavern-keeper.md`
- Link related content for easy navigation

### AI Agent Development
- Agents should be modular and campaign-agnostic where possible
- Document agent prompts and expected inputs/outputs
- Test agent responses for consistency and tone

### Mid-Game AI Usage
When using Claude as agents during gameplay:
1. **DM Assistant**: Rules clarification, encounter suggestions, improvisation help
2. **NPC Roleplay**: Voice distinct NPCs with consistent personalities
3. **Player Support**: Spell lookups, ability checks, character advice
4. **World Building**: On-the-fly location/item/plot generation

## Code Standards
- Python preferred for tools
- JSON for data storage (monsters, items, NPCs)
- Markdown for documentation and session notes

## Quick Commands
- Generate NPC: Provide race, class, personality traits
- Generate encounter: Provide party level, difficulty, environment
- Generate loot: Provide CR, theme, rarity distribution
- STL review: Check for printability issues

## Resources
- D&D 5e SRD for reference content
- OpenGameArt for CC-licensed assets
- Thingiverse/Printables for community STL files
