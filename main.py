from random import randint
from typing import Tuple

import PyQt5.uic as uic
from PyQt5.QtCore import (Qt)
from PyQt5.QtGui import (QPainter, QPaintEvent, QBrush, QPen)
from PyQt5.QtWidgets import (QApplication, QWidget)


COLOR = (255, 255, 51)


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
        uic.loadUi('UI.ui', self)
        self.button.clicked.connect(self._handle_button_click)

    def _handle_button_click(self) -> None:
        self.repaint()

    def paintEvent(self, event: QPaintEvent) -> None:
        try:
            painter = QPainter(self)
            painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            painter.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
            painter.begin(self)

            for _ in range(randint(1, 10)):
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
