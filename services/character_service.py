from models.character_model import vocations, races, base_character

FILE_PATH = 'database/database.db'


def set_name(character, name):
    character["name"] = name


def set_vocation(character, vocation):
    for attribute, value in vocations[vocation].items():
        character[attribute] += value


def set_race(character, race):
    for attribute, value in races[race].items():
        character[attribute] += value


def set_data(attributes):
    import json
    with open(FILE_PATH, 'w') as db_file:
        json.dump({'Adventurer': attributes}, db_file, indent=4)


def set_character(name, vocation, race):
    set_name(base_character, name)
    set_vocation(base_character, vocation)
    set_race(base_character, race)
    set_data(base_character)
    return base_character
