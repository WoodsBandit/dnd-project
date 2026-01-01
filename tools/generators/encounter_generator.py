#!/usr/bin/env python3
"""
D&D 5e Random Encounter Generator

Generates balanced encounters based on party level, size, difficulty, and environment.
Uses official DMG encounter building rules for CR calculations.

Usage:
    python encounter_generator.py --level 5 --size 4 --difficulty hard --environment forest
"""

import argparse
import json
import random
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class EncounterGenerator:
    """Generates D&D 5e encounters using DMG rules."""

    VALID_ENVIRONMENTS = [
        "forest", "dungeon", "urban", "mountain", "swamp",
        "desert", "arctic", "coastal", "underdark"
    ]

    VALID_DIFFICULTIES = ["easy", "medium", "hard", "deadly"]

    def __init__(self, data_file: str = "encounter_data.json"):
        """Load encounter data from JSON file."""
        script_dir = Path(__file__).parent
        data_path = script_dir / data_file

        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found: {data_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in data file: {e}")

        self.monsters = self.data["monsters"]
        self.xp_thresholds = self.data["xp_thresholds_by_level"]
        self.multipliers = self.data["encounter_multipliers"]["table"]

    def cr_to_float(self, cr: str) -> float:
        """Convert CR string to float (e.g., '1/4' -> 0.25)."""
        if "/" in cr:
            num, denom = cr.split("/")
            return float(num) / float(denom)
        return float(cr)

    def get_xp_threshold(self, level: int, size: int, difficulty: str) -> int:
        """Calculate total XP threshold for party."""
        level_str = str(level)
        if level_str not in self.xp_thresholds:
            raise ValueError(f"Invalid level: {level}. Must be 1-20.")

        per_character = self.xp_thresholds[level_str][difficulty]
        return per_character * size

    def get_encounter_multiplier(self, monster_count: int, party_size: int) -> float:
        """Get XP multiplier based on number of monsters and party size."""
        # Find base multiplier from table
        multiplier = 1.0
        for entry in self.multipliers:
            if monster_count >= entry["monsters"]:
                multiplier = entry["multiplier"]

        # Adjust for party size (DMG p.83)
        multiplier_index = next(
            (i for i, e in enumerate(self.multipliers) if e["multiplier"] == multiplier),
            0
        )

        if party_size < 3:
            # Use next higher multiplier tier
            if multiplier_index < len(self.multipliers) - 1:
                multiplier = self.multipliers[multiplier_index + 1]["multiplier"]
        elif party_size >= 6:
            # Use next lower multiplier tier
            if multiplier_index > 0:
                multiplier = self.multipliers[multiplier_index - 1]["multiplier"]

        return multiplier

    def filter_monsters_by_environment(self, environment: str) -> List[Dict]:
        """Filter monsters that appear in the specified environment."""
        env_lower = environment.lower()
        return [
            m for m in self.monsters
            if env_lower in [e.lower() for e in m.get("environments", [])]
        ]

    def filter_monsters_by_cr(self, monsters: List[Dict], max_cr: float) -> List[Dict]:
        """Filter monsters by maximum CR."""
        return [
            m for m in monsters
            if self.cr_to_float(m["cr"]) <= max_cr
        ]

    def generate_solo_encounter(
        self,
        available: List[Dict],
        xp_budget: int,
        party_size: int
    ) -> Optional[Dict]:
        """Generate a single powerful monster encounter."""
        for monster in sorted(available, key=lambda m: m["xp"], reverse=True):
            multiplier = self.get_encounter_multiplier(1, party_size)
            adjusted_xp = monster["xp"] * multiplier

            # Allow 50-110% of budget
            if xp_budget * 0.5 <= adjusted_xp <= xp_budget * 1.1:
                return {
                    "composition_type": "Solo",
                    "monsters": [{
                        "name": monster["name"],
                        "cr": monster["cr"],
                        "xp": monster["xp"],
                        "count": 1,
                        "type": monster.get("type", "unknown"),
                        "tactics": monster.get("tactics", "")
                    }],
                    "total_xp": monster["xp"],
                    "adjusted_xp": int(adjusted_xp),
                    "multiplier": multiplier
                }
        return None

    def generate_pack_encounter(
        self,
        available: List[Dict],
        xp_budget: int,
        party_size: int
    ) -> Optional[Dict]:
        """Generate a pack of identical monsters (2-6)."""
        for _ in range(20):  # Try multiple times
            pack_size = random.randint(2, 6)
            multiplier = self.get_encounter_multiplier(pack_size, party_size)
            target_xp_per_monster = xp_budget / (pack_size * multiplier)

            # Find monsters close to target XP
            candidates = [
                m for m in available
                if target_xp_per_monster * 0.4 <= m["xp"] <= target_xp_per_monster * 1.6
            ]

            if candidates:
                monster = random.choice(candidates)
                total_xp = monster["xp"] * pack_size
                adjusted_xp = total_xp * multiplier

                # Allow 50-130% of budget
                if xp_budget * 0.5 <= adjusted_xp <= xp_budget * 1.3:
                    return {
                        "composition_type": "Pack",
                        "monsters": [{
                            "name": monster["name"],
                            "cr": monster["cr"],
                            "xp": monster["xp"],
                            "count": pack_size,
                            "type": monster.get("type", "unknown"),
                            "tactics": monster.get("tactics", "")
                        }],
                        "total_xp": total_xp,
                        "adjusted_xp": int(adjusted_xp),
                        "multiplier": multiplier
                    }
        return None

    def generate_leader_minions_encounter(
        self,
        available: List[Dict],
        xp_budget: int,
        party_size: int
    ) -> Optional[Dict]:
        """Generate a leader with minions encounter."""
        for _ in range(20):  # Try multiple times
            # Leader takes ~40-50% of raw XP budget
            estimated_total_monsters = random.randint(4, 7)
            multiplier = self.get_encounter_multiplier(estimated_total_monsters, party_size)
            raw_budget = xp_budget / multiplier

            leader_budget = raw_budget * random.uniform(0.35, 0.5)

            # Find suitable leader
            leaders = [
                m for m in available
                if leader_budget * 0.5 <= m["xp"] <= leader_budget * 1.3
            ]

            if not leaders:
                continue

            leader = random.choice(leaders)
            remaining_budget = raw_budget - leader["xp"]

            # Find minions (weaker creatures)
            minion_candidates = [
                m for m in available
                if m["xp"] < leader["xp"] * 0.5
                and m["xp"] <= remaining_budget / 2
                and m["xp"] >= remaining_budget / 10
            ]

            if not minion_candidates:
                continue

            minion = random.choice(minion_candidates)
            minion_count = max(2, min(8, int(remaining_budget / minion["xp"])))

            total_monsters = 1 + minion_count
            actual_multiplier = self.get_encounter_multiplier(total_monsters, party_size)
            total_xp = leader["xp"] + (minion["xp"] * minion_count)
            adjusted_xp = total_xp * actual_multiplier

            # Allow 50-130% of budget
            if xp_budget * 0.5 <= adjusted_xp <= xp_budget * 1.3:
                return {
                    "composition_type": "Leader + Minions",
                    "monsters": [
                        {
                            "name": leader["name"],
                            "cr": leader["cr"],
                            "xp": leader["xp"],
                            "count": 1,
                            "type": leader.get("type", "unknown"),
                            "tactics": leader.get("tactics", "")
                        },
                        {
                            "name": minion["name"],
                            "cr": minion["cr"],
                            "xp": minion["xp"],
                            "count": minion_count,
                            "type": minion.get("type", "unknown"),
                            "tactics": minion.get("tactics", "")
                        }
                    ],
                    "total_xp": total_xp,
                    "adjusted_xp": int(adjusted_xp),
                    "multiplier": actual_multiplier
                }
        return None

    def generate_horde_encounter(
        self,
        available: List[Dict],
        xp_budget: int,
        party_size: int
    ) -> Optional[Dict]:
        """Generate a horde of weak creatures (7+)."""
        for _ in range(20):  # Try multiple times
            horde_size = random.randint(7, 12)
            multiplier = self.get_encounter_multiplier(horde_size, party_size)
            target_xp_per_monster = xp_budget / (horde_size * multiplier)

            # Find weak monsters
            candidates = [
                m for m in available
                if target_xp_per_monster * 0.3 <= m["xp"] <= target_xp_per_monster * 1.5
                and self.cr_to_float(m["cr"]) <= 2  # Hordes work best with weak creatures
            ]

            if candidates:
                monster = random.choice(candidates)

                # Calculate optimal horde size to hit budget
                optimal_size = int(xp_budget / (monster["xp"] * multiplier))
                optimal_size = max(6, min(15, optimal_size))

                actual_multiplier = self.get_encounter_multiplier(optimal_size, party_size)
                total_xp = monster["xp"] * optimal_size
                adjusted_xp = total_xp * actual_multiplier

                # Allow 50-130% of budget
                if xp_budget * 0.5 <= adjusted_xp <= xp_budget * 1.3:
                    return {
                        "composition_type": "Horde",
                        "monsters": [{
                            "name": monster["name"],
                            "cr": monster["cr"],
                            "xp": monster["xp"],
                            "count": optimal_size,
                            "type": monster.get("type", "unknown"),
                            "tactics": monster.get("tactics", "")
                        }],
                        "total_xp": total_xp,
                        "adjusted_xp": int(adjusted_xp),
                        "multiplier": actual_multiplier
                    }
        return None

    def generate_mixed_encounter(
        self,
        available: List[Dict],
        xp_budget: int,
        party_size: int
    ) -> Optional[Dict]:
        """Generate a mixed group of different creature types."""
        for _ in range(20):
            total_monsters = random.randint(3, 6)
            multiplier = self.get_encounter_multiplier(total_monsters, party_size)
            raw_budget = xp_budget / multiplier

            # Try to pick 2-3 different monster types
            num_types = random.randint(2, min(3, len(available)))
            if len(available) < 2:
                return None

            selected = random.sample(available, min(num_types, len(available)))

            # Distribute budget somewhat evenly
            monsters_list = []
            remaining = raw_budget
            total_count = 0

            for i, monster in enumerate(selected):
                if i == len(selected) - 1:
                    # Last monster gets remaining budget
                    count = max(1, int(remaining / monster["xp"]))
                else:
                    # Each gets a portion
                    portion = remaining / (len(selected) - i)
                    count = max(1, int(portion / monster["xp"]))

                count = min(count, 4)  # Cap individual types
                if count > 0:
                    monsters_list.append({
                        "name": monster["name"],
                        "cr": monster["cr"],
                        "xp": monster["xp"],
                        "count": count,
                        "type": monster.get("type", "unknown"),
                        "tactics": monster.get("tactics", "")
                    })
                    remaining -= monster["xp"] * count
                    total_count += count

            if monsters_list and total_count >= 2:
                actual_multiplier = self.get_encounter_multiplier(total_count, party_size)
                total_xp = sum(m["xp"] * m["count"] for m in monsters_list)
                adjusted_xp = total_xp * actual_multiplier

                if xp_budget * 0.5 <= adjusted_xp <= xp_budget * 1.3:
                    return {
                        "composition_type": "Mixed Group",
                        "monsters": monsters_list,
                        "total_xp": total_xp,
                        "adjusted_xp": int(adjusted_xp),
                        "multiplier": actual_multiplier
                    }
        return None

    def generate_encounter(
        self,
        level: int,
        size: int,
        difficulty: str,
        environment: str
    ) -> Dict:
        """Generate a complete random encounter."""
        # Validate inputs
        if level < 1 or level > 20:
            return {"error": f"Invalid level: {level}. Must be 1-20."}

        if size < 1:
            return {"error": f"Invalid party size: {size}. Must be at least 1."}

        if difficulty not in self.VALID_DIFFICULTIES:
            return {"error": f"Invalid difficulty: {difficulty}. Must be one of {self.VALID_DIFFICULTIES}"}

        if environment.lower() not in [e.lower() for e in self.VALID_ENVIRONMENTS]:
            return {"error": f"Invalid environment: {environment}. Must be one of {self.VALID_ENVIRONMENTS}"}

        # Calculate XP budget
        xp_budget = self.get_xp_threshold(level, size, difficulty)

        # Filter monsters by environment
        available = self.filter_monsters_by_environment(environment)

        if not available:
            return {"error": f"No monsters found for environment: {environment}"}

        # Calculate max CR based on party level (rough guideline)
        max_cr = level + 3  # Allow monsters up to 3 CR above party level
        available = self.filter_monsters_by_cr(available, max_cr)

        if not available:
            return {"error": "No suitable monsters found for the given parameters."}

        # Generate different encounter compositions
        encounter_options = []

        solo = self.generate_solo_encounter(available, xp_budget, size)
        if solo:
            encounter_options.append(solo)

        pack = self.generate_pack_encounter(available, xp_budget, size)
        if pack:
            encounter_options.append(pack)

        leader = self.generate_leader_minions_encounter(available, xp_budget, size)
        if leader:
            encounter_options.append(leader)

        horde = self.generate_horde_encounter(available, xp_budget, size)
        if horde:
            encounter_options.append(horde)

        mixed = self.generate_mixed_encounter(available, xp_budget, size)
        if mixed:
            encounter_options.append(mixed)

        if not encounter_options:
            return {"error": "Could not generate a balanced encounter with the given parameters."}

        # Select one randomly
        encounter = random.choice(encounter_options)

        # Add metadata
        encounter["party_level"] = level
        encounter["party_size"] = size
        encounter["difficulty"] = difficulty
        encounter["environment"] = environment
        encounter["xp_budget"] = xp_budget

        # Generate tactical notes
        encounter["tactical_notes"] = self.generate_tactical_notes(encounter)

        return encounter

    def generate_tactical_notes(self, encounter: Dict) -> List[str]:
        """Generate tactical notes for the encounter."""
        notes = []

        composition = encounter.get("composition_type", "")
        monsters = encounter.get("monsters", [])

        if composition == "Solo":
            notes.append("Single powerful creature - consider legendary actions or lair effects.")
            notes.append("Party can focus fire - creature may go down quickly.")
        elif composition == "Pack":
            notes.append("Identical creatures work together with Pack Tactics if applicable.")
            notes.append("Spread them out to avoid AoE spells devastating the group.")
        elif composition == "Leader + Minions":
            notes.append("Leader coordinates minions - take out the leader to disrupt tactics.")
            notes.append("Minions can provide flanking bonuses and action economy advantage.")
        elif composition == "Horde":
            notes.append("Many weak creatures - excellent target for AoE spells.")
            notes.append("Action economy heavily favors monsters; spread damage across party.")
        elif composition == "Mixed Group":
            notes.append("Diverse threats require varied tactics to counter.")
            notes.append("Different creature types may have conflicting vulnerabilities.")

        # Add environment-specific notes
        env = encounter.get("environment", "").lower()
        env_notes = {
            "forest": "Trees provide cover. Creatures may ambush from foliage.",
            "dungeon": "Confined spaces limit movement. Watch for traps.",
            "urban": "Civilians may be present. Buildings provide cover and verticality.",
            "mountain": "Difficult terrain and elevation. Watch for falling hazards.",
            "swamp": "Difficult terrain. Water hazards. Disease risk.",
            "desert": "Open sightlines. Extreme heat. Limited cover.",
            "arctic": "Extreme cold. Ice hazards. Limited visibility in storms.",
            "coastal": "Water nearby. Tides may affect battlefield.",
            "underdark": "Complete darkness. Creatures have darkvision or blindsight."
        }
        if env in env_notes:
            notes.append(env_notes[env])

        return notes


def format_text_output(encounter: Dict) -> str:
    """Format encounter as plain text."""
    if "error" in encounter:
        return f"Error: {encounter['error']}"

    lines = [
        "=" * 60,
        f"ENCOUNTER: {encounter['composition_type']}",
        "=" * 60,
        "",
        f"Party: {encounter['party_size']} characters at level {encounter['party_level']}",
        f"Environment: {encounter['environment'].capitalize()}",
        f"Difficulty: {encounter['difficulty'].upper()}",
        "",
        f"XP Budget: {encounter['xp_budget']:,} XP",
        f"Total XP: {encounter['total_xp']:,} XP",
        f"Adjusted XP: {encounter['adjusted_xp']:,} XP (x{encounter['multiplier']} multiplier)",
        "",
        "-" * 60,
        "MONSTERS:",
        "-" * 60,
    ]

    for monster in encounter["monsters"]:
        lines.append(f"  {monster['count']}x {monster['name']}")
        lines.append(f"     CR {monster['cr']} | {monster['xp']} XP each | Type: {monster['type']}")
        if monster.get("tactics"):
            lines.append(f"     Tactics: {monster['tactics']}")
        lines.append("")

    lines.append("-" * 60)
    lines.append("TACTICAL NOTES:")
    lines.append("-" * 60)
    for note in encounter.get("tactical_notes", []):
        lines.append(f"  * {note}")

    lines.append("")
    lines.append("=" * 60)

    return "\n".join(lines)


def format_json_output(encounter: Dict) -> str:
    """Format encounter as JSON."""
    return json.dumps(encounter, indent=2)


def format_markdown_output(encounter: Dict) -> str:
    """Format encounter as Markdown."""
    if "error" in encounter:
        return f"**Error:** {encounter['error']}"

    lines = [
        f"# Encounter: {encounter['composition_type']}",
        "",
        "## Party Information",
        f"- **Party Size:** {encounter['party_size']} characters",
        f"- **Party Level:** {encounter['party_level']}",
        f"- **Environment:** {encounter['environment'].capitalize()}",
        f"- **Difficulty:** {encounter['difficulty'].capitalize()}",
        "",
        "## XP Breakdown",
        f"- **XP Budget:** {encounter['xp_budget']:,} XP",
        f"- **Total Base XP:** {encounter['total_xp']:,} XP",
        f"- **Adjusted XP:** {encounter['adjusted_xp']:,} XP",
        f"- **Multiplier:** x{encounter['multiplier']}",
        "",
        "## Monsters",
        "",
    ]

    for monster in encounter["monsters"]:
        lines.append(f"### {monster['count']}x {monster['name']}")
        lines.append(f"- **CR:** {monster['cr']}")
        lines.append(f"- **XP:** {monster['xp']} each ({monster['xp'] * monster['count']:,} total)")
        lines.append(f"- **Type:** {monster['type'].capitalize()}")
        if monster.get("tactics"):
            lines.append(f"- **Tactics:** {monster['tactics']}")
        lines.append("")

    lines.append("## Tactical Notes")
    lines.append("")
    for note in encounter.get("tactical_notes", []):
        lines.append(f"- {note}")

    lines.append("")
    lines.append("---")

    return "\n".join(lines)


def main():
    """Main entry point for CLI."""
    parser = argparse.ArgumentParser(
        description="D&D 5e Random Encounter Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --level 5 --size 4 --difficulty hard --environment forest
  %(prog)s -l 3 -s 5 -d medium -e dungeon
  %(prog)s --level 10 --size 4 --difficulty deadly --environment underdark --format json
  %(prog)s -l 7 -s 6 -d hard -e swamp --count 3

Environments:
  forest, dungeon, urban, mountain, swamp, desert, arctic, coastal, underdark

Difficulties:
  easy, medium, hard, deadly
        """
    )

    parser.add_argument(
        "--level", "-l",
        type=int,
        required=True,
        help="Party level (1-20)"
    )

    parser.add_argument(
        "--size", "-s",
        type=int,
        required=True,
        help="Party size (number of characters)"
    )

    parser.add_argument(
        "--difficulty", "-d",
        type=str,
        required=True,
        choices=["easy", "medium", "hard", "deadly"],
        help="Encounter difficulty"
    )

    parser.add_argument(
        "--environment", "-e",
        type=str,
        required=True,
        choices=EncounterGenerator.VALID_ENVIRONMENTS,
        help="Environment type"
    )

    parser.add_argument(
        "--format", "-f",
        type=str,
        default="text",
        choices=["text", "json", "markdown"],
        help="Output format (default: text)"
    )

    parser.add_argument(
        "--count", "-c",
        type=int,
        default=1,
        help="Number of encounters to generate (default: 1)"
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducible results"
    )

    args = parser.parse_args()

    # Set random seed if provided
    if args.seed is not None:
        random.seed(args.seed)

    # Initialize generator
    try:
        generator = EncounterGenerator()
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Select formatter
    formatters = {
        "text": format_text_output,
        "json": format_json_output,
        "markdown": format_markdown_output
    }
    formatter = formatters[args.format]

    # Generate encounters
    encounters = []
    for _ in range(args.count):
        encounter = generator.generate_encounter(
            level=args.level,
            size=args.size,
            difficulty=args.difficulty,
            environment=args.environment
        )
        encounters.append(encounter)

    # Output results
    if args.format == "json" and args.count > 1:
        # For JSON with multiple encounters, output as array
        print(json.dumps(encounters, indent=2))
    else:
        for i, encounter in enumerate(encounters):
            if i > 0 and args.format != "json":
                print("\n")  # Separator between multiple encounters
            print(formatter(encounter))


if __name__ == "__main__":
    main()
