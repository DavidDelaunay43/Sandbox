from PySide2.QtCore import (
    Qt
)
from PySide2.QtGui import (
    QMouseEvent,
    QPainter
)
from PySide2.QtWidgets import (
    QGraphicsView
)


class View(QGraphicsView):

    ZOOM_IN_FACTOR = 1.25
    ZOOM_OUT_FACTOR = 1 / 1.25


    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)


    def mousePressEvent(self, event: QMouseEvent):

        if event.button() == Qt.LeftButton:
            self.setDragMode(QGraphicsView.ScrollHandDrag)
        return super().mousePressEvent(event)
    

    def mouseReleaseEvent(self, event: QMouseEvent):

        if event.button() == Qt.LeftButton:
            self.setDragMode(QGraphicsView.NoDrag)
        return super().mouseReleaseEvent(event)


    def wheelEvent(self, event: QMouseEvent):

        if event.angleDelta().y() > 0:
            zoom_factor = self.ZOOM_IN_FACTOR
        else:
            zoom_factor = self.ZOOM_OUT_FACTOR

        self.scale(zoom_factor, zoom_factor)
