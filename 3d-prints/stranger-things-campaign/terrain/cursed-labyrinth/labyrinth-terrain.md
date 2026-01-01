# Cursed Labyrinth Terrain - 3D Print Design Specifications

## Overview

The Cursed Labyrinth exists between dimensions - a place where geometry itself has become corrupted. These modular terrain pieces capture the unsettling wrongness of spaces that should not exist, with walls too smooth, angles that do not quite add up, and an ever-present sense that the maze itself is alive and watching.

---

## Design Philosophy

### The "Wrong" Aesthetic
- **Unnatural Smoothness**: Walls lack any natural texture - no stone grain, no tool marks, no weathering
- **Subtle Geometric Distortion**: Corners at 89 or 91 degrees instead of 90; walls that lean imperceptibly
- **Liminal Horror**: The maze feels abandoned yet maintained, ancient yet timeless
- **Dimensional Bleed**: Faint suggestions of other realities visible in the walls

### Visual Contrast Strategy
These pieces should feel jarringly different from natural cavern terrain:
| Cavern Terrain | Labyrinth Terrain |
|----------------|-------------------|
| Rough, organic | Smooth, artificial |
| Warm earth tones | Cold grays and blacks |
| Random formations | Precise geometry |
| Comfortable chaos | Uncomfortable order |

---

## Corridor Pieces

### 1. Straight Corridor
**Dimensions**: 2" x 6" (50mm x 150mm)
**Wall Height**: 1.5" (38mm)
**Floor Thickness**: 0.12" (3mm)

**Design Elements**:
- Walls are perfectly smooth with subtle 0.5-degree inward lean
- Floor has faint, barely-visible geometric patterns (think crop circles)
- Every 2 inches, walls have hairline vertical seams suggesting massive blocks
- Optional: Thin channel along floor edges for LED strip insertion

**Print Orientation**: Flat on build plate
**Supports**: None required
**Infill**: 15% gyroid for walls, 20% for floor

**Variants to Model**:
- Standard (clean)
- Cracked floor (something trying to break through)
- Symbol-etched (faint Upside Down markings)

---

### 2. Left Turn Corner
**Dimensions**: 2" x 2" (50mm x 50mm)
**Wall Height**: 1.5" (38mm)

**Design Elements**:
- Interior corner is slightly rounded (radius 2mm) - unnaturally perfect
- Exterior corner has impossible sharpness
- Floor pattern flows continuously around corner
- Inner wall slightly shorter than outer (creates subtle wrongness)

**Print Orientation**: Flat on build plate
**Supports**: None required
**Infill**: 15% gyroid

---

### 3. Right Turn Corner
**Dimensions**: 2" x 2" (50mm x 50mm)
**Wall Height**: 1.5" (38mm)

**Design Elements**:
- Mirror of Left Turn with identical specifications
- Consider printing both orientations from single STL using mirror in slicer

---

### 4. T-Intersection
**Dimensions**: 2" x 2" (50mm x 50mm)
**Wall Height**: 1.5" (38mm)

**Design Elements**:
- Central floor area has subtle depression (0.5mm) - draws the eye
- Wall ends have chamfered tops suggesting they continue infinitely upward
- Faint concentric circle pattern on floor centered at junction
- Each corridor branch is slightly different width (49mm, 50mm, 51mm)

**Print Orientation**: Flat on build plate
**Supports**: None required
**Infill**: 15% gyroid

---

### 5. Four-Way Intersection (Crossroads)
**Dimensions**: 2" x 2" (50mm x 50mm)
**Wall Height**: 1.5" (38mm)

**Design Elements**:
- Floor has inset compass rose or arcane symbol
- Each corner pillar is slightly different height (varies by 1mm)
- Center point has small raised dome (perfect hemisphere)
- Walls approach but do not touch corners - 1mm gaps suggest instability

**Print Orientation**: Flat on build plate
**Supports**: None required
**Infill**: 15% gyroid

---

### 6. Dead End
**Dimensions**: 2" x 2" (50mm x 50mm)
**Wall Height**: 1.5" (38mm)

**Design Elements**:
- End wall has subtle carved symbols (Upside Down language/warnings)
- Symbols are recessed 0.5mm - catch shadows dramatically
- Wall has slight convex bulge (2mm at center) - breathing?
- Floor tiles angle slightly toward end wall (things flow to dead ends)
- Optional: Hollow behind end wall for LED glow effect

**Symbol Suggestions**:
- Geometric impossibilities (Penrose triangles, Klein bottles)
- Warning glyphs (hands, eyes, spirals)
- Countdown numbers in unknown script

**Print Orientation**: Flat on build plate
**Supports**: None required
**Infill**: 15% gyroid, 0% behind symbol wall if using LED

---

## Special Pieces

### 7. Blackbird Statue Shelf
**Dimensions**: 2" x 3" (50mm x 75mm)
**Wall Height**: 1.5" (38mm)
**Total Alcoves**: 24 (arranged 6 wide x 4 high)

**Design Elements**:
- Wall-mounted piece that attaches to corridor side
- 24 small alcoves (8mm x 8mm x 10mm deep each)
- Each alcove has slightly different shape (squares, circles, hexagons, irregular)
- Alcove arrangement forms subtle pattern when viewed from distance
- Base extends 0.75" (19mm) from wall for stability
- Numbered alcoves (1-24) in tiny recessed text below each

**Alcove Layout**:
```
[01][02][03][04][05][06]
[07][08][09][10][11][12]
[13][14][15][16][17][18]
[19][20][21][22][23][24]
```

**Riddle Integration**:
- One alcove (randomize which) has deeper recess with hidden symbol
- Correct alcove has subtle differences (slightly larger, different patina)
- Consider making alcoves with magnetic inserts for bird placement

**Print Orientation**: Flat on build plate (shelf face up)
**Supports**: Required for alcove overhangs (use support interface)
**Infill**: 20% for structural integrity

---

### 8. Blackbird Statues (Set of 24)
**Dimensions**: 0.3" x 0.3" x 0.4" each (7mm x 7mm x 10mm)
**Base**: 6mm diameter circle

**Design Elements**:
- Small raven/blackbird figures in various poses
- Each bird is slightly unique (head angles, wing positions)
- Bases sized to fit snugly in shelf alcoves
- One "correct" bird has subtle differences:
  - Slightly larger
  - Different eye style (open vs closed)
  - Wing position pointing direction
  - Hidden symbol on base underside

**Bird Pose Variants** (4 of each):
1. Standing alert
2. Head tilted
3. Wings slightly raised
4. Looking backward
5. Preening
6. Calling/cawing

**Print Considerations**:
- Print on supports with small contact points
- 0.2mm layer height or finer for detail
- Consider resin printing for best detail
- Print all 24 on single plate in grid arrangement

**FDM Optimization**:
- Thicken legs to 1.5mm minimum
- Solid bases for stability
- Simplify feather detail to printable geometry
- Add small support nubs between legs (remove post-print)

---

### 9. Lost Knight Encounter Area
**Dimensions**: 4" x 4" (100mm x 100mm)
**Wall Height**: None (open floor piece)
**Floor Thickness**: 0.2" (5mm)

**Design Elements**:
- Central chamber floor with ethereal/ghostly aesthetic
- Floor has layered translucent appearance (print in clear/white)
- Concentric ripple pattern emanating from center
- Four corner positions for optional wall attachments
- Central 1" diameter raised dais for knight miniature
- Scattered "frozen moment" details: dropped weapons, footprints, handprints

**Ethereal Effect Techniques**:
- Print floor in multiple layers of increasing transparency
- Base layer: solid gray
- Middle layer: translucent white (visible pattern)
- Top layer: clear with ripple texture
- Alternative: Single print designed for LED underlighting

**Edge Details**:
- Corridor connections on all four sides (standard 2" openings)
- Edges fade from smooth labyrinth style to ethereal ripples
- Small lip (1mm) to contain any LED diffusion material

**Print Orientation**: Flat on build plate
**Supports**: None for base version; minimal for raised dais
**Infill**: 100% for floor (needed for translucent effect)
**Special Materials**: Consider clear PETG or resin for ethereal layer

---

### 10. Portal to Upside Down
**Dimensions**: 2" x 3" (50mm x 75mm)
**Archway Height**: 2" (50mm)
**Archway Width**: 1.5" (38mm)

**Design Elements**:
- Freestanding archway with thick frame
- Frame surface has flowing, organic texture (contrast to smooth walls)
- Interior of arch is open (for inserting portal effect)
- Base extends 0.5" on each side for stability
- Frame decorated with reaching tendrils and vine-like growths
- Threshold has clear demarcation line (reality boundary)

**Portal Effect Options**:

*Option A - Physical Insert*:
- Separate portal disc that friction-fits into archway
- Disc has swirling pattern (concentric warped circles)
- Print in silk or color-change filament
- Multiple discs: closed, partially open, fully open

*Option B - LED Integration*:
- Hollow frame with channel for LED strip
- Diffuser panel slot in archway
- Battery compartment in base
- Pulsing glow effect for "active" portal

*Option C - Mixed Media*:
- Open archway with mounting points
- Insert iridescent film or holographic material
- Theatrical gel or cellophane for color

**Transition Design**:
- "Before" side: Smooth labyrinth aesthetic
- "After" side: Organic Upside Down texture begins
- Frame itself is the transition (smooth to organic)

**Print Orientation**: Print archway on its back (arch opening facing up)
**Supports**: Required for arch interior
**Infill**: 20% for frame stability

---

## Modular Connection System

### The Shifting Maze Mechanic
The labyrinth rearranges itself. The connection system must allow quick reconfiguration during play.

### Connection Method: Magnetic Pins

**Components**:
- 5mm x 2mm disc magnets (N52 grade)
- Magnet recesses in all wall ends
- Polarity-matched for proper alignment

**Implementation**:
- Each wall end has 2 magnet positions (top and bottom)
- Recesses are 5.2mm diameter x 2.2mm deep
- Glue magnets after printing (consistent polarity!)
- Walls snap together satisfying and hold during play
- Easy separation for maze reconfiguration

**Magnet Placement Pattern**:
```
Wall End Cross-Section:
    [====TOP MAGNET====]
    |                  |
    |   Wall Face      |
    |                  |
    [===BOTTOM MAGNET==]
```

### Alternative: Puzzle-Lock Tabs

**For Non-Magnetic Option**:
- Male/female tabs on alternating wall ends
- Tab dimensions: 3mm wide x 2mm deep x 5mm tall
- Slight interference fit (0.1mm)
- Rounded edges for easy insertion/removal
- Print orientation critical for tab strength

### Floor Alignment

**Registration Pegs**:
- 3mm diameter pegs on floor edges
- Corresponding 3.2mm holes on adjacent pieces
- Pegs are 2mm tall, holes are 2.5mm deep
- Allows slight play for imperfect prints
- One peg per 2" of edge

---

## FDM Print Optimization

### Recommended Print Settings

| Setting | Value | Notes |
|---------|-------|-------|
| Layer Height | 0.16mm | Balance of speed and smoothness |
| Wall Count | 3 | Structural integrity |
| Top/Bottom Layers | 4 | Solid floors and wall tops |
| Infill | 15-20% | Gyroid pattern preferred |
| Print Speed | 50mm/s | Slower for smooth walls |
| Supports | Minimal | Design avoids overhangs |
| Brim | 5mm | Prevents warping on large pieces |

### Achieving "Too Smooth" Walls

**During Printing**:
- Outer wall speed: 30mm/s (slower = smoother)
- Enable ironing on top surfaces
- Z-seam: Sharpest corner or rear alignment
- Coasting: 0.1mm to reduce seam blob

**Post-Processing**:
1. Light sanding with 400-grit (optional - may add unwanted texture)
2. Filler primer spray (2-3 coats)
3. Wet sand with 800-grit
4. Final primer coat
5. High-gloss clear coat for unnatural sheen

**Filament Recommendations**:
- Primary: Gray or charcoal PLA/PETG
- Avoid wood-fill or textured filaments
- Silk filaments add unsettling sheen
- Black with gray dry-brush for depth

### Problem Prevention

**Warping**:
- Use heated bed (60C for PLA, 80C for PETG)
- Enclosure recommended for larger pieces
- Print corridors in 2" segments if warping persists

**Layer Lines**:
- Orient pieces to hide lines in corners
- Primer fills minor layer lines
- Accept some lines on floors (add to aged look)

**Stringing on Small Details**:
- Enable retraction (6mm at 45mm/s for Bowden)
- Travel speed: 150mm/s
- Combing: Within infill only
- Clean birds and symbols with heat gun briefly

---

## Assembly Instructions

### Phase 1: Printing (Recommended Order)

**Print Priority**:
1. Straight corridors (x8) - Core of any layout
2. Turn pieces (x4 each direction) - Essential navigation
3. T-intersections (x4) - Decision points
4. Four-way intersections (x2) - Major junctions
5. Dead ends (x4) - Puzzle elements
6. Special pieces - Final additions

**Batch Printing**:
- Group similar heights on same plate
- Corridors: 2 per plate typical
- Small pieces: Fill remaining space
- Birds: All 24 on single plate

### Phase 2: Post-Processing

**Step 1 - Cleanup**:
- Remove supports carefully (flush cutters)
- Clean magnet recesses with 5mm drill bit
- Remove any stringing with heat gun
- Check floor flatness (sand if needed)

**Step 2 - Assembly Prep**:
- Test fit all magnetic connections
- Mark magnet polarity before gluing
- Use thin CA glue for magnets
- Allow 24-hour cure before play

**Step 3 - Surface Treatment**:
- Filler primer (2 coats, light sanding between)
- Check for smooth labyrinth aesthetic
- Additional smoothing as needed

### Phase 3: Painting

**Labyrinth Color Palette**:
- Base coat: Dark gray (nearly black)
- Dry brush: Medium gray
- Edge highlight: Pale gray (very subtle)
- Recesses: Black wash
- Special: Hints of otherworldly color in symbols

**Painting Steps**:

1. **Prime** - Gray primer (already applied in post-processing)

2. **Base Coat** - Dark charcoal gray, full coverage

3. **First Dry Brush** - Medium gray on wall edges and floor texture

4. **Wash** - Black wash in all recesses and seams

5. **Second Dry Brush** - Light gray, very light on highest points

6. **Details**:
   - Symbols: Dark purple or teal (dimensional bleed)
   - Floor patterns: Slightly lighter gray
   - Dead end symbols: Faint glow effect (white to color gradient)

7. **Seal** - Matte varnish for most surfaces, gloss on walls for "wrong" sheen

**Bird Painting**:
- All black with slight blue-black highlights
- Eyes: Tiny dot of red or gold (unsettling)
- "Correct" bird: Subtle difference (larger eye, different color)

### Phase 4: LED Integration (Optional)

**Materials**:
- 3mm wide LED strip (warm white or cool white)
- 3V coin cell holders
- Thin wire (30 AWG)
- Diffusion material (frosted acrylic or vellum)

**Installation**:
1. Route LED strip through floor channels
2. Hide battery in dead end hollow
3. Test before final assembly
4. Secure with hot glue

**Effects**:
- Portal: Pulsing purple/red glow
- Dead ends: Faint glow behind symbols
- Encounter area: Underlighting for ethereal effect

---

## Atmosphere Tips

### Table Setup

**Lighting**:
- Dim room lighting significantly
- Single overhead lamp creates dramatic shadows
- LED candles outside maze perimeter
- Phone flashlight for player "torch" in-character

**Sound**:
- Ambient drone (low frequency)
- Occasional distant sounds (scraping, whispers)
- Silence when entering dead ends
- Heartbeat when near portal

**Props**:
- Small mirror to "reflect" impossible geometry
- Incense for otherworldly smell (use sparingly)
- Cold pack under maze section (unexpected cold spot)

### DM Techniques

**Maze Shifting**:
- When players are not looking, subtly rearrange pieces
- "The corridor behind you looks... different"
- Use T-intersections that "were definitely turns before"
- Dead ends appear where passages existed

**Blackbird Riddle Enhancement**:
- Describe each bird's subtle differences
- Allow Investigation checks to narrow options
- Wrong choices trigger effects (whispers, cold, shadows)
- Correct choice causes visible reaction (birds turn to look)

**Lost Knight Encounter**:
- Place knight mini on ethereal floor before reveal
- Describe translucent/ghostly quality
- Lighting from below enhances effect
- Knight speaks in echoes, overlapping voices

**Portal Drama**:
- Build anticipation before revealing portal
- Change portal insert from "closed" to "active"
- Describe reality warping at threshold
- Physical cold near portal (hidden cold pack)

### Player Engagement

**Sensory Description Prompts**:
- "The walls are too smooth. Your fingers find no purchase."
- "This corner feels wrong. The angle doesn't add up."
- "The floor tiles point toward the dead end. Everything flows there."
- "You hear your footsteps... and then you hear them again, delayed."

**Labyrinth Quirks**:
- Shadows fall in wrong directions
- Sound carries strangely (distant whispers feel close)
- Time feels uncertain (minutes or hours?)
- Thirst and hunger fade (dimensional effect)

---

## Quick Reference Card

### Piece Count for Standard Maze
| Piece | Minimum | Recommended |
|-------|---------|-------------|
| Straight Corridor | 6 | 10-12 |
| Left Turn | 2 | 4 |
| Right Turn | 2 | 4 |
| T-Intersection | 2 | 4 |
| Four-Way | 1 | 2 |
| Dead End | 2 | 4-6 |
| Blackbird Shelf | 1 | 1 |
| Blackbird Statues | 24 | 24 |
| Encounter Area | 1 | 1 |
| Portal | 1 | 1-2 |

### Print Time Estimates (Standard Settings)
| Piece | Time | Filament |
|-------|------|----------|
| Straight Corridor | 2.5 hrs | 25g |
| Turn Pieces | 1.5 hrs | 15g |
| T-Intersection | 1.5 hrs | 18g |
| Four-Way | 1.5 hrs | 20g |
| Dead End | 1.5 hrs | 16g |
| Blackbird Shelf | 3 hrs | 35g |
| All 24 Birds | 2 hrs | 10g |
| Encounter Area | 4 hrs | 50g |
| Portal | 3.5 hrs | 40g |

**Total Full Set**: ~30-35 hours, ~400g filament

### Troubleshooting Quick Fixes
| Problem | Solution |
|---------|----------|
| Pieces don't align | Check for warping, sand bottoms flat |
| Magnets repel | Flip one magnet (polarity reversed) |
| Birds fall over | Add tiny dot of poster tack to base |
| Walls not smooth enough | Additional primer coats and sanding |
| LED too bright | Add diffusion layer or reduce voltage |

---

## File Organization

```
cursed-labyrinth/
├── labyrinth-terrain.md (this file)
├── STL/
│   ├── corridors/
│   │   ├── straight-corridor.stl
│   │   ├── straight-corridor-cracked.stl
│   │   ├── straight-corridor-symbols.stl
│   │   ├── left-turn.stl
│   │   ├── right-turn.stl
│   │   ├── t-intersection.stl
│   │   ├── four-way-intersection.stl
│   │   └── dead-end.stl
│   ├── special/
│   │   ├── blackbird-shelf.stl
│   │   ├── blackbird-statues-all.stl
│   │   ├── encounter-area-base.stl
│   │   ├── encounter-area-ethereal-layer.stl
│   │   ├── portal-frame.stl
│   │   └── portal-inserts/
│   │       ├── portal-closed.stl
│   │       ├── portal-partial.stl
│   │       └── portal-open.stl
│   └── accessories/
│       ├── connection-test-piece.stl
│       └── magnet-alignment-jig.stl
├── print-profiles/
│   ├── labyrinth-standard.curaprofile
│   └── labyrinth-detail.curaprofile
└── reference/
    ├── magnet-polarity-guide.png
    └── paint-palette-reference.png
```

---

*"The maze remembers every step you take. And it learns."*
