from interfaces import ActionInterface

class Registration(ActionInterface):
    def __init__(self, _Database):
        self.Database = _Database

    def handlePlayerAction(self, _Player):
        key = _Player.action
        if key == 1:
            pass
