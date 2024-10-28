import sqlite3


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def register_moster(name, xp, level, attributes):
    monster_query='''
      INSERT INTO Monster (name, xp, leve_id, attribute_id)
      VALUES (?, ?, ?, ?)
'''
    attribute_query = '''
        INSERT INTO Attributes (life, attack, defense, dodge)
        VALUES (?, ?, ?, ?)
    '''
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(attribute_query, (attributes['life'], attributes['attack'], attributes['defense'], attributes['dodge']))
    attribute_id = cursor.lastrowid
    cursor.execute(monster_query, (name, xp, level, attribute_id))
    Monster_id = cursor.lastrowid
    
    conn.commit()
    conn.close()
    
    return Monster_id

def get_monsters():
    monster_query = '''
    SELECT m.Name, m.ID, m.xp, m.leve_id, a.life, a.attack, a.defense, a.dodge
    FROM Monster m
    JOIN Attributes a ON m.attribute_id = a.id
    '''
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(monster_query)
    rows = cursor.fetchall()
    conn.close()
    
    monsters = [
        {
            "name": row["Name"],
            "ID": row["ID"],
            "xp": row["xp"],
            "level_id": row["leve_id"],
            "attributes": {
                "life": row["life"],
                "attack": row["attack"],
                "defense": row["defense"],
                "dodge": row["dodge"]
            }
        }
        for row in rows
    ]
    
    return monsters
    