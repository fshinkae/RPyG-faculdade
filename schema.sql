DROP TABLE IF EXISTS Character;
DROP TABLE IF EXISTS Vocation;
DROP TABLE IF EXISTS Attributes;
DROP TABLE IF EXISTS Race;
DROP TABLE IF EXISTS MonsterLevel;
DROP TABLE IF EXISTS Monster;

CREATE TABLE Attributes
(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    life    INTEGER NOT NULL,
    attack  INTEGER NOT NULL,
    defense INTEGER NOT NULL,
    dodge   INTEGER NOT NULL
);

CREATE TABLE Race
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE Vocation
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE Character
(
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    name         TEXT    NOT NULL,
    race_id      INTEGER NOT NULL,
    vocation_id  INTEGER NOT NULL,
    level        INTEGER NOT NULL,
    xp           INTEGER NOT NULL,
    attribute_id INTEGER NOT NULL,
    FOREIGN KEY (race_id) REFERENCES Race (id),
    FOREIGN KEY (vocation_id) REFERENCES Vocation (id),
    FOREIGN KEY (attribute_id) REFERENCES Attributes (id)
);

CREATE TABLE MonsterLevel
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE Monster
(
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    name         TEXT    NOT NULL,
    level_id     INTEGER NOT NULL,
    xp           INTEGER NOT NULL,
    attribute_id INTEGER NOT NULL,
    FOREIGN KEY (level_id) REFERENCES MonsterLevel (id),
    FOREIGN KEY (attribute_id) REFERENCES Attributes (id)
);

INSERT INTO Race (Name)
VALUES ('Humano'),
       ('Elfo'),
       ('Anão');

INSERT INTO Vocation (Name)
VALUES ('Guerreiro'),
       ('Paladino'),
       ('Arqueiro');

INSERT INTO MonsterLevel (Name)
VALUES ('Fraco'),
       ('Normal'),
       ('Forte'),
       ('Boss');