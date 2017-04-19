import RPi.GPIO as GPIO
import time

greenPin = 21
redPin = 20
bluePin = 16


GPIO.setmode(GPIO.BCM)

GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

while True:
	for i in [greenPin, redPin, bluePin]:
		GPIO.output(i, GPIO.LOW)	
		time.sleep(0.5)
		GPIO.output(i, GPIO.HIGH)	
		time.sleep(0.7)


