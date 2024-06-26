from PyQt5 import QtWidgets, QtCore

class Ui_TaskBody(QtWidgets.QFrame):

    """
    Body component for Task component.
    """

    def __init__(self, parent: QtWidgets.QWidget, text: str = "Task description"):
        super().__init__(parent)
        self.setupUi(text)


    def setupUi(self, text: str):
        
        """
        Set up everything for this component.
        """

        self.setStyleSheet("border: 0px; background-color: white;")

        self.layout: QtWidgets.QGridLayout = QtWidgets.QGridLayout(self)

        self.label = QtWidgets.QLabel(self)
        self.label.setText(text)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.layout.addWidget(self.label, 0, 0, 1, 1)