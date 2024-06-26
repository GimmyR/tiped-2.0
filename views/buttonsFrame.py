from PyQt5 import QtWidgets, QtCore, QtGui
from views.chooseColorButton import Ui_ChooseColorButton
from views.saveButton import Ui_SaveButton

class Ui_ButtonsFrame(QtWidgets.QFrame):

    """
    Frame for buttons.
    """

    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.setupUi()


    def setupUi(self):
        
        """
        Set up everything in this Frame.
        """

        self.setMinimumSize(QtCore.QSize(0, 50))
        self.setMaximumSize(QtCore.QSize(16777215, 50))
        self.layout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(10)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.chooseColorButton = Ui_ChooseColorButton(self)
        self.saveButton = Ui_SaveButton(self)
        
        self.layout.addItem(spacerItem)
        self.layout.addWidget(self.chooseColorButton)
        self.layout.addWidget(self.saveButton)