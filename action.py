import telebot

from abc import ABC
from abc import abstractmethod

from datetime import date

from database import DATABASE
from keygen import KeyboardGenerator

from mainaction import WorldAction
from mainaction import PersonAction
from mainaction import QuestAction
from mainaction import NoteAction





class Action(ABC):
    @abstractmethod
    def set_player(self):
        pass

    @abstractmethod
    def handle_special(self):
        pass

    @abstractmethod
    def handle_common(self):
        pass

    @abstractmethod
    def get_reply(self):
        pass


class PreRegisterAction(Action):
    def __init__(self):
        self.player = None
        self.answer = ""
        self.keyboard = ""
        self.image = ""

        self.keygen = KeyboardGenerator()

    def set_player(self, player):
        self.player = player

    def handle_special(self):
        pass

    def handle_common(self):
        if self.player.data.text == "Начать приключение!":
            self.player.data.register = None

        data = DATABASE.get_answer(self.player.data.text, 1)
        self.answer+="\n"+data[0].replace(r"\n", "\n")
        self.keyboard=data[1]

    def get_reply(self):
        if self.keyboard == "":
            keyboard_data = telebot.types.ReplyKeyboardRemove()
        else:
            keyboard_data = telebot.types.ReplyKeyboardMarkup(True)
            self.keygen.generate(keyboard_data, self.keyboard)

        return [self.answer, keyboard_data, self.image]


class RegisterAction(Action):
    def __init__(self):
        self.player = None
        self.answer = ""
        self.keyboard = ""
        self.image = ""

        self.mode = 2
        self.race_list = ["Аласи","Элементали","Перевёртыши","Артифексы"]
        self.gender_list = ["Господин", "Госпожа"]
        self.keygen = KeyboardGenerator()

    def set_player(self, player):
        self.player = player

    def set_race_stats(self, race):
        pass

    def handle_special(self):
        if self.player.data.action == None:
            self.player.data.name = self.player.data.text

            self.player.data.action = "age"
            self.player.data.text = "age"

        elif self.player.data.action == "age":
            try:
                number = int(self.player.data.text)
                if number > 15 and number < 91:
                    self.player.data.age = number

                    self.player.data.action = "race"
                    self.player.data.text = "race"
                else:
                    raise Exception
            except:
                self.player.data.action = "age"
                self.player.data.text = "age"

        elif self.player.data.action == "race":
            if self.player.data.text in self.race_list:
                self.player.set_race_stats(self.player.data.text)

                self.player.data.action = "gender"
                self.player.data.text = "gender"
            else:
                self.player.data.action = "race"
                self.player.data.text = "race"

        elif self.player.data.action == "gender":
            if self.player.data.text in self.gender_list:
                self.player.data.gender = self.player.data.text

                self.player.data.text = "bio"
                self.player.data.action = "bio"
            else:
                self.player.data.action = "gender"
                self.player.data.text = "gender"

        elif self.player.data.action == "bio":
            self.player.data.bio = self.player.data.text

            self.player.data.text = "confirm"
            self.player.data.action = "confirm"
            self.answer+=str(self.player)

        elif self.player.data.action == "confirm":
            if self.player.data.text == "Да, всё верно!":
                self.player.data.register = True

                self.player.data.action == 0
                self.player.data.text = "registered"
                born = date.today()
                self.player.data.born = str(born.day)+"-"+str(born.month)+"-"+str(born.year)
            else:
                self.player.data.text = "Начать приключение!"
                self.player.data.action = None
                self.mode = 1

        else:
            pass

    def handle_common(self):
        if self.player.data.text == "Да, всё верно!":
            self.player.data.register = True

        data = DATABASE.get_answer(self.player.data.text, self.mode)
        self.mode = 2

        self.answer = data[0].replace(r"\n", "\n")+"\n"+self.answer
        self.keyboard=data[1]

    def get_reply(self):
        if self.keyboard == "":
            keyboard_data = telebot.types.ReplyKeyboardRemove()
        else:
            keyboard_data = telebot.types.ReplyKeyboardMarkup(True)
            self.keygen.generate(keyboard_data, self.keyboard)

        return [self.answer, keyboard_data, self.image]


class DefaultHandler():
    def __init__(self, type_reply):
        self.type_reply = type_reply

        self.answer = ""
        self.keyboard = ""
        self.image = ""
        
        self.keygen = KeyboardGenerator()

    def set_player(self, player):
        self.player = player

    def handle_special(self):
        pass

    def handle_common(self):
        
        if self.type_reply == "unknown":
            data = DATABASE.get_answer("ы", 3) #return default main menu
            self.answer+="\n"+data[0].replace(r"\n", "\n")
            self.keyboard=data[1]
        
        elif self.type_reply == "back":
            data = DATABASE.get_answer("ы", 3) #return default main menu for keyboard only
            self.answer="Назад так назад" #change answer
            self.keyboard=data[1]    

        else:
            pass


    def get_reply(self):
        keyboard_data = telebot.types.ReplyKeyboardMarkup(True)
        self.keygen.generate(keyboard_data, self.keyboard)
        return [self.answer, keyboard_data, self.image]





class MainAction():
    def __init__(self):
        self.player = None
        self.answer_data = None

        self.action_handler = None


    def set_player(self, player):
        self.player = player

        self.set_action_handler()
        
        self.action_handler.handle_special()
        self.action_handler.handle_common()

        self.answer_data = self.action_handler.get_reply()

    def set_action_handler(self):
        txt = self.player.data.text
        act = self.player.data.action

        if act in range(1000, 2000) or txt == "Мир":
            self.action_handler = WorldAction(self.player)
        
        elif act in range(2000, 3000) or txt == "Задания":
            self.action_handler = QuestAction(self.player)

        elif act in range(3000, 4000) or txt == "Персонаж":
            self.action_handler = PersonAction(self.player)

        elif act in range(4000, 5000) or txt == "Блокнот":
            self.action_handler = NoteAction(self.player)
        
        elif txt == "Назад" or act == 999:
            self.action_handler = DefaultHandler("back")
        else:
            self.action_handler = DefaultHandler("unknown")



    def get_reply(self):
        return self.answer_data

    def handle_special(self):
        pass

    def handle_common(self):
        pass