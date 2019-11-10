GET_ANSWER = """ SELECT script.data, keyboard.data, keyword.action FROM 'keyword' 
                JOIN 'script' ON script.id = keyword.script
                JOIN 'keyboard' ON keyboard.id = keyword.keyboard
                WHERE key='{0}' """
IS_RACE = """ SELECT * from `race` WHERE name='{0}' AND id<5 """

import sqlite3

class Database():
    """docstring for Database"""
    def __init__(self):
        self.data = sqlite3.connect('database/bot.db')
        self.base = self.data.cursor()

    def getAction(self, _Player):
        string = self.base.execute(GET_ANSWER.format(_Player.phrase)).fetchall()        
        if string == []:
            string = self.base.execute(GET_ANSWER.format(_Player.register)).fetchall()

        _Player.answer = string[0][0].replace(r"\n", "\n")+_Player.answer
        _Player.keyboard = string[0][1]
        _Player.action = string[0][2]

        return _Player

    def isAvailableRace(self, phrase):
        race = self.base.execute(IS_RACE.format(phrase)).fetchall()
        print(phrase)
        print(race)
        if race == []:
            return False
        return True
        

DATABASE = Database()