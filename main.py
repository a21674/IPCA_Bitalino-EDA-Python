import sys
from PyQt5.QtWidgets import *
from mainWindowConfig import CustomMainWindow
from plotConfig import *

matplotlib.use("Qt5Agg")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Plastique'))
    myGUI = CustomMainWindow()
    sys.exit(app.exec_())