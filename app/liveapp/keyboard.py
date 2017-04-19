import RPi.GPIO as GPIO
import time
from diode import *
from move import checkMove 

import os
import pickle 

def setUpAlarmState(state):
	filePickle = open('/home/pi/Programs/shared.pkl', 'w')
	shared = {'alarmState': state}
	print 'test', shared
	pickle.dump(shared, filePickle)
	
def sysAlarmState():
   	filePickle = open('/home/pi/Programs/shared.pkl')
	shared = pickle.load(filePickle)
	return shared['alarmState']

setUpAlarmState('false')

rows = [4,17,27,22]
cols = [14,15,18,23]

PASS_LEN = 4

KEYBOAR_MAP = [['1','2','3','F1'],
	       ['4','5','6','F2'],
	       ['7','8','9', 'F3'],
	       ['START', '0', 'STOP', 'F4']]

GPIO.setmode(GPIO.BCM)

for rowPin in rows:
	GPIO.setup(rowPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

for colPin in cols:
	GPIO.setup(colPin, GPIO.OUT)

def readKey():
	key = None
	for colIdx, colPin in enumerate(cols):
		GPIO.output(colPin, GPIO.HIGH)
		for rowIdx, rowPin in enumerate(rows):
			if GPIO.input(rowPin):
				blink()
				key = KEYBOAR_MAP[colIdx][rowIdx]
		GPIO.output(colPin, GPIO.LOW)
	time.sleep(0.3)	
	return key

waitintForPin = False

while True:
	key = readKey()
	password = ''		
	
	enableAlarm = sysAlarmState()

	if key == 'START' or key == 'STOP':
		while len(password) < PASS_LEN:
			passEl = readKey()
			if passEl:
				password = password + passEl
				print password

	if password == '1234':
		accessGrant()
		
		if key == 'START' and enableAlarm == 'false':
			enableAlarm = True
			setUpAlarmState('true')
			turnOn()
			
		elif key == 'STOP' and enableAlarm == 'true':
			enableAlarm = False
			setUpAlarmState('false')
			turnOff()
		else:
			print 'Upewnij sie, ze alarm jest w stanie ktorego sie spodziewasz !'

	waitintForPin = checkMove(enableAlarm, waitintForPin)
