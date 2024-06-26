from PyQt5 import QtWidgets, QtCore
from views.columnHeader import Ui_ColumnHeader
from views.columnButton import Ui_ColumnButton
from views.columnBody import Ui_ColumnBody
from views.createTask import Ui_CreateTask
from models.KBTable import KBTable
from models.KBTask import KBTask

class Ui_Column(QtWidgets.QFrame):

    """
    Column component for the Root component. 
    """

    def __init__(self, 
                 parent: QtWidgets.QWidget | None = None, 
                 columnName: str = "Column name", 
                 kanban: KBTable | None = None, 
                 removeAllMarkers = None,
                 checkChanges = None):

        super().__init__(parent=parent)
        self.setObjectName(columnName)
        self.kanban = kanban
        self.setupUi(columnName, removeAllMarkers, checkChanges)


    def setupUi(self, columnName: str, removeAllMarkers, checkChanges):

        """
        Set up everything in the column.
        """

        self.checkChanges = checkChanges
        self.setMaximumSize(QtCore.QSize(400, 16777215))
        self.layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(2)

        self.header = Ui_ColumnHeader(self, columnName)
        self.body = Ui_ColumnBody(self, columnName, removeAllMarkers, self.checkChanges)
        self.getColumnButton().clicked.connect(self.createTask)

        self.layout.addWidget(self.header)
        self.layout.addWidget(self.body)


    def insertTask(self, index: int, task: KBTask, kanban: KBTable):

        """
        Insert task to this Column component at the specified index.
        """

        self.body.insertTask(index, task, kanban)


    def appendTask(self, task: KBTask, kanban: KBTable):

        """
        Add task to the Column component at the end.
        """

        self.body.appendTask(task, kanban)


    def getColumnButton(self) -> Ui_ColumnButton:

        """
        Return the column button.
        """

        return self.header.button_add
    

    def createTask(self):

        """
        Show dialog for task creation.
        """

        createTask = Ui_CreateTask()
        createTask.exec_()

        if not createTask.iscanceled :

            text = createTask.taskEdit.toPlainText()
            color = createTask.buttonsFrame.chooseColorButton.color
            task = KBTask(self.kanban.next(), text, color)
            index = 0
            self.insertTask(index, task, self.kanban)
            self.kanban.insertTask(task, self.objectName(), index)
            self.checkChanges()


    def removeMarkers(self):

        """
        Remove all markers in this column body.
        """

        self.body.removeMarkers()
