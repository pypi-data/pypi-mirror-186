from .turtleAgent import Turtle
from .envBuilder import *
from .generator import *
# @DEBUG from .turtleAgent import Turtle
# @DEBUG from .envBuilder import *
# @DEBUG from .generator import *
import time
import random
from enum import Enum

class Action(Enum):
    FORWARD = 0, "Forward"
    TURN_RIGHT = 1, "Turn_right"
    TURN_LEFT = 2, "Turn_left"
    TOUCH = 3, "Touch"

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value

class Feedback(Enum):
    COLLISION = 0, "Collision"
    MOVED = 1, "Moved"
    IS_ON_PIZZA = 2, "Is_on_pizza"
    TOUCHED_WALL = 3, "Touched_wall"
    TOUCHED_NOTHING = 4, "Touched_nothing"
    TOUCHED_PIZZA = 5, "Touched_pizza"

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value

class Game:
    def __init__(self, envName, gui):
        self.envName = envName
        self.gui = gui
        pass

    def start(self):
        # Instanciate the envBuilder
        envbuilder = EnvBuilder(name=self.envName, gui=self.gui)
        # creates the grid and the turtle
        agent, env = envbuilder.build_grid()
        return Turtle(agent, env)


