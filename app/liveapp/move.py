import RPi.GPIO as GPIO
import time
import pickle
import threading

inputPin = 26

from mailsender import *
from diode import *

GPIO.setmode(GPIO.BCM)

GPIO.setup(inputPin, GPIO.IN)

class Time_buffer(threading.Thread):
	def run(self):
		waitOneMinuteForDisableAlarm()	

def sysAlarmState():
        filePickle = open('/home/pi/Programs/shared.pkl')
        shared = pickle.load(filePickle)
        return shared['alarmState']


def checkMove(isAlaemEnable, waitingForPin):
	move = GPIO.input(inputPin)
	
	if move and isAlaemEnable == 'true' and not waitingForPin:
		time.sleep(2)
		timeBuffer = Time_buffer(name = 'time buffer')
		timeBuffer.start()
		
	if move and isAlaemEnable == 'true':
		return True

	return False
			

def waitOneMinuteForDisableAlarm():
	waitingForPin = True
	time.sleep(60)
	if sysAlarmState() == 'true':
		print 'Ktos sie porszyl !!!'
		turnOff()
		send_email('w domu znajduje sie intruz !!!')
		
