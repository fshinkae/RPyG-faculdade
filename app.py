import os
import sqlite3

from flask import Flask, render_template, send_file, send_from_directory
from flask_cors import CORS

from controllers import character_controller, monster_adventure_controller, monster_controllers, \
    chest_adventure_controller

app = Flask(__name__)
CORS(app)

DATABASE = 'database.db'
SCHEMA = 'schema.sql'

# Character Routes
app.add_url_rule('/character', 'add_character', character_controller.add_character, methods=['POST'])
app.add_url_rule('/character/<int:character_id>', 'get_character', character_controller.get_character, methods=['GET'])
app.add_url_rule('/character/<int:character_id>/info', 'put_character_info', character_controller.put_character_info,
                 methods=['PUT'])
app.add_url_rule('/character/<int:character_id>/attributes', 'put_character_attributes',
                 character_controller.put_character_attributes, methods=['PUT'])
app.add_url_rule('/monster', 'add_monster', monster_controllers.add_monster, methods=['POST'])
app.add_url_rule('/monsters', 'get_all_monsters', monster_controllers.get_all_monsters, methods=['GET'])

# Chest Routes
app.add_url_rule('/chest/open', 'chest_adventure', chest_adventure_controller.chest_adventure, methods=['POST'])
app.add_url_rule('/chest/call_mimic', 'call_mimic_monster', monster_adventure_controller.call_mimic_monster,
                 methods=['GET'])

# Monster Adventure Routes
app.add_url_rule('/attack', 'handle_attack', monster_adventure_controller.handle_attack, methods=['POST'])
app.add_url_rule('/monster_attack', 'handle_monster_attack', monster_adventure_controller.handle_monster_attack,
                 methods=['POST'])
app.add_url_rule('/defend', 'handle_defend', monster_adventure_controller.handle_defend, methods=['POST'])
app.add_url_rule('/call_monster', 'call_random_monster', monster_adventure_controller.call_random_monster,
                 methods=['GET'])


# Initialize database (don't change this)
def init_db():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        with open('schema.sql', 'r') as f:
            conn.executescript(f.read())
        conn.commit()
        print("Database initialized successfully.")
    except sqlite3.OperationalError as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/information')
def serve_character_html():
    return render_template('information.html')

@app.route('/chest_adventure')
def chest_adventure_html():
    return render_template('chest_adventure.html')

@app.route('/monster_adventure')
def monster_adventure_html():
    return render_template('monster_adventure.html')


@app.route('/script.js')
def script():
    return send_file('templates/script.js')


@app.route('/style.css')
def style():
    return send_file('templates/style.css')


@app.route('/images/<path:path>')
def send_image(path):
    return send_from_directory('templates/images', path)


# Initialize app (don't change this)
if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    app.run()
