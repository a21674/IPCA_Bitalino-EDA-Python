from PyQt5.QtCore import *


# You need to setup a signal slot mechanism, to
# send data to your GUI in a thread-safe way..
class Communicate(QObject):
    data_signal = pyqtSignal(float)




''' End Class '''