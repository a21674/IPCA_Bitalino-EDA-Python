from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from plotConfig import CustomFigCanvas



class Ui_PlotWindow(QMainWindow):
    def __init__(self):
        super(Ui_PlotWindow, self).__init__()
        # Define the geometry of the main window
        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle("EDA Plot")
        # Create FRAME_A
        self.FRAME_A = QFrame(self)
        self.FRAME_A.setStyleSheet("QWidget { background-color: %s }" % QColor(210,210,235,255).name())
        self.LAYOUT_A = QGridLayout()
        self.FRAME_A.setLayout(self.LAYOUT_A)
        self.setCentralWidget(self.FRAME_A)

        """ # Place the start button
        self.startBtn = QPushButton(text='Start')
        self.startBtn.setFixedSize(100, 50)
        self.startBtn.clicked.connect(self.startBtnAction)
        self.LAYOUT_A.addWidget(self.startBtn, 0, 0, 1, 1)

        self.stopBtn = QPushButton(text='Stop')
        self.stopBtn.setFixedSize(100, 50)
        self.stopBtn.clicked.connect(self.stopBtnAction)
        self.LAYOUT_A.addWidget(self.stopBtn, 0, 2, 1, 1) """
        
        
        # Place the matplotlib figure
        self.myFig = CustomFigCanvas()
        self.LAYOUT_A.addWidget(self.myFig, *(0,1))
        
        self.show()
        return


    """ def startBtnAction(self):
        print("Start")
        self.stop_threads = False
        # Add the callbackfunc to ..
        self.myDataLoop = threading.Thread(name = 'myDataLoop', target = dataSendLoop, daemon = True, args = (self.addData_callbackFunc, self.stop_threads))
        self.myDataLoop.start()
        return
    
    def stopBtnAction(self):
        self.stop_threads = True        
        self.myDataLoop.join()
        print('thread killed') """
        
    
    
    def addData_callbackFunc(self, value):
        #print("Add data: " + str(value))
        self.myFig.addData(value)
        return                   
                
            
    
                    
                    
''' End Class '''

if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = Ui_PlotWindow()
    gui.show()
    app.exec_()