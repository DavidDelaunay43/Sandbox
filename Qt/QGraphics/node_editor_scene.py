import math
from PySide2.QtCore import (
    QLine,
    QRectF
)
from PySide2.QtGui import (
    QColor,
    QPainter,
    QPen
)
from PySide2.QtWidgets import (
    QGraphicsScene
)


class Scene(QGraphicsScene):


    WIDTH = 64_000
    HEIGHT = 64_000

    GRID_SIZE = 20

    BACKGROUND_COLOR = QColor("#393939")
    LIGHT_COLOR = QColor("#2f2f2f")


    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSceneRect(
            -self.WIDTH//2,
            -self.HEIGHT//2,
            self.WIDTH//2,
            self.HEIGHT//2
        )

        self._pen = QPen(self.LIGHT_COLOR)
        self._pen.setWidth(1)
        self.setBackgroundBrush(self.BACKGROUND_COLOR)


    def drawBackground(self, painter: QPainter, rect: QRectF):
        super().drawBackground(painter, rect)

        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        lines = [
            QLine(x, top, x, bottom)
            for x in range(
                left-(left%self.GRID_SIZE),
                right,
                self.GRID_SIZE
            )
        ] + [
            QLine(left, y, right, y)
            for y in range(
                top-(top%self.GRID_SIZE),
                bottom,
                self.GRID_SIZE
            )
        ]

        painter.setPen(self._pen)
        painter.drawLines(lines)
