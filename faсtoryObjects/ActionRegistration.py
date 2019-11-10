from interfaces import ActionInterface

from concreteRelease.PlayerRelease import Alasi, Artifex, Elementali, Wilder, Fox

CREATED_PERSON = """{0} {1} в возрасте {2}\nРаса: {3}\nБиография: {4}\n"""

race = {
    "Аласи": Alasi,
    "Артифексы": Artifex,
    "Перевёртыши": Wilder,
    "Элементали": Elementali
}


class Registration(ActionInterface):
    def __init__(self, _Database):
        self.Database = _Database

    def handlePlayerAction(self, _Player):
        _Player.answer = ""
        _Player.keyboard = ""
        key = _Player.action

        if key == 10:
            _Player.name = _Player.phrase
            _Player.phrase = 'gender'

        elif key == 11:
            if _Player.phrase == "М":
                _Player.gender = "Господин"
                _Player.phrase = "race"

            elif _Player.phrase == "Ж":
                _Player.gender = "Госпожа"
                _Player.phrase = "race"

            else:
                _Player.phrase = 'gender'

        elif key == 12:
            if self.Database.isAvailableRace(_Player.phrase):
                _Player = race[_Player.phrase](_Player)
                _Player.phrase = "age"
            else:
                _Player.phrase = "race"

        elif key == 13:
            try:
                if int(_Player.phrase)>9 and int(_Player.phrase)<91:
                    _Player.age = int(_Player.phrase)
                    _Player.phrase = "bio"
                else:
                    _Player.phrase = "age"
            except Exception as E:
                print(E)
                _Player.phrase = "age"

        elif key == 14:
            _Player.bio = _Player.phrase

            _Player.answer = CREATED_PERSON\
                .format(_Player.gender, _Player.name, _Player.age, _Player.race, _Player.bio)
            _Player.phrase = "confirm"


        elif key == 15:
            if _Player.phrase == "Да, всё верно!":
                _Player.register = True
            elif _Player.phrase == "Нет, пересоздать пресонажа!":
                pass
            else:
                _Player.answer = CREATED_PERSON\
                    .format(_Player.gender, _Player.name, _Player.age, _Player.race, _Player.bio)
                _Player.phrase = "confirm"

        else:
            pass

        return _Player
