from PyQt5 import QtWidgets, QtCore, QtGui

class Ui_ChooseColorButton(QtWidgets.QPushButton):

    """
    Push Button to choose the background color of the Task Header.
    """

    def __init__(self, parent: QtWidgets.QWidget, color: str = "#006CD3"):
        super().__init__(parent)
        self.setupUi(color)
        

    def setupUi(self, color: str):

        """
        Set up everything in this ChooseColor button.
        """

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        
        self.setText("Choose color")
        self.setColor(color)
        self.setMinimumSize(QtCore.QSize(130, 50))
        self.setMaximumSize(QtCore.QSize(130, 50))
        self.setFont(font)
        self.clicked.connect(self.chooseColor)


    def setColor(self, color: str):

        """
        Set color property and stylesheet.
        """

        self.color = color
        self.setStyleSheet(f"color: {self.color};")


    def chooseColor(self):

        """
        Show Color Picker dialog and choose color for the Task Header.
        """

        color = QtWidgets.QColorDialog.getColor(
            QtGui.QColor(self.color),
            None,
            "",
            QtWidgets.QColorDialog.ColorDialogOption()
        )
        
        if color.isValid():
            self.setColor(color.name())