from PyQt5 import QtWidgets, QtCore

class Ui_Marker(QtWidgets.QFrame):

    """
    Marker to put where a task will be dropped.
    """

    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.setupUi()


    def setupUi(self):

        """
        Set up everything in this marker.
        """

        self.setMinimumSize(QtCore.QSize(0, 15))
        self.setMaximumSize(QtCore.QSize(16777215, 15))
        self.setStyleSheet("background-color: rgb(98, 160, 234);")
        self.setObjectName("marker")