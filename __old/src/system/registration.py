import datetime

from db import storage as Collection


def process(index, message, action):
    #every system must check the condition itself
    if Collection.BOOL[index]["register"]:
        return [Collection.REPLY_REGISTRATION["already_registered"], ""]

    reply = " "
    if action == "name":
        Collection.NAME[index] = message
        return [Collection.REPLY_REGISTRATION[action], ""]

    elif action == "race":
        if message == "О расах":
            return [Collection.REPLY_REGISTRATION[message], ""]

        elif message == "Аласи":
            race = Collection.ALASI

        elif message == "Вечные":
            race = Collection.INFINIT

        elif message == "Артифексы":
            race = Collection.ARTIFEX

        elif message == "Перевёртыши":
            race = Collection.CHANGER

        else:
            return [Collection.REPLY_REGISTRATION["race_fail"], ""]

        Collection.PLAYER_RACE[index] = message
        Collection.HEALTH[index] = race["health"]
        Collection.MANA[index] = race["mana"]
        Collection.ATTACK[index] = race["attack"]
        Collection.DEFENCE[index] = race["defence"]
        Collection.MAGIC_ATTACK[index] = race["magic_attack"]
        Collection.MAGIC_DEFENCE[index] = race["magic_defence"]
        Collection.MAX_WEIGHT[index] = race["max_weight"]
        Collection.SPEED[index] = race["speed"]
        return [Collection.REPLY_REGISTRATION[action], ""]

    elif action == "age":
        if message.isdigit():
            if 15 < int(message) < 91:
                Collection.AGE[index] = int(message)
                return [Collection.REPLY_REGISTRATION[action], ""]
            else:
                return [Collection.REPLY_REGISTRATION["age_fail"], ""]
        else:
            return [Collection.REPLY_REGISTRATION["age_fail"], ""]

    elif action == "gender":
        if message in ["Господин", "Госпожа"]:
            Collection.GENDER[index] = message
            return [Collection.REPLY_REGISTRATION[action], ""]
        else:
            return [Collection.REPLY_REGISTRATION["gender_fail"], ""]

    elif action == "bio":
        Collection.BIO[index] = message
        reply = "Имя: {}\nВозраст: {}\nРаса: {}\nПол: {}\nБиография: {}".format(
            Collection.NAME[index],
            Collection.AGE[index],
            Collection.PLAYER_RACE[index],
            Collection.GENDER[index],
            Collection.BIO[index])
        return [Collection.REPLY_REGISTRATION[action], reply]

    elif action == "checkup":
        if message == "Всё верно":
            Collection.BOOL[index]["register"] = True
            Collection.BORN[index] = str(datetime.datetime.now().date())
            return [Collection.REPLY_REGISTRATION[message], ""]
        else:
            return [Collection.REPLY_REGISTRATION["checkup_fail"], ""]

    else:
        return [Collection.REPLY_REGISTRATION["registration_fail"], "DEAD"]
