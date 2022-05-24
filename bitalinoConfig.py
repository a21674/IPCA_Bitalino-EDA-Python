import time
from bitalino import BITalino

# The macAddress variable on Windows can be "XX:XX:XX:XX:XX:XX" or "COMX"
# while on Mac OS can be "/dev/tty.BITalino-XX-XX-DevB" for devices ending with the last 4 digits of the MAC address or "/dev/tty.BITalino-DevB" for the remaining
macAddress = "98:D3:61:FD:6E:31"
#macAddress = "98:D3:91:FD:58:66" #Rafael

batteryThreshold = 30
acqChannels = [2]  # EDA = 2 - [0, 1, 2, 3, 4, 5]
samplingRate = 10  # Hz [1, 10, 100, 1000]
nSamples = 10

# resolution : int, optional -> Sampling resolution used during acquisition (6-bit or 10-bit; default: 10-bit).
resolution = 10

# [TRANSFER FUNCTION]
# 	EDA(µS) = ((((ADC/2^n) * VCC) - 0.574) / 0.132)
# 		EMG(mV)		Sample value in mV.
# 		ADC			Value sampled from the channel (raw value)
# 		n 			Number of bits of the channel
# 		VCC			Operating voltage; 3.3V
# 		GEMG		Sensor gain (1009)
# 	[RANGE]
# 	-4.4µS to 21µS

digitalOutput_on = [1, 1]
digitalOutput_off = [0, 0]

# Connect to BITalino
device = BITalino(macAddress)

# Set battery threshold
device.battery(batteryThreshold)

# Read BITalino version
print(device.version())

# Start Acquisition
device.start(samplingRate, acqChannels)

start = time.time()
end = time.time()

