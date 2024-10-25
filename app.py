import os

from flask import Flask
import sqlite3

from controllers.character_controller import add_character, get_character

app = Flask(__name__)

DATABASE = 'database.db'
SCHEMA = 'schema.sql'

app.add_url_rule('/character', 'add_character', add_character, methods=['POST'])
app.add_url_rule('/character/<int:character_id>', 'get_character', get_character, methods=['GET'])


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


if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    app.run()
