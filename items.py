## FUNCTION

ITEMS = {
    "Health Potion":  {"type": "heal",    "value": 40,  "rarity": "common",    "one_use": True},
    "Iron Shield":    {"type": "defense", "value": 6,   "rarity": "common",    "one_use": False},
    "Spell Tome":     {"type": "attack",  "value": 10,  "rarity": "rare",      "one_use": False},
    "Elixir of Rage": {"type": "attack",  "value": 20,  "rarity": "epic",      "one_use": True},
    "Dragon Crown":   {"type": "special", "value": 0,   "rarity": "legendary", "one_use": False},
    "Antidote":       {"type": "cure",    "value": 0,   "rarity": "common",    "one_use": True},
}

def add_item(hero: dict, item_name: str) -> None:
    try:
        if item_name in ITEMS.keys():
            hero["inventory"].append((item_name, ITEMS[item_name]))
            print(f"{item_name} has been added to your inventory.")
            print(hero["inventory"])
    except ValueError:
        print(f"{item_name} does not exist")

def use_item(hero: dict, item_name: str) -> None:
    if item_name not in ITEMS.keys():
        raise ValueError
    try:
        if item_name in hero["inventory"]:
            #remove if one_use
            if hero["inventory"][item_name]["one_use"] is True:
                hero["inventory"].remove(item_name)
                print(f"{item_name} has been removed from your inventory.")
            print(f"{item_name} has been used.")
            item_value = hero["inventory"][item_name]["value"]
            #healing - hp
            if hero["inventory"][item_name]["type"] == "heal":
                if hero["hp"]+ item_value >= hero["max_hp"]:
                    hero["hp"] = hero["max_hp"]
                else:
                    hero["hp"] += item_value
            #attack
            if hero["inventory"][item_name]["type"] == "attack":
                hero["attack"] += item_value
                print(f"You gained {item_value} attack points")
            #defense
            if hero["inventory"][item_name]["type"] == "defense":
                hero["defense"] += item_value
                print(f"You gained {item_value} defense points")
            #cure
            if hero["inventory"][item_name]["type"] == "cure":
                if hero["buffs"].contains("POISONED"):
                    hero["buffs"].remove("POISONED")
                    print("You are not longer poisoned")
                print("You are cured from poison")
            #special
            if hero["inventory"][item_name]["type"] == "special":
                if not hero["buffs"].contains("DRAGON_CROWNED"):
                    hero["buffs"].add("DRAGON_CROWNED")
                    print(f"You gained the buff Dragon Crowned.")
                else:
                    print("You already have that buff")
        else:
            print(f"{item_name}")
            print("not in inventory")
    except ValueError:
        print(f"{item_name} does not exist")