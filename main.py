from hero import create_hero, gain_xp, display_hero
from items import add_item, use_item


## FUNCTION
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


## MAIN
if __name__ == '__main__':
    my_hero = create_hero("Sir JMi")
    print(my_hero)
    display_hero(my_hero)
    gain_xp(my_hero, 30)
    print(my_hero)
    gain_xp(my_hero, 45)
    print(my_hero)
    display_hero(my_hero)
    add_item(my_hero, "Spell Tome")
    add_item(my_hero, "Elixir of Rage")
    add_item(my_hero, "Dragon Crown")
    use_item(my_hero, "Dragon Crown")
    display_hero(my_hero)