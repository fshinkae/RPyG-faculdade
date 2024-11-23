import random

from flask import jsonify

from services import character_service

remaining_tries = 3


def roll_d20():
    return random.randint(1, 20)


def life_dice():
    dice = roll_d20()
    if 1 <= dice <= 15:
        return 0.25
    elif 15 <= dice <= 20:
        return 0.50


def update_character_status_chest(character_id):
    character_info = character_service.get_character_by_id(character_id)
    if character_info:
        life = character_info['attributes']['life']
        health_potion = life * life_dice()
        new_health = life + health_potion
        character_service.update_character_attributes(character_id, {'life': new_health})
        return character_info['attributes']['life']


def try_open_chest(character_id):
    global remaining_tries
    for chance in range(1, remaining_tries + 1):
        result = roll_d20()

        if result <= 9:
            remaining_tries -= 1
            message = jsonify({'message': f"Fail! You didn't open the chest, {remaining_tries} tries remaining!",
                               'remaining_tries': remaining_tries,
                               'chest_status': 'locked'})
            return message
        else:
            mimic_dice = roll_d20()
            if (mimic_dice >= 1) and (mimic_dice <= 2):
                message = jsonify({'message': "Success! You opened the chest and MIMIC appear, prepare for battle!",
                                   'remaining_tries': remaining_tries,
                                   'chest_status': 'monster'})
                return message
            else:
                life = update_character_status_chest(character_id)
                remaining_tries = 3
                message = jsonify({'message': f"Success! You opened the chest and recovered your health to {life}!",
                               'remaining_tries': remaining_tries,
                               'chest_status': 'open'})
                return message

    message = jsonify({
        "message": "All tries failed! The chest is locked!",
        'remaining_tries': remaining_tries,
        'chest_status': 'locked'
    })
    remaining_tries = 3
    return message
