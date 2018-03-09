#!/usr/bin/python

import time
import status

status.allRed()
i = 1

#The controller will keep cycling as long as the "on-off" value in status.json is set to 1
while status.state():
	#Current controller operation is 4 phases
	for x in range(1, 5):
		sigParameters = status.sigParameters()
		#If statement checks to ensure that at least 1 detector is active for each phase
		if status.readDetectorValues()[str(sigParameters["ring"]["1"][str(x)])] or status.readDetectorValues()[str(sigParameters["ring"]["2"][str(x)])]:
			status.allRed()
			status.setSignalStatus(str(sigParameters["ring"]["1"][str(x)]), 1)
			status.setSignalStatus(str(sigParameters["ring"]["2"][str(x)]), 1)
		sleep = max(sigParameters["minGreen"][str(sigParameters["ring"]["1"][str(x)])], sigParameters["minGreen"][str(sigParameters["ring"]["2"][str(x)])])
		time.sleep(sleep)