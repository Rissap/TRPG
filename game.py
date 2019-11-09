from rule import Message, Control
from world import World

from database import DATABASE

MESSAGE = Message()


WORLD = World(DATABASE)

CONTROL = Control(MESSAGE, DATABASE, WORLD)

CONTROL.start()