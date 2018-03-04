#!/usr/bin/python

import time
import status

status.allRed()
detectorValues = status.readDetectorValues()

if detectorValues[2 - 1] == "Y" or detectorValues[6 - 1] == "Y":
	status.allRed()
	status.setSignalStatus(2, "Green")
	status.setSignalStatus(6, "Green")
	time.sleep(15)
	
detectorValues = status.readDetectorValues()
if detectorValues[1 - 1] == "Y" or detectorValues[5 - 1] == "Y":
	status.allRed()
	status.setSignalStatus(1, "Green")
	status.setSignalStatus(5, "Green")
	time.sleep(15)
	
detectorValues = status.readDetectorValues()
if detectorValues[4 - 1] == "Y" or detectorValues[8 - 1] == "Y":
	status.allRed()
	status.setSignalStatus(4, "Green")
	status.setSignalStatus(8, "Green")
	time.sleep(15)
	
detectorValues = status.readDetectorValues()
if detectorValues[3 - 1] == "Y" or detectorValues[7 - 1] == "Y":
	status.allRed()
	status.setSignalStatus(3, "Green")
	status.setSignalStatus(7, "Green")
	time.sleep(15)
	