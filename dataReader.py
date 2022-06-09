from bitalinoConfig import BitalinoDataRead
from bitalino import BITalino
import time
import numpy as np
from PyQt5.QtCore import *


# You need to setup a signal slot mechanism, to
# send data to your GUI in a thread-safe way..
class Communicate(QObject):
    data_signal = pyqtSignal(float)
    data_results = pyqtSignal(float)
    
    
    

def dataSendLoop(addData_callbackFunc, calcResults_callbackFunc):
        # Setup the signal-slot mechanism.
        mySrc = Communicate()
        mySrc.data_signal.connect(addData_callbackFunc)
        mySrc.data_results.connect(calcResults_callbackFunc)
        
        # Simulate some data
        n = np.linspace(0, 499, 500)
        y = 50 + 25*(np.sin(n / 8.3)) + 10*(np.sin(n / 7.5)) - 5*(np.sin(n / 1.5))
        i = 0

        while(True):
            if(i > 499):
                i = 0
            time.sleep(0.1)
            mySrc.data_signal.emit(y[i]) # <- Here you emit a signal!
            mySrc.data_results.emit(y[i]) # <- Here you emit a signal!
            i += 1
        ###
        
        """  bita = BitalinoDataRead() #instaciação da classe Bitalino
        device = BITalino(bita.macAddress) # Connect to BITalino
        device.battery(bita.batteryThreshold) # Set battery threshold
        print(device.version()) # Read BITalino version
        device.start(bita.samplingRate, bita.acqChannels) # Start Acquisition

                    

        while True:
            samples = np.array(device.read(bita.nSamples))
            #print(samples[:, 5])
            for x in samples:
                rawData = x[5] #acesso a posição 5 do array que vem do bitalino
                uSData = ((float(rawData) / (2 ** bita.resolution)) * 3.3) / 0.132
                #print(uSData)
                mySrc.data_results.emit(uSData)
                mySrc.data_signal.emit(uSData)

                time.sleep(0.01) #segundos """
                
            

                                       
                



