#!/usr/bin/env python3
"""
D&D 5e NPC Generator
A fast, practical tool for generating NPCs during game sessions.

Usage:
    python npc_generator.py                    # Generate one random NPC
    python npc_generator.py --count 5          # Generate 5 NPCs
    python npc_generator.py --race elf         # Specify race
    python npc_generator.py --role merchant    # Specify role/occupation type
    python npc_generator.py --detailed         # Full detailed output
    python npc_generator.py --format json      # Output as JSON
"""

import argparse
import json
import random
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any


class NPCGenerator:
    """Generate random NPCs for D&D 5e."""

    def __init__(self, data_file: str = None):
        """Initialize the generator with data from JSON file."""
        if data_file is None:
            data_file = Path(__file__).parent / "npc_data.json"

        with open(data_file, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def _weighted_choice(self, weights: Dict[str, int]) -> str:
        """Make a weighted random choice from a dictionary of weights."""
        items = list(weights.keys())
        weight_values = list(weights.values())
        return random.choices(items, weights=weight_values, k=1)[0]

    def generate_race(self, specified_race: str = None) -> str:
        """Generate or return a race."""
        if specified_race:
            # Validate the specified race
            valid_races = list(self.data["names"].keys())
            if specified_race.lower() in valid_races:
                return specified_race.lower()
            else:
                print(f"Warning: '{specified_race}' not found. Using random race.")

        # Combine common and uncommon races with weights
        all_races = {}
        all_races.update(self.data["races"]["common"])
        all_races.update(self.data["races"]["uncommon"])

        return self._weighted_choice(all_races)

    def generate_gender(self) -> str:
        """Generate a random gender."""
        return random.choice(["male", "female"])

    def generate_name(self, race: str, gender: str) -> str:
        """Generate a name based on race and gender."""
        race_names = self.data["names"].get(race, self.data["names"]["human"])

        first_name = random.choice(race_names.get(gender, race_names["male"]))

        # Handle surname/clan name
        if race == "dragonborn":
            surname = random.choice(race_names.get("clan_names", ["Unknown"]))
        else:
            surname = random.choice(race_names.get("surnames", [""]))

        if surname:
            return f"{first_name} {surname}"
        return first_name

    def generate_occupation(self, role: str = None) -> str:
        """Generate an occupation based on role category."""
        occupations = self.data["occupations"]

        if role and role.lower() in occupations:
            return random.choice(occupations[role.lower()])
        elif role:
            # Try to find a matching occupation across all categories
            for category, jobs in occupations.items():
                for job in jobs:
                    if role.lower() in job.lower():
                        return job
            print(f"Warning: Role '{role}' not found. Using random occupation.")

        # Random category, weighted toward commoner
        weights = {
            "commoner": 40,
            "merchant": 15,
            "guard": 10,
            "noble": 5,
            "criminal": 8,
            "entertainer": 7,
            "religious": 5,
            "scholar": 5,
            "military": 5
        }
        category = self._weighted_choice(weights)
        return random.choice(occupations[category])

    def generate_personality_traits(self, count: int = 2) -> List[str]:
        """Generate personality traits."""
        return random.sample(self.data["personality_traits"], min(count, 3))

    def generate_ideal(self) -> Dict[str, str]:
        """Generate an ideal."""
        return random.choice(self.data["ideals"])

    def generate_bond(self) -> str:
        """Generate a bond."""
        return random.choice(self.data["bonds"])

    def generate_flaw(self) -> str:
        """Generate a flaw."""
        return random.choice(self.data["flaws"])

    def generate_motivation(self) -> str:
        """Generate a motivation."""
        return random.choice(self.data["motivations"])

    def generate_mannerism(self) -> Dict[str, str]:
        """Generate speech and physical mannerisms."""
        return {
            "speech": random.choice(self.data["mannerisms"]["speech"]),
            "physical": random.choice(self.data["mannerisms"]["physical"])
        }

    def generate_appearance(self) -> Dict[str, str]:
        """Generate appearance details."""
        appearance = self.data["appearance"]
        return {
            "build": random.choice(appearance["build"]),
            "hair": random.choice(appearance["hair"]),
            "face": random.choice(appearance["face"]),
            "distinctive": random.choice(appearance["distinctive"])
        }

    def generate_secret(self) -> str:
        """Generate a secret (for DM use)."""
        return random.choice(self.data["secrets"])

    def generate_mood(self) -> str:
        """Generate current mood."""
        return random.choice(self.data["moods"])

    def get_stat_block(self, npc_type: str = "commoner", level: int = None) -> Dict[str, Any]:
        """Get a stat block for the NPC."""
        stat_blocks = self.data["stat_blocks"]

        # Map occupation types to stat blocks
        type_mapping = {
            "guard": "guard",
            "noble": "noble",
            "spy": "spy",
            "criminal": "spy",
            "military": "veteran",
            "scholar": "mage",
            "religious": "commoner",
            "merchant": "commoner",
            "commoner": "commoner",
            "entertainer": "commoner"
        }

        block_type = type_mapping.get(npc_type.lower(), "commoner")

        # If level specified, try to scale
        if level and level > 5 and block_type in ["commoner", "guard", "noble"]:
            if level >= 10:
                block_type = "assassin" if npc_type == "criminal" else "veteran"
            elif level >= 5:
                block_type = "spy" if npc_type == "criminal" else "veteran"

        base_block = stat_blocks.get(block_type, stat_blocks["commoner"]).copy()
        base_block["type"] = block_type

        return base_block

    def generate_npc(self,
                     race: str = None,
                     role: str = None,
                     level: int = None,
                     include_secret: bool = True,
                     include_stats: bool = False) -> Dict[str, Any]:
        """Generate a complete NPC."""

        npc_race = self.generate_race(race)
        gender = self.generate_gender()

        npc = {
            "name": self.generate_name(npc_race, gender),
            "race": npc_race.title(),
            "gender": gender.title(),
            "occupation": self.generate_occupation(role),
            "personality_traits": self.generate_personality_traits(),
            "ideal": self.generate_ideal(),
            "bond": self.generate_bond(),
            "flaw": self.generate_flaw(),
            "motivation": self.generate_motivation(),
            "mannerisms": self.generate_mannerism(),
            "appearance": self.generate_appearance(),
            "mood": self.generate_mood()
        }

        if include_secret:
            npc["secret"] = self.generate_secret()

        if include_stats:
            # Determine stat block type from occupation
            occupation_lower = npc["occupation"].lower()
            stat_type = "commoner"
            for key in ["guard", "noble", "spy", "military", "criminal", "scholar"]:
                if key in occupation_lower:
                    stat_type = key
                    break
            npc["stat_block"] = self.get_stat_block(stat_type, level)

        return npc


def format_text_quick(npc: Dict[str, Any]) -> str:
    """Format NPC for quick reference (minimal output)."""
    lines = [
        f"=== {npc['name']} ===",
        f"{npc['race']} {npc['gender']} | {npc['occupation']}",
        f"Mood: {npc['mood']}",
        f"Trait: {npc['personality_traits'][0]}",
        f"Wants: {npc['motivation']}",
        f"Voice: {npc['mannerisms']['speech']}",
        f"Look: {npc['appearance']['build']}, {npc['appearance']['distinctive']}"
    ]
    if "secret" in npc:
        lines.append(f"Secret: {npc['secret']}")
    return "\n".join(lines)


def format_text_detailed(npc: Dict[str, Any]) -> str:
    """Format NPC with full details."""
    lines = [
        "=" * 50,
        f"  {npc['name']}",
        "=" * 50,
        "",
        f"Race: {npc['race']}",
        f"Gender: {npc['gender']}",
        f"Occupation: {npc['occupation']}",
        f"Current Mood: {npc['mood']}",
        "",
        "--- PERSONALITY ---",
        "Traits:"
    ]

    for trait in npc["personality_traits"]:
        lines.append(f"  - {trait}")

    ideal = npc["ideal"]
    lines.extend([
        "",
        f"Ideal: {ideal['ideal']} ({ideal['alignment']})",
        f"  \"{ideal['description']}\"",
        "",
        f"Bond: {npc['bond']}",
        "",
        f"Flaw: {npc['flaw']}",
        "",
        f"Motivation: {npc['motivation']}",
        "",
        "--- MANNERISMS ---",
        f"Speech: {npc['mannerisms']['speech']}",
        f"Physical: {npc['mannerisms']['physical']}",
        "",
        "--- APPEARANCE ---",
        f"Build: {npc['appearance']['build']}",
        f"Hair: {npc['appearance']['hair']}",
        f"Face: {npc['appearance']['face']}",
        f"Distinctive: {npc['appearance']['distinctive']}"
    ])

    if "secret" in npc:
        lines.extend([
            "",
            "--- SECRET (DM ONLY) ---",
            f"{npc['secret']}"
        ])

    if "stat_block" in npc:
        sb = npc["stat_block"]
        stats = sb["stats"]
        lines.extend([
            "",
            "--- STAT BLOCK ---",
            f"Type: {sb['type'].title()} (CR {sb['cr']})",
            f"AC: {sb['ac']} | HP: {sb['hp']} | Speed: {sb['speed']} ft.",
            f"STR: {stats['str']} | DEX: {stats['dex']} | CON: {stats['con']}",
            f"INT: {stats['int']} | WIS: {stats['wis']} | CHA: {stats['cha']}"
        ])

    lines.append("")
    return "\n".join(lines)


def format_markdown(npc: Dict[str, Any], detailed: bool = True) -> str:
    """Format NPC as Markdown."""
    lines = [
        f"# {npc['name']}",
        "",
        f"**Race:** {npc['race']} | **Gender:** {npc['gender']} | **Occupation:** {npc['occupation']}",
        "",
        f"**Current Mood:** {npc['mood']}",
        ""
    ]

    if detailed:
        lines.extend([
            "## Personality",
            "",
            "**Traits:**"
        ])
        for trait in npc["personality_traits"]:
            lines.append(f"- {trait}")

        ideal = npc["ideal"]
        lines.extend([
            "",
            f"**Ideal:** {ideal['ideal']} ({ideal['alignment']})",
            f"> {ideal['description']}",
            "",
            f"**Bond:** {npc['bond']}",
            "",
            f"**Flaw:** {npc['flaw']}",
            "",
            f"**Motivation:** {npc['motivation']}",
            "",
            "## Mannerisms",
            "",
            f"- **Speech:** {npc['mannerisms']['speech']}",
            f"- **Physical:** {npc['mannerisms']['physical']}",
            ""
        ])

    lines.extend([
        "## Appearance",
        "",
        f"- **Build:** {npc['appearance']['build']}",
        f"- **Hair:** {npc['appearance']['hair']}",
        f"- **Face:** {npc['appearance']['face']}",
        f"- **Distinctive Feature:** {npc['appearance']['distinctive']}"
    ])

    if "secret" in npc and detailed:
        lines.extend([
            "",
            "## Secret (DM Only)",
            "",
            f"*{npc['secret']}*"
        ])

    if "stat_block" in npc:
        sb = npc["stat_block"]
        stats = sb["stats"]
        lines.extend([
            "",
            "## Stat Block",
            "",
            f"**Type:** {sb['type'].title()} | **CR:** {sb['cr']}",
            "",
            f"| AC | HP | Speed |",
            f"|:--:|:--:|:-----:|",
            f"| {sb['ac']} | {sb['hp']} | {sb['speed']} ft. |",
            "",
            f"| STR | DEX | CON | INT | WIS | CHA |",
            f"|:---:|:---:|:---:|:---:|:---:|:---:|",
            f"| {stats['str']} | {stats['dex']} | {stats['con']} | {stats['int']} | {stats['wis']} | {stats['cha']} |"
        ])

    lines.append("")
    return "\n".join(lines)


def format_json(npcs: List[Dict[str, Any]], pretty: bool = True) -> str:
    """Format NPCs as JSON."""
    if len(npcs) == 1:
        output = npcs[0]
    else:
        output = {"npcs": npcs}

    if pretty:
        return json.dumps(output, indent=2)
    return json.dumps(output)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="D&D 5e NPC Generator - Generate random NPCs for your game sessions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          Generate one random NPC (quick format)
  %(prog)s --detailed               Generate one NPC with full details
  %(prog)s --race elf --role noble  Generate an elf noble
  %(prog)s --count 5 --format json  Generate 5 NPCs as JSON
  %(prog)s --role guard --stats     Generate a guard with stat block
  %(prog)s --level 10 --stats       Generate a higher-level NPC with stats

Available Races:
  human, elf, dwarf, halfling, gnome, half-elf, half-orc, tiefling, dragonborn

Available Roles:
  commoner, merchant, guard, noble, criminal, entertainer, religious,
  scholar, military, adventurer_class
        """
    )

    parser.add_argument(
        "--race", "-r",
        type=str,
        help="Specify race (e.g., human, elf, dwarf) or leave empty for random"
    )

    parser.add_argument(
        "--role", "-o",
        type=str,
        help="Specify role/occupation type (e.g., merchant, guard, noble)"
    )

    parser.add_argument(
        "--level", "-l",
        type=int,
        help="Level for classed NPCs (affects stat block scaling)"
    )

    parser.add_argument(
        "--detailed", "-d",
        action="store_true",
        help="Show full detailed output (default is quick reference)"
    )

    parser.add_argument(
        "--count", "-c",
        type=int,
        default=1,
        help="Number of NPCs to generate (default: 1)"
    )

    parser.add_argument(
        "--format", "-f",
        type=str,
        choices=["text", "json", "markdown", "md"],
        default="text",
        help="Output format (default: text)"
    )

    parser.add_argument(
        "--stats", "-s",
        action="store_true",
        help="Include stat block in output"
    )

    parser.add_argument(
        "--no-secret",
        action="store_true",
        help="Exclude secret from output"
    )

    parser.add_argument(
        "--seed",
        type=int,
        help="Random seed for reproducible results"
    )

    parser.add_argument(
        "--data-file",
        type=str,
        help="Path to custom data JSON file"
    )

    args = parser.parse_args()

    # Set random seed if provided
    if args.seed:
        random.seed(args.seed)

    # Initialize generator
    try:
        generator = NPCGenerator(args.data_file)
    except FileNotFoundError as e:
        print(f"Error: Could not find data file. {e}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in data file. {e}", file=sys.stderr)
        sys.exit(1)

    # Generate NPCs
    npcs = []
    for _ in range(args.count):
        npc = generator.generate_npc(
            race=args.race,
            role=args.role,
            level=args.level,
            include_secret=not args.no_secret,
            include_stats=args.stats
        )
        npcs.append(npc)

    # Format output
    output_format = args.format.lower()

    if output_format == "json":
        print(format_json(npcs))
    elif output_format in ["markdown", "md"]:
        for i, npc in enumerate(npcs):
            if i > 0:
                print("\n---\n")
            print(format_markdown(npc, detailed=args.detailed))
    else:  # text
        for i, npc in enumerate(npcs):
            if i > 0:
                print("\n")
            if args.detailed:
                print(format_text_detailed(npc))
            else:
                print(format_text_quick(npc))


if __name__ == "__main__":
    main()
