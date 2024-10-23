from flask import Flask, request, jsonify
from services.character_service import set_character

app = Flask(__name__)


@app.route('/character', methods=['POST'])
def set_character_controller():
    data = request.json
    name = data.get('name')
    vocation = data.get('vocation')
    race = data.get('race')

    if not name:
        return jsonify({"error": "Nome não fornecido"}), 400

    if not vocation or vocation not in ["Guerreiro", "Arqueiro", "Paladino"]:
        return jsonify({"error": "Vocação inválida ou não fornecida"}), 400

    if not race or race not in ["Anão", "Elfo", "Humano"]:
        return jsonify({"error": "Raça inválida ou não fornecida"}), 400

    character = set_character(name, vocation, race)
    return jsonify(character)
