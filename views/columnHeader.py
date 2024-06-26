from PyQt5 import QtWidgets, QtCore, QtGui
from views.columnLabel import Ui_ColumnLabel
from views.columnButton import Ui_ColumnButton

class Ui_ColumnHeader(QtWidgets.QFrame):

    """
    Header component for the Column component.
    """

    def __init__(self, parent: QtWidgets.QWidget | None = None, columnName: str = "Column name"):
        super().__init__(parent=parent)
        self.setupUi(columnName)


    def setupUi(self, columnName: str):

        """
        Set up everything for the header.
        """

        self.setMinimumSize(QtCore.QSize(0, 50))
        self.setMaximumSize(QtCore.QSize(16777215, 50))
        self.setStyleSheet("QWidget {background-color: white;}")
        self.layout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 4, 0)
        self.layout.setSpacing(0)

        self.label = Ui_ColumnLabel(self, columnName)
        self.button_add = Ui_ColumnButton(self, "+")
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button_add)
        self.layout.setStretch(0, 10)
        self.layout.setStretch(1, 1)