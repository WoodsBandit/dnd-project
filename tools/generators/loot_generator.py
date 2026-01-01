#!/usr/bin/env python3
"""
D&D 5e Loot/Treasure Generator
Fast treasure generation for mid-session "what's in the chest?" moments.
Based on DMG treasure tables.
"""

import argparse
import json
import random
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any


# Load data files
SCRIPT_DIR = Path(__file__).parent
TREASURE_FILE = SCRIPT_DIR / "treasure_tables.json"
MAGIC_ITEMS_FILE = SCRIPT_DIR / "magic_items.json"


def load_json(filepath: Path) -> dict:
    """Load JSON file with error handling."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find {filepath}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {filepath}: {e}", file=sys.stderr)
        sys.exit(1)


def roll_dice(notation: str) -> int:
    """
    Roll dice from notation like '3d6', '2d6x100', '1d4+1'.
    Returns the total.
    """
    if notation == "0":
        return 0

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

    # Parse dice notation (e.g., 3d6)
    match = re.match(r'(\d+)d(\d+)', notation)
    if match:
        num_dice = int(match.group(1))
        die_size = int(match.group(2))
        total = sum(random.randint(1, die_size) for _ in range(num_dice))
        return (total + addition) * multiplier

    # Just a number
    try:
        return int(notation) * multiplier
    except ValueError:
        return 0


def get_cr_tier(cr: int) -> str:
    """Convert CR to the appropriate tier key."""
    if cr <= 4:
        return "cr_0_4"
    elif cr <= 10:
        return "cr_5_10"
    elif cr <= 16:
        return "cr_11_16"
    else:
        return "cr_17_plus"


def roll_individual_treasure(cr: int, treasure_data: dict) -> dict:
    """Generate individual treasure (coins only) based on CR."""
    tier = get_cr_tier(cr)
    table = treasure_data["individual_treasure"][tier]

    # Roll d100
    roll = random.randint(1, 100)

    # Find matching row
    for row in table["rolls"]:
        if row["range"][0] <= roll <= row["range"][1]:
            coins = {}
            for coin_type in ["cp", "sp", "ep", "gp", "pp"]:
                amount = roll_dice(row[coin_type])
                if amount > 0:
                    coins[coin_type] = amount
            return {"coins": coins, "roll": roll}

    return {"coins": {}, "roll": roll}


def roll_hoard_treasure(cr: int, treasure_data: dict, magic_data: dict,
                        theme: Optional[str] = None) -> dict:
    """Generate hoard treasure (coins + gems + art + magic items) based on CR."""
    tier = get_cr_tier(cr)
    table = treasure_data["hoard_treasure"][tier]
    theme_config = treasure_data.get("themes", {}).get(theme, {}) if theme else {}

    # Roll base coins
    coins = {}
    coin_mult = theme_config.get("coin_multiplier", 1.0)
    for coin_type in ["cp", "sp", "ep", "gp", "pp"]:
        amount = roll_dice(table["coins"][coin_type])
        if amount > 0:
            coins[coin_type] = int(amount * coin_mult)

    # Roll d100 for additional treasure
    roll = random.randint(1, 100)
    result = {
        "coins": coins,
        "gems": [],
        "art": [],
        "magic_items": [],
        "extra_items": [],
        "roll": roll
    }

    # Find matching row
    for row in table["rolls"]:
        if row["range"][0] <= roll <= row["range"][1]:
            # Gems
            if row.get("gems"):
                gem_mult = theme_config.get("gem_multiplier", 1.0)
                preferred_gems = theme_config.get("preferred_gems", [])
                gem_value = row["gems"]["value"]

                # Use preferred gem values if theme specifies
                if preferred_gems and str(gem_value) not in preferred_gems:
                    if preferred_gems:
                        gem_value = int(random.choice(preferred_gems))

                count = int(roll_dice(str(row["gems"]["count"])) * gem_mult)
                gem_list = treasure_data["gems"].get(str(gem_value), [])
                for _ in range(count):
                    if gem_list:
                        gem = random.choice(gem_list)
                        result["gems"].append({"name": gem, "value": gem_value})

            # Art objects
            if row.get("art"):
                art_mult = theme_config.get("art_multiplier", 1.0)
                art_value = row["art"]["value"]
                count = int(roll_dice(str(row["art"]["count"])) * art_mult)
                art_list = treasure_data["art_objects"].get(str(art_value), [])
                for _ in range(count):
                    if art_list:
                        art = random.choice(art_list)
                        result["art"].append({"name": art, "value": art_value})

            # Magic items
            if row.get("magic"):
                magic_table = row["magic"]["table"]
                count_val = row["magic"]["count"]
                if isinstance(count_val, int):
                    count = count_val
                else:
                    count = roll_dice(str(count_val))

                for _ in range(count):
                    item = roll_magic_item_from_table(magic_table, magic_data, theme)
                    if item:
                        result["magic_items"].append(item)

            break

    # Add theme-specific extra items
    if theme_config.get("extra_items"):
        # 50% chance to include 1-2 extra themed items
        if random.random() < 0.5:
            num_extras = random.randint(1, 2)
            extras = random.sample(
                theme_config["extra_items"],
                min(num_extras, len(theme_config["extra_items"]))
            )
            result["extra_items"] = extras

    return result


def roll_magic_item_from_table(table_letter: str, magic_data: dict,
                                theme: Optional[str] = None) -> Optional[dict]:
    """Roll a magic item from a specific table (A-I)."""
    table = magic_data["magic_item_tables"].get(table_letter)
    if not table:
        return None

    roll = random.randint(1, 100)

    for entry in table["items"]:
        if entry["range"][0] <= roll <= entry["range"][1]:
            item_name = entry["item"]
            rarity = table["rarity"]

            # Look up description if available
            description = ""
            for rarity_items in magic_data["items_by_rarity"].values():
                for item in rarity_items:
                    if item["name"].lower() == item_name.lower():
                        description = item.get("description", "")
                        break

            return {
                "name": item_name,
                "rarity": rarity,
                "table": table_letter,
                "roll": roll,
                "description": description
            }

    return None


def roll_magic_item_by_rarity(rarity: str, magic_data: dict,
                              item_type: Optional[str] = None) -> Optional[dict]:
    """Roll a random magic item of the specified rarity."""
    items = magic_data["items_by_rarity"].get(rarity, [])

    if item_type:
        items = [i for i in items if i.get("type", "").lower() == item_type.lower()]

    if not items:
        return None

    item = random.choice(items)
    return {
        "name": item["name"],
        "rarity": rarity,
        "type": item.get("type", "unknown"),
        "description": item.get("description", "")
    }


def roll_themed_magic_item(theme: str, magic_data: dict,
                           max_rarity: Optional[str] = None) -> Optional[dict]:
    """Roll a theme-appropriate magic item."""
    themed_items = magic_data.get("themed_items", {}).get(theme, [])

    if not themed_items:
        return None

    # Filter by max rarity if specified
    rarity_order = ["common", "uncommon", "rare", "very_rare", "legendary"]
    if max_rarity:
        max_idx = rarity_order.index(max_rarity)
        themed_items = [
            i for i in themed_items
            if i.get("rarity", "varies") == "varies" or
               rarity_order.index(i.get("rarity", "common")) <= max_idx
        ]

    if not themed_items:
        return None

    item_ref = random.choice(themed_items)
    rarity = item_ref.get("rarity", "uncommon")
    if rarity == "varies":
        rarity = random.choice(["uncommon", "rare", "very_rare"])

    # Look up full item details
    items = magic_data["items_by_rarity"].get(rarity, [])
    for item in items:
        if item["name"].lower() == item_ref["name"].lower():
            return {
                "name": item["name"],
                "rarity": rarity,
                "type": item.get("type", "unknown"),
                "description": item.get("description", ""),
                "themed": True
            }

    # If not found in rarity list, return basic info
    return {
        "name": item_ref["name"],
        "rarity": rarity,
        "themed": True
    }


def format_coins(coins: dict) -> str:
    """Format coin amounts as a readable string."""
    if not coins:
        return "None"

    parts = []
    for coin, amount in coins.items():
        if amount > 0:
            parts.append(f"{amount:,} {coin}")

    return ", ".join(parts) if parts else "None"


def calculate_total_gp(coins: dict) -> float:
    """Calculate total gold piece value of coins."""
    conversion = {"cp": 0.01, "sp": 0.1, "ep": 0.5, "gp": 1, "pp": 10}
    return sum(amount * conversion.get(coin, 0) for coin, amount in coins.items())


def format_text(result: dict, treasure_type: str) -> str:
    """Format treasure result as plain text."""
    lines = []
    lines.append("=" * 50)
    lines.append(f"  {treasure_type.upper()} TREASURE")
    lines.append("=" * 50)

    # Coins
    if result.get("coins"):
        coins = result["coins"]
        lines.append(f"\nCOINS: {format_coins(coins)}")
        total = calculate_total_gp(coins)
        lines.append(f"  (Total value: {total:,.1f} gp)")

    # Gems
    if result.get("gems"):
        lines.append(f"\nGEMS ({len(result['gems'])}):")
        gem_groups = {}
        for gem in result["gems"]:
            key = f"{gem['name']} ({gem['value']} gp)"
            gem_groups[key] = gem_groups.get(key, 0) + 1
        for gem_name, count in gem_groups.items():
            if count > 1:
                lines.append(f"  - {gem_name} x{count}")
            else:
                lines.append(f"  - {gem_name}")
        total_gem_value = sum(g["value"] for g in result["gems"])
        lines.append(f"  (Total gem value: {total_gem_value:,} gp)")

    # Art objects
    if result.get("art"):
        lines.append(f"\nART OBJECTS ({len(result['art'])}):")
        art_groups = {}
        for art in result["art"]:
            key = f"{art['name']} ({art['value']} gp)"
            art_groups[key] = art_groups.get(key, 0) + 1
        for art_name, count in art_groups.items():
            if count > 1:
                lines.append(f"  - {art_name} x{count}")
            else:
                lines.append(f"  - {art_name}")
        total_art_value = sum(a["value"] for a in result["art"])
        lines.append(f"  (Total art value: {total_art_value:,} gp)")

    # Magic items
    if result.get("magic_items"):
        lines.append(f"\nMAGIC ITEMS ({len(result['magic_items'])}):")
        for item in result["magic_items"]:
            rarity = item.get("rarity", "unknown").replace("_", " ").title()
            themed = " [THEMED]" if item.get("themed") else ""
            lines.append(f"  - {item['name']} ({rarity}){themed}")
            if item.get("description"):
                lines.append(f"      {item['description']}")

    # Extra themed items
    if result.get("extra_items"):
        lines.append("\nTHEMED EXTRAS:")
        for item in result["extra_items"]:
            lines.append(f"  - {item}")

    lines.append("\n" + "=" * 50)

    # Grand total
    total_value = calculate_total_gp(result.get("coins", {}))
    total_value += sum(g["value"] for g in result.get("gems", []))
    total_value += sum(a["value"] for a in result.get("art", []))
    lines.append(f"TOTAL LIQUID VALUE: {total_value:,.1f} gp")
    lines.append("(Magic item values not included)")

    return "\n".join(lines)


def format_markdown(result: dict, treasure_type: str) -> str:
    """Format treasure result as Markdown."""
    lines = []
    lines.append(f"# {treasure_type.title()} Treasure\n")

    # Coins
    if result.get("coins"):
        coins = result["coins"]
        lines.append("## Coins")
        lines.append(f"**{format_coins(coins)}**")
        total = calculate_total_gp(coins)
        lines.append(f"*Total value: {total:,.1f} gp*\n")

    # Gems
    if result.get("gems"):
        lines.append(f"## Gems ({len(result['gems'])})")
        gem_groups = {}
        for gem in result["gems"]:
            key = (gem['name'], gem['value'])
            gem_groups[key] = gem_groups.get(key, 0) + 1
        for (name, value), count in gem_groups.items():
            qty = f" x{count}" if count > 1 else ""
            lines.append(f"- **{name}** ({value} gp){qty}")
        total_gem_value = sum(g["value"] for g in result["gems"])
        lines.append(f"\n*Total gem value: {total_gem_value:,} gp*\n")

    # Art objects
    if result.get("art"):
        lines.append(f"## Art Objects ({len(result['art'])})")
        art_groups = {}
        for art in result["art"]:
            key = (art['name'], art['value'])
            art_groups[key] = art_groups.get(key, 0) + 1
        for (name, value), count in art_groups.items():
            qty = f" x{count}" if count > 1 else ""
            lines.append(f"- **{name}** ({value} gp){qty}")
        total_art_value = sum(a["value"] for a in result["art"])
        lines.append(f"\n*Total art value: {total_art_value:,} gp*\n")

    # Magic items
    if result.get("magic_items"):
        lines.append(f"## Magic Items ({len(result['magic_items'])})")
        for item in result["magic_items"]:
            rarity = item.get("rarity", "unknown").replace("_", " ").title()
            themed = " `THEMED`" if item.get("themed") else ""
            lines.append(f"### {item['name']}{themed}")
            lines.append(f"*{rarity}*")
            if item.get("description"):
                lines.append(f"> {item['description']}")
            lines.append("")

    # Extra themed items
    if result.get("extra_items"):
        lines.append("## Themed Extras")
        for item in result["extra_items"]:
            lines.append(f"- {item}")
        lines.append("")

    # Grand total
    lines.append("---")
    total_value = calculate_total_gp(result.get("coins", {}))
    total_value += sum(g["value"] for g in result.get("gems", []))
    total_value += sum(a["value"] for a in result.get("art", []))
    lines.append(f"**Total Liquid Value:** {total_value:,.1f} gp")
    lines.append("*(Magic item values not included)*")

    return "\n".join(lines)


def format_json(result: dict, treasure_type: str) -> str:
    """Format treasure result as JSON."""
    output = {
        "type": treasure_type,
        "result": result,
        "summary": {
            "coin_value_gp": calculate_total_gp(result.get("coins", {})),
            "gem_value_gp": sum(g["value"] for g in result.get("gems", [])),
            "art_value_gp": sum(a["value"] for a in result.get("art", [])),
            "magic_item_count": len(result.get("magic_items", [])),
            "total_liquid_gp": (
                calculate_total_gp(result.get("coins", {})) +
                sum(g["value"] for g in result.get("gems", [])) +
                sum(a["value"] for a in result.get("art", []))
            )
        }
    }
    return json.dumps(output, indent=2)


def format_quick(result: dict) -> str:
    """Quick one-line summary for fast lookups."""
    coins = result.get("coins", {})
    total_gp = calculate_total_gp(coins)
    gems = len(result.get("gems", []))
    art = len(result.get("art", []))
    magic = len(result.get("magic_items", []))

    parts = []
    if total_gp > 0:
        parts.append(f"{total_gp:,.0f}gp in coins")
    if gems > 0:
        gem_val = sum(g["value"] for g in result["gems"])
        parts.append(f"{gems} gems ({gem_val:,}gp)")
    if art > 0:
        art_val = sum(a["value"] for a in result["art"])
        parts.append(f"{art} art ({art_val:,}gp)")
    if magic > 0:
        items = [m["name"] for m in result["magic_items"]]
        parts.append(f"Magic: {', '.join(items)}")

    return " | ".join(parts) if parts else "Nothing of value"


def main():
    parser = argparse.ArgumentParser(
        description="D&D 5e Loot/Treasure Generator - Fast treasure for your games!",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --type individual --cr 5
  %(prog)s --type hoard --cr 10 --theme dragon
  %(prog)s --type hoard --cr 15 --magic-items 3 --rarity rare
  %(prog)s --type individual --cr 3 --count 5
  %(prog)s --quick --type hoard --cr 8
        """
    )

    parser.add_argument(
        "--type", "-t",
        choices=["individual", "hoard", "magic"],
        default="individual",
        help="Type of treasure (default: individual)"
    )

    parser.add_argument(
        "--cr",
        type=int,
        default=1,
        help="Challenge rating (default: 1)"
    )

    parser.add_argument(
        "--theme",
        choices=[
            "dragon", "undead", "bandit", "merchant", "arcane",
            "noble", "pirate", "fey", "elemental", "fiend"
        ],
        help="Themed loot (affects item selection and flavor)"
    )

    parser.add_argument(
        "--magic-items", "-m",
        type=int,
        default=0,
        help="Additional magic items to include (rolled separately)"
    )

    parser.add_argument(
        "--rarity", "-r",
        choices=["common", "uncommon", "rare", "very_rare", "legendary"],
        help="Rarity for additional magic items (default: based on CR)"
    )

    parser.add_argument(
        "--item-type",
        choices=["weapon", "armor", "wondrous", "ring", "rod", "staff", "wand", "potion", "scroll"],
        help="Filter additional magic items by type"
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
        "--quick", "-q",
        action="store_true",
        help="Quick one-line output (overrides --format)"
    )

    parser.add_argument(
        "--seed",
        type=int,
        help="Random seed for reproducible results"
    )

    args = parser.parse_args()

    # Set random seed if specified
    if args.seed is not None:
        random.seed(args.seed)

    # Load data
    treasure_data = load_json(TREASURE_FILE)
    magic_data = load_json(MAGIC_ITEMS_FILE)

    # Determine default rarity based on CR if not specified
    if args.rarity is None:
        if args.cr <= 4:
            default_rarity = "uncommon"
        elif args.cr <= 10:
            default_rarity = "rare"
        elif args.cr <= 16:
            default_rarity = "very_rare"
        else:
            default_rarity = "legendary"
    else:
        default_rarity = args.rarity

    # Generate treasure
    results = []
    for i in range(args.count):
        if args.type == "individual":
            result = roll_individual_treasure(args.cr, treasure_data)
            treasure_type = f"Individual (CR {args.cr})"
        elif args.type == "hoard":
            result = roll_hoard_treasure(args.cr, treasure_data, magic_data, args.theme)
            theme_str = f", {args.theme.title()} Theme" if args.theme else ""
            treasure_type = f"Hoard (CR {args.cr}{theme_str})"
        else:  # magic only
            result = {"magic_items": []}
            treasure_type = f"Magic Items ({default_rarity.replace('_', ' ').title()})"

        # Add extra magic items if requested
        extra_magic = args.magic_items
        if args.type == "magic":
            extra_magic = max(extra_magic, 1)  # At least 1 for magic type

        if extra_magic > 0:
            if "magic_items" not in result:
                result["magic_items"] = []

            for _ in range(extra_magic):
                if args.theme:
                    item = roll_themed_magic_item(args.theme, magic_data, default_rarity)
                else:
                    item = roll_magic_item_by_rarity(default_rarity, magic_data, args.item_type)

                if item:
                    result["magic_items"].append(item)

        results.append((result, treasure_type))

    # Format and output
    if args.quick:
        for result, treasure_type in results:
            if args.count > 1:
                print(f"[{treasure_type}] ", end="")
            print(format_quick(result))
    else:
        output_format = args.format
        if output_format == "md":
            output_format = "markdown"

        for i, (result, treasure_type) in enumerate(results):
            if i > 0:
                print("\n" + "-" * 50 + "\n")

            if output_format == "text":
                print(format_text(result, treasure_type))
            elif output_format == "markdown":
                print(format_markdown(result, treasure_type))
            elif output_format == "json":
                print(format_json(result, treasure_type))


if __name__ == "__main__":
    main()
