from interfaces import PersonInterface

class SimplePlayer(PersonInterface):
    """docstring for Player"""
    def __init__(self, _id):
        super().__init__()
        self.id = _id
        self.register = False


class Alasi(PersonInterface):
    """docstring for Alasi"""
    def __init__(self, _Player):
        super().__init__()
        self.id = _Player.id
        self.register = False
        self.action = _Player.action


class Elementali(PersonInterface):
    def __init__(self, _Player):
        super().__init__()
        self.id = _Player.action
        self.register = False
        self.action = _Player.action


class Artifex(PersonInterface):
    def __init__(self, _Player):
        super().__init__()
        self.id = _Player.id
        self.register = False
        self.action = _Player.action


class Wilder(PersonInterface):
    def __init__(self, _Player):
        super().__init__()
        self.id = _Player.id
        self.register = False
        self.action = _Player.action


class Fox(PersonInterface):
    def __init__(self, _id):
        super().__init__()
        self.id = _id
        self.register = False
        self.action = []

