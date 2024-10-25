import os

from flask import Flask
import sqlite3

from controllers import character_controller

app = Flask(__name__)

DATABASE = 'database.db'
SCHEMA = 'schema.sql'

# Character Routes
app.add_url_rule('/character', 'add_character', character_controller.add_character, methods=['POST'])
app.add_url_rule('/character/<int:character_id>', 'get_character', character_controller.get_character, methods=['GET'])
app.add_url_rule('/character/<int:character_id>/info', 'put_character_info', character_controller.put_character_info, methods=['PUT'])
app.add_url_rule('/character/<int:character_id>/attributes', 'put_character_attributes', character_controller.put_character_attributes, methods=['PUT'])


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


# Initialize app (don't change this)
if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    app.run()
