from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QBrush, QColor, QPen
from PyQt5.QtWidgets import QWidget


class Display(QWidget):
    def __init__(self, displayUpdater):
        super().__init__()
        self.__displayUpdater = displayUpdater # Type: (PyQt5.QtGui.QPainter) -> void
        self.setFixedSize(600, 400)

        self.setStyleSheet("QWidget { border: 2px solid white; }")
    

    def paintEvent(self, event):
        painter = QPainter(self)
        self.paintDefaultBackground(painter)
        self.__displayUpdater(painter)
    
    def paintDefaultBackground(self, painter: QPainter):
        x = 0
        y = 0
        for i in range(41):
            painter.drawLine(x,0,x,400)
            painter.drawLine(0,y,600,y)
            x+=10
            y+=10
        for i in range(20):
            painter.drawLine(x,0,x,400)
            x+=10
