# NPCs Directory

This folder contains all Non-Player Characters for the campaign. Use this system to keep NPCs organized, memorable, and easy to reference during play.

---

## How to Organize NPCs

### File Structure
```
npcs/
├── README.md           # This file - master NPC index
├── _template.md        # Copy this for new NPCs
├── allies/             # (Optional) Subfolder for allied NPCs
├── enemies/            # (Optional) Subfolder for antagonists
└── [npc-name].md       # Individual NPC files
```

### Naming Convention
Use lowercase with hyphens for filenames:
- `thornwick-the-barkeep.md`
- `captain-helena-voss.md`
- `the-crimson-stranger.md`

### When to Create a Full NPC File
Create a dedicated file when an NPC:
- Has recurring importance to the story
- The party has formed a relationship with them
- They have secrets, goals, or arc potential
- You need to remember specific details about them

### Quick NPC Format (For Minor Characters)
For NPCs who don't need a full file, add them to the Quick Reference table below:

**Format:** `Name - Race/Occupation. Brief description. Disposition.`

**Example:** `Greta - Human baker. Elderly, flour-dusted, knows everyone's business. Friendly but gossipy.`

---

## Quick Reference Index

### All NPCs

| Name | Location | Faction | Category | Status | File |
|------|----------|---------|----------|--------|------|
| [Name] | [Where found] | [Affiliation] | [Ally/Enemy/Neutral] | [Alive/Dead/Missing] | `[filename].md` |
| | | | | | |
| | | | | | |
| | | | | | |

---

## NPCs by Category

### Allies
Characters who actively help or support the party.

| Name | Role | Location | Notes |
|------|------|----------|-------|
| | | | |
| | | | |

### Enemies
Antagonists, rivals, and those who oppose the party.

| Name | Threat Level | Location | Notes |
|------|--------------|----------|-------|
| | | | |
| | | | |

### Neutral / Undetermined
Characters whose allegiance is unclear or genuinely neutral.

| Name | Role | Location | Notes |
|------|------|----------|-------|
| | | | |
| | | | |

### Patrons / Quest Givers
Characters who provide missions, jobs, or guidance.

| Name | Organization | Quest Given | Status |
|------|--------------|-------------|--------|
| | | | |
| | | | |

---

## NPCs by Faction

### [Faction 1 Name]
- [NPC Name] - Role, disposition
- [NPC Name] - Role, disposition

### [Faction 2 Name]
- [NPC Name] - Role, disposition
- [NPC Name] - Role, disposition

### [Faction 3 Name]
- [NPC Name] - Role, disposition

### Unaffiliated
- [NPC Name] - Role, disposition

---

## NPCs by Location

### [Location 1]
- [NPC Name] - Brief role
- [NPC Name] - Brief role

### [Location 2]
- [NPC Name] - Brief role

### Traveling / Mobile
- [NPC Name] - Where they might be found

---

## Linking NPCs

When creating NPC files, link them to other campaign elements:

### Link to Locations
```markdown
**Location:** [The Rusty Anchor](../locations/rusty-anchor.md)
```

### Link to Factions
```markdown
**Faction:** Member of the [Merchant's Guild](../overview.md#merchants-guild)
```

### Link to Other NPCs
```markdown
**Relationships:**
- Married to [Elena](elena-blackwood.md)
- Rival of [Marcus](marcus-thorne.md)
```

### Link from Sessions
In session notes, reference NPCs:
```markdown
The party met [Thornwick](../npcs/thornwick.md) at the tavern.
```

---

## NPC Profile Template

Copy `_template.md` for each significant NPC. The template includes:

1. **Basic Info** - Race, occupation, location, faction, status
2. **Appearance** - Physical description for roleplay
3. **Personality** - Traits, ideals, bonds, flaws (D&D style)
4. **Voice/Mannerisms** - How to portray them at the table
5. **Relationship to Party** - History and current disposition
6. **What They Know** - Information they can share
7. **What They Want** - Goals and motivations
8. **Stats** - Combat statistics if needed
9. **Notes** - Ongoing developments

---

## Deceased / Removed NPCs

Track NPCs who are no longer active in the campaign:

| Name | Fate | Session | Notes |
|------|------|---------|-------|
| | [Killed by party / Died off-screen / Left region / etc.] | [#] | |
| | | | |

---

## Tips for NPC Management

1. **Update After Sessions:** Mark new NPCs, change dispositions, note developments
2. **Use Quick Reference First:** Don't over-prep minor NPCs with full files
3. **Promote NPCs:** If a minor NPC becomes important, create a full file
4. **Track Relationships:** Note how NPCs feel about each other, not just the party
5. **Keep Voices Simple:** A single memorable trait is better than a complex accent
6. **Recycle:** Unused NPCs can reappear in different contexts
