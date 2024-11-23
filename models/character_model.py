import sqlite3


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def register_character(name, race_id, vocation_id, level, xp, attribute):
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
    character_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return character_id


def get_character_info(character_id):
    character_query = '''
        SELECT c.Id, c.Name, c.race_id, c.vocation_id, c.level, c.xp, a.life, a.attack, a.defense, a.dodge
        FROM Character c
        JOIN Attributes a ON c.attribute_id = a.id
        WHERE c.id = ?
    '''

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(character_query, (character_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        character_info = {
            "id": row["id"],
            "name": row["Name"],
            "race_id": row["race_id"],
            "vocation_id": row["vocation_id"],
            "level": row["level"],
            "xp": row["xp"],
            "attributes": {
                "life": row["life"],
                "attack": row["attack"],
                "defense": row["defense"],
                "dodge": row["dodge"]
            }
        }
        return character_info
    else:
        return None


def update_info(character_id, updates):
    fields = []
    values = []

    for key, value in updates.items():
        if value is not None:
            fields.append(f"{key} = ?")
            values.append(value)

    if not fields:
        return False

    values.append(character_id)
    character_update_query = f'''
        UPDATE Character
        SET {", ".join(fields)}
        WHERE id = ?
    '''

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(character_update_query, values)
    conn.commit()
    conn.close()


def update_attributes(character_id, attributes):
    fields = []
    values = []

    for key, value in attributes.items():
        if value is not None:
            fields.append(f"{key} = ?")
            values.append(value)

    if not fields:
        return False

    values.append(character_id)
    attributes_update_query = f'''
        UPDATE Attributes
        SET {", ".join(fields)}
        WHERE id = (SELECT attribute_id FROM Character WHERE id = ?)
    '''

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(attributes_update_query, values)
    conn.commit()
    conn.close()
