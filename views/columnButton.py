from PyQt5 import QtWidgets, QtCore, QtGui

class Ui_ColumnButton(QtWidgets.QPushButton):

    """
    Button component for the Column component.
    """

    def __init__(self, parent: QtWidgets.QWidget | None = None, text: str = "Button"):
        super().__init__(parent=parent)
        self.setupUi(text)


    def setupUi(self, text: str):

        """
        Set up everything in the button.
        """

        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)

        self.setMinimumSize(QtCore.QSize(45, 40))
        self.setMaximumSize(QtCore.QSize(45, 40))
        self.setText(text)
        self.setFont(font)

        self.setStyleSheet(
            "QPushButton { border: 0px; border-radius: 5px; }\n"
            "QPushButton:hover { background-color: #E9E9E9; }\n"
            "QPushButton:pressed { background-color: #D5D5D5; }"
        )