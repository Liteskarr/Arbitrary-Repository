from random import randint, choice
from typing import Tuple

import PyQt5.uic as uic
from PyQt5.QtCore import (Qt)
from PyQt5.QtGui import (QPainter, QPaintEvent, QBrush, QPen)
from PyQt5.QtWidgets import (QApplication, QWidget, QSpacerItem, QPushButton, QSizePolicy, QVBoxLayout)


COLORS = [Qt.red, Qt.green, Qt.darkRed, Qt.black, Qt.cyan, Qt.yellow, Qt.darkYellow]


def get_random_circle(radius_bounds: Tuple[int, int],
                      widget_size: Tuple[int, int]) -> Tuple[int, int, int, int]:
    radius = randint(*radius_bounds)
    x = randint(radius, widget_size[0] - radius)
    y = randint(radius, widget_size[1] - radius)
    return x, y, radius, radius


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._configure_ui()

    def _configure_ui(self):
        self.setWindowTitle('Window')
        self.setFixedSize(600, 600)
        self.horizontal_layout = QVBoxLayout(self)

        self.spacer = QSpacerItem(10, 900, QSizePolicy.Expanding)
        self.horizontal_layout.addSpacerItem(self.spacer)

        self.button = QPushButton(self)
        self.button.setText('Отрисовать')
        self.horizontal_layout.addWidget(self.button)
        self.button.clicked.connect(self._handle_button_click)

    def _handle_button_click(self) -> None:
        self.repaint()

    def paintEvent(self, event: QPaintEvent) -> None:
        try:
            painter = QPainter(self)
            painter.begin(self)

            for _ in range(randint(1, 10)):
                color = choice(COLORS)
                painter.setBrush(QBrush(color, Qt.SolidPattern))
                painter.setPen(QPen(color, 8, Qt.SolidLine))
                ellipse = get_random_circle((10, 200), (self.height(), self.width()))
                painter.drawEllipse(*ellipse)

            painter.end()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mw = MainWidget()
    mw.show()
    sys.exit(app.exec())
