from bitalinoConfig import *
from plotConfig import Communicate
import numpy as np

def Average(lst):
    return sum(lst) / len(lst)


def dataSendLoop(addData_callbackFunc):
    # Setup the signal-slot mechanism.
    mySrc = Communicate()
    mySrc.data_signal.connect(addData_callbackFunc)

    maxPeak = 0
    avgPeak = 0
    minPeak = 0
    sampleBk = []
    
    while True:
        #print(device.read(nSamples))
        samples = np.array(device.read(nSamples))
        #print(samples[:, 5])

        for x in samples:
            for y in x:
                data = x[5]
                yAxis = ((float(data) / (2 ** resolution)) * 3.3) / 0.132
                
                sampleBk.append(yAxis)
                mySrc.data_signal.emit(yAxis)
                time.sleep(0.01) #segundos
                if (yAxis > maxPeak):
                    maxPeak = yAxis
                elif (yAxis < minPeak):
                    minPeak = yAxis
                print ('MaxPeak', maxPeak)
                

