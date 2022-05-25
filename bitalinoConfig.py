# [TRANSFER FUNCTION]
# 	EDA(µS) = ((((ADC/2^n) * VCC) - 0.574) / 0.132)
# 		EMG(mV)		Sample value in mV.
# 		ADC			Value sampled from the channel (raw value)
# 		n 			Number of bits of the channel
# 		VCC			Operating voltage; 3.3V
# 		GEMG		Sensor gain (1009)
#       resolution : int, optional -> Sampling resolution used during acquisition (6-bit or 10-bit; default: 10-bit).
# 	[RANGE]
# 	-4.4µS to 21µS

class BitalinoDataRead(object):
    def __init__(self):
        self.macAddress = "98:D3:61:FD:6E:31"
        self.batteryThreshold = 30
        self.acqChannels = [2]  # EDA = 2 - [0, 1, 2, 3, 4, 5]
        self.samplingRate = 10  # Hz [1, 10, 100, 1000]
        self.nSamples = 10
        # resolution : int, optional -> Sampling resolution used during acquisition (6-bit or 10-bit; default: 10-bit).
        self.resolution = 10
        self.digitalOutput_on = [1, 1]
        self.digitalOutput_off = [0, 0]








