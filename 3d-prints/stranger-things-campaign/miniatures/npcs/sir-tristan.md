# Sir Tristan - Quest Giver NPC
## 3D Miniature Design Specification

---

## 1. Model Overview

| Attribute | Specification |
|-----------|---------------|
| **Character Type** | Human Noble Lord |
| **Role** | Quest Giver NPC |
| **Scale** | 32mm (heroic scale) |
| **Base Size** | 25mm round |
| **Model Height** | 32mm to eye level (~38mm to top of crown) |
| **Pose Variants** | A: Standing Commanding / B: Seated on Throne |
| **Complexity** | Medium-High |
| **Print Time (est.)** | 2-3 hours at 0.05mm layer height |

---

## 2. Pose Descriptions

### Pose A: Standing Commanding
- Feet shoulder-width apart, weight evenly distributed
- Right arm extended forward, palm facing outward in a gesture of authority or blessing
- Left hand resting on sword pommel at hip
- Head tilted slightly upward, chin raised with confident expression
- Cape flowing back slightly as if caught by gentle breeze
- Chest out, shoulders back - commanding presence

### Pose B: Seated on Throne
- Seated upright on ornate wooden throne
- Right arm resting on throne armrest, hand relaxed
- Left hand holding scroll or decree
- Legs together, feet flat on throne base
- Head facing forward with regal composure
- Cape draped over throne back and pooling at sides

---

## 3. Detailed Feature Breakdown

### Head & Face
- **Face**: Distinguished middle-aged human male, strong jawline, aquiline nose
- **Expression**: Noble and approachable, slight knowing smile
- **Hair**: Shoulder-length wavy hair, parted in center, swept back
- **Facial Hair**: Well-trimmed goatee and mustache
- **Eyes**: Deep-set, wise expression

### Crown/Circlet
- **Style**: Elegant golden circlet with central gemstone
- **Design**: Three-point design with subtle filigree patterns
- **Central Gem**: Large oval cabochon (ruby or sapphire)
- **Smaller Gems**: Two flanking gems at each point
- **Band Width**: 3-4mm at center, tapering to 2mm at sides

### Attire - Upper Body
- **Doublet**: Rich velvet doublet with gold embroidery
- **Collar**: High standing collar with fur trim (ermine pattern)
- **Sleeves**: Puffed shoulders tapering to fitted forearms
- **Embroidery Pattern**: Heraldic lions or fleur-de-lis along chest panel
- **Buttons**: Row of 6 ornate golden buttons down front

### Cape/Cloak
- **Length**: Floor-length, pooling slightly at feet
- **Fastening**: Ornate golden chain and clasp at collar bones
- **Exterior**: Rich fabric with subtle pattern texture
- **Interior**: Contrasting lighter fabric (for painting variety)
- **Draping**: Natural folds following body movement
- **Hem**: Decorative border with geometric pattern

### Attire - Lower Body
- **Breeches**: Fitted noble breeches to mid-calf
- **Boots**: Knee-high leather boots with folded cuff
- **Belt**: Wide leather belt with ornate golden buckle
- **Sword**: Ceremonial longsword in decorated scabbard at left hip

### Hands & Arms
- **Rings**: Signet ring on right hand, gemmed ring on left
- **Bracers**: Decorative leather bracers with gold inlay
- **Gloves**: None (showing noble hands) or fine leather

### Throne (Pose B Only)
- **Style**: Gothic wooden throne with high back
- **Height**: 45mm to top of back
- **Width**: 30mm at armrests
- **Details**: Carved lion heads on armrest ends, heraldic crest on backrest
- **Cushion**: Padded seat cushion with tasseled corners

---

## 4. Modeling Notes for Blender

### Mesh Construction
- Start with base human mesh, adjust proportions for heroic scale
- Use subdivision surface modifier for smooth curves
- Target poly count: 50,000-80,000 for detailed version
- Create low-poly version (15,000) for faster prints

### Key Topology Considerations
- Maintain clean edge loops around face for expression
- Cape requires careful attention to draping physics or manual sculpting
- Ensure crown sits naturally on head mesh
- Sword scabbard should be modeled as separate object for easier printing

### Sculpting Priority Areas
- Face and expression (use multiresolution modifier)
- Crown gemstones and filigree
- Cape folds and fabric texture
- Embroidery patterns on doublet
- Boot leather texture

### Material Separation
Consider separating for multi-part printing:
1. Body and clothing (main piece)
2. Cape (can be printed flat and attached)
3. Crown (for resin detail printing)
4. Throne (Pose B - separate piece)
5. Sword (optional separate)

### Texture and Detail
- Add fabric texture via normal maps or subtle geometry
- Embroidery can be raised geometry (0.2-0.3mm)
- Hair strands suggested with groove patterns
- Fur trim texture with small bump pattern

---

## 5. Print Recommendations

### Resin Printing (Recommended)
| Setting | Value |
|---------|-------|
| Layer Height | 0.03-0.05mm |
| Exposure Time | Per resin specifications |
| Support Density | Medium-Heavy |
| Support Points | Cape underside, extended arm, sword |
| Orientation | 30-45 degree tilt back |

### FDM Printing
| Setting | Value |
|---------|-------|
| Layer Height | 0.08-0.12mm |
| Nozzle Size | 0.25-0.4mm |
| Infill | 15-20% |
| Supports | Tree supports for cape |
| Orientation | Upright, may need split |

### Hollowing (Resin)
- Hollow throne at 1.5mm wall thickness
- Body can remain solid at this scale
- Add drainage holes under base if hollowing

### Post-Processing
- Light sanding on support contact points
- Prime with grey or zenithal primer
- Recommended primer: Vallejo Surface Primer

---

## 6. Base Suggestions

### Standard Base Design
- 25mm round base, 3mm height
- Cobblestone or flagstone pattern (throne room floor)
- Slight texture variation for visual interest

### Enhanced Base Options

**Option A: Throne Room Floor**
- Polished stone tiles in alternating pattern
- Small decorative elements (fallen rose petals, scroll)
- Subtle heraldic crest embedded in center

**Option B: Castle Steps**
- Single raised step (3mm additional height)
- Worn stone texture with moss in cracks
- Banner pole holder position

**Option C: Audience Chamber**
- Rich carpet texture leading to figure
- Carpet edge with fringe detail
- Gold border pattern on carpet

### Base Integration
- Recessed slot for foot pegs (2mm diameter)
- Name plate area on front rim (optional)
- Magnetization option: 5mm x 1mm magnet recess in bottom

---

## Additional Notes

### Painting Guide Reference Colors
- **Cape Exterior**: Royal purple or deep crimson
- **Cape Interior**: Gold or cream
- **Doublet**: Rich blue or burgundy
- **Crown/Metalwork**: Antique gold
- **Gems**: Ruby red or sapphire blue
- **Boots**: Dark brown leather
- **Hair**: Grey-streaked brown or silver

### Scale Verification
- Standard 32mm human = 6 feet tall
- Eye level at 32mm confirms correct scale
- Crown adds approximately 6mm to total height
- Throne seated pose should maintain similar eye level to standing

### File Naming Convention
```
sir-tristan-standing-v1.blend
sir-tristan-standing-v1-print.stl
sir-tristan-throne-v1.blend
sir-tristan-throne-v1-print.stl
sir-tristan-throne-only.stl
sir-tristan-base-25mm.stl
```
