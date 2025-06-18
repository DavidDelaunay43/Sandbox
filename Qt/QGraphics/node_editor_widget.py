from PySide2.QtWidgets import (
    QGraphicsScene,
    QGraphicsView,
    QVBoxLayout,
    QWidget
)
from node_editor_scene import Scene
from node_editor_view import View


class NodeEditorWidget(QWidget):


    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Node Editor")
        self.setGeometry(200, 200, 800, 600)

        self._build_ui()


    def _build_ui(self):
        
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._main_layout)

        self._view = View(self)
        self._main_layout.addWidget(self._view)

        self._scene = Scene(self)
        self._view.setScene(self._scene)
