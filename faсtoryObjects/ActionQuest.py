from interfaces import ActionInterface

class Quest(ActionInterface):
    def __init__(self, _Database):
        self.Database = _Database

    def handlePlayerAction(self, _Player):
        pass