from flask import Flask, request, jsonify

from services.character_service import register_character

app = Flask(__name__)


@app.route('/add_character', methods=['POST'])
def add_character():
    data = request.get_json()

    if not all(key in data for key in ('name', 'race_id', 'vocation_id')):
        return jsonify({'error': 'Missing required fields'}), 400

    name = data['name']
    race_id = data['race_id']
    vocation_id = data['vocation_id']

    register_character(name, race_id, vocation_id)
    return jsonify({'message': 'Character added successfully'}), 201
