from PyQt5 import QtWidgets, QtCore, QtGui
from views.taskHeader import Ui_TaskHeader
from views.taskButton import Ui_TaskButton
from views.taskBody import Ui_TaskBody
from views.editTask import Ui_EditTask
from models.KBTask import KBTask
from models.KBTable import KBTable

class Ui_Task(QtWidgets.QFrame):

    """
    Task component for Column component.
    """

    def __init__(self, parent: QtWidgets.QWidget, task: KBTask, kanban: KBTable, removeTask, checkChanges):
        super().__init__(parent)
        self.setupUi(task, kanban, removeTask, checkChanges)
        

    def setupUi(self, task: KBTask, kanban: KBTable, removeTask, checkChanges):

        """
        Set up everything in this component.
        """

        self.kanban = kanban
        self.removeTask = removeTask
        self.checkChanges = checkChanges
        self.taskID = task.id
        self.setMinimumSize(QtCore.QSize(0, 200))
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.setStyleSheet("border: 1px solid rgb(128, 128, 128);")
        
        self.layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.header = Ui_TaskHeader(self, task.headerColor)
        self.header.button_edit.clicked.connect(self.editTask)
        self.body = Ui_TaskBody(self, task.text)

        self.layout.addWidget(self.header)
        self.layout.addWidget(self.body)


    def getHeaderColor(self) -> str:

        """
        Return the background color of the Task Header.
        """

        return self.header.backgroundColor
    

    def getText(self) -> str:

        """
        Return the text of the Task Body.
        """

        return self.body.label.text()
    

    def getTaskButton(self) -> Ui_TaskButton:
        
        """
        Return the task button.
        """

        return self.header.button_edit
    

    def editTask(self):

        """
        Show 'Ui_CreateTask' dialog and edit task.
        """

        editTask = Ui_EditTask(self.getText(), self.getHeaderColor())
        editTask.exec_()

        if not editTask.iscanceled :

            if not editTask.isremoved :

                text = editTask.taskEdit.toPlainText()
                color = editTask.buttonsFrame.chooseColorButton.color
                self.body.label.setText(text)
                self.header.setBackgroundColor(color)
                self.kanban.editTask(KBTask(self.taskID, text, color))

            else:

                self.removeTask(self)
                self.kanban.removeTask(self.toKBTask())

            self.checkChanges()


    def mouseMoveEvent(self, event):

        """
        Overriding what happens when mouseMove event occurs.
        """

        if event.buttons() == QtCore.Qt.LeftButton:
            drag = QtGui.QDrag(self)
            mime = QtCore.QMimeData()
            drag.setMimeData(mime)
            pixmap = QtGui.QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)
            drag.exec_(QtCore.Qt.MoveAction)


    def toKBTask(self):

        """
        Return a KBTask object.
        """

        return KBTask(self.taskID, self.getText(), self.getHeaderColor())