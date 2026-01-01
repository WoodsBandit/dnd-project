#!/usr/bin/env python3
"""
D&D 5e Loot Table Roller
A complete loot generation tool following DMG treasure tables.
Supports themed loot for dragon, undead, arcane, and martial encounters.

Usage:
    python loot_roller.py --cr 5 --type hoard --theme dragon
    python loot_roller.py --tier 5-10 --type individual
    python loot_roller.py --cr 15 --type hoard --format json
"""

import argparse
import json
import random
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Union


# Constants
SCRIPT_DIR = Path(__file__).parent
DATA_FILE = SCRIPT_DIR / "loot_data.json"

# Tier mappings
TIER_RANGES = {
    "0-4": (0, 4),
    "5-10": (5, 10),
    "11-16": (11, 16),
    "17+": (17, 30)
}


def load_data() -> dict:
    """Load the loot data from JSON file."""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find data file at {DATA_FILE}", file=sys.stderr)
        print("Please ensure loot_data.json exists in the same directory.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {DATA_FILE}: {e}", file=sys.stderr)
        sys.exit(1)


def roll_dice(notation: str) -> int:
    """
    Roll dice from notation like '3d6', '2d6x100', '1d4+1'.
    Returns the total.
    """
    if notation == "0" or notation == "":
        return 0

    notation = str(notation)

    # Handle multiplier (e.g., 2d6x100)
    multiplier = 1
    if 'x' in notation:
        notation, mult_str = notation.split('x')
        multiplier = int(mult_str)

    # Handle addition (e.g., 2d4+2)
    addition = 0
    if '+' in notation:
        notation, add_str = notation.split('+')
        addition = int(add_str)

    # Handle subtraction (e.g., 1d6-1)
    subtraction = 0
    if '-' in notation:
        notation, sub_str = notation.split('-')
        subtraction = int(sub_str)

    # Parse dice notation (e.g., 3d6)
    match = re.match(r'(\d+)d(\d+)', notation)
    if match:
        num_dice = int(match.group(1))
        die_size = int(match.group(2))
        total = sum(random.randint(1, die_size) for _ in range(num_dice))
        return (total + addition - subtraction) * multiplier

    # Just a number
    try:
        return int(notation) * multiplier
    except ValueError:
        return 0


def cr_to_tier(cr: int) -> str:
    """Convert CR to tier string."""
    if cr <= 4:
        return "0-4"
    elif cr <= 10:
        return "5-10"
    elif cr <= 16:
        return "11-16"
    else:
        return "17+"


def tier_to_cr(tier: str) -> int:
    """Convert tier string to a representative CR."""
    tier_map = {
        "0-4": 2,
        "5-10": 7,
        "11-16": 13,
        "17+": 20
    }
    return tier_map.get(tier, 5)


class LootRoller:
    """Main class for rolling loot tables."""

    def __init__(self, data: dict):
        self.data = data
        self.coin_tables = data["coin_tables"]
        self.gems = data["gems"]
        self.art_objects = data["art_objects"]
        self.magic_tables = data["magic_item_tables"]
        self.themes = data["themes"]

    def roll_individual(self, tier: str) -> Dict[str, Any]:
        """Roll individual treasure for the given tier."""
        table = self.coin_tables["individual"].get(tier)
        if not table:
            return {"coins": {}, "error": f"Invalid tier: {tier}"}

        roll = random.randint(1, 100)
        coins = {}

        for row in table["rolls"]:
            if row["range"][0] <= roll <= row["range"][1]:
                for coin_type in ["cp", "sp", "ep", "gp", "pp"]:
                    amount = roll_dice(row[coin_type])
                    if amount > 0:
                        coins[coin_type] = amount
                break

        return {
            "type": "individual",
            "tier": tier,
            "d100_roll": roll,
            "coins": coins,
            "total_gp": self._calculate_gp_value(coins)
        }

    def roll_hoard(self, tier: str, theme: str = "standard") -> Dict[str, Any]:
        """Roll treasure hoard for the given tier with optional theme."""
        table = self.coin_tables["hoard"].get(tier)
        if not table:
            return {"coins": {}, "error": f"Invalid tier: {tier}"}

        theme_config = self.themes.get(theme, self.themes["standard"])

        # Roll base coins with theme multiplier
        coins = {}
        coin_mult = theme_config.get("coin_multiplier", 1.0)
        for coin_type in ["cp", "sp", "ep", "gp", "pp"]:
            amount = roll_dice(table["coins"][coin_type])
            if amount > 0:
                coins[coin_type] = int(amount * coin_mult)

        # Roll d100 for additional treasure
        roll = random.randint(1, 100)
        result = {
            "type": "hoard",
            "tier": tier,
            "theme": theme,
            "d100_roll": roll,
            "coins": coins,
            "gems": [],
            "art_objects": [],
            "magic_items": [],
            "themed_extras": []
        }

        # Find matching row
        for row in table["rolls"]:
            if row["range"][0] <= roll <= row["range"][1]:
                # Roll gems
                if row.get("gems"):
                    gems = self._roll_gems(row["gems"], theme_config)
                    result["gems"] = gems

                # Roll art objects
                if row.get("art"):
                    art = self._roll_art(row["art"], theme_config)
                    result["art_objects"] = art

                # Roll magic items
                if row.get("magic"):
                    magic_items = self._roll_magic_items(row["magic"], theme, theme_config)
                    result["magic_items"] = magic_items

                break

        # Add themed extra items (50% chance)
        if theme_config.get("extra_items") and random.random() < 0.5:
            num_extras = random.randint(1, 2)
            extras = random.sample(
                theme_config["extra_items"],
                min(num_extras, len(theme_config["extra_items"]))
            )
            result["themed_extras"] = extras

        # Calculate totals
        result["total_gp"] = self._calculate_total_value(result)

        return result

    def _roll_gems(self, gem_config: dict, theme_config: dict) -> List[Dict[str, Any]]:
        """Roll gems based on configuration."""
        gem_mult = theme_config.get("gem_multiplier", 1.0)
        preferred_gems = theme_config.get("preferred_gems", [])

        gem_value = gem_config["value"]

        # Potentially use preferred gem values for theme
        if preferred_gems and str(gem_value) not in preferred_gems:
            gem_value = int(random.choice(preferred_gems))

        count = int(roll_dice(str(gem_config["count"])) * gem_mult)
        gem_list = self.gems.get(str(gem_value), [])

        gems = []
        for _ in range(count):
            if gem_list:
                gem = random.choice(gem_list)
                gems.append({
                    "name": gem["name"],
                    "description": gem["description"],
                    "value": gem_value
                })

        return gems

    def _roll_art(self, art_config: dict, theme_config: dict) -> List[Dict[str, Any]]:
        """Roll art objects based on configuration."""
        art_mult = theme_config.get("art_multiplier", 1.0)

        art_value = art_config["value"]
        count = int(roll_dice(str(art_config["count"])) * art_mult)
        art_list = self.art_objects.get(str(art_value), [])

        art_objects = []
        for _ in range(count):
            if art_list:
                art = random.choice(art_list)
                art_objects.append({
                    "name": art["name"],
                    "description": art["description"],
                    "value": art_value
                })

        return art_objects

    def _roll_magic_items(self, magic_config: dict, theme: str, theme_config: dict) -> List[Dict[str, Any]]:
        """Roll magic items from the specified table."""
        table_letter = magic_config["table"]
        count_val = magic_config["count"]

        if isinstance(count_val, int):
            count = count_val
        else:
            count = roll_dice(str(count_val))

        # Check for table bias from theme
        table_bias = theme_config.get("magic_table_bias", [])
        themed_magic = theme_config.get("themed_magic", [])

        magic_items = []
        for _ in range(count):
            # 30% chance to use themed magic item if available
            if themed_magic and random.random() < 0.3:
                item_name = random.choice(themed_magic)
                item = self._find_item_details(item_name)
                item["themed"] = True
                magic_items.append(item)
            else:
                # Use biased table if theme specifies and 40% chance
                if table_bias and random.random() < 0.4:
                    use_table = random.choice(table_bias)
                else:
                    use_table = table_letter

                item = self._roll_from_magic_table(use_table)
                if item:
                    magic_items.append(item)

        return magic_items

    def _roll_from_magic_table(self, table_letter: str) -> Optional[Dict[str, Any]]:
        """Roll a single item from a magic item table."""
        table = self.magic_tables.get(table_letter)
        if not table:
            return None

        roll = random.randint(1, 100)

        for entry in table["items"]:
            if entry["range"][0] <= roll <= entry["range"][1]:
                return {
                    "name": entry["name"],
                    "description": entry.get("description", ""),
                    "rarity": table["rarity"],
                    "table": table_letter,
                    "roll": roll,
                    "themed": False
                }

        return None

    def _find_item_details(self, item_name: str) -> Dict[str, Any]:
        """Find item details by name from magic tables."""
        for table_letter, table in self.magic_tables.items():
            for entry in table["items"]:
                if entry["name"].lower() == item_name.lower():
                    return {
                        "name": entry["name"],
                        "description": entry.get("description", ""),
                        "rarity": table["rarity"],
                        "table": table_letter,
                        "themed": True
                    }

        # If not found, return basic info
        return {
            "name": item_name,
            "description": "",
            "rarity": "unknown",
            "themed": True
        }

    def _calculate_gp_value(self, coins: dict) -> float:
        """Calculate total GP value of coins."""
        conversion = {"cp": 0.01, "sp": 0.1, "ep": 0.5, "gp": 1, "pp": 10}
        return sum(amount * conversion.get(coin, 0) for coin, amount in coins.items())

    def _calculate_total_value(self, result: dict) -> float:
        """Calculate total liquid value of treasure."""
        total = self._calculate_gp_value(result.get("coins", {}))
        total += sum(g["value"] for g in result.get("gems", []))
        total += sum(a["value"] for a in result.get("art_objects", []))
        return total


def format_coins(coins: dict) -> str:
    """Format coins as a readable string."""
    if not coins:
        return "None"

    coin_order = ["pp", "gp", "ep", "sp", "cp"]
    parts = []
    for coin in coin_order:
        if coin in coins and coins[coin] > 0:
            parts.append(f"{coins[coin]:,} {coin}")

    return ", ".join(parts) if parts else "None"


def format_text(result: dict) -> str:
    """Format result as plain text."""
    lines = []

    # Header
    treasure_type = result.get("type", "treasure").upper()
    tier = result.get("tier", "")
    theme = result.get("theme", "")

    header = f"{treasure_type} TREASURE"
    if tier:
        header += f" (CR {tier})"
    if theme and theme != "standard":
        header += f" - {theme.title()} Theme"

    lines.append("=" * 60)
    lines.append(f"  {header}")
    lines.append("=" * 60)

    # D100 roll
    if "d100_roll" in result:
        lines.append(f"\nTable Roll: {result['d100_roll']}")

    # Coins
    coins = result.get("coins", {})
    if coins:
        lines.append(f"\nCOINS: {format_coins(coins)}")
        gp_value = result.get("total_gp", 0)
        if result["type"] == "individual":
            lines.append(f"  (Value: {gp_value:,.1f} gp)")

    # Gems
    gems = result.get("gems", [])
    if gems:
        lines.append(f"\nGEMS ({len(gems)}):")
        gem_groups = {}
        for gem in gems:
            key = (gem["name"], gem["value"])
            gem_groups[key] = gem_groups.get(key, 0) + 1

        for (name, value), count in sorted(gem_groups.items(), key=lambda x: -x[0][1]):
            qty = f" x{count}" if count > 1 else ""
            lines.append(f"  - {name} ({value} gp){qty}")

        total_gem_value = sum(g["value"] for g in gems)
        lines.append(f"  Total: {total_gem_value:,} gp")

    # Art Objects
    art = result.get("art_objects", [])
    if art:
        lines.append(f"\nART OBJECTS ({len(art)}):")
        art_groups = {}
        for obj in art:
            key = (obj["name"], obj["value"])
            art_groups[key] = art_groups.get(key, 0) + 1

        for (name, value), count in sorted(art_groups.items(), key=lambda x: -x[0][1]):
            qty = f" x{count}" if count > 1 else ""
            lines.append(f"  - {name} ({value} gp){qty}")

        total_art_value = sum(a["value"] for a in art)
        lines.append(f"  Total: {total_art_value:,} gp")

    # Magic Items
    magic = result.get("magic_items", [])
    if magic:
        lines.append(f"\nMAGIC ITEMS ({len(magic)}):")
        for item in magic:
            rarity = item.get("rarity", "").replace("_", " ").title()
            themed = " [THEMED]" if item.get("themed") else ""
            table_info = f" (Table {item['table']})" if item.get("table") else ""
            lines.append(f"  - {item['name']} ({rarity}){themed}{table_info}")
            if item.get("description"):
                lines.append(f"      {item['description']}")

    # Themed Extras
    extras = result.get("themed_extras", [])
    if extras:
        lines.append("\nTHEMED EXTRAS:")
        for extra in extras:
            lines.append(f"  - {extra}")

    # Footer with totals
    lines.append("\n" + "=" * 60)
    total = result.get("total_gp", 0)
    lines.append(f"TOTAL LIQUID VALUE: {total:,.1f} gp")
    if magic:
        lines.append("(Magic item values not included)")
    lines.append("=" * 60)

    return "\n".join(lines)


def format_markdown(result: dict) -> str:
    """Format result as Markdown."""
    lines = []

    # Header
    treasure_type = result.get("type", "treasure").title()
    tier = result.get("tier", "")
    theme = result.get("theme", "")

    header = f"# {treasure_type} Treasure"
    if tier:
        header += f" (CR {tier})"
    lines.append(header)

    if theme and theme != "standard":
        lines.append(f"*Theme: {theme.title()}*\n")

    # Coins
    coins = result.get("coins", {})
    if coins:
        lines.append("## Coins")
        lines.append(f"**{format_coins(coins)}**")
        if result["type"] == "individual":
            gp_value = result.get("total_gp", 0)
            lines.append(f"*Value: {gp_value:,.1f} gp*\n")
        else:
            lines.append("")

    # Gems
    gems = result.get("gems", [])
    if gems:
        lines.append(f"## Gems ({len(gems)})")
        gem_groups = {}
        for gem in gems:
            key = (gem["name"], gem["value"], gem.get("description", ""))
            gem_groups[key] = gem_groups.get(key, 0) + 1

        for (name, value, desc), count in sorted(gem_groups.items(), key=lambda x: -x[0][1]):
            qty = f" x{count}" if count > 1 else ""
            lines.append(f"- **{name}** ({value} gp){qty}")
            if desc:
                lines.append(f"  - *{desc}*")

        total_gem_value = sum(g["value"] for g in gems)
        lines.append(f"\n*Total gem value: {total_gem_value:,} gp*\n")

    # Art Objects
    art = result.get("art_objects", [])
    if art:
        lines.append(f"## Art Objects ({len(art)})")
        art_groups = {}
        for obj in art:
            key = (obj["name"], obj["value"], obj.get("description", ""))
            art_groups[key] = art_groups.get(key, 0) + 1

        for (name, value, desc), count in sorted(art_groups.items(), key=lambda x: -x[0][1]):
            qty = f" x{count}" if count > 1 else ""
            lines.append(f"- **{name}** ({value} gp){qty}")
            if desc:
                lines.append(f"  - *{desc}*")

        total_art_value = sum(a["value"] for a in art)
        lines.append(f"\n*Total art value: {total_art_value:,} gp*\n")

    # Magic Items
    magic = result.get("magic_items", [])
    if magic:
        lines.append(f"## Magic Items ({len(magic)})")
        for item in magic:
            rarity = item.get("rarity", "").replace("_", " ").title()
            themed = " `THEMED`" if item.get("themed") else ""
            lines.append(f"### {item['name']}{themed}")
            lines.append(f"*{rarity}*")
            if item.get("description"):
                lines.append(f"> {item['description']}")
            lines.append("")

    # Themed Extras
    extras = result.get("themed_extras", [])
    if extras:
        lines.append("## Themed Extras")
        for extra in extras:
            lines.append(f"- {extra}")
        lines.append("")

    # Summary
    lines.append("---")
    total = result.get("total_gp", 0)
    lines.append(f"**Total Liquid Value:** {total:,.1f} gp")
    if magic:
        lines.append("*(Magic item values not included)*")

    return "\n".join(lines)


def format_json(result: dict) -> str:
    """Format result as JSON."""
    return json.dumps(result, indent=2)


def format_compact(result: dict) -> str:
    """Format result as a compact single-line summary."""
    parts = []

    # Coins
    coins = result.get("coins", {})
    if coins:
        gp = result.get("total_gp", 0)
        if result["type"] == "individual":
            parts.append(f"{gp:,.0f}gp")
        else:
            parts.append(f"{gp:,.0f}gp in coins/valuables")

    # Gems
    gems = result.get("gems", [])
    if gems:
        gem_value = sum(g["value"] for g in gems)
        parts.append(f"{len(gems)} gems ({gem_value:,}gp)")

    # Art
    art = result.get("art_objects", [])
    if art:
        art_value = sum(a["value"] for a in art)
        parts.append(f"{len(art)} art ({art_value:,}gp)")

    # Magic Items
    magic = result.get("magic_items", [])
    if magic:
        item_names = [m["name"] for m in magic[:3]]
        if len(magic) > 3:
            item_names.append(f"+{len(magic) - 3} more")
        parts.append(f"Magic: {', '.join(item_names)}")

    return " | ".join(parts) if parts else "Empty"


def main():
    parser = argparse.ArgumentParser(
        description="D&D 5e Loot Table Roller - Generate treasure following DMG tables",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --cr 5 --type hoard
  %(prog)s --cr 5 --type hoard --theme dragon
  %(prog)s --tier 5-10 --type individual --count 5
  %(prog)s --cr 15 --type hoard --format json
  %(prog)s --cr 20 --type hoard --theme arcane --compact

Tiers:
  0-4    : Low-level treasure
  5-10   : Mid-level treasure
  11-16  : High-level treasure
  17+    : Epic-level treasure

Themes:
  standard : Default treasure distribution
  dragon   : Dragon hoard (more coins, gems, fire-themed items)
  undead   : Tomb/crypt treasure (ancient items, anti-undead magic)
  arcane   : Wizard's tower (gems, scrolls, spellcasting items)
  martial  : Armory (weapons, armor, shields)
        """
    )

    # Tier/CR arguments (mutually exclusive group)
    tier_group = parser.add_mutually_exclusive_group(required=True)
    tier_group.add_argument(
        "--cr",
        type=int,
        help="Challenge Rating (0-30). Will be converted to appropriate tier."
    )
    tier_group.add_argument(
        "--tier",
        choices=["0-4", "5-10", "11-16", "17+"],
        help="Treasure tier (from DMG tables)"
    )

    parser.add_argument(
        "--type", "-t",
        choices=["individual", "hoard"],
        default="individual",
        help="Type of treasure (default: individual)"
    )

    parser.add_argument(
        "--theme",
        choices=["standard", "dragon", "undead", "arcane", "martial"],
        default="standard",
        help="Loot theme (default: standard). Only applies to hoards."
    )

    parser.add_argument(
        "--count", "-c",
        type=int,
        default=1,
        help="Number of times to roll (default: 1)"
    )

    parser.add_argument(
        "--format", "-f",
        choices=["text", "json", "markdown", "md"],
        default="text",
        help="Output format (default: text)"
    )

    parser.add_argument(
        "--compact",
        action="store_true",
        help="Output compact single-line summary"
    )

    parser.add_argument(
        "--seed",
        type=int,
        help="Random seed for reproducible results"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show additional details"
    )

    args = parser.parse_args()

    # Set random seed if specified
    if args.seed is not None:
        random.seed(args.seed)

    # Determine tier
    if args.cr is not None:
        tier = cr_to_tier(args.cr)
        if args.verbose:
            print(f"CR {args.cr} -> Tier {tier}", file=sys.stderr)
    else:
        tier = args.tier

    # Load data and create roller
    data = load_data()
    roller = LootRoller(data)

    # Generate treasure
    results = []
    for i in range(args.count):
        if args.type == "individual":
            result = roller.roll_individual(tier)
        else:
            result = roller.roll_hoard(tier, args.theme)
        results.append(result)

    # Format output
    output_format = args.format
    if output_format == "md":
        output_format = "markdown"

    for i, result in enumerate(results):
        if i > 0:
            if args.compact:
                print()
            else:
                print("\n" + "-" * 60 + "\n")

        if args.compact:
            if args.count > 1:
                print(f"[{i + 1}] ", end="")
            print(format_compact(result))
        elif output_format == "text":
            print(format_text(result))
        elif output_format == "markdown":
            print(format_markdown(result))
        elif output_format == "json":
            print(format_json(result))


if __name__ == "__main__":
    main()
