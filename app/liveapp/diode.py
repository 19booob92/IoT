import RPi.GPIO as GPIO
import time

greenPin = 21
redPin = 20
bluePin = 16


GPIO.setmode(GPIO.BCM)

GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

def accessGrant():
	for i in [greenPin, redPin, bluePin]:
		GPIO.output(i, GPIO.LOW)	
		time.sleep(0.2)
		GPIO.output(i, GPIO.HIGH)	
		time.sleep(0.2)

def blink():
	GPIO.output(bluePin, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(bluePin, GPIO.HIGH)

def turnOff():
	GPIO.output(greenPin, GPIO.LOW)
	time.sleep(1.)
	GPIO.output(greenPin, GPIO.HIGH)

def turnOn():
	GPIO.output(redPin, GPIO.LOW)
	time.sleep(1.)
	GPIO.output(redPin, GPIO.HIGH)

def turnOnDiode():
	GPIO.output(bluePin, GPIO.LOW)

def turnOffDiode():
	GPIO.output(bluePin, GPIO.HIGH)
