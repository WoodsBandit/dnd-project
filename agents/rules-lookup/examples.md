# Rules Lookup - Example Queries

## Spell Lookups

### Example 1: Common Combat Spell
**Query:** "Fireball stats"

**Response:**
**Fireball** | 3rd Level Evocation
**Casting:** 1 action | 150 feet | V, S, M (bat guano, sulfur)
**Duration:** Instantaneous
**Effect:** 20-foot radius sphere. Each creature makes DEX save. 8d6 fire damage on fail, half on success. Ignites flammable objects not worn/carried.
**Upcast:** +1d6 per slot level above 3rd
**Key ruling:** Spreads around corners. Can't aim to exclude allies within radius.
**Source:** PHB p.241

---

### Example 2: Concentration Spell
**Query:** "How does Hex work?"

**Response:**
**Hex** | 1st Level Enchantment
**Casting:** 1 bonus action | 90 feet | V, S, M (petrified newt eye)
**Duration:** Concentration, up to 1 hour
**Effect:** Curse target. Your attacks deal +1d6 necrotic. Choose one ability - target has disadvantage on checks with that ability. If target drops to 0 HP, use bonus action to move Hex to new creature.
**Upcast:** 8 hours at 3rd/4th, 24 hours at 5th+
**Key ruling:** Ability disadvantage affects CHECKS only, not saves or attacks. Moving Hex doesn't require new concentration.
**Source:** PHB p.251

---

### Example 3: Contested Spell Interaction
**Query:** "Counterspell vs Counterspell - can you counter a counter?"

**Response:**
**RAW:** Yes. Counterspell is a reaction to a spell being cast. If Wizard A casts Fireball and Wizard B counterspells it, Wizard A can counterspell the counterspell.

**Requirements:**
- Wizard A must have reaction available (casting Fireball uses action, not reaction)
- Wizard A must have Counterspell prepared and a slot available
- Normal Counterspell rules apply (60ft range, ability check if slot is lower than target spell)

**Common ruling:** This is legal and encouraged for dramatic moments.

**Edge case:** You cannot counterspell your own counterspell being countered - you already used your reaction.

**Source:** PHB p.228, Sage Advice Compendium

---

## Condition Lookups

### Example 4: Stunned Condition
**Query:** "What does Stunned do?"

**Response:**
**Stunned**
**Effects:**
- Incapacitated (can't take actions or reactions)
- Can't move
- Can speak only falteringly
- Automatically fails STR and DEX saving throws
- Attack rolls against the creature have advantage

**Ends when:** Source specifies (usually end of creature's next turn)

**Doesn't affect:** Concentration. Stunned doesn't break concentration - that requires Incapacitated from specific sources or damage.

**Source:** PHB p.292

---

### Example 5: Exhaustion Levels
**Query:** "Player has 3 levels of exhaustion, what happens?"

**Response:**
**Exhaustion Level 3**
**Cumulative effects:**
- Level 1: Disadvantage on ability checks
- Level 2: Speed halved
- Level 3: Disadvantage on attack rolls and saving throws

**Recovery:** One level removed per long rest (with food/water). Greater Restoration removes one level.

**Warning:** Level 4 halves HP max, Level 5 = speed 0, Level 6 = death.

**Source:** PHB p.291

---

## Combat Rules

### Example 6: Grappling
**Query:** "How does grappling work?"

**Response:**
**Grapple**
**Action cost:** Attack action (replaces one attack)
**Requirements:** Free hand, target no more than one size larger

**To initiate:**
- Athletics check vs target's Athletics OR Acrobatics (their choice)
- On success: target is Grappled

**Grappled condition:**
- Speed becomes 0
- Ends if grappler is incapacitated
- Ends if effect removes target from reach

**Moving a grappled creature:**
- Drag at half speed
- Your speed halved (unless target is 2+ sizes smaller)

**Escape:** Target's action, Athletics or Acrobatics vs your Athletics

**Common mistake:** Grappling does NOT make the target prone. That's a separate Shove action.

**Source:** PHB p.195

---

### Example 7: Opportunity Attacks
**Query:** "When exactly do opportunity attacks trigger?"

**Response:**
**Opportunity Attack**
**Trigger:** Hostile creature you can see leaves your reach using its movement, action, or reaction.

**Does NOT trigger:**
- Forced movement (shove, Thunderwave, fear effects)
- Teleportation (Misty Step, Dimension Door)
- Being moved without using movement (grappled and dragged)
- Moving within reach (circling around you)

**DOES trigger:**
- Standing up from prone (if they then move away)
- Willing movement from any source

**Action cost:** Your reaction

**Key ruling:** You get ONE reaction per round, so only one OA regardless of how many enemies flee.

**Source:** PHB p.195

---

### Example 8: Two-Weapon Fighting
**Query:** "How does dual wielding work? My player is confused about modifiers."

**Response:**
**Two-Weapon Fighting**
**Requirements:** Light weapon in each hand

**Main attack:** Normal attack action, add ability modifier to damage

**Bonus action attack:**
- Must use bonus action
- Does NOT add ability modifier to damage (unless modifier is negative)
- Still adds modifier to attack roll

**Fighting Style (Two-Weapon Fighting):** Adds ability modifier to bonus action damage

**Dual Wielder feat:** Can use non-Light weapons, +1 AC, draw two weapons at once

**Common mistake:** Bonus action attack is NOT free - it costs your bonus action. Can't also use Cunning Action, etc.

**Source:** PHB p.195

---

## Class Feature Questions

### Example 9: Smite on Ranged
**Query:** "Can a paladin smite on a thrown weapon attack?"

**Response:**
**RAW:** No. Divine Smite specifies "when you hit a creature with a melee weapon attack."

**Breakdown:**
- Thrown weapon at range = ranged weapon attack (even if it's a melee weapon)
- Thrown weapon in melee range = melee weapon attack (then yes, you can smite)

**Sage Advice confirms:** The attack type matters, not the weapon type.

**Workaround:** Some DMs allow it as homebrew. Smite spells (Branding Smite, etc.) work on ranged attacks.

**Source:** PHB p.85

---

### Example 10: Sneak Attack Clarifications
**Query:** "Does sneak attack work on opportunity attacks?"

**Response:**
**Yes.** Sneak Attack is once per TURN, not once per ROUND.

**On your turn:** Can Sneak Attack once
**On enemy's turn:** Can Sneak Attack again (via opportunity attack or Readied action)

**Requirements still apply:**
- Advantage on attack, OR
- Enemy of target within 5ft of target (and no disadvantage)
- Finesse or ranged weapon

**Maximum Sneak Attacks per round:** Technically unlimited (one per turn, many turns possible via reactions/legendary actions/etc.)

**Source:** PHB p.96, Sage Advice Compendium

---

## Edge Cases

### Example 11: Concentration + Incapacitation
**Query:** "Does being incapacitated break concentration?"

**Response:**
**RAW:** Not automatically.

**Incapacitated condition:** Can't take actions or reactions. Says nothing about concentration.

**Concentration breaks when:**
- You cast another concentration spell
- You take damage and fail CON save
- You're killed or incapacitated BY SPECIFIC EFFECTS that say so
- DM rules environment breaks it

**However:** Many effects that incapacitate ALSO specify concentration ends (like Sleep, Unconscious condition).

**Stunned specifically:** Does NOT break concentration by itself. The creature can't act but maintains focus.

**Common ruling:** Most DMs rule Stunned/Paralyzed should break concentration, but RAW it doesn't.

**Source:** PHB p.203

---

### Example 12: Stacking Advantage
**Query:** "Player has three sources of advantage. Enemy has disadvantage on saves. How does this work?"

**Response:**
**Advantage/Disadvantage never stack.**

**Rule:**
- Multiple sources of advantage = just advantage (roll 2d20, take higher)
- Multiple sources of disadvantage = just disadvantage
- ANY advantage + ANY disadvantage = straight roll (they cancel)

**Doesn't matter:**
- 3 advantages vs 1 disadvantage = straight roll
- 1 advantage vs 5 disadvantages = straight roll

**Only exception:** Elven Accuracy - if you have advantage and use DEX/INT/WIS/CHA, reroll one die. Not a third die, a reroll.

**Source:** PHB p.173

---

## Quick Reference Queries

### Example 13: Rapid Fire
**Query:** "Quick: does Hex work with Eldritch Blast? Each beam?"

**Response:**
**Yes.** Hex adds 1d6 necrotic to each attack that hits. Eldritch Blast fires multiple beams, each is a separate attack roll. Each beam that hits adds Hex damage.

Level 5 EB: 2 beams = up to 2d6 Hex damage (if both hit)
Level 11 EB: 3 beams = up to 3d6
Level 17 EB: 4 beams = up to 4d6

---

### Example 14: Instant Lookup
**Query:** "Shield spell - what's the casting time?"

**Response:**
**Shield**
**Casting:** 1 reaction (when hit by attack or targeted by Magic Missile)
**Effect:** +5 AC until start of your next turn, including against triggering attack. Blocks Magic Missile.
**Source:** PHB p.275

---

### Example 15: Yes/No Ruling
**Query:** "Can you Ready a bonus action spell?"

**Response:**
**No.** Ready action specifically says you ready an ACTION. Bonus actions cannot be readied.

**Workaround:** Ready the Attack action, then use bonus action normally on your turn before the trigger occurs.

**Source:** PHB p.193
