from abc import ABC
from abc import abstractmethod

import numpy
from datetime import date


class Alasi():
    def __init__(self):
        self.name = "Аласи"
        self.health = [50,50]
        self.mana = [150,150]
        self.attack = [1,1]
        self.defence = [1,1]
        self.magic_attack = [0.3, 0.3]
        self.magic_defence = [0.4,0.4]
        self.weight = [0,30]

    def load_data(self, data):
        #[9] is id for player race
        #[10] is for name of race
        self.health[0] = data[2]
        self.mana[0] = data[3]
        self.attack[0] = data[4]
        self.defence[0] = data[5]
        self.magic_attack[0] = data[6]
        self.magic_defence[0] = data[7]
        self.weight[0] = data[8]


class Elemental():
    def __init__(self):
        self.name = "Элементали"
        self.health = [50,50]
        self.mana = [150,150]
        self.attack = [1,1]
        self.defence = [1,1]
        self.magic_attack = [0.4,0.4]
        self.magic_defence = [0.4,0.4]
        self.weight = [0,30]

    def load_data(self, data):
       #[9] is id for player race
        #[10] is for name of race
        self.health[0] = data[2]
        self.mana[0] = data[3]
        self.attack[0] = data[4]
        self.defence[0] = data[5]
        self.magic_attack[0] = data[6]
        self.magic_defence[0] = data[7]
        self.weight[0] = data[8]


class Artifex():
    def __init__(self):
        self.name = "Артифексы"
        self.health = [150,150]
        self.mana = [50,50]
        self.attack = [5,5]
        self.defence = [5,5]
        self.magic_attack = [0.1,0.1]
        self.magic_defence = [0.1,0.1]
        self.weight = [0,60]

    def load_data(self, data):
        #[9] is id for player race
        #[10] is for name of race
        self.health[0] = data[2]
        self.mana[0] = data[3]
        self.attack[0] = data[4]
        self.defence[0] = data[5]
        self.magic_attack[0] = data[6]
        self.magic_defence[0] = data[7]
        self.weight[0] = data[8]


class Changer():
    def __init__(self):
        self.name = "Перевёртыши"
        self.health = [100,100]
        self.mana = [100,100]
        self.attack = [3,3]
        self.defence = [3,3]
        self.magic_attack = [0.2,0.2]
        self.magic_defence = [0.2,0.2]
        self.weight = [0,40]

    def load_data(self, data):
        #[9] is id for player race
        #[10] is for name of race
        self.health[0] = data[2]
        self.mana[0] = data[3]
        self.attack[0] = data[4]
        self.defence[0] = data[5]
        self.magic_attack[0] = data[6]
        self.magic_defence[0] = data[7]
        self.weight[0] = data[8]


class Fox():
    def __init__(self):
        self.name = "Хвостатые"
        self.health = [250, 250]
        self.mana = [20, 20]
        self.attack = [10, 10]
        self.defence = [1, 1]
        self.magic_attack = [0.1, 0.1]
        self.magic_defence = [0.1, 0.1]
        self.weight = [0, 60]

    def load_data(self, data):
        #[0] is id for player race
        #[1] is for name of race
        self.health[0] = data[2]
        self.mana[0] = data[3]
        self.attack[0] = data[4]
        self.defence[0] = data[5]
        self.magic_attack[0] = data[6]
        self.magic_defence[0] = data[7]
        self.weight[0] = data[8]


class Own():
    def __init__(self, data):
        self.own_list = data

    def get_list(self):
        if self.own_list == []:
            return "Отсутствует"
        else:
            return "pass"


class Dignity():
    def __init__(self, data):
        self.dignity_list = data

    def get_list(self):
        if self.dignity_list == []:
            return "Путешественник"
        else:
            return "Никто"


class Note():
    def __init__(self, data):
        self.note_list = []
        for el in data:
            self.note_list.append(el[0])

    def add_note(self, text):
        tmp = str(date.today())+" `"+text+"`"
        self.note_list.append(tmp)

    def get_list(self):
        tmp = ""
        if self.note_list == []:
            return "У тебя нет заметок."

        for el in range(len(self.note_list)):
            tmp+="№"+str(el+1)+" "+self.note_list[el]+"\n"
        
        return tmp

    def drop_note(self, number):
        try:
            number = int(number)
            if number>len(self.note_list):
                raise ValueError
            else:
                self.note_list.pop(number-1)
        except:
            pass




class PersonData():
    def __init__(self, uniq):
        self.uniq = uniq
        self.text = ""
        self.register = False
        self.action = None
        self.quest = None
        self.quest_step = []

        self.name = ""
        self.gender = ""
        self.age = 0
        self.bio = ""
        self.born = ""
        self.position = []
        self.explored = ""

    def load_data(self, data):
        #uniq already set
        #only registered players saved
        self.register = True
        #action set by default
        self.action = 0

        self.name = data[3] #+
        self.age = data[4]
        self.gender = data[5]
        self.bio = data[6]
        self.born = data[7]
        self.position = list(map(int, data[8].split(" ")))

    def get_explored(self, raw_pos):
        tmp = raw_pos[:-1].split("|")
        array = []
        for el in tmp:
            array.append(el.split(" "))
        return numpy.array(array, dtype=int)


race_list = {"Хвостатые":Fox, "Перевёртыши":Changer, "Элементали":Elemental, "Аласи":Alasi, "Артифексы":Artifex}


class Player():
    def __init__(self, data):
        self.data = data
        self.race = None
        self.note = Note([])
        self.own = Own([])
        self.dignity = Dignity([])

    def new_message(self, text):
        self.data.text = text

    def set_race_stats(self, race):
        self.race = race_list[race]()

    def __str__(self):
        return str(self.data.gender)+" "+self.data.name+" из расы "+str(self.race.name)+" в возрасте "+str(self.data.age)+"\n"+str(self.data.bio)

    def get_attack(self):
        return str(self.race.attack[0])

    def get_defence(self):
        return str(self.race.defence[0])

    def get_mag_attack(self):
        return str(self.race.magic_attack[0])

    def get_mag_defence(self):
        return str(self.race.magic_defence[0])

    def get_weight(self):
        return "0/"+str(self.race.weight[1])

    def get_timelapse(self):
        a = date.fromisoformat(self.data.born)
        b = date.today()

        return str((b-a).days)

    def get_own(self):
        return self.own.get_list()

    def get_dignity(self):
        return self.dignity.get_list()
