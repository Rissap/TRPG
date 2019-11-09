from database import DATABASE

from faсtoryObjects.ActionQuest import Quest
from faсtoryObjects.ActionRegistration import Registration

from concreteRelease.PlayerRelease import Alasi, Artifex, Elementali, Wilder, Fox


class ActionFactory():
    def __init__(self):
        pass

    def getAction(self, _Player):
        if _Player.register:
            if _Player.action == 100000:
                return Menu(DATABASE)

            elif _Player.action == 9999:
                _Player.action = 100000
                return Menu(DATABASE)
            
            else:
                pass
        else:
            #player isn't register
            return Registration(DATABASE)