from flask import Flask, request, jsonify

from services import monster_service

app = Flask(__name__)


@app.route('/monster', methods=['POST'])
def add_monster():
    data = request.get_json()

    if not all(key in data for key in ('name', 'level')):
        return jsonify({'error': 'Missing required fields'}), 400

    name = data['name']
    level = data['level']

    monster = monster_service.register_monster(name, level)
    return jsonify(monster), 201

@app.route('/monsters', methods=['GET'])
def get_all_monsters():
    monsters = monster_service.get_all_monsters()
    if monsters is None:
         return jsonify({'message': 'No have monsters on DB'}), 200
    return jsonify(monsters), 200
