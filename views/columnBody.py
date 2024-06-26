from PyQt5 import QtWidgets, QtCore
from views.task import Ui_Task
from views.marker import Ui_Marker
from models.KBTask import KBTask
from models.KBTable import KBTable

class Ui_ColumnBody(QtWidgets.QScrollArea):

    """
    Body component for the Column component.
    """

    def __init__(self, parent: QtWidgets.QWidget, columnName: str, removeAllMarkers = None, checkChanges = None):
        super().__init__(parent)
        self.setupUi(columnName, removeAllMarkers, checkChanges)


    def setupUi(self, columnName: str, removeAllMarkers, checkChanges):

        """
        Set up everything in the body.
        """

        scrollBarStyleSheet = str(
            "QScrollBar { background-color: white; }"
            "QScrollBar::handle { background-color: #C1C1C1; margin: 15px 10px 15px 10px; }"
            "QScrollBar::add-line { background-color: white; }"
            "QScrollBar::sub-line { background-color: white; }"
        )

        self.columnName = columnName
        self.removeAllMarkers = removeAllMarkers
        self.checkChanges = checkChanges
        self.setAcceptDrops(True)
        self.setStyleSheet("border: 0px; background-color: white;")
        self.verticalScrollBar().setStyleSheet(scrollBarStyleSheet)
        self.setWidgetResizable(True)
        self.content = QtWidgets.QWidget()
        self.content.setGeometry(QtCore.QRect(0, 0, 339, 558))
        self.layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout(self.content)
        self.layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(20)

        spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout.addItem(spacer)
        self.setWidget(self.content)


    def insertTask(self, index: int, task: KBTask, kanban: KBTable):

        """
        Insert task to the Column component of this Body component at the specified index.
        """

        self.layout.insertWidget(index, Ui_Task(self.content, task, kanban, self.removeTask, self.checkChanges))


    def appendTask(self, task: KBTask, kanban: KBTable):

        """
        Add task to the Column component of this Body component at the end.
        """

        self.insertTask(self.layout.count() - 1, task, kanban)


    def removeTask(self, task: Ui_Task):

        """
        Remove the specified task from the Column component of this Body component
        """

        self.layout.removeWidget(task)


    def removeAllTasks(self):

        """
        Remove the specified task from the Column component of this Body component
        """

        children = self.content.findChildren(Ui_Task)
        for child in children:
            self.layout.removeWidget(child)


    def dragEnterEvent(self, event):

        """
        Overriding what is happening when drag enter event occurs.
        """

        event.accept()


    def dragMoveEvent(self, e):

        """
        Overriding what is happening when drag move event occurs.
        """

        self.removeAllMarkers()
        self.putMarker(e, self.layout.count(), e.source())
        e.accept()


    def dropEvent(self, e):

        """
        Overriding what is happening when drop event occurs.
        """

        self.removeAllMarkers()
        self.operateDrop(e, self.layout.count(), e.source())
        e.accept()


    def operateDrop(self, e, itemsNumber: int, task: Ui_Task):

        """
        Operate the drop.
        """

        # We need to do this weird operation in below because we can already have our task in this column
        # And there is a spacer item too (we need to put all our widgets before this spacer)

        condition, pos = 0, e.pos()
    
        for i in range(itemsNumber):
            wid = self.layout.itemAt(i).widget()
            # we need to substract with the value of vertical scrollbar in below because this component is a scrollarea.
            if wid == None or (pos.y() < wid.y() - self.verticalScrollBar().value() + wid.height()):
                taskPosition = task.kanban.findTask(task.toKBTask())
                if taskPosition != None:
                    if taskPosition[0] == self.columnName and i == taskPosition[1]:
                        # if new position is exactly the old position, we don't do anything
                        continue
                    elif taskPosition[0] == self.columnName and i > taskPosition[1]:
                        # if new position is in the same column but is greater than old position, we need to add condition
                        condition = 1
                    self.operateMove(task, i - condition)
                    break


    def operateMove(self, task: Ui_Task, index: int):

        """
        Operate the movement in User Interface and in KBTable.
        """

        self.layout.insertWidget(index, task)
        ktask = task.toKBTask()
        task.kanban.removeTask(ktask)
        task.kanban.insertTask(ktask, self.columnName, index)
        self.checkChanges()


    def putMarker(self, e, itemsNumber: int, task: Ui_Task):

        """
        Put a marker where the task will be dropped.
        """
    
        pos = e.pos()
        for i in range(itemsNumber):
            wid = self.layout.itemAt(i).widget()
            if wid == None or (pos.y() < wid.y() - self.verticalScrollBar().value() + wid.height()):
                taskPosition = task.kanban.findTask(task.toKBTask())
                if taskPosition != None:
                    if taskPosition[0] == self.columnName and i < taskPosition[1]:
                        self.layout.insertWidget(i, Ui_Marker(self.content))
                    elif taskPosition[0] == self.columnName and i > taskPosition[1]:
                        if i - 1 != taskPosition[1]:
                            self.layout.insertWidget(i, Ui_Marker(self.content))
                    elif taskPosition[0] != self.columnName:
                        self.layout.insertWidget(i, Ui_Marker(self.content))
                    break
                else:
                    raise Exception("Task not found.")
                

    def removeMarkers(self):

        """
        Remove all markers in this column body.
        """

        marker = self.content.findChild(Ui_Marker, "marker")
        if marker != None:
            self.layout.removeWidget(marker)