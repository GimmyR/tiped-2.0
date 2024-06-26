from PyQt5 import QtWidgets

class Ui_TaskEdit(QtWidgets.QTextEdit):

    """
    Text Edit for Task description.
    """

    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.setupUi()


    def setupUi(self):
        
        """
        Set up everything in this Task Edit.
        """

        self.setPlaceholderText("Task description")
        self.setStyleSheet(
            "background-color: white; \n"
            "padding: 20px;"
        )