import telebot

from map import MAP
from db import DATABASE

from abc import ABC
from abc import abstractmethod

from keygen import KEYGEN
from map import MAP


MINI_MAP = 16

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

    def set_coord(self, x_move, y_move, position):
        x, y = position

        if x_move == "left":
            x-=1
        if x_move == "right":
            x+=1
        
        if y_move == "up":
            y-=1
        if y_move == "down":
            y+=1

        self.player.data.position = MAP.move_person(position, [x, y])
        self.image = MAP.get_map(self.player.data.position, MINI_MAP)
        self.answer = "Переместились!\n"+MAP.get_point_description(self.player.data.position)+" ".join(map(str, self.player.data.position))


    def handle_special(self):
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

        elif self.player.data.action == 1002:
            self.answer = DATABASE.accept_player_quest(self.player.data.uniq, text)
            self.player.data.text = "Местность"
            self.player.data.action = 1000

        elif text == "Глобальная":
            self.image = MAP.get_map(self.player.data.position, 100)

        elif text == "Местности":
            self.image = MAP.get_map(self.player.data.position, 16)

        elif text == "Координаты":
            self.player.data.action = 1001

        elif text == "Местность":
            self.answer = MAP.get_point_description(self.player.data.position)

        elif text == "Исследовать":
            self.answer = DATABASE.discover_place(self.player.data.position)

        elif text == "Взять задание":
            self.answer = DATABASE.get_quest_list(self.player.data.position)
            if "1" in self.answer:
                self.player.data.action = 1002
                self.answer+="\nВведи номер задания, которое хочешь взять:"
            else:
                self.player.data.action = 1000
                self.answer += "В этой местности нет заданий!"

        #arrows encoding
        elif text.encode('UTF-8') == b'\xe2\x86\x96':
            self.set_coord("left", "up", self.player.data.position[:])
            self.player.data.text = "Перемещение"

        elif text.encode('UTF-8') == b'\xe2\x86\x97':
            self.set_coord("right", "up", self.player.data.position[:])
            self.player.data.text = "Перемещение"

        elif text.encode('UTF-8') == b'\xe2\x86\x99':
            self.set_coord("left", "down", self.player.data.position[:])
            self.player.data.text = "Перемещение"

        elif text.encode('UTF-8') == b'\xe2\x86\x98':
            self.set_coord("right", "down", self.player.data.position[:])
            self.player.data.text = "Перемещение"

        elif text.encode('UTF-8') == b'\xe2\x86\x91':
            self.set_coord(None, "up", self.player.data.position[:])
            self.player.data.text = "Перемещение"

        elif text.encode('UTF-8') == b'\xe2\x86\x93':
            self.set_coord(None, "down", self.player.data.position[:])
            self.player.data.text = "Перемещение"

        elif text.encode('UTF-8') == b'\xe2\x86\x90':
            self.set_coord("left", None, self.player.data.position[:])
            self.player.data.text = "Перемещение"

        elif text.encode('UTF-8') == b'\xe2\x86\x92':
            self.set_coord("right", None, self.player.data.position[:])
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
            self.answer = data[0].replace(r"\n", "\n\n")+self.answer

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
        text = self.player.data.text
        act = self.player.data.action

        if act == 2001:
            self.player.data.quest = DATABASE.accept_player_quest(self.player.data.uniq, text, True)
            if self.player.data.quest == None:
                self.player.data.action = 2000
            else:

                self.answer = self.player.data.quest["start"]["caption"]
                self.keyboard = self.player.data.quest["start"]["keyboard"]
                self.player.data.action = 5000


        else:
            pass

        if text == "Задания":
            self.answer = DATABASE.get_player_quest(self.player.data.uniq)

        elif text == "Начать задание":
            self.answer = DATABASE.get_player_quest(self.player.data.uniq)
            if "1" in self.answer:
                self.player.data.action = 2001
            else:
                self.player.data.text = "Задания"


        else:
            pass
         


        if self.player.data.action in range(2000, 3000) or self.player.data.action == 5000:
            pass
        else:
            self.player.data.action = 2000


    def handle_common(self):

        data = DATABASE.get_answer(self.player.data.text, self.mode)

        if self.player.data.action != 5000:
            self.answer = data[0].replace(r"\n", "\n")+"\n"+self.answer
        
        if self.player.data.action != 5000:
            self.keyboard=data[1]



    def get_reply(self):
        if self.keyboard == "":
            keyboard_data = telebot.types.ReplyKeyboardRemove()
        else:
            keyboard_data = telebot.types.ReplyKeyboardMarkup(True)
            self.keygen.generate(keyboard_data, self.keyboard)

        return [self.answer, keyboard_data, self.image]


class ConcreteQuest(Action):
    def __init__(self, player):
        self.player = player
        
        self.quest = self.player.data.quest
        self.tmp_quest = None
        self.step = self.player.data.quest_step

        self.answer = ""
        self.keyboard = ""
        self.image = ""

        self.keygen = KEYGEN

    def step_loop(self):
        self.tmp = self.quest["start"]
        for el in self.step:
            self.tmp = self.quest[el]

    def handle_special(self):
        text = self.player.data.text

        self.step_loop()
        if text in self.tmp["keyboard"]:
            if text == "Завершить квест":
                self.player.data.action = 2000
            else:
                self.tmp = self.quest[text]
                self.player.data.quest_step.append(text)
        
        if self.player.data.action == 2000:
            self.player.data.quest = None
            self.answer = "Квест окончен"
            self.keyboard = "Начать задание||Отказаться от задания||Статистика заданий||Ежедневки||Назад|,"
        else:
            self.answer = self.tmp["caption"]
            self.keyboard = self.tmp["keyboard"] 
        
        #print(self.step["require"], self.step["revard"])
        
 
    def handle_common(self):
        pass


    def get_reply(self):
        print("concrete ", self.keyboard)
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
                +"❤ Здоровье: "+"/".join(map(str,self.player.race.health))+"\n"\
                +"• Мана: "+"/".join(map(str,self.player.race.mana))+"\n"\
                +"⚔ Атака: "+self.player.get_attack()+"\n"\
                +"🛡 Защита: "+self.player.get_defence()+"\n"\
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
                "• Местонахождение: "+MAP.get_point_description(self.player.data.position)+"\n"

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
