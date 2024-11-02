import random

from services import character_service


def roll_d20():
    return random.randint(1, 20)


def update_character_status(character_id):
    character_info = character_service.get_character_by_id(character_id)
    if character_info:
        max_health = character_info['attributes']['life']
        current_health = character_info['attributes']['life']
        health_potion = max_health * 0.50
        new_health = min(current_health + health_potion, max_health)
        character_service.update_character_info(character_id, {'life': new_health})


def try_open_chest(character_id):
    tries = 3
    for chance in range(1, tries + 1):
        result = roll_d20()
        if result <= 9:
            message = f"Fail! You didn't open the chest, {tries - chance} tries remaining!"
            return message
        else:
            message = "Success! You opened the chest! You obtained a health potion!"
            update_character_status(character_id)
            return message

    message = "All tries failed! The chest is locked!"
    return message


def chest_challenge(character_id):
    result = roll_d20()
    print(f"Dice result: {result}")
    if result <= 2:
        print("WARNING! A mimic has appeared!")
        """Mimic fight (Medium Monster)"""
        return False
    else:
        try_open_chest(character_id)