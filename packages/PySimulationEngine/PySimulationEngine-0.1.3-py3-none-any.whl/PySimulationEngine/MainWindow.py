from PyQt5 import QtWidgets, QtCore
from .LayoutWidget import LayoutWidget

# DEFAULT_WIDTH = 600
# DEFAULT_HEIGHT = 400

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, layout: LayoutWidget, width: int = None, height: int = None):
        super().__init__()
        # self.width = width if width != None else DEFAULT_WIDTH
        # self.height = height if height != None else DEFAULT_HEIGHT
        # self.setGeometry(300, 300, self.width, self.height)
        # self.resize(self.width, self.height)
        # self.setMinimumSize(QtCore.QSize(self.width, self.height))    
        self.setWindowTitle("Simulation") 
        # self.label = QtWidgets.QLabel()
        # canvas = QtGui.QPixmap(self.width, self.height)
        self.__layout = layout
        self.setCentralWidget(self.__layout)
    
    def getDisplay(self):
        return self.__layout.getDisplay()