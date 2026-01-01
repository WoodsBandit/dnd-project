# Assets Directory

This folder stores all media files for the campaign: maps, handouts, portraits, tokens, and other visual or audio resources. Keep assets organized and indexed for quick access during play.

---

## Folder Structure

Create these subfolders to organize your assets:

```
assets/
├── README.md           # This file - asset index and guidelines
├── maps/
│   ├── world/          # World and regional maps
│   ├── city/           # City and town maps
│   ├── dungeon/        # Dungeon and interior maps
│   └── battle/         # Battle/encounter maps (gridded)
├── handouts/
│   ├── letters/        # In-game correspondence
│   ├── documents/      # Contracts, notices, books
│   └── puzzles/        # Puzzle handouts and clues
├── portraits/
│   ├── npcs/           # NPC portraits
│   ├── pcs/            # Player character art
│   └── monsters/       # Monster/creature images
├── tokens/             # VTT tokens (if using virtual tabletop)
├── audio/              # Music and sound effects (optional)
└── misc/               # Miscellaneous assets
```

---

## Naming Conventions

Use consistent naming to keep assets findable:

### Maps
- `[location]-[type]-[detail].png`
- Examples:
  - `silverhold-city-overview.png`
  - `silverhold-city-market-district.png`
  - `goblin-cave-level1.png`
  - `goblin-cave-level2.png`
  - `tavern-battle-grid.png`

### Handouts
- `[session##]-[type]-[name].png`
- Examples:
  - `session05-letter-from-baron.png`
  - `session12-wanted-poster-blackhand.png`
  - `session08-puzzle-rune-door.png`

### Portraits
- `[name]-portrait.png`
- Examples:
  - `thornwick-portrait.png`
  - `captain-voss-portrait.png`
  - `goblin-shaman-portrait.png`

### Tokens
- `[name]-token.png`
- Examples:
  - `korrath-ironforge-token.png`
  - `skeleton-token.png`
  - `dire-wolf-token.png`

---

## Asset Index

### World and Regional Maps

| Name | Region/Area | Scale | File | Notes |
|------|-------------|-------|------|-------|
| [Map Name] | [What it covers] | [World/Regional/Local] | `maps/world/[file]` | [Grid? Legend? Version?] |
| | | | | |
| | | | | |

### City and Town Maps

| Name | Location | Scale | File | Notes |
|------|----------|-------|------|-------|
| [Map Name] | [Which settlement] | [Full city/District/Building] | `maps/city/[file]` | |
| | | | | |

### Dungeon and Interior Maps

| Name | Location | Levels | File | Notes |
|------|----------|--------|------|-------|
| [Dungeon Name] | [Where in world] | [# of levels] | `maps/dungeon/[file]` | [Key room references] |
| | | | | |

### Battle Maps

| Name | Environment | Grid Size | File | Notes |
|------|-------------|-----------|------|-------|
| [Map Name] | [Forest/Cave/Urban/etc.] | [5ft squares?] | `maps/battle/[file]` | [Hazards, cover, etc.] |
| | | | | |

---

## Handout Index

### Letters and Correspondence

| Name | From | To | Session Given | File |
|------|------|----|--------------:|------|
| [Description] | [Sender] | [Recipient] | [##] | `handouts/letters/[file]` |
| | | | | |

### Documents and Papers

| Name | Type | Session Given | File | Notes |
|------|------|---------------|------|-------|
| [Description] | [Contract/Notice/Book page/etc.] | [##] | `handouts/documents/[file]` | |
| | | | | |

### Puzzles and Clues

| Name | Puzzle Type | Session Used | File | Solution |
|------|-------------|--------------|------|----------|
| [Description] | [Riddle/Cipher/Physical/etc.] | [##] | `handouts/puzzles/[file]` | [Link or brief note] |
| | | | | |

---

## Portrait Index

### NPC Portraits

| NPC | Description | File | Source |
|-----|-------------|------|--------|
| [Name] | [Brief description] | `portraits/npcs/[file]` | [Original/AI/Stock/Artist] |
| | | | |

### PC Portraits

| Character | Player | File | Source |
|-----------|--------|------|--------|
| [Name] | [Player] | `portraits/pcs/[file]` | [Commission/AI/Stock/Player-made] |
| | | | |

### Monster/Creature Images

| Creature | Type | File | Source |
|----------|------|------|--------|
| [Name] | [Monster type] | `portraits/monsters/[file]` | [MM/Homebrew/AI/Artist] |
| | | | |

---

## Token Index (For VTT Users)

### PC Tokens

| Character | Size | File | Notes |
|-----------|------|------|-------|
| [Name] | [Medium/Large/etc.] | `tokens/[file]` | |
| | | | |

### NPC Tokens

| NPC | Size | File | Notes |
|-----|------|------|-------|
| [Name] | | `tokens/[file]` | |
| | | | |

### Monster Tokens

| Monster | Size | Quantity | File |
|---------|------|----------|------|
| [Name] | [Size] | [How many unique tokens] | `tokens/[file]` |
| | | | |

---

## Audio Resources (Optional)

### Ambient Music

| Name | Mood/Setting | Duration | File/Link |
|------|--------------|----------|-----------|
| [Playlist/Track name] | [Combat/Tavern/Dungeon/etc.] | [Length] | [File or streaming link] |
| | | | |

### Sound Effects

| Name | Type | File/Link |
|------|------|-----------|
| [Effect name] | [Door/Combat/Magic/etc.] | |
| | | |

---

## External Resources

### Map Resources
- [Dungeon Scrawl](https://dungeonscrawl.com/) - Free dungeon map maker
- [Inkarnate](https://inkarnate.com/) - Fantasy map making tool
- [2-Minute Tabletop](https://2minutetabletop.com/) - Free battle maps
- [Dyson Logos](https://dysonlogos.blog/) - Free dungeon maps

### Portrait Resources
- [HeroForge](https://www.heroforge.com/) - 3D character creator (screenshots)
- [ArtBreeder](https://www.artbreeder.com/) - AI portrait generation
- [Character Creator](https://www.cartographyassets.com/) - Various tools

### Token Resources
- [Token Stamp](https://rolladvantage.com/tokenstamp/) - Token creator
- [Token Tool](https://www.rptools.net/toolbox/token-tool/) - Free token maker

### Audio Resources
- [Tabletop Audio](https://tabletopaudio.com/) - Free ambient sounds
- [Syrinscape](https://syrinscape.com/) - Professional soundscapes
- [YouTube Playlists](https://youtube.com/) - Search "D&D ambient music"

---

## Asset Creation Notes

### Image Specifications

| Asset Type | Recommended Size | Format | Notes |
|------------|------------------|--------|-------|
| Battle Maps | 140px per 5ft square | PNG/JPG | Higher res for zoom |
| World Maps | 2000-4000px wide | PNG/JPG | Depends on detail |
| Portraits | 400x400px minimum | PNG | Square works best |
| Tokens | 280px diameter | PNG | Transparent background |
| Handouts | 1000px wide | PNG/JPG | Readable text |

### Naming Best Practices
1. Use lowercase with hyphens (no spaces)
2. Include location or NPC name for context
3. Add version numbers if you iterate (map-v2.png)
4. Use descriptive names you'll remember later

### Storage Tips
- Keep original/source files if you might edit later
- Compress large files that don't need high resolution
- Back up assets outside the campaign folder
- Track sources for attribution if sharing

---

## Asset Checklist for New Campaigns

### Essential
- [ ] World or regional map (overview)
- [ ] Starting location map
- [ ] PC portraits or tokens (if VTT)
- [ ] Key NPC portraits

### Recommended
- [ ] First dungeon/adventure site map
- [ ] Battle maps for likely combat locations
- [ ] Ambient music playlists

### Nice to Have
- [ ] Handout templates
- [ ] Monster tokens
- [ ] Sound effects

---

## Asset Usage Log

Track which assets have been shown to players:

| Asset | Session First Used | Context |
|-------|-------------------|---------|
| [Asset name] | [##] | [How it was used] |
| | | |
| | | |
