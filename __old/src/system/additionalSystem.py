from db import storage as Collection
import datetime

def get_player_stats(index):
    name = Collection.NAME[index]
    age = Collection.AGE[index]
    title = Collection.TITLE[index]
    race = Collection.PLAYER_RACE[index]
    glory = Collection.GLORY[index]
    gold = Collection.GOLD[index]
    place = get_player_place(index)
    days = (datetime.date.today() - datetime.datetime.strptime(
            Collection.BORN[index], '%Y-%m-%d').date()).days
    reply = "Имя: {0}\nВозраст: {1}\nТитул: {2}\nРаса: {3}\nРейтинговая слава: {4}\nЗолотa в кошельке: {5}\nМесторасположение: {6}\nДней в мире: {7}"
    reply = reply.format(name, age, title, race, glory, gold, place, days)
    return reply


def get_player_notes(index):
    reply = "У тебя нет заметок!"
    if Collection.NOTES[index]:
        reply = ""
        for note in Collection.NOTES[index]:
            date, text = note.split("|")
            year, month, day = date.split("-")
            reply += "Заметка от {0}.{1}.{2}:  {3}\n".format(day, month, year, text)
    return reply


def get_player_place(index):
    place = "\nГоризонталь: {0}\nВертикаль: {1}\n{2}"
    x, y = Collection.POSITION[index]
    #get place description
    place = place.format(x, y, "Вот туточки! Только ещё непонятно где, но прямо тут!")
    return place


def get_short_own(index):
    reply = "У тебя нет собственности!"
    if Collection.OWN[index]:
        reply = ""
        for own in range(len(Collection.OWN[index])):
            data = Collection.OWN[index][own]
            reply += "{0}. {1} `{2}`\n".format(own+1, data["type"], data["name"])
    return reply


def get_inventory_weight(index):
    weight = 0
    return weight
