from PyQt5 import QtWidgets, QtCore
from views.taskButton import Ui_TaskButton

class Ui_TaskHeader(QtWidgets.QFrame):

    """
    Header component for the Task component.
    """

    def __init__(self, parent: QtWidgets.QWidget, backgroundColor: str = "#41A0FF"):
        super().__init__(parent)
        self.backgroundColor = backgroundColor
        self.setupUi()


    def setupUi(self):
        
        """
        Set up everything in this component.
        """

        self.setMinimumSize(QtCore.QSize(0, 50))
        self.setMaximumSize(QtCore.QSize(16777215, 50))
        self.setStyleSheet(f"border: 0px; border-bottom: 1px solid rgb(128, 128, 128); background-color: {self.backgroundColor};")
        
        self.layout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_edit = Ui_TaskButton(self, "images/edit-246.svg")

        self.layout.addItem(spacer)
        self.layout.addWidget(self.button_edit)


    def setBackgroundColor(self, color: str):

        """
        Set background color of this Task Header.
        """

        self.backgroundColor = color
        self.setStyleSheet(f"border: 0px; border-bottom: 1px solid rgb(128, 128, 128); background-color: {self.backgroundColor};")