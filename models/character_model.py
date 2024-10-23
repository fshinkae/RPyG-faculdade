import json


def get_next_id():
    try:
        with open('database/id_counter.json', 'r') as f:
            data = json.load(f)
            data['id'] += 1
    except FileNotFoundError:
        data = {'id': 1}

    with open('database/id_counter.json', 'w') as f:
        json.dump(data, f)

    return data['id']

vocations = {
    "Guerreiro": {"ataque": 2, "defesa": 1, "vida": 0, "esquiva": -1},
    "Arqueiro": {"ataque": 2, "defesa": -1, "vida": -1, "esquiva": 1},
    "Paladino": {"ataque": 1, "defesa": 1, "vida": 1, "esquiva": -1}
}

races = {
    "Anão": {"ataque": 0, "defesa": 1, "vida": 2, "esquiva": 0},
    "Elfo": {"ataque": 1, "defesa": 0, "vida": 0, "esquiva": 2},
    "Humano": {"ataque": 1, "defesa": 1, "vida": 1, "esquiva": 1}
}

base_character = {"id": get_next_id(), "name": "", "ataque": 2, "defesa": 1, "vida": 8, "esquiva": 1}