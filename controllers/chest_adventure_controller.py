from flask import Flask, request, jsonify

from services import chest_adventure_service

app = Flask(__name__)


@app.route('/chest/<int:character_id>/', methods=['POST'])
def chest_adventure(character_id):
    if not character_id:
        return jsonify({'error': 'Character ID is required'}), 400

    message = chest_adventure_service.chest_challenge(character_id)
    return jsonify({'message': message}), 200