import sys
from PyQt5 import QtWidgets
from views.window import Ui_MainWindow


app = QtWidgets.QApplication(sys.argv)

ui = Ui_MainWindow()
ui.show()

sys.exit(app.exec_())