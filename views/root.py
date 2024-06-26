from PyQt5 import QtWidgets

class Ui_Root(QtWidgets.QFrame):

    """
    Root component for the window.
    """

    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.setupUi()


    def setupUi(self):

        """
        Set up everything in the frame.
        """
        
        self.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.layout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 20, 0, 20)
        self.layout.setSpacing(10)


    def addWidget(self, widget: QtWidgets.QWidget):

        """
        Add widget in the frame with a layout.
        """

        self.layout.addWidget(widget)


    def addItem(self, item: QtWidgets.QLayoutItem):

        """
        Add item in the frame with a layout.
        """

        self.layout.addItem(item)