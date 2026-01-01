#!/usr/bin/env python3
"""
D&D 5e XP Calculator

Calculate XP thresholds for a party, adjusted XP for encounters,
encounter difficulty, and XP awards per player.

Usage:
    python xp_calculator.py --party 5,5,5,4 --monsters "2xCR2,1xCR3"
    python xp_calculator.py --party 3,3,3,3,3 --monsters "4xCR1/4,1xCR2"
    python xp_calculator.py --party 8,8,7,7 --monsters "1xCR5,2xCR3,4xCR1"
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional


def load_data() -> Dict:
    """Load calculator reference data from JSON file."""
    data_path = Path(__file__).parent / "calculator_data.json"
    with open(data_path, 'r') as f:
        return json.load(f)


DATA = None


def get_data() -> Dict:
    """Lazy load data on first access."""
    global DATA
    if DATA is None:
        DATA = load_data()
    return DATA


def parse_cr(cr_str: str) -> str:
    """
    Normalize CR string to standard format.
    Accepts: "1/4", "0.25", "1", "CR1", "cr1/4", etc.
    Returns: "1/4", "1/2", "1/8", or integer string
    """
    cr_str = cr_str.strip().lower().replace("cr", "")

    # Handle fractional notations
    if cr_str in ['1/8', '0.125']:
        return '1/8'
    elif cr_str in ['1/4', '0.25']:
        return '1/4'
    elif cr_str in ['1/2', '0.5']:
        return '1/2'
    elif cr_str == '0':
        return '0'
    else:
        try:
            # Handle decimal or integer
            val = float(cr_str)
            if val == int(val):
                return str(int(val))
            return cr_str
        except ValueError:
            raise ValueError(f"Invalid CR value: {cr_str}")


def get_xp_for_cr(cr: str) -> int:
    """Get XP value for a given CR."""
    data = get_data()
    cr = parse_cr(cr)
    return data["xp_by_cr"].get(cr, 0)


def parse_monster_string(monster_str: str) -> List[Tuple[int, str]]:
    """
    Parse monster string format: "2xCR2,1xCR3" or "2xCR1/4,1xCR2"

    Returns list of (count, cr) tuples.
    """
    monsters = []
    # Remove quotes and whitespace
    monster_str = monster_str.strip().strip('"').strip("'")

    # Split by comma
    parts = monster_str.split(',')

    for part in parts:
        part = part.strip()
        if not part:
            continue

        # Match patterns like: 2xCR2, 1xCR1/4, 3x1/2, 2xcr5, 1xCR0
        match = re.match(r'(\d+)\s*x\s*(?:CR)?(.+)', part, re.IGNORECASE)
        if match:
            count = int(match.group(1))
            cr = parse_cr(match.group(2))
            monsters.append((count, cr))
        else:
            # Try single monster format: "CR2" or "2"
            cr = parse_cr(part)
            monsters.append((1, cr))

    return monsters


def parse_party_levels(party_str: str) -> List[int]:
    """
    Parse party level string: "5,5,5,4" or "5 5 5 4"

    Returns list of party member levels.
    """
    # Handle comma or space separated
    party_str = party_str.strip().strip('"').strip("'")

    if ',' in party_str:
        parts = party_str.split(',')
    else:
        parts = party_str.split()

    levels = []
    for part in parts:
        part = part.strip()
        if part:
            try:
                level = int(part)
                if 1 <= level <= 20:
                    levels.append(level)
                else:
                    raise ValueError(f"Level must be 1-20: {level}")
            except ValueError:
                raise ValueError(f"Invalid level value: {part}")

    return levels


def calculate_party_thresholds(levels: List[int]) -> Dict[str, int]:
    """
    Calculate XP thresholds for the entire party.

    Returns dict with easy, medium, hard, deadly thresholds.
    """
    data = get_data()
    thresholds = {"easy": 0, "medium": 0, "hard": 0, "deadly": 0}

    for level in levels:
        level_str = str(level)
        level_thresholds = data["xp_thresholds_by_level"].get(level_str, {})
        for difficulty in thresholds:
            thresholds[difficulty] += level_thresholds.get(difficulty, 0)

    return thresholds


def get_encounter_multiplier(monster_count: int, party_size: int) -> float:
    """
    Get encounter XP multiplier based on monster count and party size.

    Adjusts multiplier tier based on party size per DMG guidelines:
    - Party of 1-2: Use next higher multiplier tier
    - Party of 3-5: Use standard multiplier
    - Party of 6+: Use next lower multiplier tier
    """
    data = get_data()

    # Find base multiplier from monster count
    multiplier = 1.0
    multiplier_index = 0
    multipliers = data["encounter_multipliers"]

    for i, tier in enumerate(multipliers):
        if tier["monsters_min"] <= monster_count <= tier["monsters_max"]:
            multiplier = tier["multiplier"]
            multiplier_index = i
            break

    # Adjust based on party size
    if party_size <= 2:
        # Use next higher tier (increase multiplier)
        if multiplier_index < len(multipliers) - 1:
            multiplier = multipliers[multiplier_index + 1]["multiplier"]
    elif party_size >= 6:
        # Use next lower tier (decrease multiplier)
        if multiplier_index > 0:
            multiplier = multipliers[multiplier_index - 1]["multiplier"]

    return multiplier


def calculate_encounter_xp(monsters: List[Tuple[int, str]], party_size: int) -> Dict:
    """
    Calculate total and adjusted XP for an encounter.

    Args:
        monsters: List of (count, cr) tuples
        party_size: Number of party members

    Returns:
        Dict with base_xp, adjusted_xp, multiplier, monster breakdown
    """
    total_count = sum(count for count, _ in monsters)
    base_xp = 0
    breakdown = []

    for count, cr in monsters:
        cr_xp = get_xp_for_cr(cr)
        monster_xp = count * cr_xp
        base_xp += monster_xp
        breakdown.append({
            "count": count,
            "cr": cr,
            "xp_each": cr_xp,
            "xp_total": monster_xp
        })

    multiplier = get_encounter_multiplier(total_count, party_size)
    adjusted_xp = int(base_xp * multiplier)

    return {
        "base_xp": base_xp,
        "adjusted_xp": adjusted_xp,
        "multiplier": multiplier,
        "monster_count": total_count,
        "monsters": breakdown
    }


def determine_difficulty(adjusted_xp: int, thresholds: Dict[str, int]) -> str:
    """
    Determine encounter difficulty based on adjusted XP vs party thresholds.

    Returns: "trivial", "easy", "medium", "hard", "deadly", or "beyond deadly"
    """
    if adjusted_xp < thresholds["easy"]:
        return "trivial"
    elif adjusted_xp < thresholds["medium"]:
        return "easy"
    elif adjusted_xp < thresholds["hard"]:
        return "medium"
    elif adjusted_xp < thresholds["deadly"]:
        return "hard"
    elif adjusted_xp < thresholds["deadly"] * 1.5:
        return "deadly"
    else:
        return "beyond deadly"


def calculate_xp_per_player(base_xp: int, party_size: int) -> Dict:
    """
    Calculate XP award per player.

    Note: XP award is based on BASE XP, not adjusted XP.
    Adjusted XP is only for difficulty calculation.
    """
    if party_size <= 0:
        return {"per_player": 0, "total": base_xp, "remainder": base_xp}

    per_player = base_xp // party_size
    remainder = base_xp % party_size

    return {
        "per_player": per_player,
        "total": base_xp,
        "party_size": party_size,
        "remainder": remainder
    }


def display_results(party_levels: List[int], monsters: List[Tuple[int, str]]) -> None:
    """Display full encounter calculation results."""
    party_size = len(party_levels)

    # Calculate thresholds
    thresholds = calculate_party_thresholds(party_levels)

    # Calculate encounter XP
    encounter = calculate_encounter_xp(monsters, party_size)

    # Determine difficulty
    difficulty = determine_difficulty(encounter["adjusted_xp"], thresholds)

    # Calculate XP per player
    xp_award = calculate_xp_per_player(encounter["base_xp"], party_size)

    # Display
    print("\n" + "=" * 60)
    print("D&D 5e ENCOUNTER XP CALCULATOR")
    print("=" * 60)

    # Party info
    print("\n--- PARTY ---")
    print(f"  Members: {party_size}")
    print(f"  Levels: {', '.join(str(l) for l in party_levels)}")
    avg_level = sum(party_levels) / party_size
    print(f"  Average Level: {avg_level:.1f}")

    # Party thresholds
    print("\n--- PARTY XP THRESHOLDS ---")
    print(f"  {'Easy:':<12} {thresholds['easy']:>8,} XP")
    print(f"  {'Medium:':<12} {thresholds['medium']:>8,} XP")
    print(f"  {'Hard:':<12} {thresholds['hard']:>8,} XP")
    print(f"  {'Deadly:':<12} {thresholds['deadly']:>8,} XP")

    # Monster breakdown
    print("\n--- MONSTERS ---")
    for m in encounter["monsters"]:
        print(f"  {m['count']}x CR {m['cr']}: {m['xp_each']:,} XP each = {m['xp_total']:,} XP")
    print(f"  Total monsters: {encounter['monster_count']}")

    # XP calculation
    print("\n--- XP CALCULATION ---")
    print(f"  Base XP: {encounter['base_xp']:,}")
    print(f"  Multiplier: x{encounter['multiplier']}")
    print(f"  Adjusted XP: {encounter['adjusted_xp']:,}")

    # Difficulty
    print("\n--- ENCOUNTER DIFFICULTY ---")
    difficulty_display = difficulty.upper()
    if difficulty == "beyond deadly":
        difficulty_display = "BEYOND DEADLY (!)"
    print(f"  Difficulty: {difficulty_display}")

    # Show threshold comparison
    print(f"\n  Adjusted XP ({encounter['adjusted_xp']:,}) vs Thresholds:")
    for diff_name in ["easy", "medium", "hard", "deadly"]:
        threshold = thresholds[diff_name]
        if encounter["adjusted_xp"] >= threshold:
            marker = " <--" if diff_name == difficulty else ""
            print(f"    {diff_name.capitalize()}: {threshold:,} XP [EXCEEDED]{marker}")
        else:
            print(f"    {diff_name.capitalize()}: {threshold:,} XP")

    # XP Award
    print("\n--- XP AWARD ---")
    print(f"  Total XP to award: {xp_award['total']:,}")
    print(f"  XP per player: {xp_award['per_player']:,}")
    if xp_award['remainder'] > 0:
        print(f"  (Remainder: {xp_award['remainder']} XP)")

    print("\n" + "=" * 60)


def display_thresholds_table(level: Optional[int] = None) -> None:
    """Display XP threshold reference table."""
    data = get_data()
    thresholds = data["xp_thresholds_by_level"]

    print("\n" + "=" * 60)
    print("XP THRESHOLDS BY CHARACTER LEVEL")
    print("=" * 60)
    print(f"\n{'Level':<8}{'Easy':<12}{'Medium':<12}{'Hard':<12}{'Deadly':<12}")
    print("-" * 56)

    levels_to_show = range(1, 21)
    if level:
        levels_to_show = [level]

    for lvl in levels_to_show:
        lvl_str = str(lvl)
        if lvl_str in thresholds:
            t = thresholds[lvl_str]
            marker = " <--" if level and lvl == level else ""
            print(f"{lvl:<8}{t['easy']:<12,}{t['medium']:<12,}{t['hard']:<12,}{t['deadly']:<12,}{marker}")


def display_cr_xp_table() -> None:
    """Display CR to XP reference table."""
    data = get_data()
    xp_table = data["xp_by_cr"]
    cr_order = data["cr_order"]

    print("\n" + "=" * 60)
    print("XP BY CHALLENGE RATING")
    print("=" * 60)
    print(f"\n{'CR':<10}{'XP':<15}")
    print("-" * 25)

    for cr in cr_order:
        xp = xp_table.get(cr, 0)
        print(f"{cr:<10}{xp:<15,}")


def display_multiplier_table() -> None:
    """Display encounter multiplier reference table."""
    data = get_data()
    multipliers = data["encounter_multipliers"]

    print("\n" + "=" * 60)
    print("ENCOUNTER MULTIPLIERS BY MONSTER COUNT")
    print("=" * 60)
    print("\n# of Monsters      Multiplier")
    print("-" * 30)

    for tier in multipliers:
        if tier["monsters_max"] == 999:
            range_str = f"{tier['monsters_min']}+"
        elif tier["monsters_min"] == tier["monsters_max"]:
            range_str = str(tier["monsters_min"])
        else:
            range_str = f"{tier['monsters_min']}-{tier['monsters_max']}"
        print(f"{range_str:<18}x{tier['multiplier']}")

    print("\nNote: Party size affects multiplier tier:")
    print("  - Party of 1-2: Use next HIGHER multiplier")
    print("  - Party of 3-5: Use standard multiplier")
    print("  - Party of 6+:  Use next LOWER multiplier")


def main():
    parser = argparse.ArgumentParser(
        description="D&D 5e XP Calculator - Calculate encounter difficulty and XP awards",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --party 5,5,5,4 --monsters "2xCR2,1xCR3"
      Calculate encounter with party levels 5,5,5,4 vs 2 CR2 + 1 CR3 monsters

  %(prog)s --party 3,3,3,3,3 --monsters "4xCR1/4,1xCR2"
      Party of five level 3s vs 4 CR1/4 goblins and 1 CR2 orc

  %(prog)s --party 8,8,7,7 --monsters "1xCR5,2xCR3,4xCR1"
      High-level party vs mixed encounter

  %(prog)s --thresholds
      Display XP threshold table for all levels

  %(prog)s --cr-table
      Display CR to XP conversion table

  %(prog)s --multipliers
      Display encounter multiplier reference
        """
    )

    parser.add_argument(
        '--party',
        type=str,
        metavar='LEVELS',
        help='Party member levels, comma-separated (e.g., "5,5,5,4")'
    )

    parser.add_argument(
        '--monsters',
        type=str,
        metavar='MONSTERS',
        help='Monsters in format "NxCR,NxCR" (e.g., "2xCR2,1xCR3" or "4xCR1/4,1xCR2")'
    )

    parser.add_argument(
        '--thresholds',
        action='store_true',
        help='Display XP threshold table by level'
    )

    parser.add_argument(
        '--level',
        type=int,
        metavar='LVL',
        help='Show thresholds for specific level (use with --thresholds)'
    )

    parser.add_argument(
        '--cr-table',
        action='store_true',
        help='Display CR to XP conversion table'
    )

    parser.add_argument(
        '--multipliers',
        action='store_true',
        help='Display encounter multiplier reference'
    )

    parser.add_argument(
        '--json',
        action='store_true',
        help='Output results as JSON'
    )

    args = parser.parse_args()

    # If no arguments, show help
    if len(sys.argv) == 1:
        parser.print_help()
        return

    # Show reference tables
    if args.thresholds:
        display_thresholds_table(args.level)
        return

    if args.cr_table:
        display_cr_xp_table()
        return

    if args.multipliers:
        display_multiplier_table()
        return

    # Calculate encounter
    if args.party and args.monsters:
        try:
            party_levels = parse_party_levels(args.party)
            monsters = parse_monster_string(args.monsters)

            if args.json:
                # JSON output
                party_size = len(party_levels)
                thresholds = calculate_party_thresholds(party_levels)
                encounter = calculate_encounter_xp(monsters, party_size)
                difficulty = determine_difficulty(encounter["adjusted_xp"], thresholds)
                xp_award = calculate_xp_per_player(encounter["base_xp"], party_size)

                result = {
                    "party": {
                        "size": party_size,
                        "levels": party_levels,
                        "average_level": sum(party_levels) / party_size,
                        "thresholds": thresholds
                    },
                    "encounter": encounter,
                    "difficulty": difficulty,
                    "xp_award": xp_award
                }
                print(json.dumps(result, indent=2))
            else:
                display_results(party_levels, monsters)

        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.party or args.monsters:
        print("Error: Both --party and --monsters are required for encounter calculation")
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
