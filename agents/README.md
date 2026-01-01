# AI Agents

Claude-powered agents for enhanced D&D gameplay.

## Subfolders

- **dm-assistant/** - Rules clarification, encounter ideas, improvisation support
- **npc-roleplay/** - Consistent NPC voices and personalities
- **rules-lookup/** - Quick SRD reference and rulings

## Agent Structure

Each agent folder contains:
- `prompt.md` - System prompt for the agent
- `examples.md` - Example inputs/outputs
- `config.json` - Parameters and settings

## Mid-Game Usage

### DM Assistant
- "What happens if a player tries to grapple a flying creature?"
- "Give me 3 quick plot hooks for this tavern"
- "The players did something unexpected - help me improvise"

### NPC Roleplay
- Provide: NPC name, race, personality, current situation
- Get: In-character dialogue and reactions
- Maintains consistency across sessions

### Rules Lookup
- Quick spell/ability lookups
- Edge case rulings
- Action economy clarifications

## Creating New Agents

1. Create folder in `agents/[agent-name]/`
2. Write `prompt.md` with clear instructions
3. Add `examples.md` with sample interactions
4. Test for consistency and tone
