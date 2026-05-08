# ⚔️ Dragon's Dungeon 🐉 Python Recap Exercise

> *The ancient dragon **PYTHONUS** has awakened. Its hoard of corrupted data structures and spaghetti code poisons all it touches. You are the last Code Knight standing. Navigate the dungeon, survive multi-phase boss fights, and restore order to the realm, one clean function at a time.*

---

## 🎯 Objective

Build a **turn-based dungeon crawler** running in the terminal. The project is intentionally close to a small real-world codebase: multiple modules, non-trivial state management, clear separation of concerns, and edge cases to handle.

---

## 👥 Team

Solo or **pair (2 max)**. If working as a pair, the Git bonus is essentially mandatory, you'll need branching just to avoid stepping on each other's code.

---

## 🗂️ Project Structure

```
dragons_dungeon/
│
├── main.py           # Entry point : game loop, user input
├── hero.py           # Hero creation, leveling, stat management
├── combat.py         # Combat engine : turn resolution, damage calc
├── dungeon.py        # Dungeon layout, room traversal, events
├── items.py          # Item registry, inventory operations
├── logger.py         # Action log : tracks everything that happens
└── README.md
```

Each file is a module. `main.py` is the **only** entry point. All others use the `if __name__ == "__main__":` guard.

---

## 🧩 Detailed Specifications

---

### Module 1 : `hero.py`

#### `create_hero(name: str) -> dict`

Returns the hero's full state as a dictionary:

```python
{
    "name": str,
    "hp": int,              # current HP
    "max_hp": int,          # 100 at start
    "attack": int,          # 15 at start
    "defense": int,         # 5 at start
    "level": int,           # starts at 1
    "xp": int,              # starts at 0
    "inventory": [],        # list of item name strings
    "buffs": set(),         # set of active passive buff names — no duplicates
    "position": (0, 0),     # tuple — (floor, room_index), immutable coordinates
    "visited_rooms": set(), # set of room id tuples already explored
    "kills": 0,
}
```

#### `gain_xp(hero: dict, amount: int) -> bool`

Adds XP to the hero. Returns `True` if the hero **leveled up**, `False` otherwise.

Level-up threshold: `level * 40` XP needed to reach the next level.
On level-up: `max_hp += 15`, `attack += 3`, `defense += 1`, reset `xp` to 0, increment `level`.

#### `display_hero(hero: dict) -> None`

Prints a formatted stat block using f-strings. Must include a visual HP bar:

```
╔══════════════════════════════╗
║  ⚔  Sir Aldric  — Lv. 3     ║
║  HP  [████████░░░░]  72/100  ║
║  ATK 21  |  DEF 7  |  XP 15 ║
║  Buffs: SHIELD_AURA          ║
╚══════════════════════════════╝
```

Build the HP bar using string multiplication: `"█" * filled + "░" * empty`.

#### `get_stat_triplet(hero: dict) -> tuple`

Returns `(hp, attack, defense)` as an immutable tuple — useful for snapshotting state before a fight.

---

### Module 2 : `items.py`

#### Item registry

```python
ITEMS = {
    "Health Potion":  {"type": "heal",    "value": 40,  "rarity": "common",    "one_use": True},
    "Iron Shield":    {"type": "defense", "value": 6,   "rarity": "common",    "one_use": False},
    "Spell Tome":     {"type": "attack",  "value": 10,  "rarity": "rare",      "one_use": False},
... (349 lines left)

README.md
16 KB
﻿

# ⚔️ Dragon's Dungeon 🐉 Python Recap Exercise

> *The ancient dragon **PYTHONUS** has awakened. Its hoard of corrupted data structures and spaghetti code poisons all it touches. You are the last Code Knight standing. Navigate the dungeon, survive multi-phase boss fights, and restore order to the realm, one clean function at a time.*

---

## 🎯 Objective

Build a **turn-based dungeon crawler** running in the terminal. The project is intentionally close to a small real-world codebase: multiple modules, non-trivial state management, clear separation of concerns, and edge cases to handle.

---

## 👥 Team

Solo or **pair (2 max)**. If working as a pair, the Git bonus is essentially mandatory, you'll need branching just to avoid stepping on each other's code.

---

## 🗂️ Project Structure

```
dragons_dungeon/
│
├── main.py           # Entry point : game loop, user input
├── hero.py           # Hero creation, leveling, stat management
├── combat.py         # Combat engine : turn resolution, damage calc
├── dungeon.py        # Dungeon layout, room traversal, events
├── items.py          # Item registry, inventory operations
├── logger.py         # Action log : tracks everything that happens
└── README.md
```

Each file is a module. `main.py` is the **only** entry point. All others use the `if __name__ == "__main__":` guard.

---

## 🧩 Detailed Specifications

---

### Module 1 : `hero.py`

#### `create_hero(name: str) -> dict`

Returns the hero's full state as a dictionary:

```python
{
    "name": str,
    "hp": int,              # current HP
    "max_hp": int,          # 100 at start
    "attack": int,          # 15 at start
    "defense": int,         # 5 at start
    "level": int,           # starts at 1
    "xp": int,              # starts at 0
    "inventory": [],        # list of item name strings
    "buffs": set(),         # set of active passive buff names — no duplicates
    "position": (0, 0),     # tuple — (floor, room_index), immutable coordinates
    "visited_rooms": set(), # set of room id tuples already explored
    "kills": 0,
}
```

#### `gain_xp(hero: dict, amount: int) -> bool`

Adds XP to the hero. Returns `True` if the hero **leveled up**, `False` otherwise.

Level-up threshold: `level * 40` XP needed to reach the next level.
On level-up: `max_hp += 15`, `attack += 3`, `defense += 1`, reset `xp` to 0, increment `level`.

#### `display_hero(hero: dict) -> None`

Prints a formatted stat block using f-strings. Must include a visual HP bar:

```
╔══════════════════════════════╗
║  ⚔  Sir Aldric  — Lv. 3     ║
║  HP  [████████░░░░]  72/100  ║
║  ATK 21  |  DEF 7  |  XP 15 ║
║  Buffs: SHIELD_AURA          ║
╚══════════════════════════════╝
```

Build the HP bar using string multiplication: `"█" * filled + "░" * empty`.

#### `get_stat_triplet(hero: dict) -> tuple`

Returns `(hp, attack, defense)` as an immutable tuple — useful for snapshotting state before a fight.

---

### Module 2 : `items.py`

#### Item registry

```python
ITEMS = {
    "Health Potion":  {"type": "heal",    "value": 40,  "rarity": "common",    "one_use": True},
    "Iron Shield":    {"type": "defense", "value": 6,   "rarity": "common",    "one_use": False},
    "Spell Tome":     {"type": "attack",  "value": 10,  "rarity": "rare",      "one_use": False},
    "Elixir of Rage": {"type": "attack",  "value": 20,  "rarity": "epic",      "one_use": True},
    "Dragon Crown":   {"type": "special", "value": 0,   "rarity": "legendary", "one_use": False},
    "Antidote":       {"type": "cure",    "value": 0,   "rarity": "common",    "one_use": True},
}
```

Permanent items (`one_use: False`) modify the hero's base stats and stay in inventory as a record.
Consumable items (`one_use: True`) are removed after use.

#### `add_item(hero: dict, item_name: str) -> None`
Appends the item name to `hero["inventory"]`. Raises `ValueError` if the item doesn't exist in `ITEMS`.

#### `use_item(hero: dict, item_name: str) -> str`
Applies the item effect to the hero dict. Removes it if `one_use`. Returns a descriptive string (passed to the logger). Raises `ValueError` if item is not in inventory.

Apply effects as follows:
- `"heal"` → `hero["hp"] = min(hero["hp"] + value, hero["max_hp"])`
- `"defense"` → `hero["defense"] += value`
- `"attack"` → `hero["attack"] += value`
- `"cure"` → remove `"POISONED"` from `hero["buffs"]`
- `"special"` → add `"DRAGON_CROWNED"` to `hero["buffs"]`

#### `get_rare_items(hero: dict) -> list`
Returns a **list comprehension** of item names in the hero's inventory whose rarity is `"rare"`, `"epic"`, or `"legendary"`. Must be a one-liner.

#### `show_inventory(hero: dict) -> None`
Prints inventory grouped by rarity. Use a **dict comprehension** to build the grouping:

```python
grouped = {rarity: [item for item in hero["inventory"] if ITEMS[item]["rarity"] == rarity]
           for rarity in {ITEMS[i]["rarity"] for i in hero["inventory"]}}
```

Then print each group.

---

### Module 3 : `logger.py`

The logger is a **stateful module** — it holds a global list and a turn counter at module level.

```python
_log: list = []
_turn: int = 0
```

#### `log(message: str) -> None`
Increments `_turn`, appends `f"[T+{_turn}] {message}"` to `_log`.

#### `get_log() -> list`
Returns `_log`.

#### `print_last(n: int = 5) -> None`
Prints the last `n` entries.

#### `export_log(filename: str) -> None`
Writes each log entry to `filename`, one per line.

> **Hard constraint:** `logger.py` must **never** import from any other game module. Circular imports will crash your program at load time and are a common real-world pitfall.

---

### Module 4 : `combat.py`

Import from `hero.py`, `items.py`, `logger.py`, and `copy`.

#### Enemy definitions

```python
ENEMIES = {
    "Giant Spider": {
        "name": "Giant Spider",
        "hp": 55, "max_hp": 55, "attack": 10, "defense": 2,
        "xp_reward": 30, "loot": "Antidote",
        "phases": 1, "current_phase": 0,
    },
    "Skeleton Mage": {
        "name": "Skeleton Mage",
        "hp": 80, "max_hp": 80, "attack": 16, "defense": 4,
        "xp_reward": 50, "loot": "Spell Tome",
        "phases": 1, "current_phase": 0,
    },
    "PYTHONUS": {
        "name": "PYTHONUS",
        "hp": 200, "max_hp": 200, "attack": 25, "defense": 8,
        "xp_reward": 150, "loot": "Dragon Crown",
        "phases": 3, "current_phase": 0,
        "phase_thresholds": [0.66, 0.33],
        "phase_messages": [
            "💀 PYTHONUS roars - its scales harden!  DEF +6",
            "🔥 PYTHONUS is ENRAGED - claws glow red!  ATK +10",
        ],
        "phase_buffs": [
            {"defense": 6},
            {"attack": 10},
        ],
    },
}
```

#### `calculate_damage(attacker_attack: int, defender_defense: int) -> int`

```python
damage = max(1, attacker_attack - defender_defense + random.randint(-3, 3))
return damage
```

#### `resolve_turn(hero: dict, enemy: dict) -> tuple`

Simulates one full combat turn:
1. Hero attacks enemy → apply damage, log it
2. If enemy HP > 0: enemy attacks hero → apply damage, log it
3. Returns `(hero_alive: bool, enemy_alive: bool)`

#### `check_phase_transition(enemy: dict) -> None`

After each turn, check if `enemy["hp"] / enemy["max_hp"]` has dropped below the next phase threshold. If so: apply the corresponding buff dict to `enemy`, print and log the phase message, increment `enemy["current_phase"]`. Only applies to enemies with `phases > 1`.

#### `fight(hero: dict, enemy_name: str) -> bool`

1. `enemy = copy.deepcopy(ENEMIES[enemy_name])` — **never mutate the global dict**
2. Print fight intro
3. Loop each turn:
   - Print a mini status: `Hero HP: X  |  Enemy HP: Y`
   - Prompt: `[A]ttack  [U]se item  [R]un`
   - `A` → `resolve_turn`, then `check_phase_transition`
   - `U` → show inventory, ask which item, call `use_item`, then enemy attacks once (no hero attack this turn)
   - `R` → log the retreat, return `False`
4. If hero wins: call `gain_xp`, add loot to inventory, return `True`
5. If hero dies: return `False`

---

### Module 5 : `dungeon.py`

#### Dungeon data

```python
DUNGEON = [
    # Floor 0
    [
        {"id": (0, 0), "name": "Collapsed Entrance",  "enemy": None,            "loot": "Health Potion", "event": "trap"},
        {"id": (0, 1), "name": "Spider Nest",          "enemy": "Giant Spider",  "loot": None,            "event": None},
        {"id": (0, 2), "name": "Cursed Armory",        "enemy": None,            "loot": "Iron Shield",   "event": None},
    ],
    # Floor 1
    [
        {"id": (1, 0), "name": "Hall of Whispers",     "enemy": "Skeleton Mage", "loot": None,            "event": "riddle"},
        {"id": (1, 1), "name": "Dragon's Antechamber", "enemy": None,            "loot": "Elixir of Rage","event": None},
        {"id": (1, 2), "name": "The Sanctum — FINAL",  "enemy": "PYTHONUS",      "loot": "Dragon Crown",  "event": None},
    ],
]
```

Room `id` is a **tuple** `(floor, room_index)`.

#### `get_room(dungeon: list, position: tuple) -> dict | None`
Returns the room at `position`, or `None` if not found.

#### `handle_event(hero: dict, event: str) -> None`

- `"trap"` → deal 10 damage, add `"TRAP_TRIGGERED"` to `hero["buffs"]`, log it
- `"riddle"` → print a hardcoded Python question. Correct answer: `gain_xp(hero, 20)`. Wrong: deal 15 damage. Log the result.

Example riddle:
```
❓ What does this return?
   s = {1, 2, 2, 3}
   len(s)
> Your answer: _
```

#### `explore(hero: dict, dungeon: list) -> None`

Iterates through all rooms in order:
1. Print a floor separator when the floor changes
2. Update `hero["position"]` (a tuple) and add it to `hero["visited_rooms"]` (a set)
3. Print room name and coordinates
4. Call `handle_event` if applicable
5. If enemy: call `fight`
   - If `fight` returns `False`: print game over, log it, `return`
6. Award loot if any, call `display_hero`
7. After all rooms: print victory screen

---

### `main.py`

```python
from hero import create_hero, display_hero
from dungeon import explore, DUNGEON
from logger import export_log

if __name__ == "__main__":
    name = input("Enter your hero's name, Code Knight: ").strip() or "Anonymous"
    hero = create_hero(name)
    display_hero(hero)
    input("\nPress Enter to descend into the dungeon...")
    explore(hero, DUNGEON)
    export_log("run_log.txt")
    print("\nYour adventure has been saved to run_log.txt")
```

`main.py` stays thin. **No game logic here.**

---

## ✅ Requirements Checklist

| # | Requirement                                                              |
|---|--------------------------------------------------------------------------|
| 1 | All 5 modules exist, importable, have `__name__` guards                  |
| 2 | No circular imports, `logger` never imports from the project             |
| 3 | `create_hero` returns the exact structure (set, tuple, list all present) |
| 4 | Level-up logic uses the `level * 40` threshold formula                   |
| 5 | HP bar uses string multiplication and renders dynamically                |
| 6 | `get_rare_items` is a one-liner list comprehension                       |
| 7 | `show_inventory` uses a dict comprehension for grouping                  |
| 8 | Logger state is module-level, not passed around as a parameter           |
| 9 | `fight` deep-copies the enemy, global `ENEMIES` is never mutated         |
| 10 | PYTHONUS has 3 phases; transitions apply stat buffs and are logged       |
| 11 | `[R]un` option works, hero survives but the room is considered failed    |
| 12 | Room ids are tuples; `visited_rooms` is a set of tuples                  |
| 13 | Riddle event is implemented and affects hero state                       |
| 14 | `export_log` writes a `.txt` file on disk                                |
| 15 | `main.py` contains no game logic                                         |

---

## 🏆 Bonus 1 - Git Workflow

### Setup
One person creates the repo with `main` and `develop` branches. The other is added as collaborator. **Nobody ever commits directly to `main`.**

### One branch per module
```
feature/hero
feature/items
feature/logger
feature/combat
feature/dungeon
feature/game-loop
```

### Pull Request rules
- Every branch merges into `develop` via a PR
- The partner reviews and approves before merge
- At least one meaningful review comment per PR (not just "ok")

### Commit convention
```
feat: add gain_xp() with level-up threshold logic
fix: prevent negative damage in calculate_damage
refactor: extract HP bar rendering to a helper
docs: add docstrings to all combat functions
test: manually verify PYTHONUS phase 2 transition
```

### Delivery
The final `main` branch must be clean and runnable.

---

## 🔥 Bonus 2 - Loot Optimizer (Algorithm + Complexity Analysis)

> *Before descending, the Code Knight visits the dungeon shop. The carry limit is strict. Choose wisely.*

### Context

You have a **carrying capacity of W = 50 weight units**. Each item has a weight and a power value. Your goal: maximize total power without exceeding W.

This is the **0/1 Knapsack problem**, a classic dynamic programming exercise and a staple of technical interviews.

### Shop inventory

```python
SHOP = [
    # (name,                weight, power)
    ("Health Potion",           5,    10),
    ("Iron Shield",            12,    25),
    ("Spell Tome",             10,    30),
    ("Elixir of Rage",          8,    40),
    ("Shadow Cloak",           15,    35),
    ("Boots of Swiftness",      7,    20),
    ("Enchanted Blade",        20,    60),
    ("Ring of Vitality",        3,    15),
]
```

### What to implement

Create a new file `optimizer.py`.

#### `knapsack(items: list, capacity: int) -> tuple`

Solve the problem using **bottom-up dynamic programming**.

Build a 2D list `dp` where `dp[i][w]` is the maximum power achievable using the first `i` items with a weight limit of `w`:

```
For each item i (1 to n):
    For each capacity w (0 to W):
        if item[i].weight > w:
            dp[i][w] = dp[i-1][w]              # can't take this item
        else:
            dp[i][w] = max(
                dp[i-1][w],                     # skip the item
                dp[i-1][w - weight] + power     # take the item
            )
```

Then **backtrack** through the table to recover which items were chosen.

Returns `(total_power: int, chosen_items: list[str])`.

#### `display_loadout(chosen: list, total_power: int) -> None`
Prints the chosen items and total power cleanly.

### Required complexity analysis

Add this comment block to `optimizer.py`, you must fill in all four answers:

```python
# === COMPLEXITY ANALYSIS ===
#
# Time complexity:  O(?)
#   Justify in your own words:
#
# Space complexity: O(?)
#   Justify in your own words:
#   Can you reduce it to O(W) instead of O(n*W)? How, and what do you lose?
#
# Why a greedy approach fails for 0/1 knapsack:
#   A greedy strategy (e.g. always pick the highest power/weight ratio)
#   does NOT always give the optimal answer here.
#   Give a concrete counter-example using items from SHOP above.
#
# Why O(n * W) is called pseudo-polynomial:
#   (Hint: W is a numeric value. What is the actual size of W as input in bits?)
```

### Integration

Call `knapsack(SHOP, 50)` at the start of `main.py`, print the chosen loadout, and add the chosen items to the hero's starting inventory before the dungeon begins.

---

*PYTHONUS awaits. May your commits be atomic, your functions pure, and your Big O be humble.*

README.md
16 KB
