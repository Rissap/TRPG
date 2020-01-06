import telebot

from map import MAP
from database import DATABASE

from abc import ABC
from abc import abstractmethod

from keygen import KeyboardGenerator


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
        self.keygen = KeyboardGenerator()


    def handle_special(self):
        pass


    def handle_common(self):

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


class QuestAction(Action):
    def __init__(self, player):
        self.player = player
        self.answer = ""
        self.keyboard = ""
        self.image = ""

        self.mode = 2000
        self.keygen = KeyboardGenerator()


    def handle_special(self):
        pass


    def handle_common(self):

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


class PersonAction(Action):
    def __init__(self, player):
        self.player = player
        self.answer = ""
        self.keyboard = ""
        self.image = ""

        self.mode = 3000
        self.keygen = KeyboardGenerator()


    def handle_special(self):
        pass


    def handle_common(self):
       
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


class NoteAction(Action):
    def __init__(self, player):
        self.player = player
        self.answer = ""
        self.keyboard = ""
        self.image = ""

        self.mode = 4000
        self.keygen = KeyboardGenerator()


    def handle_special(self):
        pass


    def handle_common(self):
        
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