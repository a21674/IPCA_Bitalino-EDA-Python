from bitalinoConfig import *
from plotConfig import Communicate
import numpy as np

def dataSendLoop(addData_callbackFunc):
    # Setup the signal-slot mechanism.
    mySrc = Communicate()
    mySrc.data_signal.connect(addData_callbackFunc)

    # Simulate some data

    while True:
        #print(device.read(nSamples))
        samples = np.array(device.read(nSamples))
        #print(samples[:, 5])

        for x in samples:
            for y in x:
                data = x[5]
                yAxis = ((float(data) / (2 ** resolution)) * 3.3) / 0.132
                print(yAxis)
                mySrc.data_signal.emit(yAxis)
        time.sleep(0.01) #segundos

