from db import storage as Collection

import datetime

def process(index, message, action):
    key = ""
    indexes, additional = [], ""

    if action == "edit_bio":
        print("Message ", action)
        if message != "Назад":
            Collection.BIO[index] = message
            key = "confirm_bio"
        else:
            key = "Назад"

    elif action == "add_note":
        if message != "Назад":
            date = str(datetime.date.today())
            text = date + "|" + message
            Collection.NOTES[index].append(text)
            key = "confirm_note"
        else:
            key = "Назад"

    elif action == "delete_notes":
        if message != "Назад":
            Collection.NOTES[index] = []
            key = "Да, удалить заметки"
        else:
            key = "Назад"

    elif action == "own":
        key = "Назад"

    else:
        key = "message_error"

    indexes = Collection.REPLY_REGISTERED[key]

    return [indexes, additional]
