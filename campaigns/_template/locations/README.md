# Locations Directory

This folder contains all significant locations for the campaign. Use this system to keep locations organized, interconnected, and ready to reference during play.

---

## How to Organize Locations

### File Structure
```
locations/
├── README.md           # This file - master location index
├── _template.md        # Copy this for new locations
├── regions/            # (Optional) Subfolder for large regions/continents
├── cities/             # (Optional) Subfolder for settlements
├── dungeons/           # (Optional) Subfolder for adventure sites
└── [location-name].md  # Individual location files
```

### Naming Convention
Use lowercase with hyphens for filenames:
- `silverhold-city.md`
- `whispering-woods.md`
- `temple-of-the-fallen-sun.md`
- `the-rusty-anchor-tavern.md`

### Location Hierarchy
Organize locations by scale:

1. **World/Continent** - The largest geographical scope
2. **Region/Kingdom** - Countries, provinces, major geographical areas
3. **Settlement** - Cities, towns, villages
4. **District/Area** - Neighborhoods, quarters, zones within settlements
5. **Building/Site** - Specific structures or points of interest
6. **Room/Feature** - Detailed areas within a site (usually for dungeons)

### When to Create a Full Location File
Create a dedicated file when a location:
- Is a recurring setting for the campaign
- Has important NPCs, secrets, or plot hooks
- The party will explore in detail
- Needs maps or complex descriptions

### Quick Location Format (For Minor Locations)
For locations that don't need a full file, add them to the Quick Reference below:

**Format:** `Name - Type. Brief description. Notable feature.`

**Example:** `The Copper Kettle - Tavern. Working-class establishment near the docks. Known for cheap ale and dice games in the back.`

---

## Quick Reference Index

### All Locations

| Name | Type | Region | Status | File |
|------|------|--------|--------|------|
| [Name] | [City/Dungeon/Wilderness/etc.] | [Region] | [Active/Destroyed/Hidden] | `[filename].md` |
| | | | | |
| | | | | |
| | | | | |

---

## Locations by Region

### [Region 1 Name]
**Description:** [Brief overview of this region]

| Location | Type | Notes |
|----------|------|-------|
| [Location Name] | [Type] | [One-line description] |
| | | |

### [Region 2 Name]
**Description:** [Brief overview of this region]

| Location | Type | Notes |
|----------|------|-------|
| | | |
| | | |

---

## Locations by Type

### Major Cities
| City | Region | Population | Government | Notes |
|------|--------|------------|------------|-------|
| | | | | |
| | | | | |

### Towns and Villages
| Settlement | Region | Notable For | Notes |
|------------|--------|-------------|-------|
| | | | |
| | | | |

### Dungeons and Adventure Sites
| Site | Region | Difficulty | Status | Notes |
|------|--------|------------|--------|-------|
| | | [Levels X-Y] | [Cleared/Active/Unknown] | |
| | | | | |

### Wilderness Areas
| Area | Region | Terrain | Dangers | Notes |
|------|--------|---------|---------|-------|
| | | | | |
| | | | | |

### Points of Interest
| Location | Type | Region | Notes |
|----------|------|--------|-------|
| | [Temple/Ruin/Landmark/etc.] | | |
| | | | |

---

## Map References

### World/Regional Maps
| Map Name | Covers | File/Link |
|----------|--------|-----------|
| [Map Name] | [What area it shows] | `../assets/maps/[file]` |
| | | |

### Battle Maps
| Map Name | Location | File/Link |
|----------|----------|-----------|
| [Map Name] | [Where it's used] | `../assets/maps/[file]` |
| | | |

### Map Sources
- [Link to map-making tools or resources you use]
- [Link to pre-made maps you've collected]

---

## Connecting Locations

When creating location files, link them to other campaign elements:

### Link to Parent Regions
```markdown
**Region:** Part of the [Northern Reaches](northern-reaches.md)
```

### Link to NPCs
```markdown
**Key NPCs:**
- [Mayor Thornbury](../npcs/mayor-thornbury.md) - Runs the town
- [Gareth the Smith](../npcs/gareth-smith.md) - Owns the forge
```

### Link to Other Locations
```markdown
**Connections:**
- North road leads to [Silverhold](silverhold-city.md) (3 days travel)
- Secret tunnel connects to [The Undercroft](undercroft-dungeon.md)
```

### Link from Sessions
In session notes, reference locations:
```markdown
The party traveled to [Millbrook](../locations/millbrook.md) and investigated the mill.
```

---

## Location Profile Template

Copy `_template.md` for each significant location. The template includes:

1. **Basic Info** - Type, region, population, government
2. **Description** - What the party sees on arrival
3. **Points of Interest** - Specific places within the location
4. **Notable NPCs** - Who can be found here
5. **Shops/Services** - Commercial establishments
6. **Rumors/Information** - What people are talking about
7. **Threats/Dangers** - What makes this place risky
8. **Secrets** - Hidden information for the DM
9. **History** - Relevant backstory
10. **Connections** - How it links to other locations
11. **Notes** - Session-by-session developments

---

## Party Progress

### Visited Locations
| Location | First Visited | Status | Notable Events |
|----------|---------------|--------|----------------|
| | Session [#] | [Explored/Partially Explored/Passed Through] | [What happened there] |
| | | | |

### Discovered But Not Visited
| Location | How Discovered | Party Interest |
|----------|----------------|----------------|
| [Name] | [Heard rumor / Saw on map / NPC mentioned] | [High/Medium/Low] |
| | | |

### Locations of Interest (Foreshadowed)
[Places you've hinted at that the party might eventually visit]
- [Location] - [How it was foreshadowed]
- [Location] - [How it was foreshadowed]

---

## Destroyed / Changed Locations

Track locations that have been significantly altered:

| Location | What Happened | Session | Current State |
|----------|---------------|---------|---------------|
| | [Destroyed/Corrupted/Abandoned/etc.] | [#] | [Description of current state] |
| | | | |

---

## Tips for Location Management

1. **Start Small:** Only detail locations the party will definitely visit
2. **Expand as Needed:** Add detail when the party shows interest
3. **Connect Everything:** Locations should feel like part of a living world
4. **Use Sensory Details:** Describe what they see, hear, smell, feel
5. **Include Hooks:** Every location should have something to do or discover
6. **Update After Sessions:** Note what changed, what was revealed, what was destroyed
7. **Reuse and Recycle:** An unused location can appear elsewhere with minor changes
