# Miniature Sculptor - Detailed Workflows

## Workflow 1: Complete Character Mini (Blender)

### Prerequisites
- Blender 3.6+ installed
- Reference images of character
- Decided on scale (28mm or 32mm)
- Know your printer type (FDM or resin)

### Step-by-Step Process

#### Phase 1: Project Setup (10 minutes)

```
1. Open Blender, delete default cube (X)

2. Set units to millimeters:
   - Properties Panel > Scene > Units
   - Unit System: Metric
   - Length: Millimeters

3. Set up reference:
   - Add > Image > Reference
   - Load front view, position at X=0
   - Load side view, position at Y=0
   - Scale to match your target height

4. Create scale reference:
   - Add > Mesh > Cube
   - Scale to 32mm height (32mm scale) or 28mm
   - This is your "character must fit in this box"

5. Save file with descriptive name:
   character_wizard_v01.blend
```

#### Phase 2: Base Mesh Creation (30-60 minutes)

**Option A: Build from Primitives**
```
1. Add > Mesh > Cylinder (torso)
   - Vertices: 12
   - Scale roughly to torso size

2. Add > Mesh > UV Sphere (head)
   - Segments: 16, Rings: 8
   - Position at neck height

3. Add > Mesh > Cylinder (arms, legs)
   - Create one, duplicate and mirror

4. Add Mirror Modifier:
   - Select all body parts
   - Join (Ctrl+J)
   - Add Modifier > Mirror
   - Axis: X
   - Enable Clipping

5. Basic shaping in Edit Mode:
   - Proportional editing (O) for smooth adjustments
   - Move vertices to match reference
```

**Option B: Use MakeHuman/MB-Lab Addon**
```
1. Install MB-Lab addon (Edit > Preferences > Add-ons)

2. Create base human:
   - Set to "anime" or "stylized" preset
   - Adjust proportions for heroic scale
   - Export as OBJ, import to main file

3. Simplify mesh:
   - Decimate modifier if too high poly
   - Remove internal geometry
```

#### Phase 3: Blocking Major Forms (45-90 minutes)

```
1. POSE FIRST (if dynamic):
   - Add Armature > Single Bone
   - Build simple skeleton
   - Parent mesh to armature
   - Pose, then apply armature

2. Block clothing/armor:
   - Duplicate body mesh
   - Delete inner vertices
   - Extrude outward for clothing thickness
   - Use Solidify modifier (1mm minimum)

3. Block hair:
   - Start with sphere or cone
   - Sculpt basic mass shape
   - Don't detail yet - just volume

4. Block equipment:
   - Weapons as simple cylinders/cubes
   - Shield as flattened sphere
   - Staff as cylinder (2mm+ diameter)

5. CHECK SILHOUETTE:
   - View from all angles
   - Should be recognizable even as blocks
   - Strong, interesting shape
```

#### Phase 4: Sculpting Detail (2-4 hours)

```
1. ENTER SCULPT MODE:
   - Select mesh
   - Tab or mode dropdown > Sculpt Mode

2. ENABLE DYNTOPO:
   - Sculpt menu > Dyntopo
   - Detail Size: 10px (start coarse)
   - Detailing: Relative Detail

3. PRIMARY FORMS (Dyntopo 8-10px):
   Brushes: Clay Strips, Inflate, Smooth
   - Refine body anatomy
   - Major cloth folds
   - Hair mass shapes

4. SECONDARY FORMS (Dyntopo 4-6px):
   Brushes: Clay Strips, Crease, Dam Standard
   - Facial features
   - Fingers/hands
   - Armor edges
   - Fabric fold details

5. TERTIARY DETAILS (Dyntopo 2-3px):
   Brushes: Crease, Draw Sharp, Pinch
   - Fine facial detail
   - Stitching, rivets
   - Hair texture
   - Surface textures

6. USE ALPHA TEXTURES:
   - Download alphas: chainmail, leather, scales
   - Brush > Texture > Load image
   - Drag brush for repeating patterns
```

#### Phase 5: Print Preparation (30-60 minutes)

```
1. APPLY ALL MODIFIERS:
   - For each modifier: Apply (Ctrl+A in modifier panel)
   - Mirror, Solidify, Subdivision - all applied

2. JOIN ALL OBJECTS:
   - Select all parts (A in object mode)
   - Join (Ctrl+J)
   - Now one single mesh

3. CHECK FOR ERRORS:
   - Edit Mode > Select > All by Trait > Non-Manifold
   - If anything selected, you have holes
   - Fix: Fill holes (F), or Mesh > Clean Up > Fill Holes

4. CHECK NORMALS:
   - Edit Mode > Overlay > Face Orientation
   - Blue = correct, Red = inverted
   - Fix: Select red faces > Mesh > Normals > Flip

5. BOOLEAN UNION (if intersecting parts):
   - Modifier > Boolean > Union
   - Apply modifier
   - This merges overlapping geometry

6. DECIMATE (reduce poly count):
   - Add Modifier > Decimate
   - Ratio: 0.5 (adjust to taste)
   - Target: 100k-500k triangles
   - Apply

7. SCALE CHECK:
   - Select model
   - N panel > Dimensions
   - Should show correct mm (e.g., Z: 32mm for 32mm scale)
   - If wrong: scale and Apply Scale (Ctrl+A > Scale)

8. EXPORT:
   - File > Export > STL
   - Selection Only: checked
   - Scale: 1.0
   - Forward: Y Forward (usually)
```

#### Phase 6: Slicer Preparation

**For Resin:**
```
1. Import STL to slicer (Chitubox, Lychee, etc.)

2. Hollow model:
   - Wall thickness: 1.5-2mm
   - Add drain holes: 2-3mm diameter
   - Place holes in hidden spots

3. Orient model:
   - Tilt 30-45° from vertical
   - Face angled up (best detail)
   - Minimize large flat areas parallel to bed

4. Add supports:
   - Auto-generate first
   - Manually add to: face, hands, weapon tips
   - Remove supports from detailed areas if possible

5. Slice and preview:
   - Check each layer for islands
   - Verify supports reach build plate
```

**For FDM:**
```
1. Import STL to slicer (Cura, PrusaSlicer, etc.)

2. Orient model:
   - Upright is usually best
   - Or split and print parts flat

3. Settings:
   - Layer height: 0.08-0.12mm
   - Supports: Tree supports usually best
   - Support angle: 45°

4. Slice and preview:
   - Check overhangs have support
   - Verify no spaghetti areas
```

---

## Workflow 2: Quick Kitbash Mini (30 minutes)

For when you need a mini fast by combining existing parts.

### Prerequisites
- Collection of base meshes/parts
- Meshmixer installed

### Process

```
1. GATHER PARTS:
   - Download base body from Thingiverse/MyMiniFactory
   - Find head, weapons, accessories separately
   - All should be roughly same scale

2. IMPORT TO MESHMIXER:
   - File > Import each STL
   - They'll stack at origin

3. POSITION PARTS:
   - Transform tool (T)
   - Move head to neck
   - Position weapons in hands
   - Add accessories

4. SCALE MATCHING:
   - If parts are different scales
   - Edit > Transform
   - Scale to match

5. BOOLEAN COMBINE:
   - Select two overlapping parts
   - Edit > Boolean > Union
   - Repeat until all combined

6. FIX SEAMS:
   - Sculpt > Brushes > Smooth
   - Blend transition areas
   - Or: leave seams, fill with putty after print

7. REPAIR MESH:
   - Analysis > Inspector
   - Click "Auto Repair All"
   - Fixes holes and errors

8. EXPORT:
   - File > Export STL
   - Ready to print
```

---

## Workflow 3: Weapon/Accessory Creation (Fusion 360)

Best for hard-surface items: swords, axes, shields, armor pieces.

### Process

```
1. CREATE NEW COMPONENT:
   - File > New Component
   - Name: "Longsword"

2. SKETCH PROFILE:
   - Create > Sketch
   - Select plane (front view)
   - Draw sword silhouette using:
     - Line, Arc, Spline tools
   - Dimension everything precisely
   - Blade width: 2mm minimum!

3. EXTRUDE BLADE:
   - Create > Extrude
   - Select blade profile
   - Thickness: 2mm for blade
   - Taper angle for edge bevel

4. ADD GUARD:
   - New sketch on blade
   - Draw guard cross-section
   - Extrude or Revolve

5. CREATE HANDLE:
   - Sketch circle for grip
   - Extrude cylinder
   - Add Fillet for pommel shape

6. COMBINE ALL:
   - Modify > Combine
   - Join all bodies

7. ADD DETAILS:
   - Chamfer edges
   - Emboss patterns
   - Fillet sharp corners

8. EXPORT:
   - File > Export > STL
   - Refinement: High
```

---

## Workflow 4: Hollowing for Resin (Meshmixer)

Save resin and reduce print time.

### Process

```
1. IMPORT SOLID MODEL:
   - File > Import
   - Load your STL

2. MAKE HOLLOW:
   - Edit > Hollow
   - Offset Distance: 1.5-2mm (wall thickness)
   - Solid Accuracy: 200+ (higher = better)
   - Mesh Density: 150+
   - Click Accept

3. ADD DRAIN HOLES:
   - Edit > Add Tube (or use Boolean subtract)
   - Position: hidden spots (under base, inside robe)
   - Diameter: 2.5-3mm
   - Must penetrate inner and outer wall
   - Minimum 2 holes for airflow

4. VERIFY HOLLOW:
   - Edit > Plane Cut (temporary)
   - Slice through model
   - Confirm walls are uniform thickness
   - Undo the cut

5. REPAIR:
   - Analysis > Inspector
   - Auto Repair All

6. EXPORT:
   - File > Export
   - Format: STL Binary
```

---

## Workflow 5: Adding Pre-Made Supports (Lychee/Chitubox)

### Lychee Slicer Process

```
1. IMPORT & ORIENT:
   - Import STL
   - Rotate: 30-45° tilt
   - Face angled upward

2. SUPPORT SETTINGS:
   - Light supports for most areas
   - Medium for overhangs, weapons
   - Heavy for large flat surfaces

3. AUTO-GENERATE:
   - Click "Magic" or auto-support
   - Review placement

4. MANUAL ADJUSTMENT:
   - Remove supports from:
     - Face details
     - Smooth surfaces that will show
   - Add supports to:
     - Islands (floating parts)
     - Thin extremities (fingers, sword tips)
     - Heavy overhangs

5. RAFT SETTINGS:
   - Enable raft
   - Raft type: Skate or Mini
   - Helps release from build plate

6. SLICE & VALIDATE:
   - Run slicer
   - Preview each layer
   - Check for unsupported islands (red)
   - Fix any issues

7. EXPORT:
   - Save as printer format (.ctb, .photon, etc.)
```

---

## Workflow 6: Multi-Part Model Assembly Design

### Planning

```
1. DECIDE SPLIT POINTS:
   - Natural breaks: neck, wrists, waist
   - Hidden seams: under cloaks, in hair
   - Functional swaps: weapon hands, heads

2. CONNECTION TYPE:
   - Peg/hole: simple, permanent or friction fit
   - Ball/socket: poseable
   - Magnet: swappable
   - Flat+pin: glue joint with alignment
```

### Blender Implementation

```
1. MODEL COMPLETE FIRST:
   - Full character, posed
   - Finalize before splitting

2. CREATE CUTTING PLANE:
   - Add > Mesh > Plane
   - Scale large
   - Position at split point

3. BOOLEAN SPLIT:
   - Select character
   - Add Modifier > Boolean
   - Operation: Difference
   - Object: cutting plane
   - Apply modifier
   - Now you have top piece

4. REPEAT FOR BOTTOM:
   - Duplicate original character
   - Boolean > Intersect with plane
   - Apply
   - Now you have bottom piece

5. ADD CONNECTION GEOMETRY:

   For Peg (on one piece):
   - Add > Mesh > Cylinder
   - 2.5mm diameter, 4mm length
   - Position at connection point
   - Boolean > Union with that piece

   For Hole (on other piece):
   - Add > Mesh > Cylinder
   - 2.6mm diameter, 4.5mm length
   - Position matching peg location
   - Boolean > Difference to cut hole

6. TEST FIT (optional):
   - Print just the connection area
   - Test tolerance
   - Adjust if needed

7. EXPORT EACH PIECE:
   - Select one piece
   - Export STL (selection only)
   - Repeat for each piece
   - Name clearly: character_body.stl, character_head.stl
```

---

## Workflow 7: Base Creation

### Simple Textured Base

```
1. CREATE DISC:
   - Add > Mesh > Cylinder
   - Vertices: 32
   - Depth: 3mm
   - Radius: 12.5mm (25mm base) or 15mm (30mm base)

2. ADD TEXTURE:
   - Sculpt mode
   - Dyntopo: 3-4px
   - Clay Strips brush: add rocky texture
   - Or: use alpha stamps for cobblestone, grass, etc.

3. ADD ELEMENTS:
   - Small rocks: spheres, deformed
   - Skulls: import or sculpt
   - Debris: random small cylinders

4. ENSURE FLAT BOTTOM:
   - Edit mode
   - Select bottom face
   - S > Z > 0 (scale Z to 0)
   - G > Z (move to Z=0)

5. ADD FOOT SLOTS (if needed):
   - Create cylinder slightly larger than foot pegs
   - Boolean subtract from base top
   - Character feet slot into these
```

### Scenic Base

```
1. START WITH LARGER BASE:
   - 30-40mm diameter for scene
   - 4-5mm depth

2. SCULPT TERRAIN:
   - Hills, rocks, ruins
   - Use reference images

3. ADD PROPS:
   - Treasure chest
   - Fallen enemies
   - Environmental details

4. POSITION CHARACTER SLOT:
   - Ensure character has stable footing
   - Cut slots for any foot pegs

5. EXPORT AS SEPARATE FILE:
   - Base can be printed separately
   - Different infill/settings than character
```
