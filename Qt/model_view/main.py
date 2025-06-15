import sys
from PySide2.QtCore import (
    Qt
)
from PySide2.QtWidgets import (
    QApplication,
    QListView
)
from lib.model import Model


def main():

    app = QApplication()
    list_view = QListView()
    list_model = Model(app, ["etno", "bud", "gorgious", "candy"])
    
    list_view.setModel(list_model)
    list_view.show()

    print(list_model.rowCount()) # 4

    for i in range(list_model.rowCount()):
        print(list_model.data(
            list_model.index(i), Qt.DisplayRole
        ))

    return app.exec_()


main()
