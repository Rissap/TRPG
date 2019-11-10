from interfaces import WorldInterface
from factory import ActionFactory

from concreteRelease.PlayerRelease import SimplePlayer

class World(WorldInterface):
    """docstring for World"""
    def __init__(self, _Database):
        self.Database = _Database
        self.ActionFactory = ActionFactory()
        self.Action = None
        
        self.ConcretePlayer = None
        self.PlayerList = []

    def saveAllData():
        """save all data from playerList to Database"""
        pass

    def raisePlayerData(self, _id, _text):
        """get ConcretePlayer class"""
        _text = _text.replace("\"", "`").replace("'", "`")

        for player in self.PlayerList:
            if player.id == _id:
                self.ConcretePlayer = player
                self.ConcretePlayer.phrase = _text
                return None

        #if player not in list
        self.ConcretePlayer = SimplePlayer(_id)
        self.PlayerList.append(self.ConcretePlayer)
        self.ConcretePlayer.phrase = _text

    def refreshPlayerList(self):
        """set ConcretePlayer with changed data on his place into the list"""
        for position in range(len(self.PlayerList)):
            if self.PlayerList[position].id == self.ConcretePlayer.id:
                self.PlayerList[position] = self.ConcretePlayer
                break

    def updatePlayerAction(self):
        """add a phrase into the action for future processing"""
        self.Database.getAction(self.ConcretePlayer)

    def handlePlayerAction(self):
        """use fabric to set ActionClass and call a handle method"""
        self.Action = self.ActionFactory.getAction(self.ConcretePlayer)
        self.ConcretePlayer = self.Action.handlePlayerAction(self.ConcretePlayer)
        self.refreshPlayerList()



