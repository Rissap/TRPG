from database import DATABASE

from faсtoryObjects.ActionMenu import Menu
from faсtoryObjects.ActionQuest import Quest
from faсtoryObjects.ActionPerson import Person
from faсtoryObjects.ActionRegistration import Registration


MENU_RANGE = [90000, 100000, 200000, 300000, 400000, 98000, 99000]


class ActionFactory():
    def __init__(self):
        pass

    def getAction(self, _Player):
        if _Player.register:
            if _Player.action in MENU_RANGE:
                return Menu(DATABASE)

            elif _Player.action in rage(100000, 200000):
                
                return Person(DATABASE)
            
            else:
                return Menu(DATABASE)
        else:
            #player isn't register
            return Registration(DATABASE)