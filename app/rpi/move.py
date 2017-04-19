import RPi.GPIO as GPIO
import time
inputPin = 26

from diode import *

GPIO.setmode(GPIO.BCM)

GPIO.setup(inputPin, GPIO.IN)

def checkMove(isAlaemEnable):
	move = GPIO.input(inputPin)
	
	if move and isAlaemEnable:
		print 'Ktos sie porszyl !!!'
		turnOff()
		time.sleep(2)
