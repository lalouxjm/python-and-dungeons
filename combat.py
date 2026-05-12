import copy
import random

import my_func
from hero import gain_xp
from items import add_item

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

def calculate_damage(attacker_attack: int, defender_defense: int) -> int:
    damage = max(1, attacker_attack - defender_defense + random.randint(-3, 3))
    return damage

def resolve_turn(hero: dict, enemy: dict) -> tuple:
    h_atk, h_def, e_atk, e_def = hero["attack"], hero["defense"], enemy["attack"], enemy["defense"]
    h_dmg, e_dmg = calculate_damage(h_atk, e_def), calculate_damage(e_atk, h_def)

    #hero's turn
    enemy["hp"] -= h_dmg
    print(my_func.green(f"{hero["name"]} deals {h_dmg} damage(s) to {enemy["name"]}."))
    #mini_status(hero, enemy)

    if enemy["hp"] > 0:
        hero["hp"] -= e_dmg
        print(my_func.red(f"{enemy["name"]} deals {e_dmg} damage(s) to {hero["name"]}."))
        if hero["hp"] <= 0:
            print(my_func.red("💀 You died! 💀"))
    else:
        enemy["hp"] = 0
        print(my_func.green(f"💀 {enemy["name"]} has been defeated!"))
        gain_xp(hero, enemy["xp_reward"])
        loot_item(hero, enemy)

    return hero, enemy

def loot_item(hero, enemy):
    print(f"You looted {enemy['name']} and received {enemy['loot']}.")
    add_item(hero, enemy["loot"])

def mini_status(hero, enemy):
    print(my_func.blue("Fight Status:"),
          my_func.green(f"{hero["name"]} - 💚 {hero["hp"]}/{hero["max_hp"]}hp"), " --- ",
          my_func.red(f"{enemy["name"]} - ❤️ {enemy["hp"]}/{enemy["max_hp"]}hp"))

def fight(hero: dict, enemy_name: str) -> bool:
    enemy = copy.deepcopy(ENEMIES[enemy_name])
    ran_away = False
    print(my_func.blue("⚔️==FIGHT==⚔️"))

    print(f"{enemy["name"]} has entered the fight")

    while True:
        #display oneliner with hero and enemy health
        mini_status(hero, enemy)

        #if someone is dead, the fight is over
        if hero["hp"] <= 0 or enemy["hp"] <= 0:
            break

        player_choice = input("[A]ttack - [U]se item - [R]un")

        match player_choice:
            #Attack the enemy
            case p if p.lower() == "a":
                hero, enemy = resolve_turn(hero, enemy)
            #Use an item from your inventory
            case p if p.lower() == "u":
                print("use items")
            #Run Away from the combat
            case p if p.lower() == "r":
                if my_func.random_func(75):
                    print(my_func.blue("You successfully ran away!"))
                    ran_away = True
                else:
                    print(my_func.red("You failed to run away!"))



        if ran_away:
            break
    return True