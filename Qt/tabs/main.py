from enum import Enum
from functools import partial
import sys
from PySide2.QtCore import (
    Qt,
    QPoint,
    QSize
)
from PySide2.QtWidgets import (
    QAction,
    QApplication,
    QMainWindow,
    QMenu,
    QTabWidget,
    QToolButton,
    QVBoxLayout,
    QWidget
)
import qtawesome as qta


class RootDirectoy(Enum):

    ASSET = "Asset"
    MASTER = "Master"
    SHOT = "Shot"
    PUBLISH = "Publish"
    CACHE = "Cache"


class RootWidget(QWidget):


    def  __init__(self, parent=None):
        super().__init__(parent)


class TabWidget(QTabWidget):


    def __init__(self, parent=None):
        super().__init__(parent)

        self.setTabsClosable(True)
        self.setMovable(True)
        self.setUsesScrollButtons(True)
        self.setTabPosition(QTabWidget.TabPosition.North) # Default
        self.setTabShape(QTabWidget.TabShape.Rounded) # Default

        self._context_menu = QMenu(self)
        for root_dir in RootDirectoy:
            action = QAction(root_dir.value, self._context_menu)
            action.triggered.connect(
                partial(self.show_tab, root_dir.value)
            )
            self._context_menu.addAction(action)

        self.tabCloseRequested.connect(self.removeTab)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self._show_context_menu)


    def show_tab(self, root_dir_name: str):

        self.addTab(
            RootWidget(self),
            root_dir_name
        )
        

    def _show_context_menu(self, pos: QPoint):
        self._context_menu.exec_(self.mapToGlobal(pos))


class CentralWidget(QWidget):


    def __init__(self, parent=None):
        super().__init__(parent)

        self.build_ui()


    def sizeHint(self):
        return QSize(1000, 400)


    def build_ui(self):

        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)

        self.tab_widget = TabWidget(self)
        self.main_layout.addWidget(self.tab_widget)


class MainWindow(QMainWindow):
    

    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = CentralWidget(self)
        self.setCentralWidget(self.central_widget)


if __name__ == "__main__":

    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
