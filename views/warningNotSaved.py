from PyQt5 import QtWidgets

class Ui_WarningNotSaved(QtWidgets.QMessageBox):

    """
    A warning dialog to display when file is not saved.
    """

    def __init__(self, handleChoice, event = None, parent: QtWidgets.QWidget | None = None):
        super().__init__(parent)
        self.setupUi(handleChoice, event)


    def setupUi(self, handleChoice, event):

        """
        Set up everything in this dialog.
        """

        self.event = event
        self.handleChoice = handleChoice
        self.setWindowTitle("Warning information")
        self.setText("Current Kanban Table is not saved.\nDo you want to continue ?")
        self.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        self.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        self.buttonClicked.connect(self.action)


    def action(self, btn):

        if self.handleChoice != None:
            if self.event == None:
                self.handleChoice(btn.text())
            else:
                self.handleChoice(btn.text(), self.event)
        else:
            raise Exception("HandleChoice must be a function, not None.")