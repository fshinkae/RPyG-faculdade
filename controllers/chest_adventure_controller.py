from flask import Flask, request, jsonify

from services import chest_adventure_service

app = Flask(__name__)


@app.route('/chest/open', methods=['POST'])
def chest_adventure():
    data = request.json
    character_id = data['character_id']
    if not character_id:
        return jsonify({'error': 'Character ID is required'}), 400

    message = chest_adventure_service.try_open_chest(character_id)
    return message, 200