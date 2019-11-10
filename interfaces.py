class WorldInterface():
    """docstring for WorldInterface"""
    def __init__(self, _Database):
        self.Database = _Database
        self.infoForPlayer = ""

    def saveAllData():
        pass

    def raisePlayerData(self, _id):
        pass

    def handlePlayerRequest(self, _text):
        pass

    def getText(self):
        pass


class PersonInterface():
    """docstring for PlayerInterface"""
    def __init__(self):
        self.phrase = ""
        self.answer = ""
        self.keyboard = ""
        self.action = 0

        self.name = ""
        self.gender = ""
        
        self.age = 0
        self.race = ""
        self.bio = ""

    def setPhrase(self, _text):
        self.phrase = _text

    def getAnswer(self):
        return self.answer

    def getKeyboard(self):
        return self.keyboard


class AnimalInterface():
    """docstring for AnimalInterface"""
    def __init__(self):
        pass


class InventoryInterface():
    """docstring for InventoryInterface"""
    def __init__(self):
        pass


class ItemInterface():
    """docstring for ItemInterface"""
    def __init__(self):
        pass


class QuestInterface():
    """docstring for QuestInterface"""
    def __init__(self):
        pass


class EquipmentInterface():
    """docstring for EquipmentInterface"""
    def __init__(self):
        pass

class ActionInterface():
    """docstring for ActionInterface"""
    def __init__(self):
        pass

    def handlePlayerData(self, _Player):
        pass
