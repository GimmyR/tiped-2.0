from PyQt5 import QtWidgets, QtCore, QtGui

class Ui_SearchBar(QtWidgets.QLineEdit):

    """
    Search bar to display in the main window.
    """

    width, height, marginLeft, marginBottom = 500, 50, 10, 10
    
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):

        """
        Set up everything in this Search bar.
        """

        self.setPlaceholderText("Search")
        self.setGeometry(QtCore.QRect(Ui_SearchBar.marginLeft, self.calculateY(), Ui_SearchBar.width, Ui_SearchBar.height))
        self.setStyleSheet("padding-left: 15px; padding-right: 15px; background-color: white;")
        self.hide()


    def calculateY(self):

        """
        Return Y position in relation to window height.
        """

        return self.parent().height() - Ui_SearchBar.marginBottom - Ui_SearchBar.height


    def updatePosition(self):

        """
        Change position (y here) in relation to size (height here) of window.
        """

        self.setGeometry(QtCore.QRect(Ui_SearchBar.marginLeft, self.calculateY(), Ui_SearchBar.width, Ui_SearchBar.height))


    def toggleShow(self):

        """
        Show this search bar if hidden, hide if showed.
        """

        if self.isHidden():
            self.show()
            self.setFocus()
        else:
            self.hide()
            self.clearFocus()


    def keyPressEvent(self, e: QtGui.QKeyEvent):

        """
        Overrding what to do when key is pressed.
        """

        if e.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            self.parent().search()

        else:
            super(Ui_SearchBar, self).keyPressEvent(e)