from combat import fight
from hero import create_hero, gain_xp, display_hero
from items import add_item, use_item, get_rare_items, show_inventory


## FUNCTION
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


## MAIN
if __name__ == '__main__':

    print("create hero")
    my_hero = create_hero("Sir JMi")
    display_hero(my_hero)

    gain_xp(my_hero, 30)
    display_hero(my_hero)

    gain_xp(my_hero, 45)
    display_hero(my_hero)

    add_item(my_hero, "Spell Tome")
    add_item(my_hero, "Elixir of Rage")
    add_item(my_hero, "Dragon Crown")
    show_inventory(my_hero)
    get_rare_items(my_hero)

    use_item(my_hero, "Dragon Crown")
    display_hero(my_hero)

    use_item(my_hero, "Spell Tome")
    display_hero(my_hero)

    use_item(my_hero, "Elixir of Rage")
    display_hero(my_hero)
    show_inventory(my_hero)


    add_item(my_hero, "Health Potion")
    add_item(my_hero, "Iron Shield")
    show_inventory(my_hero)

    won = fight(my_hero, "Giant Spider")
    display_hero(my_hero)
