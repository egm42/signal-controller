#!/usr/bin/python
import time

#signalStatus file is updated every 15 seconds with the indication colors
#Currently only supports green and red
statusFile = "/var/www/html/signal-controller/controller/signalStatus"
time.sleep(15)
file = open(statusFile, "w")
file.write("Red\nGreen\nRed\nRed\nRed\nGreen\nRed\nRed")
file.close()
time.sleep(15)
file = open(statusFile, "w")
file.write("Green\nRed\nRed\nRed\nGreen\nRed\nRed\nRed")
file.close()
time.sleep(15)
file = open(statusFile, "w")
file.write("Red\nRed\nRed\nGreen\nRed\nRed\nRed\nGreen")
file.close()
time.sleep(15)
file = open(statusFile, "w")
file.write("Red\nRed\nGreen\nRed\nRed\nRed\nGreen\nRed")
file.close()
