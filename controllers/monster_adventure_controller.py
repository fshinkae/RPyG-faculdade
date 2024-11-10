import random

from flask import Flask, request, jsonify
from services import monster_adventure_service, monster_service, character_service

app = Flask(__name__)

monsters_in_memory = []
monster_memory = None


def roll_d20():
    return random.randint(1, 20)


def get_monsters():
    get_all_monsters = monster_service.get_all_monsters()
    monsters_in_memory.append(get_all_monsters)
    return get_all_monsters


def random_monster():
    global monster_memory
    dice = roll_d20()
    monsters = get_monsters()
    monster = {}
    if 1 <= dice <= 8:
        monster = next(monster for monster in monsters if monster["level_id"] == 1)
    elif 9 <= dice <= 14:
        monster = next(monster for monster in monsters if monster["level_id"] == 2)
    elif 15 <= dice <= 18:
        monster = next(monster for monster in monsters if monster["level_id"] == 3)
    elif 19 <= dice <= 20:
        monster = next(monster for monster in monsters if monster["level_id"] == 4)
    monster_memory = monster
    return monster


@app.route('/attack', methods=['POST'])
def handle_attack():
    global monster_memory
    data = request.json
    character_id = data['character_id']

    if not character_id:
        return jsonify({'error': 'Character ID is required'}), 404

    character_info = character_service.get_character_by_id(character_id)
    if not character_info:
        return jsonify({'error': 'Character not found'}), 404

    if monster_memory:
        attack_result = monster_adventure_service.character_attack(character_info, monster_memory)
        if attack_result is None:
            return jsonify({'message': 'Character attack failed'}), 200

        result, damage = attack_result
        if result:
            if monster_memory['attributes']['life'] <= 0:
                xp = monster_memory['xp']
                character_service.gain_experience(character_id, xp)
                monster_memory.clear()
                return jsonify({'message': f'Monster is dead, you earned {xp} xp'}), 200
            return jsonify(
                {'message': f'Attack successful! You dealt {damage} damage.', 'monster': monster_memory}), 200
        else:
            return jsonify({'message': 'Attack missed', 'monster': monster_memory}), 200
    return jsonify({'message': 'Monster not found'}), 404


@app.route('/monster_attack', methods=['POST'])
def handle_monster_attack():
    global monster_memory
    data = request.json
    character_id = data['character_id']

    if not character_id:
        return jsonify({'message': 'Character ID is required'}), 400

    if not monster_memory:
        return jsonify({'message': 'Monster not found'}), 404

    result, damage = monster_adventure_service.monster_attack(character_id, monster_memory)

    if result:
        character = character_service.get_character_by_id(character_id)
        if character['attributes']['life'] <= 0:
            return jsonify({'message': 'You are dead!!!'}), 200

        return jsonify({'message': f'The monster attacked successfully! You took {damage} damage.', 'character': character}), 200
    else:
        return jsonify({'message': 'The monster attack missed', 'monster': monster_memory}), 200


@app.route('/defend', methods=['POST'])
def handle_defend():
    data = request.json
    character_id = data['character_id']

    if not character_id:
        return jsonify({'message': 'Character ID is required'}), 400

    character_info = character_service.get_character_by_id(character_id)
    if not character_info:
        return jsonify({'message': 'Character not found'}), 404

    result, defense = monster_adventure_service.defend_character(character_info, character_id)
    if result or defense > 0:
        return jsonify({'message': f'Defense successful, increase you defense is {defense} in next round!',
                        'character': result}), 200
    return jsonify({'message': 'Defense failed'}), 200


@app.route('/call_monster', methods=['GET'])
def call_random_monster():
    global monster_memory
    if monster_memory:
        if monster_memory['attributes']['life'] <= 0:
            monster = random_monster()
            return jsonify({'message': 'Monster created', 'monster': monster}), 200
        return jsonify({'message': 'Monster already exists', 'monster': monster_memory}), 200
    monster = random_monster()
    return jsonify({'message': 'Monster created', 'monster': monster}), 200
