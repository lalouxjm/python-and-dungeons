import my_func


## FUNCTION

def create_hero(name:str) -> dict:
    hero = {
        "name": name,
        "hp": 100,  # current HP
        "max_hp": 100,  # 100 at start
        "attack": 15,  # 15 at start
        "defense": 5,  # 5 at start
        "level": 1,  # starts at 1
        "xp": 0,  # starts at 0
        "inventory": [],  # list of item name strings
        "buffs": set(),  # set of active passive buff names — no duplicates
        "position": (0, 0),  # tuple — (floor, room_index), immutable coordinates
        "visited_rooms": set(),  # set of room id tuples already explored
        "kills": 0,
    }

    return hero

def gain_xp(hero: dict, amount: int) -> bool:

    lvl_up:bool = False
    hero_xp:int = hero["xp"]
    xp_for_lvl_up:int = hero['level'] * 40
    print(my_func.green(f"You gain {amount}xp⭐!"))


    if hero_xp + amount >= xp_for_lvl_up:
        lvl_up = True
        remaining = hero_xp + amount - xp_for_lvl_up
        hero['level'] += 1
        hero['hp'] += 15
        hero['max_hp'] += 15
        hero['attack'] += 3
        hero['defense'] += 1
        print(my_func.green(f"Congratz! You lvl up! You reached lvl {hero['level']} 🆙"))
        if remaining >= xp_for_lvl_up:
            gain_xp(hero, remaining)
        else:
            hero["xp"] = remaining
    else:
        hero_xp += amount
        hero['xp'] += amount

    return lvl_up

def get_stat_triplets(hero: dict):
    atk:int = hero['attack']
    defense:int = hero['defense']
    xp:int = hero['xp']
    return atk, defense, xp

def display_hero(hero: dict):
    total_blocks = 10
    filled_blocks = int((hero['hp'] / hero['max_hp']) * total_blocks)
    empty_blocks = total_blocks - filled_blocks
    hp_bar = '█' * filled_blocks + '░' * empty_blocks
    buffs = hero['buffs']
    buffs_str = ', '.join(buffs) if buffs else 'None'

    print(my_func.yellow('╔' + '═' * 30 + '╗'))
    print(my_func.yellow('║', f' {hero["name"]} - LvL {hero["level"]:<15}' ,    '║'))
    print(my_func.yellow('║', ' HP ', my_func.red(f'[{hp_bar}]'),my_func.yellow(f'  {hero['hp']}/{hero['max_hp']:<8}'),  my_func.yellow('║')))
    print(my_func.yellow('║', f' ATK: {get_stat_triplets(hero)[0]:<2} - DEF: {get_stat_triplets(hero)[1]:<2} - XP: {get_stat_triplets(hero)[2]:<5}', '║'))
    print(my_func.yellow('║', f' BUFF: {buffs_str:<23}','║'))
    print(my_func.yellow('╚' + '═' * 30 + '╝'))
