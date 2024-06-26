from PyQt5 import QtWidgets, QtCore, QtGui

class Ui_TaskButton(QtWidgets.QPushButton):

    """
    Button component for the Task component.
    """

    def __init__(self, parent: QtWidgets.QWidget, filename: str):
        super().__init__(parent)
        self.setupUi(filename)


    def setupUi(self, filename: str):
        
        """
        Set up everything for this component.
        """
        
        self.qss = {
            "normal": "border: 0px; background-color: rgba(0,0,0,0); color: rgba(0,0,0,0);",
            "hover": "background-color: rgba(255,0,0,1); color: rgba(255,255,255,1);",
            "pressed": "background-color: rgba(212,0,0,1);"
        }
        
        self.setMinimumSize(QtCore.QSize(50, 49))
        self.setMaximumSize(QtCore.QSize(50, 49))
        self.setStyleSheet(self.qss["normal"])

        pixmap = QtGui.QPixmap(filename)
        mask = pixmap.createMaskFromColor(QtGui.QColor("black"), QtCore.Qt.MaskOutColor)
        pixmap.fill(QtGui.QColor("white"))
        pixmap.setMask(mask)
        self.setIcon(QtGui.QIcon(pixmap))
        self.setIconSize(QtCore.QSize(0, 0))


    def enterEvent(self, e: QtCore.QEvent):

        """
        Overriding what to do when mouse is entering.
        """

        self.setIconSize(QtCore.QSize(25, 25))
        self.setStyleSheet(self.qss["hover"])


    def leaveEvent(self, e: QtCore.QEvent):

        """
        Overriding what to do when mouse is leaving.
        """

        self.setIconSize(QtCore.QSize(0, 0))
        self.setStyleSheet(self.qss["normal"])


    def mousePressEvent(self, e: QtGui.QMouseEvent):

        """
        Overriding what to do when mouse is pressed.
        """

        self.setIconSize(QtCore.QSize(25, 25))
        self.setStyleSheet(self.qss["pressed"])


    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):

        """
        Overriding what to do when mouse is released.
        """

        self.setIconSize(QtCore.QSize(25, 25))
        self.setStyleSheet(self.qss["hover"])
        self.clicked.emit()