from PySide2.QtCore import (
    Qt,
    QAbstractListModel,
    QModelIndex
)


class Model(QAbstractListModel):


    def __init__(self, parent=None, items=None):
        super().__init__(parent)
        self._items = items or []


    def rowCount(self, parent=QModelIndex()):
        return len(self._items)


    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            row = index.row()
            if 0 <= row < len(self._items):
                return self._items[row]
