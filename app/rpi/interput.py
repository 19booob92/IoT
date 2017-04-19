import RPi.GPIO as GPIO
import time
from diode import *
from diode import accessGrant
from move import checkMove 

class Interput():

	rows = [4,17,27,22]
	cols = [14,15,18,23]
	
	PASS_LEN = 4
	
	enableAlarm = False
	
	KEYBOAR_MAP = [['1','2','3','F1'],
		       ['4','5','6','F2'],
		       ['7','8','9', 'F3'],
		       ['START', '0', 'STOP', 'F4']]
	
	
	def init(self):	
		GPIO.setmode(GPIO.BCM)
		
		for colPin in self.cols:
			GPIO.setup(colPin, GPIO.OUT)
			GPIO.add_event_detect(colPin, GPIO.FALLING, callback = self.watchKeyboard)

		for rowPin in self.rows:
			GPIO.setup(rowPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
			GPIO.add_event_detect(rowPin, GPIO.FALLING, callback = self.watchKeyboard)
	
	def readKey(self):
		key = None
		for colIdx, colPin in enumerate(self.cols):
			GPIO.output(colPin, GPIO.HIGH)
			for rowIdx, rowPin in enumerate(self.rows):
				if GPIO.input(rowPin):
					blink()
					key = self.KEYBOAR_MAP[colIdx][rowIdx]
			GPIO.output(colPin, GPIO.LOW)
		time.sleep(0.3)	
		return key
	
	def watchKeyboard(self, enableAlarm):
		key = self.readKey()
		password = ''		
		
		if key == 'START' or key == 'STOP':
			while len(password) < self.PASS_LEN:
				passEl = self.readKey()
				if passEl:
					password = password + passEl
					print password
	
		if password == '1234':
			accessGrant()
			
			if key == 'START' and not self.enableAlarm:
				self.enableAlarm = True
				turnOn()
				
			elif key == 'STOP' and self.enableAlarm:
				self.enableAlarm = False
				turnOff()
			else:
				print 'Upewnij sie, ze alarm jest w stanie ktorego sie spodziewasz !'
	
		checkMove(enableAlarm)
	
