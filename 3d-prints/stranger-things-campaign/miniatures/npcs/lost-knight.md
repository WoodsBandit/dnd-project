# The Lost Knight - Labyrinth Guardian
## 3D Miniature Design Specification

---

## 1. Model Overview

| Attribute | Specification |
|-----------|---------------|
| **Character Type** | Spectral/Ethereal Knight |
| **Role** | Labyrinth Guardian NPC |
| **Scale** | 32mm (heroic scale) |
| **Base Size** | 25mm round |
| **Model Height** | 35mm to eye level (~42mm to helmet crest) |
| **Visual Effect** | Ghostly/Translucent with wispy edges |
| **Complexity** | High (ethereal effects require careful modeling) |
| **Print Time (est.)** | 3-4 hours at 0.05mm layer height |

---

## 2. Pose Description

### Primary Pose: The Riddler's Gesture
- Standing with slight forward lean, creating sense of engagement
- Right arm extended, pointing forward with index finger (indicating path or presenting riddle)
- Left hand resting on pommel of ancient greatsword, blade tip touching ground
- Head tilted slightly to one side, suggesting contemplation or mystery
- Legs in wide stance, one foot slightly forward
- Cape/spectral wisps flowing upward and outward, defying gravity
- Overall silhouette suggests both wisdom and warning

### Alternative Pose: The Warden's Watch
- Arms crossed over chest, greatsword strapped to back
- Head bowed slightly, eyes visible beneath helm
- More static, imposing guardian presence
- Spectral effects concentrated at feet, rising like mist

---

## 3. Detailed Feature Breakdown

### Helmet
- **Style**: Ancient gothic full helm with T-shaped visor
- **Condition**: Weathered, with battle damage (dents, scratches)
- **Crest**: Faded plume or broken crest mount
- **Visor**: Slightly open, revealing ethereal glow within (no visible face)
- **Details**: Rivets, breathing holes, articulated gorget
- **Spectral Effect**: Edges become wispy, translucent at top of helm

### Armor - Upper Body
- **Cuirass**: Ornate plate armor with gothic styling
- **Decoration**: Faded heraldic symbols (maze/labyrinth motif)
- **Condition**: Ancient, corroded in places, ethereal holes
- **Pauldrons**: Layered shoulder guards with decorative edges
- **Gorget**: Articulated neck protection, partially transparent
- **Breastplate**: Central ridge with faded engraved patterns

### Spectral/Ethereal Effects
- **Edge Treatment**: All armor edges fade into wispy, smoke-like tendrils
- **Transparency Zones**:
  - Lower legs transition to transparent/missing below knee
  - Cape dissolves into spectral trails
  - Gaps in armor show ethereal glow, not flesh
- **Floating Debris**: Small armor fragments orbit the figure
- **Ground Connection**: Wisps of ectoplasm connect to base

### Armor - Lower Body
- **Tassets**: Hip guards, increasingly transparent toward edges
- **Legs**: Armored to mid-thigh, then fade to spectral wisps
- **Feet**: Suggestion of sabatons dissolving into mist
- **Grounding**: Spectral tendrils anchor figure to base

### Greatsword
- **Type**: Ancient two-handed longsword
- **Length**: 35mm blade length (scaled)
- **Blade**: Partially ethereal, with ghostly runes glowing along fuller
- **Crossguard**: Ornate, maze pattern in guard design
- **Pommel**: Large cabochon gem (glowing ethereal light)
- **Condition**: Ancient but uncorroded (magical preservation)

### Cape/Cloak
- **Attachment**: Clasped at shoulders with spectral chains
- **Shape**: Flowing upward and outward, defying gravity
- **Edges**: Completely dissolve into wispy tendrils
- **Interior**: Void-like darkness suggested
- **Movement**: Captured mid-billow, dramatic effect

### Spectral Aura Elements
- **Inner Glow**: Core of figure more solid
- **Outer Fade**: Extremities increasingly transparent
- **Floating Particles**: Small orbs or motes around figure
- **Ground Mist**: Spectral fog at base level
- **After-image**: Subtle duplicate edges suggesting movement blur

---

## 4. Modeling Notes for Blender

### Mesh Construction Strategy

#### Solid Core Approach
- Model complete armored knight as base mesh
- Use boolean operations to create ethereal holes
- Add wispy tendril geometry as separate meshes
- Target poly count: 80,000-120,000 for detail version

#### Layered Transparency Method
- Create outer "ghost shell" mesh for translucent printing
- Inner core mesh for solid areas
- Separate meshes for spectral effects

### Ethereal Edge Technique
```
1. Model base armor with clean edges
2. Add displacement modifier with cloud texture for edge dissolution
3. Use vertex weight painting to control effect intensity
4. Convert to mesh and manually refine wispy shapes
5. Add tendril geometry using curve-based hair or manual modeling
```

### Key Topology Considerations
- Wisps require clean, flowing topology for natural curves
- Armor damage (holes, dents) should have proper edge support
- Cape flow needs consideration for print support placement
- Floating elements need thin connection points

### Material Zones for Multi-Material Printing
1. **Solid Armor Core**: Standard opaque resin/filament
2. **Ethereal Edges**: Clear or translucent resin
3. **Glowing Elements**: Could use glow-in-dark or paint

### Sculpting Priority Areas
- Armor weathering and battle damage
- Wispy tendril flow and natural curves
- Helmet interior glow suggestion
- Sword rune engravings
- Cape billowing dynamics

### Spectral Particle Effects
- Model small spheres (1-2mm) on thin stalks
- Arrange in orbital pattern around torso
- These can break in printing - model as optional separate piece

---

## 5. Print Recommendations

### Resin Printing (Highly Recommended)

#### Standard Opaque Print
| Setting | Value |
|---------|-------|
| Layer Height | 0.03-0.05mm |
| Resin Type | Standard grey or white |
| Support Density | Heavy (complex geometry) |
| Support Points | Under cape, pointing arm, sword blade |
| Orientation | 45 degree tilt, sword toward plate |

#### Translucent Effect Print
| Setting | Value |
|---------|-------|
| Layer Height | 0.03mm |
| Resin Type | Clear or translucent blue |
| Post-Cure | Minimal (maintains clarity) |
| Special Note | Underexpose slightly for softer edges |

#### Dual-Print Approach (Best Results)
1. Print solid core in grey/white resin
2. Print ethereal effects in clear resin
3. Assemble with UV resin or CA glue
4. Paint solid areas, leave clear areas translucent

### FDM Printing
| Setting | Value |
|---------|-------|
| Feasibility | Challenging - loss of fine detail |
| Layer Height | 0.08mm minimum |
| Nozzle Size | 0.25mm strongly recommended |
| Material | PLA for detail |
| Supports | Heavy tree supports |
| Recommendation | Simplify wisps for FDM |

### Post-Processing for Ethereal Effect
1. Prime solid areas only
2. Apply translucent blue/green wash to edges
3. Dry brush silver on armor
4. Apply glow effect with fluorescent paint on eyes/gems
5. Seal clear areas with gloss varnish

---

## 6. Base Suggestions

### Primary Base Design: Labyrinth Floor
- 25mm round base, 3mm height
- Worn stone floor with maze pattern etched into surface
- Cracks with ethereal mist emerging
- Spectral wisps modeled rising from cracks

### Enhanced Base Options

**Option A: Crossroads**
- Intersection of labyrinth corridors suggested
- Directional arrows or worn paths visible
- Central rune circle beneath knight
- Ground fog tendrils reaching upward

**Option B: Forgotten Altar**
- Raised circular dais (2mm rise)
- Ancient runes around edge
- Cracked and weathered stone
- Small offerings (skulls, coins) at edges

**Option C: Ethereal Anchor**
- Abstract base with swirling spectral patterns
- Figure appears to emerge from the mist itself
- Less defined stone, more supernatural
- Floating stone fragments around edge

### Spectral Ground Effects
- Model wispy tendrils rising from base to connect with figure
- These serve dual purpose: visual effect AND structural support
- Thickness: 1.5-2mm at base, tapering to 0.5mm at connection

### Base Integration
- Pin locations hidden within spectral wisps
- 2mm diameter brass rod recommended for stability
- Clear acrylic rod option for "floating" effect
- Magnet recess (6mm x 2mm) centered in base bottom

---

## Additional Notes

### Painting Guide Reference Colors

#### Armor
- **Base**: Dark gunmetal or tarnished steel
- **Highlights**: Cold silver, almost blue-tinted
- **Shadows**: Deep blue-black
- **Verdigris**: Turquoise in recesses

#### Ethereal Effects
- **Core Glow**: Pale ice blue or spectral green
- **Edge Fade**: Lighter tint of core color
- **Wisps**: White to translucent blue gradient
- **Eyes**: Bright ethereal glow (OSL effect)

#### Accent Details
- **Gems**: Ethereal blue-white glow
- **Runes**: Glowing pale gold or silver
- **Cape Interior**: Deep void black with blue edge highlight

### Special Effect Techniques
- **OSL (Object Source Lighting)**: Paint glow effects from eyes, gems
- **Zenithal Prime**: White from above on armor, blue-tinge for ethereal
- **Dry Brush**: Heavy silver dry brush for ancient armor texture
- **Wash**: Blue-black wash in armor recesses

### Scale Verification
- Knight is slightly taller than standard human (spectral nature)
- 35mm to eye level (was larger in life)
- Floating pose can add 2-3mm perceived height
- Helmet crest reaches 42mm maximum

### File Naming Convention
```
lost-knight-riddler-pose-v1.blend
lost-knight-riddler-pose-v1-solid.stl
lost-knight-riddler-pose-v1-ethereal.stl
lost-knight-warden-pose-v1.blend
lost-knight-base-labyrinth-25mm.stl
lost-knight-floating-debris.stl
```

### Technical Challenges
1. **Wispy Edges**: May require iterative test prints
2. **Structural Integrity**: Thin wisps may break - consider thickening for gaming use
3. **Clear Resin**: Requires different support strategy (thick supports, careful removal)
4. **Assembly**: Multi-part approach recommended for best effect
