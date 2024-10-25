from flask import Flask, request, jsonify

from controllers.Dto import character_dto
from services import character_service

app = Flask(__name__)


@app.route('/character', methods=['POST'])
def add_character():
    data = request.get_json()

    if not all(key in data for key in ('name', 'race_id', 'vocation_id')):
        return jsonify({'error': 'Missing required fields'}), 400

    name = data['name']
    race_id = data['race_id']
    vocation_id = data['vocation_id']

    character = character_service.register_character(name, race_id, vocation_id)
    character_info = character_dto.character_dto(character)
    return jsonify(character_info), 201


@app.route('/character/<int:character_id>', methods=['GET'])
def get_character(character_id):

    if not character_id:
        return jsonify({'error': 'Character ID is required'}), 400

    character = character_service.get_character_by_id(character_id)

    if character is None:
        return jsonify({'error': 'Character not found'}), 404

    return jsonify(character), 200


@app.route('/character/<int:character_id>/info', methods=['PUT'])
def put_character_info(character_id):
    data = request.get_json()

    updates = {
        'Name': data.get('name'),
        'race_id': data.get('race_id'),
        'vocation_id': data.get('vocation_id'),
        'level': data.get('level'),
        'xp': data.get('xp')
    }

    character = character_service.update_character_info(character_id, updates)
    if not character:
        return jsonify({'error': 'Failed to update character info'}), 500

    character_info = character_dto.character_dto(character)
    return jsonify(character_info), 200


@app.route('/character/<int:character_id>/attributes', methods=['PUT'])
def put_character_attributes(character_id):
    data = request.get_json()

    updates = {
        'life': data.get('life'),
        'attack': data.get('attack'),
        'defense': data.get('defense'),
        'dodge': data.get('dodge')
    }

    character = character_service.update_character_attributes(character_id, updates)
    if not character:
        return jsonify({'error': 'Failed to update character attributes'}), 500

    return jsonify(character), 200
