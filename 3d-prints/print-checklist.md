# 3D Print Checklist

Pre-print, printing, and post-processing checklists for consistent quality prints.

---

## Pre-Print: File Preparation

### STL File Check

- [ ] File opens correctly in slicer (no errors)
- [ ] Model is manifold (watertight, no holes)
- [ ] Scale is correct (28mm for standard minis)
- [ ] Model is oriented correctly on bed
- [ ] No parts clipping through build plate
- [ ] Thin walls are thick enough to print

### Repair If Needed

- [ ] Run auto-repair in slicer
- [ ] Use Meshmixer or Netfabb for complex repairs
- [ ] Check for inverted normals
- [ ] Merge overlapping parts

### Model Preparation

- [ ] Remove unnecessary parts (separate supports, bases)
- [ ] Split large models if needed
- [ ] Add keying features for multi-part prints
- [ ] Hollow large resin prints (if applicable)
- [ ] Add drain holes to hollow resin prints

---

## Pre-Print: Slicer Checklist

### Profile Selection

- [ ] Correct printer selected
- [ ] Correct material profile selected
- [ ] Layer height appropriate for model type:
  - 0.08-0.12mm for minis
  - 0.16-0.24mm for terrain
- [ ] Print speed appropriate for detail level

### Orientation Check

- [ ] Model oriented for best detail on important surfaces
- [ ] Faces print near end (not against supports)
- [ ] Minimal support surface area
- [ ] Cross-section doesn't have large flat layers

### Support Settings

- [ ] Supports enabled where needed
- [ ] Support type selected (tree/normal for FDM, light/medium for resin)
- [ ] Supports not touching faces or critical details
- [ ] Paint-on supports added for problem areas
- [ ] Support blockers placed appropriately
- [ ] Check for islands (resin) - all areas supported

### Critical Settings Verified

- [ ] Temperature correct for filament/resin
- [ ] Bed temperature set
- [ ] Retraction settings correct
- [ ] Cooling enabled (FDM)
- [ ] Infill pattern and density set
- [ ] Wall count sufficient

### Final Preview

- [ ] Slice and review layer-by-layer
- [ ] Check first few layers look correct
- [ ] Verify support placement in preview
- [ ] Note any potential problem areas
- [ ] Check estimated print time is acceptable
- [ ] Check estimated material usage

### Export

- [ ] Save project file (.3mf, .lys) for future reference
- [ ] Export GCODE/print file
- [ ] Transfer to printer (SD card, USB, network)

---

## Pre-Print: Printer Preparation

### FDM Printer

- [ ] Build plate is clean (IPA wipe)
- [ ] Bed is level/tramming verified
- [ ] Z-offset calibrated
- [ ] Nozzle is clean, no debris
- [ ] Correct nozzle size installed
- [ ] Filament loaded and feeding smoothly
- [ ] No tangles in filament spool
- [ ] Bowden tube secure (if applicable)
- [ ] Print bed adhesion applied (glue/hairspray if needed)
- [ ] Enclosure closed (if printing ABS/ASA)

### Resin Printer

- [ ] Vat has sufficient resin
- [ ] Resin is shaken/stirred well
- [ ] Resin is at room temperature (warm if cold)
- [ ] FEP is clean and undamaged
- [ ] Build plate is clean and dry
- [ ] Build plate leveled to vat
- [ ] LCD screen clean (check from below)
- [ ] Resin vat seated correctly
- [ ] Cover ready to block ambient light

### Environment Check

- [ ] Room temperature appropriate (18-25C ideal)
- [ ] No drafts on FDM printer
- [ ] Resin area has ventilation
- [ ] Fire safety (smoke detector works, printer not unattended long-term)

---

## During Print: Monitoring

### First Layers (Critical)

- [ ] First layer adheres properly
- [ ] No warping or lifting at corners
- [ ] Lines are squished but not too flat
- [ ] Supports adhering correctly
- [ ] No skipping or grinding sounds

### Early Print Check (First 30 min)

- [ ] Print progressing normally
- [ ] No layer shifts visible
- [ ] Supports printing correctly
- [ ] No stringing issues developing
- [ ] Temperature stable

### Periodic Checks

- [ ] Model still adhered to bed
- [ ] No spaghetti (failed print)
- [ ] Filament still feeding (FDM)
- [ ] No unusual noises
- [ ] Resin level sufficient (resin)

### Problem Signs to Watch For

- [ ] Layer separation
- [ ] Excessive stringing
- [ ] Clicking extruder (FDM)
- [ ] Shifting layers
- [ ] Warping or lifting
- [ ] Supports detaching

---

## Post-Print: Removal

### FDM Prints

- [ ] Wait for bed to cool (PLA releases easier cold)
- [ ] Remove print carefully
- [ ] Don't force - use scraper at low angle
- [ ] Flex plate if available
- [ ] Check for any stuck parts

### Resin Prints

- [ ] Wear gloves (always!)
- [ ] Remove build plate from printer
- [ ] Use metal scraper at low angle
- [ ] Let excess resin drip back into vat
- [ ] Place in wash container
- [ ] Cover resin vat when done

---

## Post-Print: Cleanup

### FDM Post-Processing

- [ ] Remove supports
  - [ ] Snap off main supports
  - [ ] Use flush cutters for stubborn parts
  - [ ] Needle nose pliers for tight spots
- [ ] Clean support nubs
  - [ ] Hobby knife for rough spots
  - [ ] Light sanding if needed
- [ ] Check for stringing and remove
- [ ] Inspect for any defects or issues
- [ ] Clean build plate for next print

### Resin Post-Processing

- [ ] First wash (dirty IPA/water) - 2-3 minutes
- [ ] Second wash (clean IPA/water) - 2-3 minutes
- [ ] Air dry completely (15-20 minutes)
- [ ] Remove supports
  - [ ] Use flush cutters
  - [ ] Hobby knife for nubs
  - [ ] Support removal easier before full cure
- [ ] Final cure under UV
  - [ ] 3-6 minutes per side
  - [ ] Rotate for even exposure
- [ ] Final inspection
- [ ] Clean FEP and vat for next print

---

## Quality Check

### Dimensional Accuracy

- [ ] Base fits standard 25mm/1" grid (minis)
- [ ] Tiles connect properly (modular terrain)
- [ ] Overall size matches expectations
- [ ] No significant shrinkage or expansion

### Surface Quality

- [ ] Layer lines acceptable for use case
- [ ] No blobs or zits
- [ ] Details are crisp
- [ ] Overhangs printed cleanly
- [ ] Top surfaces smooth

### Structural

- [ ] Print is solid, no hollow areas where shouldn't be
- [ ] Thin parts intact, not broken
- [ ] Supports removed cleanly
- [ ] No delamination
- [ ] Base is flat (not warped)

### Print Issues to Log

If problems occurred, note:
- [ ] What went wrong
- [ ] At what layer/time
- [ ] Possible causes
- [ ] Settings used
- [ ] Update profile if needed

---

## Painting Prep

### Before Priming

- [ ] All supports removed
- [ ] Support scars cleaned up
- [ ] Mold lines removed (if present)
- [ ] Washed to remove oils/residue
- [ ] Completely dry

### Priming

- [ ] Use appropriate primer
  - Grey for most uses
  - White for bright colors
  - Black for dark/metallic schemes
  - Zenithal for pre-shading
- [ ] Thin coats, multiple passes
- [ ] Check for missed spots
- [ ] Let cure fully before painting

---

## Storage and Organization

### Completed Prints

- [ ] Label with model name and date
- [ ] Store in appropriate container
- [ ] Group by type (minis, terrain, props)
- [ ] Note any issues for future reference

### Failed Prints

- [ ] Document what went wrong
- [ ] Save for analysis if learning
- [ ] Dispose of properly
- [ ] FDM plastic: regular trash or recycling
- [ ] Resin: must be fully cured before disposal

### Print Files

- [ ] Keep project file (.3mf, .lys)
- [ ] Note successful settings
- [ ] Update print log
- [ ] Organize by category

---

## Quick Reference: Print Checklist

### 5-Minute Pre-Print Check

1. [ ] STL loaded and scaled correctly
2. [ ] Profile matches print type
3. [ ] Supports look reasonable
4. [ ] Bed is clean and level
5. [ ] Filament/resin ready
6. [ ] Print started, first layer watched

### 5-Minute Post-Print Check

1. [ ] Print removed carefully
2. [ ] Supports removed
3. [ ] Quick quality inspection
4. [ ] Bed cleaned
5. [ ] Log updated (if tracking)

---

## Emergency Troubleshooting

### Print Failed Mid-Way (FDM)

1. Stop print
2. Note layer number
3. Cool and remove carefully
4. Diagnose issue
5. Consider if salvageable
6. Restart if needed

### Print Failed Mid-Way (Resin)

1. Stop print
2. Check for stuck residue on FEP
3. Carefully remove build plate
4. Filter resin for cured bits
5. Inspect FEP for damage
6. Clean and restart

### First Layer Not Sticking

1. Stop print
2. Clean bed with IPA
3. Re-level if needed
4. Adjust Z-offset (closer)
5. Add adhesion (glue stick)
6. Restart

### Supports Failed (Resin)

1. Add more supports to problem areas
2. Increase contact diameter
3. Slow lift speed
4. Check exposure settings
5. Re-orient model
6. Restart

---

## Maintenance Schedule

### Every Print (FDM)

- [ ] Clean nozzle tip
- [ ] Check bed cleanliness

### Weekly (FDM)

- [ ] Clean build surface thoroughly
- [ ] Check belt tension
- [ ] Lubricate Z-axis lead screws
- [ ] Check for loose screws/connections

### Monthly (FDM)

- [ ] Deep clean hotend
- [ ] Check bowden tube condition
- [ ] Verify bed level
- [ ] Clean fans
- [ ] Check wire connections

### Every Print (Resin)

- [ ] Filter resin if any failures
- [ ] Clean FEP
- [ ] Wipe vat edges

### Weekly (Resin)

- [ ] Deep clean vat
- [ ] Inspect FEP for wear
- [ ] Clean LCD with appropriate cleaner
- [ ] Replace IPA wash if cloudy

### Monthly (Resin)

- [ ] Replace FEP if worn
- [ ] Calibrate exposure (test print)
- [ ] Check seals and o-rings
- [ ] Deep clean build plate
