from PyQt5 import QtWidgets
from .Display import Display


class LayoutWidget(QtWidgets.QWidget):
    def __init__(self, display: Display):
        super().__init__()
        self.layout = QtWidgets.QGridLayout()
        self.__display = display
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        randWidget = QtWidgets.QWidget()
        randWidget.setFixedSize(100, 100)
        self.layout.addWidget(randWidget, 0, 0)
        self.layout.addWidget(display, 1, 1, 6, 4)
        self.layout.addWidget(randWidget, 7, 5)

        self.setLayout(self.layout)
    
    def getDisplay(self):
        return self.__display
