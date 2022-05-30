import sys
from PyQt5 import QtWidgets
from ui.mainWindowUi import Ui_MainWindowUi



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindowUi = QtWidgets.QMainWindow()
    ui = Ui_MainWindowUi()
    ui.setupUi(MainWindowUi)
    MainWindowUi.show()
    sys.exit(app.exec_())
    
