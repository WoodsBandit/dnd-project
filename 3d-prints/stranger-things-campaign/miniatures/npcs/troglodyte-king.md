# Troglodyte King (Sketh-Kra) - Diplomacy NPC
## 3D Miniature Design Specification

---

## 1. Model Overview

| Attribute | Specification |
|-----------|---------------|
| **Character Type** | Large Troglodyte Chieftain |
| **Role** | Diplomacy Option NPC |
| **Scale** | 32mm heroic (figure is 1.5x normal troglodyte) |
| **Base Size** | 40mm round |
| **Model Height** | 48mm to eye level (~55mm to crown top) |
| **Size Category** | Large (for D&D purposes) |
| **Visual Theme** | Intelligent, regal savage king |
| **Complexity** | Medium-High |
| **Print Time (est.)** | 4-5 hours at 0.05mm layer height |

---

## 2. Pose Description

### Primary Pose: The Audience
- Standing atop raised stone platform/dais
- Body slightly angled, presenting authority without full frontal aggression
- Right arm extended in gesture of measured welcome or command
- Left hand resting on ornate bone staff planted beside him
- Head held high, chin raised, surveying visitors
- Chest out, shoulders back - proud bearing
- Tail extended behind for balance, slightly raised
- Weight on back leg, front leg slightly forward on platform edge

### Expression & Bearing
- Eyes sharp and calculating, not feral
- Mouth closed or slightly open (not snarling)
- Expression suggests cunning intelligence
- Posture conveys "I am in control here"

### Alternative Pose: The Treaty
- Seated on bone throne
- Both hands on armrests
- More diplomatic, approachable stance
- Head tilted forward, listening

---

## 3. Detailed Feature Breakdown

### Head & Face
- **Shape**: Reptilian/amphibian hybrid, elongated snout
- **Size**: Proportionally larger head than standard troglodyte (sign of age/wisdom)
- **Eyes**: Large, intelligent, forward-facing (unusual for prey species - evolved predator)
- **Eye Detail**: Slit pupils, heavy brow ridges, slight glow suggested
- **Snout**: Shorter than feral troglodyte, broader (more humanoid influence)
- **Mouth**: Visible teeth but not prominently displayed
- **Nostrils**: Pronounced, flared
- **Frills/Crests**: Large head crest/frill, partially erectile (display feature)
- **Texture**: Scaled with larger plates on brow and crown

### Crown
- **Style**: Crude but impressive golden crown
- **Construction**: Hammered gold plates riveted together
- **Design**: Circlet base with three major points
- **Decoration**:
  - Inset gems (rough-cut, unpolished)
  - Primitive engravings (swirl patterns, cave art style)
  - Dangling teeth or claws from chains
- **Fit**: Sized for large reptilian head, sits between head crests
- **Condition**: Dented but cared for, shows age and battles

### Body Build
- **Physique**: Powerful, muscular, but not brutish
- **Height**: 1.5x standard troglodyte (~7 feet in-world)
- **Proportions**: Thick torso, powerful shoulders
- **Posture**: More upright than feral kin (evolved/intelligent bearing)
- **Skin Texture**: Amphibian-like with scale patches
- **Coloration Zones**: Lighter belly, darker back (painting reference)

### Bone Jewelry & Adornments
- **Necklace**: Multiple strands of bones, teeth, and gold beads
- **Arm Bands**: Bone and gold bands on upper arms
- **Wrist Guards**: Crude hammered gold bracers
- **Chest Piece**: Partial bone breastplate (ribs of large creature)
- **Piercings**: Bone spikes through ear frills
- **Trophy Display**: Notable enemy skulls on belt or necklace

### Attire (Minimal)
- **Loincloth**: Leather and scale hide, decorated hem
- **Belt**: Wide leather with gold buckle and trophy hooks
- **Sash**: Crude woven fabric draped over one shoulder
- **Cloak/Cape**: Short fur or hide cape from shoulder (optional)

### Staff/Scepter
- **Length**: 40mm (scaled to figure)
- **Shaft**: Large bone (femur of great beast), carved with runes
- **Head**: Cluster of crystals or large gemstone in bone cage
- **Decoration**: Wrapped leather grip, dangling feathers/teeth
- **Purpose**: Symbol of office, possibly magical

### Tail
- **Length**: Approximately 30-35mm
- **Thickness**: Substantial, powerful
- **Position**: Extended behind, slight upward curve
- **Texture**: Scaled, with ridge of small spines
- **Function**: Balance and expression (raised = confident)

### Raised Platform/Dais
- **Shape**: Irregular stone platform
- **Size**: 30mm diameter, 8-10mm height
- **Construction**: Stacked rough-hewn stones
- **Details**:
  - Carved tribal symbols
  - Inset gems or gold patches
  - Skull decorations at base
  - Worn smooth on top from use

---

## 4. Modeling Notes for Blender

### Mesh Construction

#### Base Anatomy
1. Start with reptilian humanoid base mesh
2. Scale to 1.5x standard humanoid
3. Adjust proportions: longer arms, shorter legs, thick torso
4. Add tail as separate mesh initially, merge for printing

#### Reptilian Features
```
1. Use sculpt mode for skin texture
2. Create scale alpha brush for consistent pattern
3. Vary scale size: larger on back/shoulders, smaller on joints
4. Add wrinkle/fold detail at joints
5. Head crest requires careful topology for smooth curves
```

### Crown Modeling
- Model as separate piece for detail work
- Hammered texture via displacement or sculpt
- Boolean for gem insets
- Add damage/dent details
- Chain elements can be modeled or suggested

### Jewelry Complexity
- Necklace strands: curve-based modeling, convert to mesh
- Individual teeth/bones as instanced objects
- Gold elements with smooth surface, slight wear
- Keep connection points thick enough for printing

### Platform Construction
```
1. Start with cylinder, heavy subdivision
2. Sculpt to irregular stone shape
3. Add stacked stone layers with boolean or sculpt
4. Carve symbols into surface
5. Add decorative elements (skulls, gems)
6. Ensure flat bottom for base attachment
```

### Topology Considerations
- Face needs clean loops for expression
- Scales can be geometry or normal map (geometry preferred for 3D printing)
- Jewelry chains: simplify for printing, minimum 1mm thickness
- Tail requires good edge flow for natural curve
- Target poly count: 80,000-120,000

### Multi-Part Breakdown
For easier printing:
1. Main body with integral jewelry
2. Staff (separate for painting access)
3. Crown (optional separate for detail printing)
4. Platform/dais (separate piece)
5. Tail (can be separate if print angle problematic)

---

## 5. Print Recommendations

### Resin Printing (Recommended)

#### Standard Print
| Setting | Value |
|---------|-------|
| Layer Height | 0.04-0.05mm |
| Resin Type | Standard grey or ABS-like |
| Support Density | Medium-Heavy |
| Critical Supports | Staff, extended arm, tail, jewelry |
| Orientation | 30-35 degree tilt, tail toward plate |

#### Large Model Considerations
- Model is significantly larger than standard mini
- Resin cost approximately 2x standard figure
- Print time extended due to larger cross-section
- Consider hollowing torso (2mm walls)

### FDM Printing
| Setting | Value |
|---------|-------|
| Feasibility | Good (larger scale helps) |
| Layer Height | 0.1-0.12mm |
| Nozzle Size | 0.3-0.4mm |
| Material | PLA or PETG |
| Supports | Tree supports, heavy density |
| Orientation | Upright, may need to split |

### Split Points for FDM
If splitting model:
1. Torso at waist (hide seam with belt)
2. Staff as separate piece
3. Platform as separate piece
4. Arms at shoulder (hide with jewelry)

### Hollowing (Resin)
- Hollow torso with 2mm walls
- Add drainage holes: bottom of feet, under platform
- Keep head solid for detail
- Keep jewelry solid (too thin to hollow)

### Support Strategy
- Heavy supports under extended arm
- Medium supports under tail
- Light supports on jewelry (careful removal needed)
- Thick supports on platform underside

---

## 6. Base Suggestions

### Primary Base: Tribal Throne Room

#### 40mm Round Base Design
- Larger base (40mm) reflects Large creature size
- 4-5mm height for presence
- Cave/cavern floor theme

#### Surface Details
- **Floor Texture**: Rough stone, water-worn smooth in paths
- **Bone Scatter**: Small bones and skulls at edges
- **Gold/Gem Offerings**: Small piles of tribute
- **Carved Patterns**: Tribal symbols etched in stone
- **Wet Areas**: Glossy patches suggesting cave moisture

### Platform Integration
- Platform rises from base center
- Continuous stone material
- Steps optional (suggest access from sides)
- Total height with platform: 12-15mm

### Enhanced Base Options

**Option A: Treasure Hoard**
- Platform surrounded by gold coins and gems
- Skulls of enemies displayed
- Partially buried artifacts
- Suggests wealth and power

**Option B: Ritual Chamber**
- Carved runework around platform edges
- Small ritual fires (raised flame elements)
- Sacrificial symbols
- More mystical atmosphere

**Option C: Audience Hall**
- Clean stone floor with geometric pattern
- Steps leading to platform
- Torch holder positions suggested
- More "civilized" appearance

### Environmental Touches
- Mushrooms at base edges (cave ecosystem)
- Dripping water stalactite remnants
- Gecko or small reptile (loyalty symbol)
- Tribal banner pole socket

### Base Integration
- Platform pins into base (2.5mm diameter)
- Figure pins into platform (2mm diameter)
- Magnet option: 8mm x 2mm in base bottom
- Weight consideration: larger model needs stable base

---

## Additional Notes

### Painting Guide Reference Colors

#### Skin Tones
- **Primary**: Mottled green-grey or brown-grey
- **Belly/Underside**: Lighter tan or pale green
- **Back/Shoulders**: Darker, almost black-green
- **Frills/Crest**: Possible display colors (red, orange, yellow tips)

#### Crown & Gold
- **Base**: Rich antique gold
- **Shadows**: Dark bronze or brown
- **Highlights**: Bright gold
- **Gems**: Deep red (rubies) or green (emeralds)
- **Wear**: Edge highlighting for hammered texture

#### Bone Jewelry
- **Base**: Aged bone (cream to tan)
- **Shadows**: Brown wash in crevices
- **Highlights**: Almost white on edges
- **Variation**: Some bones darker (older), some lighter

#### Equipment
- **Staff Bone**: Ancient yellowed ivory
- **Staff Gems**: Glowing crystals (any color)
- **Leather**: Dark brown to black
- **Fur/Hide**: Natural animal tones

#### Eyes
- **Style**: Intelligent, knowing gaze
- **Color**: Yellow or amber with black slit pupil
- **Effect**: Slight reflective gloss

### Character Personality Notes
- This is NOT a mindless monster
- Should convey: cunning, patience, authority
- Expression: measuring, evaluating, in control
- Body language: confident but not aggressive
- Represents potential ally, not just enemy

### Scale Reference
| Comparison | Height |
|------------|--------|
| Standard Troglodyte | 32mm eye level |
| Sketh-Kra | 48mm eye level |
| With Crown | 55mm total |
| Human Fighter | 32mm eye level |
| On Platform | +10mm display |

### File Naming Convention
```
troglodyte-king-audience-v1.blend
troglodyte-king-audience-v1-body.stl
troglodyte-king-audience-v1-staff.stl
troglodyte-king-audience-v1-platform.stl
troglodyte-king-audience-v1-complete.stl
troglodyte-king-treaty-pose-v1.blend
troglodyte-king-base-tribal-40mm.stl
```

### Gameplay Considerations
- 40mm base fits Large creature footprint
- Platform adds to impressive table presence
- Staff could be modeled as removable for transport
- Consider gaming version with simpler jewelry (durability)
- Display version can have full detail

### Reference Imagery Suggestions
- Monitor lizard facial structure
- Salamander skin texture
- Aztec/Mayan gold craftsmanship
- Tribal chieftain bearing/posture
- Intelligent predator expressions (crocodile eyes)
