#!/usr/bin/python
import sys
sys.path.insert(0, "/../../var/www/html/signal-controller/controller")
import time
import status

for x in range(1, 9):
	status.setDetectorValues(x, "Y")

detectorValues = status.readDetectorValues()
if detectorValues[2 - 1] == "Y" and detectorValues[6 - 1] == "Y":
	status.setSignalStatus(2, "Green")
	status.setSignalStatus(6, "Green")
	status.setDetectorValues(2, "N")
	status.setDetectorValues(6, "N")
else:
	status.setSignalStatus(4, "Green")
	status.setSignalStatus(8, "Green")
	status.setDetectorValues(4, "N")
	status.setDetectorValues(8, "N")
time.sleep(5)
	
detectorValues = status.readDetectorValues()
if detectorValues[2 - 1] == "Y" and detectorValues[6 - 1] == "Y":
	status.setSignalStatus(2, "Green")
	status.setSignalStatus(6, "Green")
	status.setDetectorValues(2, "N")
	status.setDetectorValues(6, "N")
else:
	status.setSignalStatus(4, "Green")
	status.setSignalStatus(8, "Green")
	status.setDetectorValues(4, "N")
	status.setDetectorValues(8, "N")
	
time.sleep(5)