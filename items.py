## FUNCTION
import my_func

ITEMS = {
    "Health Potion":  {"type": "heal",    "value": 40,  "rarity": "common",    "one_use": True},
    "Iron Shield":    {"type": "defense", "value": 6,   "rarity": "common",    "one_use": False},
    "Spell Tome":     {"type": "attack",  "value": 10,  "rarity": "rare",      "one_use": False},
    "Elixir of Rage": {"type": "attack",  "value": 20,  "rarity": "epic",      "one_use": True},
    "Dragon Crown":   {"type": "special", "value": 0,   "rarity": "legendary", "one_use": False},
    "Antidote":       {"type": "cure",    "value": 0,   "rarity": "common",    "one_use": True},
}

# Add an item from the items dict
def add_item(hero: dict, item_name: str) -> None:
    try:
        if item_name in ITEMS.keys():
            hero["inventory"].append((item_name, ITEMS[item_name]))
            print(my_func.green(f"{item_name} has been added to your inventory."))
            #print(hero["inventory"])
    except ValueError:
        print(my_func.red(f"{item_name} does not exist").upper())

def use_item1(hero: dict, item_name: str) -> None:
    if item_name not in ITEMS.keys():
        raise ValueError
    try:
        if item_name in hero["inventory"]:
            #remove if one_use
            if hero["inventory"][item_name]["one_use"] is True:
                hero["inventory"].remove(item_name)
                print(my_func.red(f"{item_name} has been removed from your inventory."))
            print(my_func.blue(f"{item_name} has been used."))
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
                print(my_func.green(f"You gained {item_value} attack points"))
            #defense
            if hero["inventory"][item_name]["type"] == "defense":
                hero["defense"] += item_value
                print(my_func.green(f"You gained {item_value} defense points"))
            #cure
            if hero["inventory"][item_name]["type"] == "cure":
                if hero["buffs"].contains("POISONED"):
                    hero["buffs"].remove("POISONED")
                    print(my_func.blue("You are not longer poisoned"))
                print("You are cured from poison")
            #special
            if hero["inventory"][item_name]["type"] == "special":
                if not hero["buffs"].contains("DRAGON_CROWNED"):
                    hero["buffs"].add("DRAGON_CROWNED")
                    print(my_func.blue("You gained the buff Dragon Crowned."))
                else:
                    print(my_func.red("You already have that buff"))
        else:
            print(my_func.red(f"{item_name } not in inventory"))
    except ValueError:
        print(my_func.red(f"{item_name} does not exist").upper())

def check_item(hero: dict, item_name: str):

    # find item in inventory
    inventory_item = None

    for name, data in hero["inventory"]:
        if name == item_name:
            inventory_item = (name, data)
            break

    # item not found
    if inventory_item is None:
        print(my_func.red(f"{item_name} not in inventory"))

    return inventory_item

# Use an item from the hero inventory
def use_item(hero: dict, item_name: str) -> None:

    inventory_item = check_item(hero, item_name)

    name, item = inventory_item
    item_value = item["value"]
    print(my_func.blue(f"{item_name} has been used."))

    # HEAL
    if item["type"] == "heal":
        hero["hp"] = min(hero["hp"] + item_value, hero["max_hp"])
        #hero["hp"] += item_value
        #if hero["hp"] > hero["max_hp"]:
            #hero["hp"] = hero["max_hp"]

        print(my_func.green(f"You recovered {item_value} HP."))

    # ATTACK
    if item["type"] == "attack":
        hero["attack"] += item_value
        print(my_func.green(f"You gained {item_value} attack points."))

    # DEFENSE
    if item["type"] == "defense":
        hero["defense"] += item_value
        print(my_func.green(f"You gained {item_value} defense points."))

    # CURE
    if item["type"] == "cure":
        if "POISONED" in hero["buffs"]:
            hero["buffs"].remove("POISONED")
            print(my_func.blue("You are no longer poisoned."))
        else:
            print(my_func.red("You are not poisoned."))

    # SPECIAL
    if item["type"] == "special":
        if "DRAGON_CROWNED" not in hero["buffs"]:
            hero["buffs"].add("DRAGON_CROWNED")
            print(my_func.blue("You gained the buff Dragon Crowned."))
        else:
            print(my_func.red("You already have that buff."))

    # remove if consumable
    if item["one_use"]:
        hero["inventory"].remove(inventory_item)
        print(my_func.red(f"{item_name} has been removed from your inventory."))

def get_rare_items(hero: dict) -> list:
    rare_list = []

    for name, item in hero["inventory"]:
        if item["rarity"] == "rare" or item["rarity"] == "epic" or item["rarity"] == "legendary":
            rare_list.append(name)
    if not rare_list:
        print(my_func.red(f"You don't have any rare items."))
    else:
        print(f"You have {len(rare_list)} rare items.")
        print(f"{rare_list}")
    return rare_list

def show_inventory(hero: dict) -> None:
    legendary, epic, rare, common = "", "", "",""

    for name, item in hero["inventory"]:
        rarity = item["rarity"]
        if rarity == "legendary":
            if not legendary:
                legendary = f"{name}"
            else:
                legendary += f", {name}"
        if rarity == "epic":
            if not epic:
                epic = f"{name}"
            else:
                epic += f", {name}"
        if rarity == "rare":
            if not rare:
                rare = f"{name}"
            else:
                rare += f", {name}"
        if rarity == "common":
            if not common:
                common = f"{name}"
            else:
                common += f", {name}"
    if legendary or epic or rare or common:
        print(my_func.blue("💰==INVENTORY==💰"))
    if legendary:
        print(f"Legendary: {legendary}")
    if epic:
        print(f"Epic: {epic}")
    if rare:
        print(f"Rare: {rare}")
    if common:
        print(f"Common: {common}")