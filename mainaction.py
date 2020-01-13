import telebot

from map import MAP
from database import DATABASE

from abc import ABC
from abc import abstractmethod

from keygen import KEYGEN
from map import MAP


class Action(ABC):
    @abstractmethod
    def handle_special(self):
        pass

    @abstractmethod
    def handle_common(self):
        pass

    @abstractmethod
    def get_reply(self):
        pass


class WorldAction(Action):
    def __init__(self, player):
        self.player = player
        self.answer = ""
        self.keyboard = ""
        self.image = ""

        self.mode = 1000
        self.keygen = KEYGEN


    def handle_special(self):

        #print(self.player.data.text.encode('UTF-8'))
        #print(self.player.data.text.encode('UTF-8').decode())

        self.answer = ""
        self.image = ""
        text = self.player.data.text

        #print("encode = ", text.encode('UTF-8'), "\nequal = ", text.encode('UTF-8')==b'\xe2\x86\x96')
       
        if self.player.data.action == 1001:
            require = self.player.data.text.split(" ")
            self.player.data.position = MAP.move_person(self.player.data.position, require)
            self.image = MAP.get_map(self.player.data.position, 16)
            self.answer = "Переместились!"
            self.player.data.text = "Перемещение"
            self.player.data.action = 1000
       
        elif text == "Глобальная":
            self.image = MAP.get_map(self.player.data.position, 100)

        elif text == "Местности":
            self.image = MAP.get_map(self.player.data.position, 16)

        elif text == "Координаты":
            self.player.data.action = 1001

        #arrows encoding
        elif text.encode('UTF-8') == b'\xe2\x86\x96':
            require = self.player.data.position[:]
            require[1] = require[1]-1
            require[0] = require[0]-1
            self.player.data.position = MAP.move_person(self.player.data.position, require)
            self.image = MAP.get_map(self.player.data.position, 16)
            self.answer = "Переместились!"
            self.player.data.text = "Перемещение"
            #print("left up")

        elif text.encode('UTF-8') == b'\xe2\x86\x97':
            require = self.player.data.position[:]
            require[1] = require[1]-1
            require[0] = require[0]+1
            self.player.data.position = MAP.move_person(self.player.data.position, require)
            self.image = MAP.get_map(self.player.data.position, 16)
            self.answer = "Переместились!"
            self.player.data.text = "Перемещение"
            #print("right up")

        elif text.encode('UTF-8') == b'\xe2\x86\x99':
            require = self.player.data.position[:]
            require[1] = require[1]+1
            require[0] = require[0]-1
            self.player.data.position = MAP.move_person(self.player.data.position, require)
            self.image = MAP.get_map(self.player.data.position, 16)
            self.answer = "Переместились!"
            self.player.data.text = "Перемещение"
            #print("left down")

        elif text.encode('UTF-8') == b'\xe2\x86\x98':
            require = self.player.data.position[:]
            require[1] = require[1]+1
            require[0] = require[0]+1
            self.player.data.position = MAP.move_person(self.player.data.position, require)
            self.image = MAP.get_map(self.player.data.position, 16)
            self.answer = "Переместились!"
            self.player.data.text = "Перемещение"
            #print("right down")

        elif text.encode('UTF-8') == b'\xe2\x86\x91':
            require = self.player.data.position[:]
            require[1] = require[1]-1
            self.player.data.position = MAP.move_person(self.player.data.position, require)
            self.image = MAP.get_map(self.player.data.position, 16)
            self.answer = "Переместились!"
            self.player.data.text = "Перемещение"

        elif text.encode('UTF-8') == b'\xe2\x86\x93':
            require = self.player.data.position[:]
            require[1] = require[1]+1
            self.player.data.position = MAP.move_person(self.player.data.position, require)
            self.image = MAP.get_map(self.player.data.position, 16)
            self.answer = "Переместились!"
            self.player.data.text = "Перемещение"

        elif text.encode('UTF-8') == b'\xe2\x86\x90':
            require = self.player.data.position[:]
            require[0] = require[0]-1
            self.player.data.position = MAP.move_person(self.player.data.position, require)
            self.image = MAP.get_map(self.player.data.position, 16)
            self.answer = "Переместились!"
            self.player.data.text = "Перемещение"

        elif text.encode('UTF-8') == b'\xe2\x86\x92':
            require = self.player.data.position[:]
            require[0] = require[0]+1
            self.player.data.position = MAP.move_person(self.player.data.position, require)
            self.image = MAP.get_map(self.player.data.position, 16)
            self.answer = "Переместились!"
            self.player.data.text = "Перемещение"

        else:
            pass


        if self.player.data.action in range(1000, 2000):
            pass
        else:
            self.player.data.action = 1000

        


    def handle_common(self):
        
        data = DATABASE.get_answer(self.player.data.text, self.mode)

        if self.answer=="":
            self.answer = data[0].replace(r"\n", "\n")+"\n"+self.answer

        self.keyboard = data[1]

    def get_reply(self):
        if self.keyboard == "":
            keyboard_data = telebot.types.ReplyKeyboardRemove()
        else:
            keyboard_data = telebot.types.ReplyKeyboardMarkup(True)
            self.keygen.generate(keyboard_data, self.keyboard)

        return [self.answer, keyboard_data, self.image]


class QuestAction(Action):
    def __init__(self, player):
        self.player = player
        self.answer = ""
        self.keyboard = ""
        self.image = ""

        self.mode = 2000
        self.keygen = KEYGEN


    def handle_special(self):
        self.player.data.action = 2000


    def handle_common(self):

        data = DATABASE.get_answer(self.player.data.text, self.mode)

        self.answer = data[0].replace(r"\n", "\n")+"\n"+self.answer
        self.keyboard=data[1]

    def get_reply(self):
        if self.keyboard == "":
            keyboard_data = telebot.types.ReplyKeyboardRemove()
        else:
            keyboard_data = telebot.types.ReplyKeyboardMarkup(True)
            self.keygen.generate(keyboard_data, self.keyboard)

        return [self.answer, keyboard_data, self.image]


class PersonAction(Action):
    def __init__(self, player):
        #довабить в статистику описание собстенности
        self.player = player
        self.answer = ""
        self.keyboard = ""
        self.image = ""

        self.mode = 3000
        self.keygen = KEYGEN


    def handle_special(self):
        txt = self.player.data.text

        if self.player.data.action == 3001:
            if txt!="Отмена" and txt!="Назад":
                self.player.data.bio = txt
            self.player.data.action = 3000
            txt = "Биография"
            self.player.data.text = "Биография"

        elif self.player.data.action == 3002:
            if txt!="Отмена" and txt!="Назад":
                self.player.note.add_note(txt)
    
            txt = "Записная книжка"
            self.player.data.text = "Записная книжка"
            self.player.data.action = 3000

        elif self.player.data.action == 3003:
            if txt!="Отмена" and txt!="Назад":
                self.player.note.drop_note(txt)
    
            txt = "Записная книжка"
            self.player.data.text = "Записная книжка"
            self.player.data.action = 3000

        else:
            pass

        if txt == "Характеристика":
            self.answer = "• Раса: "+self.player.race.name+"\n"\
                +"• Здоровье: "+"/".join(map(str,self.player.race.health))+"\n"\
                +"• Мана: "+"/".join(map(str,self.player.race.mana))+"\n"\
                +"• Атака: "+self.player.get_attack()+"\n"\
                +"• Защита: "+self.player.get_defence()+"\n"\
                +"• Магическая атака: "+self.player.get_mag_attack()+"\n"\
                +"• Магическая защита: "+self.player.get_mag_defence()+"\n"\
                +"• Вес инвентаря: "+self.player.get_weight()
        
        elif txt == "Статистика":
            self.answer = "• Имя: "+self.player.data.name+"\n"\
                "• Раса: "+self.player.race.name+"\n"\
                "• Возраст: "+str(self.player.data.age)+"\n"\
                "• Пол: "+self.player.data.gender+"\n"\
                "• Статус: "+str(self.player.get_dignity())+"\n"\
                "• Собственность: "+str(self.player.get_own())+"\n"\
                "• Дней в игре: "+self.player.get_timelapse()+"\n"\
                "• Местонахождение: "+MAP.get_position(self.player.data.position)+"\n"

        elif txt == "Биография":
            self.answer = self.player.data.bio

        elif txt == "Изменить био":
            self.player.data.action = 3001

        elif txt == "Записная книжка":
            self.answer = self.player.note.get_list()

        elif txt == "Добавить запись":
            self.player.data.action = 3002

        elif txt == "Удалить запись":
            self.player.data.action = 3003            

        else:
            pass

        if self.player.data.action in range(3000, 4000):
            pass
        else:
            self.player.data.action = 3000


    def handle_common(self):
       
        data = DATABASE.get_answer(self.player.data.text, self.mode)

        self.answer = data[0].replace(r"\n", "\n")+"\n"+self.answer
        self.keyboard=data[1]

    def get_reply(self):
        if self.keyboard == "":
            keyboard_data = telebot.types.ReplyKeyboardRemove()
        else:
            keyboard_data = telebot.types.ReplyKeyboardMarkup(True)
            self.keygen.generate(keyboard_data, self.keyboard)

        return [self.answer, keyboard_data, self.image]


class NoteAction(Action):
    def __init__(self, player):
        self.player = player
        self.answer = ""
        self.keyboard = ""
        self.image = ""

        self.mode = 4000
        self.keygen = KEYGEN


    def handle_special(self):



        self.player.data.action = 4000


    def handle_common(self):
        
        data = DATABASE.get_answer(self.player.data.text, self.mode)

        self.answer = data[0].replace(r"\n", "\n")+"\n"+self.answer
        self.keyboard = data[1]

    def get_reply(self):
        if self.keyboard == "":
            keyboard_data = telebot.types.ReplyKeyboardRemove()
        else:
            keyboard_data = telebot.types.ReplyKeyboardMarkup(True)
            self.keygen.generate(keyboard_data, self.keyboard)

        return [self.answer, keyboard_data, self.image]
