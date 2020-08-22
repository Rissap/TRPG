from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

from db import storage as Collection

from src.system import answer as AnswerSys
from src.system import mainSys as MainSys

class World:
    def get_reply(self, index, message, action):
        reply, additional, keyboard = "", "", None

        if action:
            indexes, additional = MainSys.process(index, message, action)
        else:
            indexes, additional = AnswerSys.process(index, message)

        try:
            Ireply, Ikeyboard, Iaction = indexes
            reply = Collection.MESSAGE[Ireply] + additional
            Collection.PLAYER_ACTION[index] = Collection.ACTION[Iaction]
        except Exception as E:
            print("[WORLD]: ", E)


        if Ikeyboard is None:
            keyboard = ReplyKeyboardRemove()
        else:
            keyboard = ReplyKeyboardMarkup(
                keyboard=Collection.KEYBOARD[Ikeyboard],
                resize_keyboard=True,
                one_time_keyboard=False)
        return [reply, keyboard]


class ProcessRequest:
    WORLD = World()

    def process(self, user, message):
        for obj in Collection.PLAYERS:
            if obj["id"] == user:
                index = obj["index"]
                process = Collection.PLAYER_ACTION[index]
                reply = self.WORLD.get_reply(index, message, process)
                return reply

        Collection.set_new_player(user)
        reply = self.WORLD.get_reply(-1, message, None)
        return reply

    def stop(self):
        Collection.store_data()
