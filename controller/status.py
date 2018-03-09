import json

def readDetectorValues():
	with open("/var/www/html/signal-controller/controller/status.json", "r") as file:
		fileJSON = json.loads(file.read())
		return fileJSON["input"]["vehicle"]

def setDetectorValues(detector, trigger):
	with open("/var/www/html/signal-controller/controller/status.json", "r") as file:
		fileJSON = json.loads(file.read())
		fileJSON["input"]["vehicle"][str(phase)] = trigger
	
	with open("/var/www/html/signal-controller/controller/status.json", "w") as file:
		json.dump(fileJSON, file)
		file.close()
	
def setSignalStatus(phase, phaseIndication):
	with open("/var/www/html/signal-controller/controller/status.json", "r") as file:
		fileJSON = json.loads(file.read())
		fileJSON["output"]["vehicle"][str(phase)] = phaseIndication
	
	with open("/var/www/html/signal-controller/controller/status.json", "w") as file:
		json.dump(fileJSON, file)
		file.close()
	
def allRed():
	for x in range(1, 9):
		setSignalStatus(x, 3)
		
def sigParameters():
	with open("/var/www/html/signal-controller/controller/sigParameters.json", "r") as file:
		fileJSON = json.loads(file.read())
		return fileJSON
		
def state():
	with open("/var/www/html/signal-controller/controller/status.json", "r") as file:
		fileJSON = json.loads(file.read())
		return fileJSON["on-off"]