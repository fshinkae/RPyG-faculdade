from models import character_model


def calculate_attributes(race_id, vocation_id):
    base_attributes = {
        "life": 8,
        "attack": 2,
        "defense": 1,
        "dodge": 1
    }

    race_attributes = {
        1: {"defense": 1, "life": 2},
        2: {"dodge": 2, "attack": 1},
        3: {"life": 1, "attack": 1, "defense": 1, "dodge": 1}
    }

    vocation_attributes = {
        1: {"attack": 2, "defense": 1, "dodge": -1},
        2: {"attack": 2, "dodge": 1, "defense": -1, "life": -1},
        3: {"defense": 1, "life": 1, "attack": 1, "dodge": -1}
    }

    for attr, value in race_attributes[race_id].items():
        base_attributes[attr] += value

    for attr, value in vocation_attributes[vocation_id].items():
        base_attributes[attr] += value

    return base_attributes


def register_character(name, race_id, vocation_id):
    attributes = calculate_attributes(race_id, vocation_id)
    xp_base = 0
    level_base = 1
    try:
        character_id = character_model.register_character(name, race_id, vocation_id, level_base, xp_base, attributes)
        character_info = character_model.get_character_info(character_id)
        return character_info
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def get_character_by_id(character_id):
    try:
        character_info = character_model.get_character_info(character_id)
        return character_info
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def update_character_info(character_id, updates):
    try:
        character_model.update_info(character_id, updates)
        character_info = character_model.get_character_info(character_id)
        return character_info
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def update_character_attributes(character_id, updates):
    try:
        character_model.update_attributes(character_id, updates)
        character_info = character_model.get_character_info(character_id)
        return character_info
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def calculate_exp_for_next_level(current_level):
    if current_level == 1:
        return 100
    else:
        return int(100 * (1.4 ** (current_level - 1)))


def gain_experience(character_id, exp_gained):
    character_info = get_character_by_id(character_id)
    if not character_info:
        return "Character not found."

    current_exp = character_info['xp']
    current_level = character_info['level']
    new_exp = current_exp + exp_gained

    exp_for_next_level = calculate_exp_for_next_level(current_level)
    if new_exp >= exp_for_next_level:
        new_level = current_level + 1
        new_exp -= exp_for_next_level
        new_attributes = {attr: int(value * 1.5) for attr, value in character_info['attributes'].items()}
        update_character_attributes(character_id, {'level': new_level, 'xp': new_exp, 'attributes': new_attributes})
        return f"Level up! New level: {new_level}"
    else:
        update_character_attributes(character_id, {'xp': new_exp})
        return f"Experience gained: {exp_gained}. Total experience: {new_exp}"
