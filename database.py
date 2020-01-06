import sqlite3

from person import Player
from person import PersonData
from person import race_list

GET_ANSWER = """ SELECT message.data, keyboard.data FROM scripts 
                JOIN message ON scripts.message=message.id
                JOIN keyboard ON scripts.keyboard=keyboard.id
                WHERE keyword='{0}' AND point={1} """

LATEST_ID = """ SELECT max(id) FROM player_race """

THIS_ID = """ SELECT player_race FROM players WHERE id={0} """

LOAD_PLAYERS = """ SELECT * FROM players JOIN player_race ON player_race.id=players.player_race """

SAVE_RACE_DATA = """ INSERT INTO player_race VALUES ({0},"{1}",{2},{3},{4},{5},{6},{7},{8},{9}) """

SAVE_PERSON_DATA = """ INSERT INTO players VALUES ({0},{1},"{2}","{3}",{4},"{5}","{6}","{7}") """

UPDATE_RACE_DATA = """ UPDATE player_race SET name="{1}", health={2}, mana={3}, attack={4}, defence={5}, magic_attack={6}, magic_defence={7}, speed={8}, weight={9} WHERE id={0}"""

UPDATE_PERSON_DATA = """ UPDATE players SET action="{2}", name="{3}", age={4}, gender="{5}", bio="{6}", born="{7}" WHERE id={0} """

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

            tmp.race = race_list[el[9]]()
            tmp.race.load_data(el)

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

            self.base.execute(race.format(
                race_id,
                player.race.name,
                player.race.health[0],
                player.race.mana[0],
                player.race.attack[0],
                player.race.defence[0],
                player.race.magic_attack[0],
                player.race.magic_defence[0],
                player.race.speed[0],
                player.race.weight[0]
            ))

            self.base.execute(data.format(
                player.data.uniq,
                race_id,
                player.data.action,
                name,
                player.data.age,
                player.data.gender,
                player.data.bio,
                player.data.born
            ))

            self.data.commit()


DATABASE = GlobalDatabase()

'''




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

    def getAllInvenntory(self, _id):
        return None

    def getAllQuest(self, _id):
        self.base.execute()


        return None

    def raiseAllData(self):
        playerData = self.base.execute(ALL_FROM_PLAYER).fetchall()
        #get race from data collection and from dictionary with races select one and call copy constructor
        mass = []
        for el in playerData:
            pers = race[el[4]](None)
            pers.setData(el)

            quest = self.getAllQuest(pers.id)
            inventory = self.getAllInventory(pers.id)

            questCont = QuestContainer(quest)
            inventoryCont = InventoryContainer(inventory)

            pers.setContainer(questCont, inventoryCont)
            mass.append(pers)

        return mass
        
    def saveAllData(self, mass):
        for player in mass:
            if self.base.execute(PLAYER_ALREADY_EXIST.format(player.id)).fetchall()==[]:
                STRING_DATA = NEW_PLAYER_DATA
            else:
                STRING_DATA = OLD_PLAYER_DATA

            self.base.execute(
                STRING_DATA.format(player.id, player.action, player.name, player.gender, 
                    player.race, player.age, player.bio, player.register, player.gold, player.glory, ",".join(map(str, player.position)) ))

        self.data.commit()
'''
