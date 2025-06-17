import sys
from PySide2.QtWidgets import (
    QApplication
)
from node_editor_widget import NodeEditorWidget


if __name__ == "__main__":

    app = QApplication()
    node_editor_widget = NodeEditorWidget()
    node_editor_widget.show()
    sys.exit(app.exec_())
