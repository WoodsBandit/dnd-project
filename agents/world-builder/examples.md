# World Builder Agent - Example Interactions

## Location Generation

### Example 1: Quick Tavern
**Input:**
```
Tavern, port city, gritty tone
```

**Output:**
> **The Drowned Rat** - Dockside dive bar
> **Atmosphere:** Stale beer and tar smoke; creaking floorboards over lapping water; flickering whale-oil lanterns
> **Notable Feature:** Built on a half-sunken ship - the back room is below waterline and floods at high tide
> **Who's Here:** Sailors between jobs, a one-eyed information broker named **Kelp Mara**, dockworkers avoiding the foreman
> **Secret:** The flooded back room has a hatch to smuggler tunnels beneath the harbor
> **Hook:** Kelp Mara knows who killed the harbormaster - but she wants a favor first

---

### Example 2: Dungeon Room Description
**Input:**
```
Dungeon room, ancient dwarven ruins, puzzle focus
```

**Output:**
> **The Reckoning Chamber**
> **First Impression:** Circular room, 40ft across. Seven stone statues of dwarven ancestors ring the walls, each holding a stone bowl. A massive set of scales dominates the center, one pan holding a fist-sized ruby.
> **The Puzzle:** Each bowl has a dwarven rune (the seven virtues). Placing offerings of matching "weight" in all bowls unlocks the far door. The ruby is a test - taking it triggers the trap.
> **Sensory:** Dust thick in the air, grinding stone mechanisms beneath the floor, cold radiating from the statues
> **Trap:** Taking the ruby causes statues to animate (use Stone Golem stats, reduced HP). Placing items of equal moral weight (a personal sacrifice, an oath-stone, etc.) in the opposite pan balances the scales properly.
> **Reward:** The door reveals the Vault of Grudges - contains the *Hammer of Broken Oaths* and the clan's death-ledger (plot relevant)

---

### Example 3: City District Creation
**Input:**
```
Create a market district for a desert trading city. Heroic tone.
```

**Output:**
> **The Sunbazaar** - Grand Market District
> **Atmosphere:** Riot of colored silk awnings; spice-heavy air mixing with camel musk; merchants crying wares in six languages; bells and chimes marking the hour
> **Layout:** Radiating lanes from the central **Fountain of Thirst** - each lane specializes (Spice Road, Silk Street, The Weapon Walk, Curio Court)
> **Notable Features:**
> - The fountain is magical - water is always cool and never runs dry
> - Floating carpets carry wealthy patrons above the crowd
> - The **Weighmaster's Tower** settles all disputes over measure
>
> **Key NPCs:**
> - **Hazan the Honest** - Scale merchant, actually honest, invaluable contact
> - **The Painted Lady** - Fortune teller whose predictions are unsettlingly accurate
>
> **Secret:** Beneath the fountain is an entrance to the old city, buried in a sandstorm centuries ago
> **Hook:** Someone is counterfeiting the Weighmaster's seals - trade is grinding to a halt as trust collapses

---

## Faction Generation

### Example 4: Criminal Faction
**Input:**
```
Criminal organization, large city, gritty. They deal in secrets.
```

**Output:**
> **The Listening Post**
> **Type:** Information brokers and blackmail network
> **Symbol:** An ear with a keyhole in the lobe, often worn as an earring
> **Goals:** Know everything; be indispensable to those in power; accumulate leverage over everyone who matters
> **Methods:** Bribery, eavesdropping, planted servants, intercepted letters, magical scrying (rare and expensive). Never violence - that creates enemies. Leverage creates assets.
> **Leader:** **The Curator** - identity unknown, communicates through intermediaries. Rumored to be a noble, a lich, a copper dragon, or three gnomes in a cloak.
> **Key Operations:**
> - "Subscriptions" - pay monthly for competitors' secrets
> - "Insurance" - pay to keep your secrets buried
> - "The Market" - rare information auctions, invitation only
>
> **Conflict:** The city watch wants them destroyed. The nobles want them controlled. The thieves' guild resents the competition. The Curator wants everyone exactly where they are.
> **Hook:** A player's embarrassing secret arrives via anonymous note: "We should talk."

---

### Example 5: Religious Order
**Input:**
```
Faction: a knightly order that's losing relevance. Heroic but melancholy tone.
```

**Output:**
> **The Order of the Dawning Shield**
> **Type:** Holy knights sworn to fight undead
> **Symbol:** A rising sun behind a kite shield, rays breaking over the rim
> **History:** Founded 400 years ago during the Necromancer Wars. Heroes of legend. Statues in every major city.
> **Current State:** The undead threat is mostly gone. Younger generations see them as relics. Funding has dried up. Chapter houses are closing.
> **Goals:** Maintain vigilance against the undead return; preserve their traditions; find purpose in a world that's moved on
> **Methods:** Patrols of old battlefields, maintaining blessed grounds, training young warriors, hunting isolated undead threats
> **Leader:** **Dame Seraphina Duskmantle** - 60 years old, saw real combat in her youth, terrified the Order will die on her watch
> **Membership:** 200 knights remain (down from 2000 at their height). Aging. Proud. Desperately seeking worthy quests.
> **Conflict:** A faction of young knights wants to expand their mandate to all evil. Traditionalists refuse. The schism may destroy what's left.
> **Hook:** Dame Seraphina has heard rumors of necromantic activity in the eastern provinces. She needs capable adventurers to investigate - the Order can't afford to be wrong about this.

---

## History & Lore

### Example 6: Historical Event
**Input:**
```
What happened to the old empire that these ruins are from?
```

**Output:**
> **The Sundering of Valdros**
> **When:** 800 years ago (dates are fuzzy - records were lost)
> **What Happened:** The Valdrosian Empire stretched across the continent. Their archmages attempted to bind a god to fuel eternal prosperity. The ritual succeeded - briefly. The god broke free in fury, shattering the imperial heartland into the Blasted Reach. The magical backlash killed every mage of the third circle or higher across the empire.
> **Evidence Today:**
> - The Blasted Reach - warped, magic-scarred wasteland, still dangerous
> - Valdrosian ruins everywhere, far more advanced than current structures
> - Deep cultural fear of "overreaching" magic
> - The bound god (*Aethon, Lord of Boundaries*) is now a mad, fragmented entity haunting the Reach
>
> **Truth vs. Legend:** The ritual wasn't hubris - they were trying to prevent a prophesied apocalypse. They failed... but may have only delayed it.
> **Hook:** A scholar has found evidence the Valdrosians left contingency plans. The instructions are in these ruins.

---

## Rumors & News

### Example 7: Tavern Rumor Table
**Input:**
```
Give me 6 rumors for a tavern in a logging town at the edge of a forest. Mix of true and false.
```

**Output:**
> **1.** "Loggers found an old elven shrine deep in the forest. Boss man says leave it alone, but Torvin's crew has been going back at night."
> **Truth:** True. Torvin found silver artifacts. The shrine is to a forgotten fey lord who will notice the desecration.
>
> **2.** "The miller's daughter ran off with a traveling bard last month. Broke her father's heart."
> **Truth:** False. She's been taken by something in the woods. The "bard" was never real.
>
> **3.** "Old Henrik says wolves have been acting strange - moving in patterns, like they're being directed."
> **Truth:** True. A druid is testing the town's defenses before making demands.
>
> **4.** "The Baron's raising taxes again. Third time this year. Some folks are talking about not paying."
> **Truth:** True, but incomplete. The Baron is being blackmailed and needs the money desperately.
>
> **5.** "They say there's gold in the river upstream, past the falls. That's why the company won't let anyone up there."
> **Truth:** False. The company is hiding something, but it's not gold - it's that they accidentally released something from underground.
>
> **6.** "Heard the priest has been holding secret services at midnight. Nobody knows to which god."
> **Truth:** Dangerously misleading. The priest is performing warding rituals to protect the town, but suspicion is making his job harder.

---

## Weather & Travel

### Example 8: Travel Conditions
**Input:**
```
Party traveling through mountains in late autumn. Give me conditions for the next 3 days.
```

**Output:**
> **Day 1 - Clear but Cold**
> **Conditions:** Bright sun, bitter wind, frost on the ground. Visibility excellent.
> **Travel Impact:** Normal pace, but short rest requires fire or cold damage (1d4) from exposure
> **Encounter Modifier:** Flying creatures more likely; ambush predators disadvantaged
> **Opportunity:** Perfect conditions for scouting - can spot the trail ahead, notice a mountain goat path as shortcut
>
> **Day 2 - Fog and Drizzle**
> **Conditions:** Thick fog in valleys, cold rain, visibility 60 feet. Ground slick.
> **Travel Impact:** Half pace or risk getting lost; DEX saves to avoid slipping on steep sections
> **Encounter Modifier:** Ambush encounters likely; flying creatures grounded
> **Complication:** The trail forks and both paths are obscured. Navigation check DC 15 or lose half a day
>
> **Day 3 - Early Snowstorm**
> **Conditions:** Heavy snow begins midday. Temperature drops sharply. 2 inches by nightfall.
> **Travel Impact:** Must find shelter by evening or face exhaustion. Travel only possible until midday.
> **Encounter Modifier:** Most creatures shelter; desperate or territorial ones still active
> **Opportunity:** Fresh snow reveals tracks - can clearly see what passed through recently
> **Complication:** A mountain pass they planned to use is becoming impassable. Shelter nearby, but it's occupied.

---

## Quest Hooks

### Example 9: Quick Hook Generation
**Input:**
```
Give me 3 quest hooks for a level 5 party in a coastal town. Mix of scales.
```

**Output:**
> **Hook 1: The Returning Tide** (Local)
> **Premise:** Fishermen are hauling up strange catches - fish with too many eyes, crabs with human-like faces, eels that whisper.
> **Twist:** A merfolk community offshore is fleeing something deeper. They're accidentally pushing corrupted creatures toward the surface.
> **Stakes:** If ignored, the corruption spreads. Within a month, the bay is unfishable. Within three, something comes up.
> **Reward:** Merfolk alliance, underwater cache of shipwreck treasures, information about what's below
>
> **Hook 2: The Captain's Debt** (Regional)
> **Premise:** A retired pirate captain wants to die in peace, but his old crew has found him. They want the location of their final buried haul - or his head.
> **Twist:** The treasure is real, but it's in a sea cave that's become a sahuagin breeding ground. The captain isn't afraid of dying - he's afraid they'll make him watch his grandchildren die first.
> **Stakes:** The crew will start hurting innocents in 3 days. The sahuagin are weeks from swarming the coast anyway.
> **Reward:** The captain's share of the treasure, a map to two other caches, his old ship (needs repairs), sahuagin threat revealed early
>
> **Hook 3: Letters from the Dead** (Personal)
> **Premise:** A player character receives a letter from someone they know to be dead. "I need your help. Come to the lighthouse. Tell no one. - [Name]"
> **Twist:** It's actually them - they faked their death years ago to escape [threat]. That threat has found them again.
> **Stakes:** Old connection dies for real this time; the threat turns attention to the player
> **Reward:** Reconnected relationship, information about the threat, possible new ally with useful skills/connections

---

## Regional Descriptions

### Example 10: Wilderness Region
**Input:**
```
Describe a swamp region at the border of two kingdoms. Gritty tone.
```

**Output:**
> **The Mirelands** - Contested border swamp
> **Terrain:** Miles of sucking bog, stagnant water, and curtains of moss. Solid ground exists but locals guard its locations jealously. Permanent fog below the treeline.
> **Climate:** Humid year-round; mild winters, brutal summers with biting insects and disease
> **Landmarks:**
> - **The Drowned Road** - Ancient imperial highway, mostly submerged, still the fastest route through
> - **Gallows Isle** - Where both kingdoms dump criminals; has become its own lawless community
> - **The Gasping Pools** - Sulfurous hot springs; locals claim healing properties, but the fumes cause visions
>
> **Inhabitants:**
> - Marsh folk - insular, suspicious, know the safe paths
> - Deserters from both kingdoms' armies hiding in the deep swamp
> - Lizardfolk tribes (neutral, trade for metal)
> - Something old and hungry in the deepest reaches
>
> **Danger:** Getting lost and drowning; disease (swamp fever); will-o'-wisps; the lizardfolk are tolerant but territorial; neither kingdom polices here
> **Resources:** Rare medicinal herbs, peat for fuel, frogs and fish, hidden ruins from before the empire
> **Rumors:** "Don't follow the lights." "The marsh folk know a path to a hidden city." "The kingdoms are about to go to war - the Mirelands will see fighting first."

---

## Expansion Example

### Example 11: Expanding Previous Content
**Input:**
```
Expand on The Listening Post from earlier. Tell me more about how they recruit and their base of operations.
```

**Output:**
> **Recruitment - The Listening Post**
> The Post doesn't recruit - it *cultivates*. Promising individuals are observed for months. A word in the right ear, a problem solved anonymously, a debt purchased. When the approach finally comes, the mark already owes them.
>
> **The Approach:** Always tailored. For the ambitious: "We can make you important." For the desperate: "We can make this go away." For the curious: "We can tell you who really killed your father." The offer is membership or silence. Most choose membership.
>
> **The Oath:** New members share a secret about themselves - something that would destroy them if revealed. This is their "subscription fee." They're in now, with the same leverage held over them as everyone else.
>
> **Base of Operations - The Archive**
> Location unknown. Members only know dead-drop points and intermediate contacts. Those who've been deeper describe:
> - A renovated section of the old city sewers, clean and dry
> - Rooms of filing cabinets, each lock keyed to different clearances
> - A "reading room" where sensitive meetings occur - completely soundproofed
> - The Curator's office, which only three people have ever entered
>
> **Public Fronts:**
> - **Mercer's Scribing Service** - Provides clerks and scribes to noble houses (who report everything they see)
> - **The Velvet Quill** - Upscale gambling den where lips loosen
> - **Greymoor Moneylending** - Because nothing reveals desperation like who needs loans
>
> **The Curator's Rules:**
> 1. Never kill. Dead men tell no secrets, and live enemies are leverage.
> 2. Never lie about information sold. Reputation is everything.
> 3. Some secrets stay buried. The Curator decides which.

---

### Example 12: Whimsical Tone Generation
**Input:**
```
Generate a wizard's tower. Whimsical tone.
```

**Output:**
> **The Somewhat Crooked Spire of Magnificus the Mostly Accurate**
> **Atmosphere:** Slight smell of burnt sugar and regret; the sound of arguing books; inexplicable draft that only affects left ears
> **Exterior:** Stone tower, definitely leaning, held up by what appears to be optimism and a very stressed flying buttress. The door knocker is a brass face that critiques your outfit before letting you in.
> **Notable Feature:** Each floor is a different season. Third floor (eternal autumn) has the best reading light but watch out for the melancholy.
> **Who's Here:**
> - **Magnificus** - Elderly wizard, 80% sure of most things, keeps "borrowing" spells from other dimensions
> - **Herbert** - His familiar, a toad who used to be a tax collector and preferred this
> - **The Broom Collective** - Animated brooms that have unionized and demand regular bristle maintenance
>
> **Oddities:**
> - The stairs rearrange when they feel underappreciated
> - Tea is always available, brewed by an kettle with control issues
> - The library is organized by "vibes" and is somehow the only sensible system
>
> **Secret:** Magnificus accidentally opened a portal to a dimension of pure chaos. It's in the basement. He's been feeding it socks to keep it stable. It's working so far.
> **Hook:** The portal is getting hungry for more than socks. Magnificus needs help finding something else it might like. "Perhaps a used emotion? Does anyone have a spare Tuesday?"
