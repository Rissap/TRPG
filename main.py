import telebot
import datetime

from secureFile import token #my .gitignore file with token

from database import DATABASE

from action import MainAction
from action import RegisterAction
from action import PreRegisterAction

from person import Player
from person import PersonData


class GlobalControlHandler():
    def __init__(self):
        self.action = None #one from action module

        self.this_player = None
        self.this_player_index = None

        self.answer = ""
        self.keyboard = None
        self.image = ""

        self.players = []

    def save_all(self):
        for player in self.players:
            DATABASE.save_player(player)
            DATABASE.save_notes(player.data.uniq, player.note.note_list)

    def load_all(self):
        self.players = DATABASE.load_player()

    def handle_special_request(self, uniq:int, command:str):
        self.handle_request(uniq, "")
        if command == "start":
            self.answer = "Свежая кровь желает стать частью чего-то большего?"
            self.keyboard = telebot.types.ReplyKeyboardMarkup(True)
            self.keyboard.row('Что это за место?', 'Кто ты?')
            self.keyboard.row('Начать приключение!')
            self.keyboard.row('Краткое инфо', 'О ролевой')

    def handle_request(self, uniq:int, text:str):
        for person in self.players:
            if person.data.uniq == uniq:
                self.this_player = person
                self.this_player_index = self.players.index(person)
                self.this_player.new_message(text)
                return True

        #if person doesn't exists
        self.players.append(Player(PersonData(uniq)))
        self.this_player = self.players[-1]
        self.this_player_index = len(self.players)-1
        self.this_player.new_message(text)

    def handle_player(self):
        #factory method
        if self.this_player.data.register == False:
            self.action = PreRegisterAction()

        elif self.this_player.data.register == None:
            self.action = RegisterAction()

        elif self.this_player.data.register == True:
            self.action = MainAction()

        else:
            pass

        self.action.set_player(self.this_player)
        self.action.handle_special()
        self.action.handle_common()

        self.players[self.this_player_index] = self.this_player

        #check keyboard
        self.answer, self.keyboard, self.image = self.action.get_reply()

    def reply(self, bot):
        if self.answer == "":
        	self.answer = "Я не могу ответить"
        bot.send_message(self.this_player.data.uniq,
            self.answer, reply_markup=self.keyboard)
        if self.image!="":
            bot.send_photo(self.this_player.data.uniq, photo=self.image)


Global = GlobalControlHandler()
Global.load_all()

print("START")

bot = telebot.TeleBot(token)

#handle messages
@bot.message_handler(commands=['start'])
def special(message):
    Global.handle_special_request(message.chat.id, "start")
    Global.reply(bot)

@bot.message_handler(commands=['stop'])
def special(message):
    if message.chat.id == 331535417:
        Global.save_all()
        bot.send_message(message.chat.id, "Мой создатель. Благодарю за отдых.")
        bot.stop_polling()
    else:
        bot.send_message(message.chat.id, "Ахах, шалунишка. Ты не имеешь надо мной власти.")


@bot.message_handler(content_types=['text'])
def common(message):
    Global.handle_request(message.chat.id, message.text)
    Global.handle_player()
    Global.reply(bot)


bot.infinity_polling()