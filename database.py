import sqlite3
import json

from person import Player
from person import PersonData
from person import race_list
from person import Note

GET_ANSWER = """ SELECT message.data, keyboard.data FROM scripts 
                JOIN message ON scripts.message=message.id
                JOIN keyboard ON scripts.keyboard=keyboard.id
                WHERE keyword='{0}' AND point={1} """

LATEST_ID = """ SELECT max(id) FROM player_race """

LATEST_QUEST = """ SELECT max(id) FROM player_quest """

LATEST_NOTE_ID = """ SELECT max(id) FROM notes """

GET_PLAYER_NOTE = """ SELECT data FROM notes WHERE player = {0} """

SAVE_PLAYER_NOTES = """ INSERT INTO notes VALUES ({0},{1},"{2}")"""

DROP_PLAYER_NOTES = """ DELETE FROM notes WHERE player={0}"""

THIS_ID = """ SELECT player_race FROM players WHERE id={0} """

LOAD_PLAYERS = """ SELECT * FROM players JOIN player_race ON player_race.id=players.player_race """

SAVE_RACE_DATA = """ INSERT INTO player_race VALUES ({0},"{1}",{2},{3},{4},{5},{6},{7},{8}) """

SAVE_PERSON_DATA = """ INSERT INTO players VALUES ({0},{1},"{2}","{3}",{4},"{5}","{6}","{7}","{8}") """

SELECT_PLACE_QUEST = """ SELECT name FROM quest_place JOIN quest ON quest.id=quest_place.quest  WHERE quest_place.place={0}"""

GET_SPECIAL_POSITION = """ SELECT * FROM special_place WHERE x={0} AND y={1} """

UPDATE_PERSON_DATA = """ UPDATE players SET age={4}, gender="{5}", bio="{6}", born="{7}", position="{8}" WHERE id={0} """

UPDATE_RACE_DATA = """ UPDATE player_race SET health={2}, mana={3}, attack={4}, defence={5}, magic_attack={6}, magic_defence={7}, weight={8} WHERE id={0}"""

SET_QUEST = """ INSERT INTO player_quest VALUES ({0}, {1}, {2}, "{3}")"""

IS_NUM_OF_QUEST = """ SELECT * FROM quest WHERE id={0} """

IS_ALREADY_TAKEN_QUEST = """ SELECT * FROM player_quest WHERE players={0} AND quest={1} """

GET_PLAYER_QUEST = """ SELECT quest.name FROM player_quest JOIN quest on player_quest.quest=quest.id WHERE players={0} AND status="{1}" """

class GlobalDatabase():
    def __init__(self):
        self.data = sqlite3.connect('database/bot.db', check_same_thread=False)
        self.base = self.data.cursor()
        
        self.quest = json.loads(open("database/quests.json", 'rb').read())

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

    def get_quest(self, uniq, point=None):
        if type(point)==list:
            x, y = point
            data = self.base.execute(GET_SPECIAL_POSITION.format(x, y)).fetchall()
            if data==[]:
                return "Здесь нет заданий!"
            uniq = data[0][0]                
        
        tmp=""
        data = self.base.execute(SELECT_PLACE_QUEST.format(uniq)).fetchall()
        if data!=[]:
            tmp+="\nДоступные задания:\n"
            i=1
            for el in data[0]:
                tmp+="№"+str(i)+" "+el+"\n"
                i+=1
            return tmp
        return "Здесь нет заданий!"

    def discover_place(self, position):
        x, y = position
        data = self.base.execute(GET_SPECIAL_POSITION.format(x, y)).fetchall()
        if data!=[]:
            tmp = data[0][3]
            tmp+=self.get_quest(data[0][0])

            return tmp
        else:
            return "Здесь нечего исследовать!"

    def accept_player_quest(self, uniq, text, request=False):
        try:
            text = int(text)-1
            d1 = self.base.execute(IS_NUM_OF_QUEST.format(text)).fetchall()
            d2 = self.base.execute(IS_ALREADY_TAKEN_QUEST.format(uniq, text)).fetchall()

            #if quest id is not in quest list
            if d1 == []:
                if request:
                    return None
                raise ValueError
        
            if request and d2 != []:
                name = d1[0][1]
                return self.quest[name]

            elif request and d2 == []:
                return None
            
            else:
                pass

            #if player already has this quest
            if d2 != []:
                raise ValueError

            ID = self.base.execute(LATEST_QUEST).fetchall()
            if ID[0][0] == None:
                ID = 1
            else:
                ID = ID[0][0]

            self.base.execute(SET_QUEST.format(ID, uniq, text, "apply"))
            self.data.commit()
            return "Ты успешно взял квест!"
        except Exception as E:
            print(E)
            return "Ты не смог взять квест!"

    def get_player_quest(self, uniq):
        tmp="\n"
        data = self.base.execute(GET_PLAYER_QUEST.format(uniq, "apply")).fetchall()
        if data == []:
            return "У тебя нет заданий!"
            
        for el in range(len(data)):
            tmp+="№ "+str(el+1)+" "+data[el][0]+"\n"
        return tmp

    def prepare_quest(self, uniq, text):
        return True


DATABASE = GlobalDatabase()
