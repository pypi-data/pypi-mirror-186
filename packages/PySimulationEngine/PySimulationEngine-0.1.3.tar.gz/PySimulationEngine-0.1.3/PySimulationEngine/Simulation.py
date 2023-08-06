import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from .MainWindow import MainWindow
from .LayoutWidget import LayoutWidget
from .Statistic import Statistic
from .Display import Display
from .StartPauseButton import StartPauseButton
from .WorldView import WorldView
from .WorldViewUpdater import WorldViewUpdater


class Simulation():
    def __init__(self, worldView: WorldView = None):
        self.__app = QtWidgets.QApplication(sys.argv)
        self.__speed = 1
        self.__statistics: Statistic = []
        self.__terminalClosure = True
        display = Display(self.__updater)
        layout = LayoutWidget(display)
        self.__mainWindow = MainWindow(layout)
        self.__timer = QtCore.QTimer(display)
        self.__worldView = worldView
        self.__worldViewUpdaters = []


        self.__startPauseButton = StartPauseButton(self.__mainWindow, self.__startPauseClickMethod)
        self.__timer.timeout.connect(display.update)
        self.__timer.setInterval(self.__speed*100)  # Update the rectangle every (100 * self.__speed) milliseconds

        self.x, self.y = 10, 10

    def launchGui(self):
        self.__mainWindow.show()
        sys.exit(self.__app.exec_())

    def getWorldView(self):
        return self.__worldView
    
    def setSpeed(self, newSpeed: int):
        self.__speed = newSpeed
        self.__timer.setInterval(self.__speed*100)
    
    def addWorldViewUpdater(self, updater: WorldViewUpdater):
        self.__worldViewUpdaters.append(updater)

    def __startPauseClickMethod(self, started: bool):
        if started:
            self.__timer.stop()
        else:
            self.__timer.start()
    
    def __updater(self, painter: QtGui.QPainter):
        if self.__worldView is not None:
            agents = self.__worldView.getAgents()
            env = self.__worldView.getEnv()
            for a in agents:
                a.next(env)
                a.display(painter)
            for u in self.__worldViewUpdaters:
                u.update(self.__worldView)
        else:
            painter.setBrush(QtGui.QBrush(QtGui.QColor('#ff0000')))  # Set the fill color to red
            painter.drawRect(self.x,self.y,10,10)
            self.x = self.x + 5
            self.y = self.y + 5

if __name__ == "__main__":
    sim = Simulation()
    sim.launchGui()