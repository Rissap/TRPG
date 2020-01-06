from abc import ABC
from abc import abstractmethod


class Alasi():
    def __init__(self):
        self.name = "Аласи"
        self.health = [50,50]
        self.mana = [150,150]
        self.attack = [1,1]
        self.defence = [1,1]
        self.magic_attack = [0.3, 0.3]
        self.magic_defence = [0.4,0.4]
        self.speed = [3,3]
        self.weight = [0,30]

    def load_data(self, data):
        self.health[0] = data[10]
        self.mana[0] = data[11]
        self.attack[0] = data[12]
        self.defence[0] = data[13]
        self.magic_attack[0] = data[14]
        self.magic_defence[0] = data[15]
        self.speed[0] = data[16]
        self.weight[0] = data[17]

    def __str__(self):
        return self.name


class Elemental():
    def __init__(self):
        self.name = "Элементали"
        self.health = [50,50]
        self.mana = [150,150]
        self.attack = [1,1]
        self.defence = [1,1]
        self.magic_attack = [0.4,0.4]
        self.magic_defence = [0.4,0.4]
        self.speed = [4,4]
        self.weight = [0,30]

    def load_data(self, data):
        self.health[0] = data[10]
        self.mana[0] = data[11]
        self.attack[0] = data[12]
        self.defence[0] = data[13]
        self.magic_attack[0] = data[14]
        self.magic_defence[0] = data[15]
        self.speed[0] = data[16]
        self.weight[0] = data[17]

    def __str__(self):
        return self.name


class Artifex():
    def __init__(self):
        self.name = "Артифексы"
        self.health = [150,150]
        self.mana = [50,50]
        self.attack = [5,5]
        self.defence = [5,5]
        self.magic_attack = [0.1,0.1]
        self.magic_defence = [0.1,0.1]
        self.speed = [6,6]
        self.weight = [0,60]

    def load_data(self, data):
        self.health[0] = data[10]
        self.mana[0] = data[11]
        self.attack[0] = data[12]
        self.defence[0] = data[13]
        self.magic_attack[0] = data[14]
        self.magic_defence[0] = data[15]
        self.speed[0] = data[16]
        self.weight[0] = data[17]

    def __str__(self):
        return self.name


class Changer():
    def __init__(self):
        self.name = "Перевёртыши"
        self.health = [100,100]
        self.mana = [100,100]
        self.attack = [3,3]
        self.defence = [3,3]
        self.magic_attack = [0.2,0.2]
        self.magic_defence = [0.2,0.2]
        self.speed = [5,5]
        self.weight = [0,40]

    def load_data(self, data):
        self.health[0] = data[10]
        self.mana[0] = data[11]
        self.attack[0] = data[12]
        self.defence[0] = data[13]
        self.magic_attack[0] = data[14]
        self.magic_defence[0] = data[15]
        self.speed[0] = data[16]
        self.weight[0] = data[17]

    def __str__(self):
        return self.name


class Fox():
    def __init__(self):
        self.name = "Хвостатые"
        self.health = [250, 250]
        self.mana = [20, 20]
        self.attack = [10, 10]
        self.defence = [1, 1]
        self.magic_attack = [0.1, 0.1]
        self.magic_defence = [0.1, 0.1]
        self.speed = [2, 2]
        self.weight = [0, 60]

    def load_data(self, data):
        self.health[0] = data[10]
        self.mana[0] = data[11]
        self.attack[0] = data[12]
        self.defence[0] = data[13]
        self.magic_attack[0] = data[14]
        self.magic_defence[0] = data[15]
        self.speed[0] = data[16]
        self.weight[0] = data[17]

    def __str__(self):
        return self.name


class PersonData():
    def __init__(self, uniq):
        self.uniq = uniq
        self.text = ""
        self.register = False
        self.action = None

        self.name = ""
        self.gender = ""
        self.age = 0
        self.bio = ""
        self.born = ""

    def load_data(self, data):
        self.register = True
        self.action = data[2]
        self.name = data[3]
        self.age = data[4]
        self.gender = data[5]
        self.bio = data[6]
        self.born = data[7]


race_list = {"Хвостатые":Fox, "Перевёртыши":Changer, "Элементали":Elemental, "Аласи":Alasi, "Артифексы":Artifex}


class Player():
    def __init__(self, data):
        self.data = data
        self.race = None

    def new_message(self, text):
        self.data.text = text

    def set_race_stats(self, race):
        self.race = race_list[race]()

    def __str__(self):
        return str(self.data.gender)+" "+self.data.name+" из расы "+str(self.race)+" в возрасте "+str(self.data.age)+"\n"+str(self.data.bio)
