from flask import Flask, request, jsonify

from controllers.Dto.character_dto import character_dto
from services.character_service import register_character, get_character_by_id

app = Flask(__name__)


@app.route('/character', methods=['POST'])
def add_character():
    data = request.get_json()

    if not all(key in data for key in ('name', 'race_id', 'vocation_id')):
        return jsonify({'error': 'Missing required fields'}), 400

    name = data['name']
    race_id = data['race_id']
    vocation_id = data['vocation_id']

    character = register_character(name, race_id, vocation_id)
    character_info = character_dto(character)
    return jsonify(character_info), 201


@app.route('/character/<int:character_id>', methods=['GET'])
def get_character(character_id):
    # character_id = request.args.get('character_id')

    if not character_id:
        return jsonify({'error': 'Character ID is required'}), 400

    character = get_character_by_id(character_id)

    if character is None:
        return jsonify({'error': 'Character not found'}), 404

    return jsonify(character), 200
