from PyQt5 import QtWidgets, QtGui, QtCore

class Ui_ColumnLabel(QtWidgets.QLabel):

    """
    Label component for the Column component.
    """

    def __init__(self, parent: QtWidgets.QWidget, columnName: str = "Column name"):
        super().__init__(parent)
        self.setupUi(columnName)


    def setupUi(self, columnName: str):

        """
        Set up everything in the label.
        """

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.setText(columnName)
        self.setFont(font)
        self.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.setIndent(16)