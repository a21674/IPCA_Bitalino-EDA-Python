
from PyQt5.QtWidgets import *
import numpy as np
from ui.mainWindowUi import Ui_MainWindowUi

def dataResults_callbackFunc(value):
    data = Ui_MainWindowUi()
    data.calcResults(value)
    #print("Add data: " + str(value))
        

