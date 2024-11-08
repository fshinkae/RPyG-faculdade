import random

from services import character_service, monster_service

defense_buff_active = {}


def roll_d20():
    return random.randint(1, 20)


def check_character_life(character_id):
    character_info = character_service.get_character_by_id(character_id)
    if character_info:
        return character_info['attributes']['life']
    return None


def dodge_character(character_info, monster):
    dice = roll_d20()
    dice_monster = roll_d20()
    character_dodge = dice + character_info['attributes']['dodge']
    monster_dodge = dice_monster + monster['attributes']['dodge']
    if character_dodge >= monster_dodge:
        return True
    return False


def dodge_monster(character_info, monster):
    dice = roll_d20()
    dice_character = roll_d20()
    monster_dice = dice + monster['attributes']['dodge']
    character_dice = dice_character + character_info['attributes']['dodge']
    if monster_dice >= character_dice:
        return True
    return False


def character_attack(character_id, opponent_defense, monster):
    global defense_buff_active
    character_info = character_service.get_character_by_id(character_id)
    if character_info:
        attack = character_info['attributes']['attack']
        dice = roll_d20()

        if not dodge_monster(character_info, monster):
            if dice + attack >= opponent_defense:
                if dice == 20:
                    damage = attack - opponent_defense
                    damage = damage * 2
                    monster['attributes']['life'] -= damage
                else:
                    damage = attack - opponent_defense
                    monster['attributes']['life'] -= damage
                return monster, damage
            else:
                return None, 0
        return None, 0


def monster_attack(character_id, monster):
    global defense_buff_active
    character_info = character_service.get_character_by_id(character_id)
    if character_info:
        defense = character_info['attributes']['defense']
        dice = roll_d20()
        attack = dice + monster['attributes']['attack']

        if not dodge_character(character_info, monster):
            if attack >= defense:
                if dice == 20:
                    damage = (monster['attributes']['attack'] * 2) - defense
                else:
                    damage = monster['attributes']['attack'] - defense

                character_info['attributes']['life'] -= damage

                if defense_buff_active.get(character_id):
                    character_info['attributes']['defense'] -= 5
                    character_service.update_character_info(character_id, character_info)
                    defense_buff_active[character_id] = False

                result = character_service.update_character_attributes(character_id, character_info['attributes'])
                return result, damage
            else:
                return None, 0
        return None, 0


def defend_character(character_id):
    global defense_buff_active
    character_info = character_service.get_character_by_id(character_id)
    if character_info:
        character_info['attributes']['defense'] += 5
        character_service.update_character_info(character_id, character_info)
        defense_buff_active[character_id] = True
        return character_info, character_info['attributes']['defense']
    return None
