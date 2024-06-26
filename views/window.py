# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from models.KBTable import KBTable
from PyQt5 import QtCore, QtWidgets, QtGui
from views.root import Ui_Root
from views.column import Ui_Column
from views.menuBar import Ui_MenuBar
from views.warningNotSaved import Ui_WarningNotSaved
from views.aboutDialog import Ui_AboutDialog
from views.searchBar import Ui_SearchBar
from views.task import Ui_Task


class Ui_MainWindow(QtWidgets.QMainWindow):
    
    """
    Main window for Tiped application.
    """

    def __init__(self, parent: QtWidgets.QWidget | None = None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):

        """
        Set up everything in the window.
        """

        self.resize(1280, 840)
        self.title = "Tiped"
        self.fileIsSaved = True
        self.menubar = Ui_MenuBar(self)
        self.root = Ui_Root(self)
        self.kanban = KBTable()
        spacerLeft = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        spacerRight = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.root.addItem(spacerLeft)
        
        for column in KBTable.columns :
            self.root.addWidget(Ui_Column(self.root, column, self.kanban, self.removeMarkers, self.checkChanges))

        self.root.addItem(spacerRight)
        self.setMenuBar(self.menubar)
        self.setCentralWidget(self.root)
        self.searchBar = Ui_SearchBar(self)
        self.setWindowTitle(self.title)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.connectMenuBarSignals()
        QtCore.QMetaObject.connectSlotsByName(self)


    def findColumn(self, columnName: str) -> Ui_Column:

        """
        Return the Column component with the specified column name.
        """

        return self.root.findChild(Ui_Column, columnName)
    

    def openFile(self, filename: str):

        """
        Open file with the specified file name and load data in the application.
        """

        self.kanban.filename = filename
        self.kanban.openFile()
        self.checkChanges()
        self.displayData()


    def displayData(self): 

        """
        Display loaded data in the application.
        """

        for key in self.kanban.content.keys():
            column = self.findColumn(key)
            column.body.removeAllTasks()
            for task in self.kanban.content[key]:
                column.appendTask(task, self.kanban)


    def saveToFile(self, filename: str):

        """
        Save in the specified file name the current Kanban Table.
        """

        self.kanban.filename = filename
        self.kanban.saveToFile()
        self.checkChanges()


    def save(self):

        """
        Save the current Kanban Table in the current file.
        """

        self.kanban.saveToFile()
        self.checkChanges()


    def removeMarkers(self):

        """
        Remove all markers in this application.
        """

        columns = self.root.findChildren(Ui_Column)
        for column in columns:
            column.removeMarkers()


    def checkChanges(self):

        """
        Edit Window Title if current kanban is different or not from that contained in the file.
        """

        windowTitle = "Tiped"
        
        if self.kanban.filename == None:
            windowTitle = f"* {self.title} ({self.kanban.percentageOfIncrease()}% Done) - untitled"
            self.fileIsSaved = False
        elif self.kanban.filename != None and self.kanban.hasChanged():
            windowTitle = f"* {self.title} ({self.kanban.percentageOfIncrease()}% Done) - {self.kanban.filename}"
            self.fileIsSaved = False
        else:
            windowTitle = f"{self.title} ({self.kanban.percentageOfIncrease()}% Done) - {self.kanban.filename}"
            self.fileIsSaved = True

        self.setWindowTitle(windowTitle)


    def connectMenuBarSignals(self):

        """
        Connect all actions in menu bar with a method.
        """

        self.menubar.actionNew.triggered.connect(self.newFileIsTriggered)
        self.menubar.actionOpen.triggered.connect(self.openFileIsTriggered)
        self.menubar.actionSave.triggered.connect(self.saveIsTriggered)
        self.menubar.actionSaveAs.triggered.connect(self.saveAsIsTriggered)
        self.menubar.actionExit.triggered.connect(self.exitIsTriggered)
        self.menubar.actionAbout.triggered.connect(self.aboutIsTriggered)
        self.menubar.actionSearch.triggered.connect(self.searchBar.toggleShow)
        self.menubar.actionToDo.triggered.connect(self.root.findChild(Ui_Column, self.menubar.actionToDo.objectName()).createTask)
        self.menubar.actionInProgress.triggered.connect(self.root.findChild(Ui_Column, self.menubar.actionInProgress.objectName()).createTask)
        self.menubar.actionDone.triggered.connect(self.root.findChild(Ui_Column, self.menubar.actionDone.objectName()).createTask)


    def openFileIsTriggered(self):

        """
        Do this when actionOpen is triggered.
        """

        if self.fileIsSaved:
            self.doOpenFile()

        else:
            msg = Ui_WarningNotSaved(self.handleChoiceOpen)
            msg.exec_()


    def doOpenFile(self):

        """
        Do what all we need to do to open file.
        """

        fileinfo = QtWidgets.QFileDialog.getOpenFileName(None, "Open File", None, "KBT File (*.kbt)")
        if fileinfo[0] != "":
            self.openFile(fileinfo[0])


    def handleChoiceOpen(self, text: str):

        """
        Manage what to do when we click on "Yes" or "No" in the warning dialog.
        """

        if text == "&Yes":
            self.doOpenFile()


    def saveAsIsTriggered(self):

        """
        Do this when actionSaveAs is triggered.
        """

        fileinfo = QtWidgets.QFileDialog.getSaveFileName(None, "Save as", "table.kbt", "KBT File (*.kbt)")
        if fileinfo[0] != "":
            self.saveToFile(fileinfo[0])


    def saveIsTriggered(self):

        """
        Do this when actionSave is triggered.
        """

        if self.kanban.filename != None:
            self.save()

        else:
            self.saveAsIsTriggered()


    def newFileIsTriggered(self):

        """
        Do this when actionNew is triggered.
        """

        if self.fileIsSaved:
            self.doNewFile()

        else:
            msg = Ui_WarningNotSaved(self.handleChoiceNew)
            msg.exec_()


    def doNewFile(self):

        """
        Do what all we need to do to create new kanban table.
        """

        self.kanban = KBTable()
        self.checkChanges()
        self.displayData()


    def handleChoiceNew(self, text: str):

        """
        Manage what to do when we click on "Yes" or "No" in the warning dialog.
        """

        if text == "&Yes":
            self.doNewFile()


    def exitIsTriggered(self):

        """
        Do this when actionExit is triggered.
        """

        self.close()


    def closeEvent(self, e):

        """
        Do this when closeEvent is triggered.
        """

        if self.fileIsSaved:
            self.doClose(e)

        else:
            msg = Ui_WarningNotSaved(self.handleChoiceClose, e)
            msg.exec_()


    def doClose(self, event):

        """
        Close definitively the window.
        """

        super(QtWidgets.QMainWindow, self).closeEvent(event)


    def handleChoiceClose(self, text: str, event):

        """
        Manage what to do when we click on "Yes" or "No" in the warning dialog.
        """

        if text == "&Yes":
            self.doClose(event)
        else:
            event.ignore()


    def aboutIsTriggered(self):

        """
        Do this when actionAbout is triggered.
        """

        about = Ui_AboutDialog()
        about.exec_()


    def resizeEvent(self, e):
        
        """
        Overriding what to do when resize event occurs.
        """

        super(Ui_MainWindow, self).resizeEvent(e)
        self.searchBar.updatePosition()


    def search(self):

        """
        Search text from search bar in kanban table.
        """

        position = self.kanban.findTaskByText(self.searchBar.text())
        
        if position != None:
            column = self.findColumn(position[0])
            task = column.body.layout.itemAt(position[1]).widget()
            column.body.ensureWidgetVisible(task)