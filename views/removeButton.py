from PyQt5 import QtWidgets, QtCore, QtGui

class Ui_RemoveButton(QtWidgets.QPushButton):

    """
    Push Button to remove task.
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

        self.setMinimumSize(QtCore.QSize(50, 50))
        self.setMaximumSize(QtCore.QSize(50, 50))
        self.setFont(font)
        self.setStyleSheet(
            "QPushButton { border: 0px; border-radius: 4px; background-color: #FF0000; }\n"
            "QPushButton:hover { background-color: #DF0000; }\n"
            "QPushButton:pressed { background-color: #A60000; }"
        )

        pixmap = QtGui.QPixmap("images/trash-can-3.svg")
        mask = pixmap.createMaskFromColor(QtGui.QColor("black"), QtCore.Qt.MaskOutColor)
        pixmap.fill(QtGui.QColor("white"))
        pixmap.setMask(mask)
        self.setIcon(QtGui.QIcon(pixmap))
        self.setIconSize(QtCore.QSize(20, 20))