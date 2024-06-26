from PyQt5 import QtWidgets, QtCore, QtGui

class Ui_SaveButton(QtWidgets.QPushButton):

    """
    Push Button to save task.
    """

    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.setupUi()


    def setupUi(self):

        """
        Set up everything in this Save Button.
        """

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.setText("Save")
        self.setMinimumSize(QtCore.QSize(100, 50))
        self.setMaximumSize(QtCore.QSize(100, 50))
        self.setFont(font)
        self.setStyleSheet(
            "QPushButton { border: 0px; background-color: #006CD3; color: white; }\n"
            "QPushButton:hover { background-color: #0064C3; }\n"
            "QPushButton:pressed { background-color: #0152A0; }"
        )