#!/bin/python
import liveapp.config
import pickle

class Controller:
    pin = liveapp.config.pin

    def setUpAlarmState(self, state):
   	filePickle = open('/home/pi/Programs/shared.pkl', 'w')
	shared = {'alarmState': state}
	pickle.dump(shared, filePickle)
	
    def sysAlarmState(self):
   	filePickle = open('/home/pi/Programs/shared.pkl')
	shared = pickle.load(filePickle)
	return shared['alarmState']
