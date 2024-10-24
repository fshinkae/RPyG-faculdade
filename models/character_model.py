import sqlite3


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def add_database_character(name, race_id, vocation_id, level, xp, attribute):
    character_query = '''
        INSERT INTO Character (Name, race_id, vocation_id, level, xp, attribute_id)
        VALUES (?, ?, ?, ?, ?, ?)
    '''
    attribute_query = '''
        INSERT INTO Attributes (life, attack, defense, dodge)
        VALUES (?, ?, ?, ?)
    '''
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(attribute_query, (attribute['life'], attribute['attack'], attribute['defense'], attribute['dodge']))
    attribute_id = cursor.lastrowid
    cursor.execute(character_query, (name, race_id, vocation_id, level, xp, attribute_id))

    conn.commit()
    conn.close()
