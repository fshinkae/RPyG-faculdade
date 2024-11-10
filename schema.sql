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



INSERT INTO Attributes (id, life, attack, defense, dodge) VALUES (1, 8, 3, 1, 2);
INSERT INTO Monster (id, name, level_id, xp, attribute_id) VALUES (1, 'Goblin', 1, 50, 1);

INSERT INTO Attributes (id, life, attack, defense, dodge) VALUES (2, 12, 4, 1, 4);
INSERT INTO Monster (id, name, level_id, xp, attribute_id) VALUES (2, 'Troll', 2, 100, 2);

INSERT INTO Attributes (id, life, attack, defense, dodge) VALUES (3, 20, 6, 2, 6);
INSERT INTO Monster (id, name, level_id, xp, attribute_id) VALUES (3, 'Golen', 3, 200, 3);

INSERT INTO Attributes (id, life, attack, defense, dodge) VALUES (4, 45, 10, 5, 8);
INSERT INTO Monster (id, name, level_id, xp, attribute_id) VALUES (4, 'Dragon', 4, 500, 4);

INSERT INTO Attributes (id, life, attack, defense, dodge) VALUES (5, 12, 4, 1, 4);
INSERT INTO Monster (id, name, level_id, xp, attribute_id) VALUES (5, 'Mimic', 2, 100, 5);       