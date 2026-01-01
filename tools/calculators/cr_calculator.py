#!/usr/bin/env python3
"""
D&D 5e CR Calculator

Estimate Challenge Rating for custom/homebrew monsters based on DMG guidelines.
Calculates offensive CR, defensive CR, and final CR with XP value.

Usage:
    python cr_calculator.py --hp 135 --ac 18 --attack 8 --damage 50
    python cr_calculator.py --hp 200 --ac 17 --attack 10 --damage 80 --save-dc 16
    python cr_calculator.py --hp 150 --ac 16 --attack 7 --damage 45 --special pack_tactics magic_resistance
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple


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


def get_cr_index(cr: str) -> int:
    """Get the index of a CR in the ordered CR list."""
    data = get_data()
    try:
        return data["cr_order"].index(cr)
    except ValueError:
        # Handle numeric CRs not in standard list
        try:
            numeric = float(cr)
            if numeric > 30:
                return len(data["cr_order"]) - 1
            return int(numeric) + 3  # Offset for fractional CRs
        except ValueError:
            return 0


def get_cr_from_index(index: int) -> str:
    """Get CR string from index in ordered list."""
    data = get_data()
    cr_order = data["cr_order"]
    if index < 0:
        return cr_order[0]
    if index >= len(cr_order):
        return cr_order[-1]
    return cr_order[index]


def calculate_defensive_cr(hp: int, ac: int) -> Tuple[str, Dict]:
    """
    Calculate defensive CR based on HP and AC.

    Process:
    1. Find base CR from HP range
    2. Compare actual AC to expected AC for that CR
    3. Adjust CR by +/-1 for every 2 points of AC difference

    Returns:
        Tuple of (defensive_cr, calculation_details)
    """
    data = get_data()
    stats = data["monster_statistics_by_cr"]
    cr_order = data["cr_order"]

    # Find base CR from HP
    base_cr = "0"
    for cr in cr_order:
        cr_stats = stats.get(cr, {})
        if cr_stats.get("hp_min", 0) <= hp <= cr_stats.get("hp_max", 0):
            base_cr = cr
            break
        elif hp > cr_stats.get("hp_max", 0):
            base_cr = cr

    # Get expected AC for base CR
    expected_ac = stats.get(base_cr, {}).get("ac", 13)

    # Calculate AC difference and CR adjustment
    ac_diff = ac - expected_ac
    cr_adjustment = ac_diff // 2

    # Apply adjustment
    base_index = get_cr_index(base_cr)
    final_index = base_index + cr_adjustment
    defensive_cr = get_cr_from_index(final_index)

    details = {
        "hp": hp,
        "ac": ac,
        "base_cr_from_hp": base_cr,
        "expected_ac": expected_ac,
        "ac_difference": ac_diff,
        "cr_adjustment": cr_adjustment,
        "defensive_cr": defensive_cr
    }

    return defensive_cr, details


def calculate_offensive_cr(damage: int, attack_bonus: int, save_dc: Optional[int] = None) -> Tuple[str, Dict]:
    """
    Calculate offensive CR based on damage per round and attack bonus/save DC.

    Process:
    1. Find base CR from damage per round
    2. Compare attack bonus AND save DC to expected values
    3. Use whichever adjustment is higher
    4. Adjust CR by +/-1 for every 2 points difference

    Returns:
        Tuple of (offensive_cr, calculation_details)
    """
    data = get_data()
    stats = data["monster_statistics_by_cr"]
    cr_order = data["cr_order"]

    # Find base CR from damage
    base_cr = "0"
    for cr in cr_order:
        cr_stats = stats.get(cr, {})
        if cr_stats.get("damage_min", 0) <= damage <= cr_stats.get("damage_max", 0):
            base_cr = cr
            break
        elif damage > cr_stats.get("damage_max", 0):
            base_cr = cr

    # Get expected values for base CR
    cr_stats = stats.get(base_cr, {})
    expected_attack = cr_stats.get("attack_bonus", 3)
    expected_dc = cr_stats.get("save_dc", 13)

    # Calculate attack bonus adjustment
    atk_diff = attack_bonus - expected_attack
    atk_adjustment = atk_diff // 2

    # Calculate save DC adjustment (if provided)
    dc_diff = 0
    dc_adjustment = 0
    if save_dc is not None:
        dc_diff = save_dc - expected_dc
        dc_adjustment = dc_diff // 2

    # Use higher adjustment
    cr_adjustment = max(atk_adjustment, dc_adjustment)

    # Apply adjustment
    base_index = get_cr_index(base_cr)
    final_index = base_index + cr_adjustment
    offensive_cr = get_cr_from_index(final_index)

    details = {
        "damage_per_round": damage,
        "attack_bonus": attack_bonus,
        "base_cr_from_damage": base_cr,
        "expected_attack": expected_attack,
        "attack_difference": atk_diff,
        "attack_cr_adjustment": atk_adjustment,
        "cr_adjustment_used": cr_adjustment,
        "offensive_cr": offensive_cr
    }

    if save_dc is not None:
        details["save_dc"] = save_dc
        details["expected_save_dc"] = expected_dc
        details["save_dc_difference"] = dc_diff
        details["save_dc_cr_adjustment"] = dc_adjustment

    return offensive_cr, details


def apply_special_adjustments(base_cr: str, specials: List[str]) -> Tuple[str, List[Dict]]:
    """
    Apply CR adjustments for special abilities.

    Accepts both named abilities (pack_tactics, magic_resistance) and
    custom numeric adjustments (+2, -1).

    Returns:
        Tuple of (adjusted_cr, list_of_adjustments)
    """
    data = get_data()
    ability_table = data["special_ability_adjustments"]

    total_adjustment = 0
    adjustments = []

    for special in specials:
        special_key = special.lower().replace(" ", "_").replace("-", "_")

        if special_key in ability_table:
            # Known ability
            info = ability_table[special_key]
            adj = info["cr_mod"]
            total_adjustment += adj
            adjustments.append({
                "ability": special,
                "adjustment": adj,
                "notes": info["notes"]
            })
        else:
            # Try to parse as numeric adjustment (+2, -1, etc.)
            try:
                if special.startswith("+") or special.startswith("-"):
                    adj = int(special)
                    total_adjustment += adj
                    adjustments.append({
                        "ability": f"Custom ({special})",
                        "adjustment": adj,
                        "notes": "Manual CR adjustment"
                    })
                else:
                    adjustments.append({
                        "ability": special,
                        "adjustment": 0,
                        "notes": "Unknown ability - no adjustment"
                    })
            except ValueError:
                adjustments.append({
                    "ability": special,
                    "adjustment": 0,
                    "notes": "Unknown ability - no adjustment"
                })

    # Apply total adjustment
    base_index = get_cr_index(base_cr)
    final_index = base_index + total_adjustment
    adjusted_cr = get_cr_from_index(final_index)

    return adjusted_cr, adjustments


def calculate_final_cr(hp: int, ac: int, damage: int, attack_bonus: int,
                       save_dc: Optional[int] = None,
                       specials: Optional[List[str]] = None) -> Dict:
    """
    Calculate final CR by averaging defensive and offensive CRs.

    Process:
    1. Calculate defensive CR (from HP/AC)
    2. Calculate offensive CR (from damage/attack/DC)
    3. Average the two CRs
    4. Apply special ability adjustments

    Returns:
        Complete calculation result dictionary
    """
    data = get_data()

    # Calculate component CRs
    def_cr, def_details = calculate_defensive_cr(hp, ac)
    off_cr, off_details = calculate_offensive_cr(damage, attack_bonus, save_dc)

    # Average defensive and offensive CRs
    def_index = get_cr_index(def_cr)
    off_index = get_cr_index(off_cr)
    avg_index = (def_index + off_index) // 2
    average_cr = get_cr_from_index(avg_index)

    # Apply special adjustments
    final_cr = average_cr
    special_adjustments = []

    if specials:
        final_cr, special_adjustments = apply_special_adjustments(average_cr, specials)

    # Get XP and proficiency for final CR
    xp_value = data["xp_by_cr"].get(final_cr, 0)
    stats = data["monster_statistics_by_cr"].get(final_cr, {})
    proficiency = stats.get("prof_bonus", 2)

    return {
        "final_cr": final_cr,
        "xp_value": xp_value,
        "proficiency_bonus": proficiency,
        "defensive_cr": def_cr,
        "offensive_cr": off_cr,
        "average_cr": average_cr,
        "defensive_details": def_details,
        "offensive_details": off_details,
        "special_adjustments": special_adjustments,
        "input": {
            "hp": hp,
            "ac": ac,
            "damage_per_round": damage,
            "attack_bonus": attack_bonus,
            "save_dc": save_dc,
            "specials": specials or []
        }
    }


def display_result(result: Dict) -> None:
    """Display CR calculation results in formatted output."""
    print("\n" + "=" * 65)
    print("D&D 5e CR CALCULATOR - MONSTER ESTIMATION")
    print("=" * 65)

    # Summary
    print(f"\n  FINAL CR: {result['final_cr']}")
    print(f"  XP Value: {result['xp_value']:,}")
    print(f"  Proficiency Bonus: +{result['proficiency_bonus']}")

    # Input stats
    print("\n" + "-" * 65)
    print("INPUT STATISTICS")
    print("-" * 65)
    inp = result["input"]
    print(f"  Hit Points: {inp['hp']}")
    print(f"  Armor Class: {inp['ac']}")
    print(f"  Damage/Round: {inp['damage_per_round']}")
    print(f"  Attack Bonus: +{inp['attack_bonus']}")
    if inp['save_dc']:
        print(f"  Save DC: {inp['save_dc']}")

    # Defensive CR calculation
    print("\n" + "-" * 65)
    print("DEFENSIVE CR (HP + AC)")
    print("-" * 65)
    d = result["defensive_details"]
    print(f"  1. Base CR from {d['hp']} HP: CR {d['base_cr_from_hp']}")
    print(f"  2. Expected AC for CR {d['base_cr_from_hp']}: {d['expected_ac']}")
    print(f"  3. Actual AC: {d['ac']} (difference: {d['ac_difference']:+d})")
    print(f"  4. CR adjustment from AC: {d['cr_adjustment']:+d}")
    print(f"  => Defensive CR: {d['defensive_cr']}")

    # Offensive CR calculation
    print("\n" + "-" * 65)
    print("OFFENSIVE CR (Damage + Attack/DC)")
    print("-" * 65)
    o = result["offensive_details"]
    print(f"  1. Base CR from {o['damage_per_round']} DPR: CR {o['base_cr_from_damage']}")
    print(f"  2. Expected Attack for CR {o['base_cr_from_damage']}: +{o['expected_attack']}")
    print(f"  3. Actual Attack: +{o['attack_bonus']} (difference: {o['attack_difference']:+d})")
    print(f"  4. Attack CR adjustment: {o['attack_cr_adjustment']:+d}")

    if 'save_dc' in o:
        print(f"  5. Expected Save DC for CR {o['base_cr_from_damage']}: {o['expected_save_dc']}")
        print(f"  6. Actual Save DC: {o['save_dc']} (difference: {o['save_dc_difference']:+d})")
        print(f"  7. Save DC CR adjustment: {o['save_dc_cr_adjustment']:+d}")

    print(f"  => CR adjustment used: {o['cr_adjustment_used']:+d}")
    print(f"  => Offensive CR: {o['offensive_cr']}")

    # Final calculation
    print("\n" + "-" * 65)
    print("FINAL CR CALCULATION")
    print("-" * 65)
    print(f"  Defensive CR: {result['defensive_cr']}")
    print(f"  Offensive CR: {result['offensive_cr']}")
    print(f"  Average: ({get_cr_index(result['defensive_cr'])} + {get_cr_index(result['offensive_cr'])}) / 2 = CR {result['average_cr']}")

    if result['special_adjustments']:
        print("\n  Special Ability Adjustments:")
        for adj in result['special_adjustments']:
            sign = "+" if adj['adjustment'] >= 0 else ""
            print(f"    - {adj['ability']}: {sign}{adj['adjustment']} CR")
            print(f"      ({adj['notes']})")

    print(f"\n  FINAL CR: {result['final_cr']}")
    print(f"  XP VALUE: {result['xp_value']:,}")

    print("\n" + "=" * 65)


def display_statistics_table() -> None:
    """Display monster statistics by CR reference table."""
    data = get_data()
    stats = data["monster_statistics_by_cr"]
    cr_order = data["cr_order"]

    print("\n" + "=" * 80)
    print("MONSTER STATISTICS BY CR (DMG Guidelines)")
    print("=" * 80)
    print(f"\n{'CR':<6}{'Prof':<6}{'AC':<6}{'HP Range':<14}{'Attack':<8}{'Damage/Rd':<14}{'Save DC':<8}")
    print("-" * 72)

    for cr in cr_order[:21]:  # Show CR 0-20
        s = stats.get(cr, {})
        hp_range = f"{s.get('hp_min', 0)}-{s.get('hp_max', 0)}"
        dmg_range = f"{s.get('damage_min', 0)}-{s.get('damage_max', 0)}"
        print(f"{cr:<6}+{s.get('prof_bonus', 2):<5}{s.get('ac', 13):<6}{hp_range:<14}+{s.get('attack_bonus', 3):<7}{dmg_range:<14}{s.get('save_dc', 13):<8}")

    print("\n  (Table continues to CR 30 - use --json for full data)")


def display_special_abilities() -> None:
    """Display special ability adjustment reference."""
    data = get_data()
    abilities = data["special_ability_adjustments"]

    print("\n" + "=" * 70)
    print("SPECIAL ABILITY CR ADJUSTMENTS")
    print("=" * 70)
    print("\nUse these with --special to adjust CR calculation.\n")

    for ability, info in abilities.items():
        name = ability.replace("_", " ").title()
        adj = info["cr_mod"]
        sign = "+" if adj >= 0 else ""
        print(f"  {name}:")
        print(f"    Keyword: {ability}")
        print(f"    CR Adjustment: {sign}{adj}")
        print(f"    Notes: {info['notes']}")
        print()

    print("Custom Adjustments:")
    print("  Use +N or -N for manual adjustments (e.g., --special +2 -1)")
    print("\nExample:")
    print("  python cr_calculator.py --hp 150 --ac 16 --damage 45 --attack 7 \\")
    print("    --special pack_tactics magic_resistance +1")


def display_xp_table() -> None:
    """Display CR to XP reference table."""
    data = get_data()
    xp_table = data["xp_by_cr"]
    stats = data["monster_statistics_by_cr"]
    cr_order = data["cr_order"]

    print("\n" + "=" * 50)
    print("CHALLENGE RATING TO XP")
    print("=" * 50)
    print(f"\n{'CR':<8}{'XP':<15}{'Proficiency':<12}")
    print("-" * 35)

    for cr in cr_order:
        xp = xp_table.get(cr, 0)
        prof = stats.get(cr, {}).get("prof_bonus", 2)
        print(f"{cr:<8}{xp:<15,}+{prof}")


def main():
    parser = argparse.ArgumentParser(
        description="D&D 5e CR Calculator - Estimate CR for custom monsters based on DMG",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --hp 135 --ac 18 --attack 8 --damage 50
      Basic CR calculation for a monster

  %(prog)s --hp 200 --ac 17 --attack 10 --damage 80 --save-dc 16
      Include save DC in calculation (uses higher adjustment)

  %(prog)s --hp 150 --ac 16 --attack 7 --damage 45 --special pack_tactics magic_resistance
      Apply special ability adjustments

  %(prog)s --hp 100 --ac 15 --attack 6 --damage 30 --special +2
      Apply custom +2 CR adjustment

  %(prog)s --stats
      Display monster statistics table by CR

  %(prog)s --abilities
      Display special ability adjustments reference

  %(prog)s --xp
      Display CR to XP conversion table

How CR is Calculated:
  1. DEFENSIVE CR: Based on HP (find CR range), adjusted by AC
     - Each 2 AC above/below expected = +/- 1 CR

  2. OFFENSIVE CR: Based on damage/round, adjusted by attack bonus or save DC
     - Each 2 attack/DC above/below expected = +/- 1 CR
     - If both attack and DC provided, uses higher adjustment

  3. FINAL CR: Average of defensive and offensive, plus special adjustments

Tips:
  - Damage/round = total expected damage from all attacks
  - For spellcasters, use highest damage spell for DPR
  - Resistances/immunities effectively double HP vs common damage
  - Add regeneration x3 to effective HP
        """
    )

    # Required stats for calculation
    parser.add_argument('--hp', type=int, metavar='HP',
                        help='Monster hit points')
    parser.add_argument('--ac', type=int, metavar='AC',
                        help='Monster armor class')
    parser.add_argument('--attack', type=int, metavar='BONUS',
                        help='Attack bonus (e.g., 8 for +8)')
    parser.add_argument('--damage', type=int, metavar='DPR',
                        help='Average damage per round (all attacks)')

    # Optional stats
    parser.add_argument('--save-dc', type=int, metavar='DC',
                        help='Save DC for abilities (optional)')
    parser.add_argument('--special', nargs='+', metavar='ABILITY',
                        help='Special abilities or adjustments (e.g., pack_tactics +2)')

    # Reference tables
    parser.add_argument('--stats', action='store_true',
                        help='Display monster statistics by CR')
    parser.add_argument('--abilities', action='store_true',
                        help='Display special ability adjustments')
    parser.add_argument('--xp', action='store_true',
                        help='Display CR to XP table')

    # Output format
    parser.add_argument('--json', action='store_true',
                        help='Output result as JSON')

    args = parser.parse_args()

    # If no arguments, show help
    if len(sys.argv) == 1:
        parser.print_help()
        return

    # Display reference tables
    if args.stats:
        display_statistics_table()
        return

    if args.abilities:
        display_special_abilities()
        return

    if args.xp:
        display_xp_table()
        return

    # Validate required arguments
    if not all([args.hp, args.ac, args.attack, args.damage]):
        if not any([args.stats, args.abilities, args.xp]):
            print("Error: --hp, --ac, --attack, and --damage are required for CR calculation")
            print("Use --stats, --abilities, or --xp to view reference tables")
            sys.exit(1)
        return

    # Calculate CR
    result = calculate_final_cr(
        hp=args.hp,
        ac=args.ac,
        damage=args.damage,
        attack_bonus=args.attack,
        save_dc=args.save_dc,
        specials=args.special
    )

    # Output
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        display_result(result)


if __name__ == "__main__":
    main()
