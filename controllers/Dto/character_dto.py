def character_dto(character):
    return {
        "id": character["id"],
        "name": character["name"],
        "race_id": character["race_id"],
        "vocation_id": character["vocation_id"],
        "level": character["level"],
        "xp": character["xp"],
    }
