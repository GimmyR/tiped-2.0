from PyQt5 import QtWidgets

class Ui_AboutDialog(QtWidgets.QMessageBox):

    """
    A dialog for about the application.
    """

    def __init__(self, parent: QtWidgets.QWidget | None = None):
        super().__init__(parent)
        self.setupUi()


    def setupUi(self):

        """
        Set up everything in this dialog.
        """

        self.setWindowTitle("About")
        self.setText("Tiped 2 is an application of kanban table developed by Gimmy Anjaniaina Razafimbelo.")
        self.setIcon(QtWidgets.QMessageBox.Icon.Information)