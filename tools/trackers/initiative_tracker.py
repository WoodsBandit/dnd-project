#!/usr/bin/env python3
"""
D&D 5e Initiative Tracker
Interactive CLI tool for tracking combat encounters.
"""

import json
import random
import os
import re
from dataclasses import dataclass, field, asdict
from typing import Optional
from pathlib import Path

# Directory where this script is located (for loading conditions.json)
SCRIPT_DIR = Path(__file__).parent


@dataclass
class Condition:
    """Represents a condition applied to a combatant."""
    name: str
    rounds_remaining: Optional[int] = None  # None = indefinite

    def tick(self) -> bool:
        """Reduce duration by 1. Returns True if condition expired."""
        if self.rounds_remaining is not None:
            self.rounds_remaining -= 1
            return self.rounds_remaining <= 0
        return False

    def to_dict(self) -> dict:
        return {"name": self.name, "rounds_remaining": self.rounds_remaining}

    @classmethod
    def from_dict(cls, data: dict) -> "Condition":
        return cls(name=data["name"], rounds_remaining=data.get("rounds_remaining"))


@dataclass
class Combatant:
    """Represents a creature or character in combat."""
    name: str
    initiative: int
    hp: int
    max_hp: int
    ac: int
    dex_mod: int = 0
    conditions: list = field(default_factory=list)
    is_dead: bool = False
    is_unconscious: bool = False
    group_id: Optional[str] = None  # For grouping identical monsters

    def apply_damage(self, amount: int) -> int:
        """Apply damage and return actual damage dealt."""
        actual = min(amount, self.hp)
        self.hp -= actual
        if self.hp <= 0:
            self.hp = 0
            self.is_unconscious = True
        return actual

    def apply_healing(self, amount: int) -> int:
        """Apply healing and return actual healing done."""
        if self.is_dead:
            return 0
        old_hp = self.hp
        self.hp = min(self.hp + amount, self.max_hp)
        if self.hp > 0:
            self.is_unconscious = False
        return self.hp - old_hp

    def add_condition(self, condition_name: str, rounds: Optional[int] = None):
        """Add a condition with optional duration."""
        # Remove existing condition of same type
        self.conditions = [c for c in self.conditions if c.name.lower() != condition_name.lower()]
        self.conditions.append(Condition(condition_name, rounds))

    def remove_condition(self, condition_name: str) -> bool:
        """Remove a condition. Returns True if found and removed."""
        original_len = len(self.conditions)
        self.conditions = [c for c in self.conditions if c.name.lower() != condition_name.lower()]
        return len(self.conditions) < original_len

    def tick_conditions(self) -> list:
        """Tick all conditions and return list of expired condition names."""
        expired = []
        remaining = []
        for cond in self.conditions:
            if cond.tick():
                expired.append(cond.name)
            else:
                remaining.append(cond)
        self.conditions = remaining
        return expired

    def get_status_line(self, is_current: bool = False) -> str:
        """Get a formatted status line for display."""
        marker = ">>>" if is_current else "   "
        status = ""
        if self.is_dead:
            status = " [DEAD]"
        elif self.is_unconscious:
            status = " [UNCONSCIOUS]"

        cond_str = ""
        if self.conditions:
            cond_list = []
            for c in self.conditions:
                if c.rounds_remaining is not None:
                    cond_list.append(f"{c.name}({c.rounds_remaining})")
                else:
                    cond_list.append(c.name)
            cond_str = f" [{', '.join(cond_list)}]"

        hp_display = f"{self.hp}/{self.max_hp}"
        return f"{marker} {self.initiative:2d} | {self.name:<20} | HP: {hp_display:<9} | AC: {self.ac}{status}{cond_str}"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "initiative": self.initiative,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "ac": self.ac,
            "dex_mod": self.dex_mod,
            "conditions": [c.to_dict() for c in self.conditions],
            "is_dead": self.is_dead,
            "is_unconscious": self.is_unconscious,
            "group_id": self.group_id
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Combatant":
        conditions = [Condition.from_dict(c) for c in data.get("conditions", [])]
        return cls(
            name=data["name"],
            initiative=data["initiative"],
            hp=data["hp"],
            max_hp=data["max_hp"],
            ac=data["ac"],
            dex_mod=data.get("dex_mod", 0),
            conditions=conditions,
            is_dead=data.get("is_dead", False),
            is_unconscious=data.get("is_unconscious", False),
            group_id=data.get("group_id")
        )


class InitiativeTracker:
    """Main tracker class for managing combat."""

    def __init__(self):
        self.combatants: list[Combatant] = []
        self.current_index: int = 0
        self.round_number: int = 1
        self.combat_started: bool = False
        self.group_counters: dict[str, int] = {}  # Track monster group numbers
        self.conditions_ref = self._load_conditions()

    def _load_conditions(self) -> dict:
        """Load conditions reference from JSON file."""
        conditions_file = SCRIPT_DIR / "conditions.json"
        if conditions_file.exists():
            with open(conditions_file, 'r') as f:
                data = json.load(f)
                return data.get("conditions", {})
        return {}

    def add_combatant(self, name: str, initiative: int, hp: int, ac: int,
                      dex_mod: int = 0, count: int = 1) -> list[str]:
        """Add one or more combatants. Returns list of names added."""
        added = []
        for i in range(count):
            if count > 1:
                # Grouped monsters
                if name not in self.group_counters:
                    self.group_counters[name] = 0
                self.group_counters[name] += 1
                actual_name = f"{name} {self.group_counters[name]}"
                group_id = name
            else:
                actual_name = name
                group_id = None

            combatant = Combatant(
                name=actual_name,
                initiative=initiative,
                hp=hp,
                max_hp=hp,
                ac=ac,
                dex_mod=dex_mod,
                group_id=group_id
            )
            self.combatants.append(combatant)
            added.append(actual_name)

        self._sort_combatants()
        return added

    def roll_initiative(self, name: str, dex_mod: int = 0, count: int = 1,
                        hp: int = 10, ac: int = 10) -> list[tuple[str, int]]:
        """Roll initiative for new combatant(s). Returns list of (name, roll) tuples."""
        results = []
        for i in range(count):
            roll = random.randint(1, 20) + dex_mod

            if count > 1:
                if name not in self.group_counters:
                    self.group_counters[name] = 0
                self.group_counters[name] += 1
                actual_name = f"{name} {self.group_counters[name]}"
                group_id = name
            else:
                actual_name = name
                group_id = None

            combatant = Combatant(
                name=actual_name,
                initiative=roll,
                hp=hp,
                max_hp=hp,
                ac=ac,
                dex_mod=dex_mod,
                group_id=group_id
            )
            self.combatants.append(combatant)
            results.append((actual_name, roll))

        self._sort_combatants()
        return results

    def _sort_combatants(self):
        """Sort combatants by initiative (desc), then DEX mod (desc), then name."""
        self.combatants.sort(key=lambda c: (-c.initiative, -c.dex_mod, c.name))

    def find_combatant(self, name: str) -> Optional[Combatant]:
        """Find a combatant by name (case-insensitive, partial match)."""
        name_lower = name.lower()
        # Exact match first
        for c in self.combatants:
            if c.name.lower() == name_lower:
                return c
        # Partial match
        for c in self.combatants:
            if name_lower in c.name.lower():
                return c
        return None

    def find_combatants_by_group(self, group_name: str) -> list[Combatant]:
        """Find all combatants in a group."""
        return [c for c in self.combatants if c.group_id and c.group_id.lower() == group_name.lower()]

    def next_turn(self) -> Optional[Combatant]:
        """Advance to next turn. Returns the new current combatant."""
        if not self.combatants:
            return None

        self.combat_started = True

        # Tick conditions for current combatant at end of their turn
        if self.combatants:
            current = self.combatants[self.current_index]
            expired = current.tick_conditions()
            if expired:
                print(f"  Conditions expired on {current.name}: {', '.join(expired)}")

        self.current_index += 1
        if self.current_index >= len(self.combatants):
            self.current_index = 0
            self.round_number += 1
            print(f"\n=== ROUND {self.round_number} ===")

        return self.combatants[self.current_index] if self.combatants else None

    def prev_turn(self) -> Optional[Combatant]:
        """Go back to previous turn. Returns the new current combatant."""
        if not self.combatants:
            return None

        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.combatants) - 1
            self.round_number = max(1, self.round_number - 1)

        return self.combatants[self.current_index] if self.combatants else None

    def remove_combatant(self, name: str) -> bool:
        """Remove a combatant from combat. Returns True if found."""
        combatant = self.find_combatant(name)
        if combatant:
            idx = self.combatants.index(combatant)
            self.combatants.remove(combatant)
            if idx < self.current_index:
                self.current_index -= 1
            elif idx == self.current_index and self.current_index >= len(self.combatants):
                self.current_index = 0
            return True
        return False

    def clear(self):
        """Reset the tracker completely."""
        self.combatants = []
        self.current_index = 0
        self.round_number = 1
        self.combat_started = False
        self.group_counters = {}

    def get_status(self) -> str:
        """Get formatted status display."""
        if not self.combatants:
            return "No combatants in initiative."

        lines = []
        lines.append(f"\n{'='*60}")
        lines.append(f"  ROUND {self.round_number}")
        lines.append(f"{'='*60}")
        lines.append(f"{'':3} {'Init':>4} | {'Name':<20} | {'HP':<13} | AC")
        lines.append(f"{'-'*60}")

        for i, c in enumerate(self.combatants):
            is_current = (i == self.current_index and self.combat_started)
            lines.append(c.get_status_line(is_current))

        lines.append(f"{'='*60}\n")
        return '\n'.join(lines)

    def save(self, filename: str):
        """Save encounter state to file."""
        if not filename.endswith('.json'):
            filename += '.json'

        data = {
            "round_number": self.round_number,
            "current_index": self.current_index,
            "combat_started": self.combat_started,
            "group_counters": self.group_counters,
            "combatants": [c.to_dict() for c in self.combatants]
        }

        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load(self, filename: str) -> bool:
        """Load encounter state from file. Returns True if successful."""
        if not filename.endswith('.json'):
            filename += '.json'

        if not os.path.exists(filename):
            return False

        with open(filename, 'r') as f:
            data = json.load(f)

        self.round_number = data.get("round_number", 1)
        self.current_index = data.get("current_index", 0)
        self.combat_started = data.get("combat_started", False)
        self.group_counters = data.get("group_counters", {})
        self.combatants = [Combatant.from_dict(c) for c in data.get("combatants", [])]
        return True

    def show_condition_info(self, condition_name: str) -> str:
        """Get info about a specific condition."""
        cond_lower = condition_name.lower()
        if cond_lower in self.conditions_ref:
            cond = self.conditions_ref[cond_lower]
            lines = [f"\n{condition_name.upper()}:"]
            for effect in cond.get("effects", []):
                lines.append(f"  - {effect}")
            lines.append(f"  Common durations: {', '.join(cond.get('common_durations', []))}")
            return '\n'.join(lines)
        return f"Unknown condition: {condition_name}"


def print_help():
    """Print help message."""
    help_text = """
D&D 5e INITIATIVE TRACKER - COMMANDS
=====================================
ADDING COMBATANTS:
  add <name> <init> <hp> <ac> [count]  - Add combatant(s) with set initiative
  roll <name> <dex_mod> <hp> <ac> [count] - Roll initiative for combatant(s)

TURN MANAGEMENT:
  next, n           - Advance to next turn
  prev, p           - Go back to previous turn
  start             - Start combat (set to first combatant)

DAMAGE & HEALING:
  damage <name> <amount>, dmg, d      - Apply damage
  heal <name> <amount>, h             - Heal combatant
  kill <name>                         - Mark as dead
  revive <name>                       - Revive (set to 1 HP)

CONDITIONS:
  condition <name> <cond> [rounds]    - Add condition (no rounds = indefinite)
  cond <name> <cond> [rounds]         - Shorthand for condition
  uncondition <name> <cond>           - Remove condition
  uncond <name> <cond>                - Shorthand
  info <condition>                    - Show condition effects

MANAGEMENT:
  remove <name>, rm                   - Remove from combat
  set <name> init/hp/ac <value>       - Modify combatant stats
  status, s                           - Show current state
  clear                               - Reset tracker

FILE OPERATIONS:
  save <filename>                     - Save encounter
  load <filename>                     - Load encounter

OTHER:
  help, h, ?                          - Show this help
  quit, exit, q                       - Exit tracker

TIPS:
  - Names support partial matching (e.g., "gob" matches "Goblin 1")
  - Use count parameter to add multiple identical monsters
  - Conditions auto-decrement at end of each combatant's turn
"""
    print(help_text)


def parse_command(input_str: str) -> tuple[str, list[str]]:
    """Parse input into command and arguments."""
    parts = input_str.strip().split()
    if not parts:
        return "", []
    return parts[0].lower(), parts[1:]


def main():
    """Main interactive loop."""
    tracker = InitiativeTracker()
    print("\nD&D 5e Initiative Tracker")
    print("Type 'help' for commands.\n")

    while True:
        try:
            user_input = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        cmd, args = parse_command(user_input)

        # Help
        if cmd in ("help", "h", "?"):
            print_help()

        # Quit
        elif cmd in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        # Add combatant
        elif cmd == "add":
            if len(args) < 4:
                print("Usage: add <name> <init> <hp> <ac> [count]")
                continue
            try:
                name = args[0]
                init = int(args[1])
                hp = int(args[2])
                ac = int(args[3])
                count = int(args[4]) if len(args) > 4 else 1
                added = tracker.add_combatant(name, init, hp, ac, count=count)
                print(f"Added: {', '.join(added)}")
            except ValueError:
                print("Invalid numbers. Usage: add <name> <init> <hp> <ac> [count]")

        # Roll initiative
        elif cmd == "roll":
            if len(args) < 4:
                print("Usage: roll <name> <dex_mod> <hp> <ac> [count]")
                continue
            try:
                name = args[0]
                dex_mod = int(args[1])
                hp = int(args[2])
                ac = int(args[3])
                count = int(args[4]) if len(args) > 4 else 1
                results = tracker.roll_initiative(name, dex_mod, count, hp, ac)
                for rname, roll in results:
                    print(f"  {rname}: {roll} (1d20{dex_mod:+d})")
            except ValueError:
                print("Invalid numbers. Usage: roll <name> <dex_mod> <hp> <ac> [count]")

        # Next turn
        elif cmd in ("next", "n"):
            current = tracker.next_turn()
            if current:
                print(f"\n>>> {current.name}'s turn <<<")
                print(tracker.get_status())
            else:
                print("No combatants in initiative.")

        # Previous turn
        elif cmd in ("prev", "p"):
            current = tracker.prev_turn()
            if current:
                print(f"\n>>> {current.name}'s turn <<<")
                print(tracker.get_status())
            else:
                print("No combatants in initiative.")

        # Start combat
        elif cmd == "start":
            if tracker.combatants:
                tracker.combat_started = True
                tracker.current_index = 0
                current = tracker.combatants[0]
                print(f"\n=== COMBAT BEGINS - ROUND 1 ===")
                print(f">>> {current.name}'s turn <<<")
                print(tracker.get_status())
            else:
                print("No combatants to start combat with.")

        # Damage
        elif cmd in ("damage", "dmg", "d"):
            if len(args) < 2:
                print("Usage: damage <name> <amount>")
                continue
            try:
                name = args[0]
                amount = int(args[1])
                combatant = tracker.find_combatant(name)
                if combatant:
                    actual = combatant.apply_damage(amount)
                    print(f"{combatant.name} takes {actual} damage. HP: {combatant.hp}/{combatant.max_hp}")
                    if combatant.is_unconscious:
                        print(f"  {combatant.name} falls unconscious!")
                else:
                    print(f"Combatant '{name}' not found.")
            except ValueError:
                print("Invalid damage amount.")

        # Heal
        elif cmd in ("heal", "h"):
            if len(args) < 2:
                print("Usage: heal <name> <amount>")
                continue
            try:
                name = args[0]
                amount = int(args[1])
                combatant = tracker.find_combatant(name)
                if combatant:
                    actual = combatant.apply_healing(amount)
                    print(f"{combatant.name} heals {actual} HP. HP: {combatant.hp}/{combatant.max_hp}")
                else:
                    print(f"Combatant '{name}' not found.")
            except ValueError:
                print("Invalid heal amount.")

        # Kill
        elif cmd == "kill":
            if len(args) < 1:
                print("Usage: kill <name>")
                continue
            combatant = tracker.find_combatant(args[0])
            if combatant:
                combatant.is_dead = True
                combatant.is_unconscious = False
                combatant.hp = 0
                print(f"{combatant.name} is dead.")
            else:
                print(f"Combatant '{args[0]}' not found.")

        # Revive
        elif cmd == "revive":
            if len(args) < 1:
                print("Usage: revive <name>")
                continue
            combatant = tracker.find_combatant(args[0])
            if combatant:
                combatant.is_dead = False
                combatant.is_unconscious = False
                if combatant.hp == 0:
                    combatant.hp = 1
                print(f"{combatant.name} is revived. HP: {combatant.hp}/{combatant.max_hp}")
            else:
                print(f"Combatant '{args[0]}' not found.")

        # Add condition
        elif cmd in ("condition", "cond"):
            if len(args) < 2:
                print("Usage: condition <name> <condition> [rounds]")
                continue
            name = args[0]
            condition = args[1]
            rounds = int(args[2]) if len(args) > 2 else None
            combatant = tracker.find_combatant(name)
            if combatant:
                combatant.add_condition(condition, rounds)
                duration = f"for {rounds} rounds" if rounds else "indefinitely"
                print(f"{combatant.name} is now {condition} {duration}.")
            else:
                print(f"Combatant '{name}' not found.")

        # Remove condition
        elif cmd in ("uncondition", "uncond"):
            if len(args) < 2:
                print("Usage: uncondition <name> <condition>")
                continue
            name = args[0]
            condition = args[1]
            combatant = tracker.find_combatant(name)
            if combatant:
                if combatant.remove_condition(condition):
                    print(f"Removed {condition} from {combatant.name}.")
                else:
                    print(f"{combatant.name} doesn't have {condition}.")
            else:
                print(f"Combatant '{name}' not found.")

        # Condition info
        elif cmd == "info":
            if len(args) < 1:
                print("Usage: info <condition>")
                continue
            print(tracker.show_condition_info(args[0]))

        # Remove combatant
        elif cmd in ("remove", "rm"):
            if len(args) < 1:
                print("Usage: remove <name>")
                continue
            if tracker.remove_combatant(args[0]):
                print(f"Removed '{args[0]}' from combat.")
            else:
                print(f"Combatant '{args[0]}' not found.")

        # Set stat
        elif cmd == "set":
            if len(args) < 3:
                print("Usage: set <name> <init|hp|ac|maxhp> <value>")
                continue
            name = args[0]
            stat = args[1].lower()
            try:
                value = int(args[2])
                combatant = tracker.find_combatant(name)
                if combatant:
                    if stat == "init":
                        combatant.initiative = value
                        tracker._sort_combatants()
                    elif stat == "hp":
                        combatant.hp = min(value, combatant.max_hp)
                        combatant.is_unconscious = combatant.hp <= 0
                    elif stat == "maxhp":
                        combatant.max_hp = value
                        combatant.hp = min(combatant.hp, value)
                    elif stat == "ac":
                        combatant.ac = value
                    else:
                        print(f"Unknown stat: {stat}")
                        continue
                    print(f"Set {combatant.name}'s {stat} to {value}.")
                else:
                    print(f"Combatant '{name}' not found.")
            except ValueError:
                print("Invalid value.")

        # Status
        elif cmd in ("status", "s"):
            print(tracker.get_status())

        # Clear
        elif cmd == "clear":
            tracker.clear()
            print("Tracker cleared.")

        # Save
        elif cmd == "save":
            if len(args) < 1:
                print("Usage: save <filename>")
                continue
            tracker.save(args[0])
            print(f"Saved to {args[0]}.json")

        # Load
        elif cmd == "load":
            if len(args) < 1:
                print("Usage: load <filename>")
                continue
            if tracker.load(args[0]):
                print(f"Loaded {args[0]}")
                print(tracker.get_status())
            else:
                print(f"File not found: {args[0]}")

        else:
            print(f"Unknown command: {cmd}. Type 'help' for commands.")


if __name__ == "__main__":
    main()
