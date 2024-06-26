from PyQt5 import QtWidgets, QtCore
from models.KBTable import KBTable

class Ui_MenuBar(QtWidgets.QMenuBar):

    """
    Menu bar for Tiped application.
    """

    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.setupUi()


    def setupUi(self):

        """
        Set up everything in this menu bar.
        """

        self.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuFile = QtWidgets.QMenu(self)
        self.menuFile.setTitle("File")
        self.menuEdit = QtWidgets.QMenu(self)
        self.menuEdit.setTitle("Edit")
        self.menuHelp = QtWidgets.QMenu(self)
        self.menuHelp.setTitle("Help")

        self.actionNew = QtWidgets.QAction(self.parent())
        self.actionNew.setText("New")
        self.actionNew.setShortcut("Ctrl+N")
        self.actionOpen = QtWidgets.QAction(self.parent())
        self.actionOpen.setText("Open")
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionSave = QtWidgets.QAction(self.parent())
        self.actionSave.setText("Save")
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSaveAs = QtWidgets.QAction(self.parent())
        self.actionSaveAs.setText("Save as")
        self.actionSaveAs.setShortcut("Ctrl+Shift+S")
        self.actionExit = QtWidgets.QAction(self.parent())
        self.actionExit.setText("Exit")
        self.actionExit.setShortcut("Ctrl+Q")
        self.actionSearch = QtWidgets.QAction(self.parent())
        self.actionSearch.setText("Show/Hide Search Bar")
        self.actionSearch.setShortcut("Ctrl+F")
        self.actionToDo = QtWidgets.QAction(self.parent())
        self.actionToDo.setText("New To do Task")
        self.actionToDo.setShortcut("Ctrl+T")
        self.actionToDo.setObjectName(KBTable.columns[0])
        self.actionInProgress = QtWidgets.QAction(self.parent())
        self.actionInProgress.setText("New In progress Task")
        self.actionInProgress.setShortcut("Ctrl+I")
        self.actionInProgress.setObjectName(KBTable.columns[1])
        self.actionDone = QtWidgets.QAction(self.parent())
        self.actionDone.setText("New Done Task")
        self.actionDone.setShortcut("Ctrl+D")
        self.actionDone.setObjectName(KBTable.columns[2])
        self.actionAbout = QtWidgets.QAction(self.parent())
        self.actionAbout.setText("About")
        self.actionAbout.setShortcut("Ctrl+?")

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionSearch)
        self.menuEdit.addAction(self.actionToDo)
        self.menuEdit.addAction(self.actionInProgress)
        self.menuEdit.addAction(self.actionDone)
        self.menuHelp.addAction(self.actionAbout)
        self.addAction(self.menuFile.menuAction())
        self.addAction(self.menuEdit.menuAction())
        self.addAction(self.menuHelp.menuAction())