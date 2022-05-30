
from PyQt5.QtWidgets import *
from ui.PlotWindowConfig import Ui_PlotWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


def openPlotWindow():
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Plastique'))
    myGUI = Ui_PlotWindow()
    sys.exit(app.exec_())

    
