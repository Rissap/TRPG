from db import storage as Collection

from src.system import registration as RegistrationSys
from src.system import statsSystem as StatsSys

def process(index, message, action):
    indexes, additional = None, ""

    if not Collection.BOOL[index]["register"]:
        system = RegistrationSys
    elif action in Collection.PERSON_ACTION_KEYS:
        system = StatsSys
    else:
        pass

    indexes, additional = system.process(index, message, action)
    return [indexes, additional]
