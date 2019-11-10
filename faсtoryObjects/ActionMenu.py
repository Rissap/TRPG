from interfaces import ActionInterface


class Menu(ActionInterface):
    def __init__(self, _Database):
        self.Database = _Database

    def handlePlayerAction(self, _Player):
        _Player.answer = ""
        _Player.keyboard = ""
        key = _Player.action

        if key == 0:
            pass
            
        else:
            pass

        return _Player
