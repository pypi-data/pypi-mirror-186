from abc import ABC, abstractmethod
from PyQt5 import QtGui


class Agent(ABC):
    xPos = None
    yPos = None

    def __init__(self, xPos: int = None, yPos: int = None):
        self.xPos = xPos
        self.yPos = yPos

    @abstractmethod
    def next(self, env: 'list[list]'):
        pass

    @abstractmethod
    def display(self, painter: QtGui.QPainter):
        pass

    def getPos(self):
        return self.xPos, self.yPos
