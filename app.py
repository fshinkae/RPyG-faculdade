from flask import Flask
import sqlite3

app = Flask(__name__)

DATABASE = 'database.db'
SCHEMA = 'schema.sql'


@app.route('/')
def hello_world():
    return 'Hello World!'

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
    init_db()
    app.run()
