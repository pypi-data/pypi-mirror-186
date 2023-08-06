from PyQt5 import QtWidgets
from .MainWindow import MainWindow


class StartPauseButton(QtWidgets.QPushButton):
    def __init__(self, mainWindow: MainWindow, externalClickEvent):
        super().__init__('Start', mainWindow)
        self.resize(100,32)
        self.move(50, 50)
        self.started = False
        self.externalClickEvent = externalClickEvent
        self.clicked.connect(self.clickEvent)

    def clickEvent(self):
        self.externalClickEvent(self.started)
        self.started = not self.started
        self.setText('Pause' if self.started else 'Start')