DROP TABLE IF EXISTS Character;
DROP TABLE IF EXISTS Vocation;
DROP TABLE IF EXISTS Attributes;
DROP TABLE IF EXISTS Race;
DROP TABLE IF EXISTS MonsterLevel;
DROP TABLE IF EXISTS Monster;

CREATE TABLE Attributes
(
    ID      INTEGER PRIMARY KEY AUTOINCREMENT,
    life    INTEGER NOT NULL,
    attack  INTEGER NOT NULL,
    defense INTEGER NOT NULL,
    dodge   INTEGER NOT NULL
);


CREATE TABLE Race
(
    ID   INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL
);

CREATE TABLE Vocation
(
    ID   INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL
);

CREATE TABLE Character
(
    ID           INTEGER PRIMARY KEY AUTOINCREMENT,
    Name         TEXT    NOT NULL,
    race_id      INTEGER NOT NULL,
    vocation_id  INTEGER NOT NULL,
    level        INTEGER NOT NULL,
    xp           INTEGER NOT NULL,
    attribute_id INTEGER NOT NULL,
    FOREIGN KEY (race_id) REFERENCES Race (ID),
    FOREIGN KEY (vocation_id) REFERENCES Vocation (ID),
    FOREIGN KEY (attribute_id) REFERENCES Attributes (ID)
);


CREATE TABLE MonsterLevel
(
    ID   INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL
);


CREATE TABLE Monster
(
    ID           INTEGER PRIMARY KEY AUTOINCREMENT,
    Name         TEXT    NOT NULL,
    leve_id      INTEGER NOT NULL,
    xp           INTEGER NOT NULL,
    attribute_id INTEGER NOT NULL,
    FOREIGN KEY (leve_id) REFERENCES MonsterLevel (ID),
    FOREIGN KEY (attribute_id) REFERENCES Attributes (ID)
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
INSERT INTO Monster (Name, leve_id, attribute_id, xp)
VALUES ('Goblin', 1, 1, 50),
       ('Orc', 2, 2, 100),
       ('Troll', 3, 3, 200),
       ('Dragão', 4, 4, 500);
