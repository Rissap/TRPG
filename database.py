GET_ANSWER = """ SELECT script.data, keyboard.data, keyword.action FROM 'keyword' 
                JOIN 'script' ON script.id = keyword.script
                JOIN 'keyboard' ON keyboard.id = keyword.keyboard
                WHERE key='{0}' """


import sqlite3

class Database():
    """docstring for Database"""
    def __init__(self):
        self.data = sqlite3.connect('database/bot.db')
        self.base = self.data.cursor()

    def getAction(self, _Player, phrase):
        string = self.base.execute(GET_ANSWER.format(phrase)).fetchall()        
        if string == []:
            string = self.base.execute(GET_ANSWER.format(_Player.register)).fetchall()

        _Player.answer = string[0][0]
        _Player.keyboard = string[0][1]
        _Player.action = string[0][2]

        

DATABASE = Database()