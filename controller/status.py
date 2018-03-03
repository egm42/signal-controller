
def readDetectorValues():
	file = open("detectorStatus", "r")
	values = file.read().split("\n")
	return values;

def setDetectorValues(detector, trigger):
	file = open("detectorStatus", "r")
	status = file.read().split("\n")
	status[detector - 1] = trigger
	file = open("detectorStatus", "w")
	file.write("\n".join(status))
	file.close()

def setSignalStatus(phase, phaseIndication):
	file = open("signalStatus", "r")
	status = file.read().split("\n")
	status[phase - 1] = phaseIndication
	file = open("signalStatus", "w")
	file.write("\n".join(status))
	file.close()