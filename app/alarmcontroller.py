#!/bin/python

from controller import Controller
from alarmdata import AlarmData
import json
import os

class AlarmController(object, Controller):
    alarmData = AlarmData()

    def satUpAlarm(self, request):
        request.setHeader('Access-Control-Allow-Origin', '*')

	print 'test ///* ** true'
	self.setUpAlarmState('true')
	return 'alarm is on'

    def disableAlarm(self, request, pin):
        request.setHeader('Access-Control-Allow-Origin', '*')
        if self.sysAlarmState() == 'false':
            request.setResponseCode(405)
            return 'alarm is off yet'

        if pin == self.pin:
            request.setResponseCode(200)
            self.setUpAlarmState('false')
            return 'alarm is off'
        request.setResponseCode(401)
        return 'wrong pin'

    def getAlarmState(self, request):
        request.setResponseCode(200)
        return self.sysAlarmState()

    def saveAlarmData(self, request):
        self.alarmData.secondsToDeactivate = request.args['secondsToDeactivate']
        self.alarmData.sendMailDelay = request.args['sendMailDelay']
        request.redirect('/index.html')

    def getAlarmData(self, request):
        request.setHeader('Content-Type', 'application/json')
        return json.dumps(
            {'secondsToDeactivate': self.alarmData.secondsToDeactivate,
             'sendMailDelay': self.alarmData.sendMailDelay})
