import RPi.GPIO as GPIO
import time
from diode import *
from diode import accessGrant
from move import checkMove 

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

def watchKeyboard(enableAlarm):
	while True:
		key = readKey()
		password = ''		
		
		if key == 'START' or key == 'STOP':
			while len(password) < PASS_LEN:
				passEl = readKey()
				if passEl:
					password = password + passEl
					print password

		if password == '1234':
			accessGrant()
			
			if key == 'START' and not enableAlarm:
				enableAlarm = True
				turnOn()
				
			elif key == 'STOP' and enableAlarm:
				enableAlarm = False
				turnOff()
			else:
				print 'Upewnij sie, ze alarm jest w stanie ktorego sie spodziewasz !'

		checkMove(enableAlarm)

