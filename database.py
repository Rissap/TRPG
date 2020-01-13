import sqlite3

from person import Player
from person import PersonData
from person import race_list
from person import Note

GET_ANSWER = """ SELECT message.data, keyboard.data FROM scripts 
                JOIN message ON scripts.message=message.id
                JOIN keyboard ON scripts.keyboard=keyboard.id
                WHERE keyword='{0}' AND point={1} """

LATEST_ID = """ SELECT max(id) FROM player_race """

LATEST_NOTE_ID = """ SELECT max(id) FROM notes """

GET_PLAYER_NOTE = """ SELECT data FROM notes WHERE player = {0} """

SAVE_PLAYER_NOTES = """ INSERT INTO notes VALUES ({0},{1},"{2}")"""

DROP_PLAYER_NOTES = """ DELETE FROM notes WHERE player={0}"""

THIS_ID = """ SELECT player_race FROM players WHERE id={0} """

LOAD_PLAYERS = """ SELECT * FROM players JOIN player_race ON player_race.id=players.player_race """

SAVE_RACE_DATA = """ INSERT INTO player_race VALUES ({0},"{1}",{2},{3},{4},{5},{6},{7},{8}) """

SAVE_PERSON_DATA = """ INSERT INTO players VALUES ({0},{1},"{2}","{3}",{4},"{5}","{6}","{7}","{8}") """

UPDATE_PERSON_DATA = """ UPDATE players SET age={4}, gender="{5}", bio="{6}", born="{7}", position="{8}" WHERE id={0} """

UPDATE_RACE_DATA = """ UPDATE player_race SET health={2}, mana={3}, attack={4}, defence={5}, magic_attack={6}, magic_defence={7}, weight={8} WHERE id={0}"""

'''
IS_RACE = """ SELECT * from `race` WHERE name='{0}' AND id<5 """

ALL_FROM_PLAYER = """ SELECT * FROM player  """

PLAYER_ALREADY_EXIST = """ SELECT * FROM player WHERE id={0} """

NEW_PLAYER_DATA = """ INSERT INTO player VALUES ({0}, {1}, '{2}', '{3}', '{4}', {5}, '{6}', '{7}', {8}, {9}, '{10}' ) """

OLD_PLAYER_DATA = """ UPDATE player SET action={1} name='{2}' gender='{3}' race='{4}' age={5} bio='{6}' register='{7}' gold = {8} glory={9} position = '{10}' """
'''


class GlobalDatabase():
    def __init__(self):
        self.data = sqlite3.connect('database/bot.db', check_same_thread=False)
        self.base = self.data.cursor()

    def get_answer(self, text, point):
        answer = self.base.execute(GET_ANSWER.format(text, point)).fetchall()

        if answer == []:
            if point == 1:
                return ["Не понял тебя. Попробуй сказать иначе!","Что это за место?|Кто ты?||Начать приключение!||Краткое инфо|О ролевой"]
            elif point == 2:
                pass
            elif point == 3:
                return ["Не понял тебя. Попробуй сказать иначе!", "Персонаж||Мир||Задания||Блокнот||Помощь|Ошибки"]
            else:
                return ["Не понял тебя. Попробуй сказать иначе!", "Персонаж||Мир||Задания||Блокнот||Помощь|Ошибки"]
        return answer[0]

    def load_player(self):
        players = self.base.execute(LOAD_PLAYERS).fetchall()
        player_list = []
        
        for el in players:
            tmp = Player(PersonData(el[0]))
            tmp.data.load_data(el)

            for race in race_list.keys():
                if race in el:
                    tmp.race = race_list[race]()
            tmp.race.load_data(el[len(el)-9:])

            note = self.base.execute(GET_PLAYER_NOTE.format(el[0])).fetchall()
            if note != []:
                tmp.note = Note(note)

            player_list.append(tmp)

        del players
        return player_list

    def save_player(self, player):
        if player.data.register:
            keys = self.data.execute(THIS_ID.format(player.data.uniq)).fetchall()
            
            if keys==[]:
                try:
                    race_id = self.base.execute(LATEST_ID).fetchall()[0][0]+1
                except:
                    race_id = 0
                data = SAVE_PERSON_DATA
                race = SAVE_RACE_DATA
            else:
                race_id = self.base.execute(THIS_ID.format(player.data.uniq)).fetchall()[0][0]
                data = UPDATE_PERSON_DATA
                race = UPDATE_RACE_DATA

            name = player.data.name.replace("\"", "`")
            name = name.replace("'", "`")
            position = str(player.data.position[0])+" "+str(player.data.position[1])

            self.base.execute(data.format(
                player.data.uniq,
                race_id,
                player.data.action,
                name,
                player.data.age,
                player.data.gender,
                player.data.bio,
                player.data.born,
                position
            ))

            self.base.execute(race.format(
                race_id,
                player.race.name,
                player.race.health[0],
                player.race.mana[0],
                player.race.attack[0],
                player.race.defence[0],
                player.race.magic_attack[0],
                player.race.magic_defence[0],
                player.race.weight[1]
            ))


            self.data.commit()

    def save_notes(self, uniq, notes):
        self.base.execute(DROP_PLAYER_NOTES.format(uniq))
        
        try:
            note_id = self.base.execute(LATEST_NOTE_ID).fetchall()[0][0]+1
        except:
            note_id = 0

        for el in notes:
            self.base.execute(SAVE_PLAYER_NOTES.format(note_id, uniq, el))
            note_id+=1

        self.data.commit()


DATABASE = GlobalDatabase()
