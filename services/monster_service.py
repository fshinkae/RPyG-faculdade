

from models import monster_model


def calculate_monster_register(level):
        monster_attributes_level = {
                1: {"defense": 1, "life": 8, "attack": 3, "dodge": 2},
                2: {"defense": 1, "life": 12, "attack": 4, "dodge": 4},
                3: {"defense": 2, "life": 20, "attack": 6, "dodge": 6},
                4: {"defense": 5, "life": 45, "attack": 10, "dodge": 8}
        }

        if (level == 1):
             return monster_attributes_level[1]
        if (level == 2):
             return monster_attributes_level[2]
        if (level == 3):
             return monster_attributes_level[3]
        if (level == 4):
             return monster_attributes_level[4]

def calculate_monster_xp(level):
        xp_level = [50, 100, 200, 500]
        return xp_level[level]


def register_monster(name, level):
    attributes = calculate_monster_register(level)
    xp_monster = calculate_monster_xp(level)
    try:
        monster = monster_model.register_moster(name, xp_monster, level, attributes)
        return monster
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def get_all_monsters():
     try:
        monsters = monster_model.get_monsters()
        return monsters
     except Exception as e:
        print(f"An error occurred: {e}")
        return False