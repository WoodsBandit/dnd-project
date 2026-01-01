# The Proud Princess - Upside Down Info NPC
## 3D Miniature Design Specification

---

## 1. Model Overview

| Attribute | Specification |
|-----------|---------------|
| **Character Type** | Spectral Noble Woman |
| **Role** | Information NPC (Upside Down Realm) |
| **Scale** | 32mm (heroic scale) |
| **Base Size** | 25mm round with corruption details |
| **Model Height** | 30mm to eye level (seated) |
| **Total Height** | ~45mm including corrupted throne |
| **Visual Theme** | Melancholic ghost on corrupted throne |
| **Complexity** | High (ethereal + environmental) |
| **Print Time (est.)** | 4-5 hours at 0.05mm layer height |

---

## 2. Pose Description

### Primary Pose: Eternal Mourning
- Seated on corrupted throne, body language conveying centuries of sorrow
- Torso slightly slumped forward, shoulders rounded
- Head tilted downward and to one side, hair falling across face
- Right hand limp at side, fingers trailing toward ground
- Left hand raised to chest, clutching faded locket or rose
- Legs together, feet flat or one slightly extended
- Gown pooling around throne base, merging with corruption

### Expression & Mood
- Eyes downcast, perhaps closed or half-lidded
- Subtle tear track suggested on cheek
- Mouth in neutral melancholic set
- Overall impression: tragic beauty frozen in grief

### Alternative Pose: The Warning
- Seated upright, one hand raised in caution
- Eyes wide, looking at viewer
- More alert, urgent expression
- Body language suggests important message to convey

---

## 3. Detailed Feature Breakdown

### Face & Expression
- **Features**: Delicate, aristocratic beauty
- **Age Appearance**: Young adult, early twenties
- **Expression**: Deep melancholy, haunting sadness
- **Eyes**: Large, downcast, ethereal glow suggested
- **Tears**: Subtle tear trails on cheeks (raised detail)
- **Lips**: Slightly parted, sorrowful
- **Skin Texture**: Smooth but with slight translucency

### Hair
- **Style**: Long, flowing, partially unbound
- **Length**: Past shoulders, cascading down back
- **Condition**: Once elaborate styling now disheveled
- **Details**: Some strands falling across face
- **Movement**: Hair flows as if underwater, defying gravity
- **Ethereal Effect**: Ends dissolve into wisps

### Crown/Tiara
- **Style**: Delicate princess tiara, partially broken
- **Material**: Silver with gemstones (now tarnished)
- **Condition**: Cracked, one point broken off
- **Gems**: Some missing, some cracked
- **Position**: Askew on head, suggesting tragedy

### Gown - Upper Body
- **Style**: Once-elegant court dress, empire waistline
- **Neckline**: Sweetheart or off-shoulder design
- **Sleeves**: Long, flowing bell sleeves
- **Condition**: Tattered, with tears and worn edges
- **Details**: Faded embroidery, hanging threads
- **Ethereal Effect**: Fabric becomes increasingly translucent at edges

### Gown - Lower Body
- **Skirt**: Full ball gown style, pooling extensively
- **Layers**: Multiple visible petticoat layers
- **Condition**: Hem completely tattered, trailing into mist
- **Tears**: Strategic rips showing underlayers
- **Corruption**: Lower portions merging with Upside Down tendrils
- **Details**: Once-beautiful lace now cobwebbed and torn

### Jewelry & Accessories
- **Necklace**: Delicate chain with locket (clutched in hand)
- **Earrings**: Simple drops, one possibly missing
- **Bracelet**: Thin chain, broken clasp
- **Ring**: Wedding or betrothal ring on left hand
- **All Jewelry**: Tarnished, aged appearance

### Ethereal/Ghost Effects
- **Core Solidity**: Torso and face most solid
- **Edge Dissolution**: Extremities fade to translucent
- **Hair Wisps**: Strands become spectral tendrils
- **Gown Trails**: Fabric dissolves into ectoplasmic streams
- **Glow Source**: Subtle inner luminescence from chest
- **Floating Particles**: Small motes around figure

### Corrupted Throne
- **Base Structure**: Once-elegant wooden throne
- **Corruption Level**: 60% overtaken by Upside Down growths
- **Organic Growths**: Vine-like tendrils climbing up sides
- **Texture**: Fleshy, alien biomass covering wood
- **Details**:
  - Original carved details visible beneath growths
  - Pulsing vein-like structures
  - Small pustules or pods
  - Sticky web-like strands
- **Integration**: Gown and throne corruption merge seamlessly

---

## 4. Modeling Notes for Blender

### Mesh Construction Strategy

#### Multi-Layer Approach
1. **Core Figure**: Solid princess body and face
2. **Clothing Layer**: Separate mesh for gown with tatter details
3. **Ethereal Layer**: Wispy/dissolving edges as separate mesh
4. **Throne Base**: Solid wooden throne structure
5. **Corruption Overlay**: Organic growth mesh on throne

### Gown Modeling Technique
```
1. Create base dress shape with cloth simulation or sculpting
2. Add multiple subdivision levels
3. Use sculpt tools to create fabric folds and draping
4. Boolean or manual modeling for tears and holes
5. Add flowing ethereal extensions at edges
6. Create separate underlayer mesh visible through tears
```

### Ethereal Effect Method
- Use vertex alpha or weight painting to indicate fade zones
- Model wispy geometry extending from solid edges
- Hair strands transition to thin curves
- Gown edges become increasingly chaotic geometry

### Corruption/Upside Down Growth
```
1. Model base throne with clean geometry
2. Create organic vine/tendril meshes using curves
3. Use metaball-to-mesh for blobby growths
4. Add detail with sculpting (veins, texture)
5. Merge corruption mesh with throne for printability
6. Extend tendrils to connect with gown hem
```

### Topology Considerations
- Face requires clean loops for subtle expression
- Gown folds need supporting edge loops
- Corruption organics should flow naturally
- Ensure watertight mesh at figure/throne connection
- Target poly count: 100,000-150,000 for detailed version

### Material/Part Separation
For potential multi-material or assembly:
1. Princess figure (translucent or standard)
2. Throne with corruption (standard resin)
3. Base with environmental effects
4. Floating debris/particles (optional)

---

## 5. Print Recommendations

### Resin Printing (Required for Detail)

#### Single Material Print
| Setting | Value |
|---------|-------|
| Layer Height | 0.03-0.05mm |
| Resin Type | Standard grey/white |
| Support Density | Heavy |
| Support Points | Throne back, extended fabric, hair |
| Orientation | 35-40 degree tilt backward |

#### Dual Material Print (Optimal)
| Component | Resin Type |
|-----------|------------|
| Throne + Corruption | Grey/bone standard |
| Princess Figure | Clear or translucent white |
| Assembly | UV resin bonding |

#### Translucent Ghost Print
| Setting | Value |
|---------|-------|
| Layer Height | 0.03mm |
| Resin Type | Clear or translucent blue-white |
| Post-Cure | Minimal for clarity |
| Painting | Interior surfaces for depth effect |

### FDM Printing
| Setting | Value |
|---------|-------|
| Feasibility | Very Challenging |
| Recommendation | Print throne only; purchase/resin print figure |
| If Attempted | 0.08mm layers, extensive supports |
| Material | White or translucent PLA |

### Hollowing Strategy
- Throne interior can be hollowed (2mm walls)
- Add drainage holes in throne base
- Figure too small to hollow effectively
- Corruption growths should remain solid

### Support Placement Critical Points
- Underneath all fabric overhangs
- Hair falling forward
- Extended sleeves
- Throne back decorative elements
- Corruption tendrils reaching outward

---

## 6. Base Suggestions

### Primary Base: Upside Down Corruption

#### Design Concept
- 25mm round base, 3-4mm height
- Surface appears to be corrupted throne room floor
- Organic growths spreading from throne
- Cracked stone with fleshy tendrils emerging

#### Environmental Elements
- **Cracked Flagstones**: Original floor breaking apart
- **Organic Tendrils**: Vine-like growths in cracks
- **Pustules**: Small biomass pods scattered
- **Webbing**: Sticky strands connecting elements
- **Spore Particles**: Tiny floating debris (optional thin stalks)

### Enhanced Base Options

**Option A: Corrupted Dais**
- Raised circular platform (5mm height)
- Once-elegant carved stone, now crumbling
- Corruption concentrated at edges
- Central area still recognizable as royal

**Option B: Memory Fragment**
- Half the base shows original beautiful floor
- Half shows complete Upside Down corruption
- Sharp diagonal division
- Suggests the "before and after"

**Option C: Vine Throne Integration**
- Base and throne are continuous piece
- Corruption roots deep into base
- No visible separation between throne and ground
- Most dramatic but larger footprint

### Corruption Texture Details
- Veiny, organic patterns
- Slight pulsing/bulging forms
- Contrast between smooth organic and cracked stone
- Small eye-like nodes or sensory growths
- Web strands connecting corruption patches

### Base Integration
- Throne legs integrate directly with base corruption
- Pin holes hidden within organic growths
- Magnet recess: 8mm x 2mm (larger for stability)
- Weight consideration: throne model is heavier

---

## Additional Notes

### Painting Guide Reference Colors

#### Princess Figure
- **Skin**: Pale, almost grey-blue (deathly pallor)
- **Hair**: Faded blonde or auburn with grey streaks
- **Eyes**: Milky white with faint iris color, or solid ethereal glow
- **Lips**: Pale purple or grey
- **Tears**: Gloss varnish for wet look

#### Gown
- **Base Color**: Faded royal blue or deep purple (once vibrant)
- **Underlayers**: Aged white or cream
- **Embroidery**: Tarnished gold thread
- **Shadows**: Deep blue-grey
- **Ethereal Edges**: White fading to transparent

#### Throne & Corruption
- **Original Wood**: Dark brown, visible in patches
- **Corruption Base**: Deep purple-black
- **Organic Growths**: Reddish-purple with blue veins
- **Pustules**: Pale flesh with purple tinge
- **Webbing**: Translucent grey-white
- **Veins**: Dark purple-red, slight gloss

### Special Painting Techniques
- **Ghostly Glow**: White dry brush from center outward
- **Corruption Blend**: Wet blend where gown meets growths
- **OSL**: Soft glow from chest locket
- **Contrast**: Sharp difference between ethereal beauty and organic horror
- **Weathering**: Dry brush original throne color through corruption

### Thematic Considerations
- Represents tragedy and loss in the Upside Down
- Visual contrast between former beauty and current horror
- Melancholy mood should be clear from silhouette
- Corruption is consuming but she remains distinct

### Scale Verification
- Seated figure eye level: 30mm
- Standing she would be standard human height
- Throne adds 10-15mm to total height
- Base corruption may extend 2-3mm beyond 25mm circle

### File Naming Convention
```
proud-princess-mourning-v1.blend
proud-princess-mourning-v1-figure.stl
proud-princess-mourning-v1-throne.stl
proud-princess-mourning-v1-complete.stl
proud-princess-warning-pose-v1.blend
proud-princess-base-corrupted-25mm.stl
```

### Assembly Notes
- Figure and throne should be modeled for single-piece printing if possible
- If separating: throne has flat top for figure attachment
- Corruption tendrils on gown must align with throne corruption
- Consider scenic display version with larger base (40mm)
