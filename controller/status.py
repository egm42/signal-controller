
def readDetectorValues():
	file = open("/var/www/html/signal-controller/controller/detectorStatus", "r")
	values = file.read().split("\n")
	return values;

def setDetectorValues(detector, trigger):
	file = open("/var/www/html/signal-controller/controller/detectorStatus", "r")
	status = file.read().split("\n")
	status[detector - 1] = trigger
	file = open("/var/www/html/signal-controller/controller/detectorStatus", "w")
	file.write("\n".join(status))
	file.close()

def setSignalStatus(phase, phaseIndication):
	file = open("/var/www/html/signal-controller/controller/signalStatus", "r")
	status = file.read().split("\n")
	status[phase - 1] = phaseIndication
	file = open("/var/www/html/signal-controller/controller/signalStatus", "w")
	file.write("\n".join(status))
	file.close()

def allRed():
	for x in range(1, 9):
		setSignalStatus(x, "Red")