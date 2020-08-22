# -*- coding: utf-8
import json

#reply
REPLY_REGISTRATION = {}
REPLY_REGISTERED = {}

MESSAGE = []
KEYBOARD = []
ACTION = []

ACTION_KEYS = {}
PERSON_ACTION_KEYS = []

#race stats
ALASI = {}
CHANGER = {}
ARTIFEX = {}
INFINIT = {}
FOX = {}

#player
PLAYERS = []
BOOL = []
PLAYER_RACE = []
PLAYER_ACTION = []

NAME = []
GENDER = []
AGE = []
BIO = []
BORN = []


HEALTH = []
MANA = []
ATTACK = []
DEFENCE = []
MAGIC_ATTACK = []
MAGIC_DEFENCE = []
SPEED = []
MAX_WEIGHT = []
POSITION = []

TITLE = []
GLORY = []
GOLD = []
NOTES = []
OWN = []

with open('db/json/players.json', 'r', encoding="utf-8") as file:
    data = json.load(file)
    PLAYERS = data["players"]
    BOOL = data["bool"]
    PLAYER_ACTION = data["player_action"]
    PLAYER_RACE = data["player_race"]
    NAME = data["name"]
    GENDER = data["gender"]
    AGE = data["age"]
    BIO = data["bio"]
    BORN = data["born"]
    POSITION = data["position"]
    HEALTH = data["health"]
    MANA = data["mana"]
    ATTACK = data["attack"]
    DEFENCE = data["defence"]
    MAGIC_ATTACK = data["magic_attack"]
    MAGIC_DEFENCE = data["magic_defence"]
    MAX_WEIGHT = data["max_weight"]
    SPEED = data["speed"]
    TITLE = data["title"]
    GLORY = data["glory"]
    GOLD = data["gold"]
    NOTES = data["notes"]
    OWN = data["own"]

with open('db/json/reply.json', 'r', encoding="utf-8") as file:
    data = json.load(file)
    REPLY_REGISTRATION = data["reply_registration"]
    REPLY_REGISTERED = data["reply_registered"]
    MESSAGE = data["message"]
    KEYBOARD = data["keyboard"]
    ACTION = data["action"]
    ACTION_KEYS = data["action_keys"]

    PERSON_ACTION_KEYS = ACTION_KEYS["player_stats"]

with open('db/json/race.json', 'r', encoding="utf-8") as file:
    data = json.load(file)
    ALASI = data["Аласи"]
    CHANGER = data["Перевёртыши"]
    ARTIFEX = data["Артифексы"]
    INFINIT = data["Вечные"]
    FOX = data["Хвостатые"]


def set_new_player(user):
    PLAYERS.append({"id": user, "index": len(PLAYERS)})
    BOOL.append({"register": False})

    PLAYER_ACTION.append(None)
    PLAYER_RACE.append("")
    NAME.append("")
    GENDER.append("")
    AGE.append(0)
    BIO.append("")
    BORN.append(0)
    POSITION.append([0, 0])
    HEALTH.append(100)
    MANA.append(100)
    ATTACK.append(10)
    DEFENCE.append(5)
    MAGIC_ATTACK.append(0.5)
    MAGIC_DEFENCE.append(0.5)
    MAX_WEIGHT.append(50)
    SPEED.append(1)
    TITLE.append("Странник")
    GLORY.append(0)
    GOLD.append(20)
    NOTES.append([])
    OWN.append([])


def store_data():
    with open('db/json/players.json', 'w') as file:
        json.dump({
            "players": PLAYERS,
            "bool": BOOL,
            "player_action": PLAYER_ACTION,
            "player_race": PLAYER_RACE,
            "name": NAME,
            "gender": GENDER,
            "age": AGE,
            "bio": BIO,
            "born": BORN,
            "position": POSITION,
            "health": HEALTH,
            "mana": MANA,
            "attack": ATTACK,
            "defence": DEFENCE,
            "magic_attack": MAGIC_ATTACK,
            "magic_defence": MAGIC_DEFENCE,
            "max_weight": MAX_WEIGHT,
            "speed": SPEED,
            "title": TITLE,
            "glory": GLORY,
            "gold": GOLD,
            "notes": NOTES,
            "own": OWN
        }, file, indent=4)
