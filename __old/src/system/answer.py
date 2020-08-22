from db import storage as Collection
from . import additionalSystem as AddSys

def get_addition(index, message):
    reply = ""

    if message == "Статистика":
        reply = AddSys.get_player_stats(index)

    elif message == "Биография":
        reply = "\n"+Collection.BIO[index]

    elif message == "Записная книжка":
        reply = AddSys.get_player_notes(index)

    elif message == "Собственность":
        reply = AddSys.get_short_own(index)

    else:
        pass
    return reply


def process(index, message):
    addition = ""
    if Collection.BOOL[index]["register"]:
        if message in Collection.REPLY_REGISTERED.keys():
            Ireply, Ikeyboard, Iaction = Collection.REPLY_REGISTERED[message]

            addition = get_addition(index, message)

        else:
            Ireply, Ikeyboard, Iaction = Collection.REPLY_REGISTERED["message_error"]
    else:
        if message in Collection.REPLY_REGISTRATION.keys():
            Ireply, Ikeyboard, Iaction = Collection.REPLY_REGISTRATION[message]
        else:
            Ireply, Ikeyboard, Iaction = Collection.REPLY_REGISTRATION["unregister_error"]

    return [[Ireply, Ikeyboard, Iaction], addition]
