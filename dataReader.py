from bitalinoConfig import BitalinoDataRead
from bitalino import BITalino
from communicate import Communicate
import time
import numpy as np



def dataSendLoop(addData_callbackFunc, stop):
        # Setup the signal-slot mechanism.
        mySrc = Communicate()
        mySrc.data_signal.connect(addData_callbackFunc)
        
        bita = BitalinoDataRead() #instaciação da classe Bitalino
        device = BITalino(bita.macAddress) # Connect to BITalino
        device.battery(bita.batteryThreshold) # Set battery threshold
        print(device.version()) # Read BITalino version
        device.start(bita.samplingRate, bita.acqChannels) # Start Acquisition

        running_time = 15
        start = time.time()
        end = time.time()

        exportSamples = []

        while (end - start) < running_time:
            
            samples = np.array(device.read(bita.nSamples))
            #print(samples[:, 5])

            for x in samples:
                for y in x:
                    data = x[5]
                    yAxis = ((float(data) / (2 ** bita.resolution)) * 3.3) / 0.132
                    
                    exportSamples.append(yAxis)
                    mySrc.data_signal.emit(yAxis)
                    time.sleep(0.01) #segundos
                    
                    end = time.time()
                    
                    #se for invocado o stop para o loop
                    if (stop):
                        break
            
            handleData(exportSamples);
                                       
                
def handleData(exportSamples):
    print('teste export samples', exportSamples)