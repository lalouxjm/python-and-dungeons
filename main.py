from hero import create_hero, gain_xp, display_hero


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

