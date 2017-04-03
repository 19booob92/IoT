#!/bin/python

from controller import Controller
from alarmdata import AlarmData
import json


class AlarmController(object, Controller):
    isAlarmEnable = False
    alarmData = AlarmData()

    def satUpAlarm(self, request):
        request.setHeader('Access-Control-Allow-Origin', '*')
        if self.isAlarmEnable:
            request.setResponseCode(405)
            return 'alarm is on yet'

        self.isAlarmEnable = True
        return 'alarm is on'

    def disableAlarm(self, request, pin):
        request.setHeader('Access-Control-Allow-Origin', '*')
        if not self.isAlarmEnable:
            request.setResponseCode(405)
            return 'alarm is off yet'

        if pin == self.pin:
            request.setResponseCode(200)
            self.isAlarmEnable = False
            return 'alarm is off'
        request.setResponseCode(401)
        return 'wrong pin'

    def getAlarmState(self, request):
        request.setResponseCode(200)
        return str(self.isAlarmEnable)

    def saveAlarmData(self, request):
        self.alarmData.secondsToDeactivate = request.args['secondsToDeactivate']
        self.alarmData.sendMailDelay = request.args['sendMailDelay']
        request.redirect('/index.html')

    def getAlarmData(self, request):
        request.setHeader('Content-Type', 'application/json')
        return json.dumps(
            {'secondsToDeactivate': self.alarmData.secondsToDeactivate,
             'sendMailDelay': self.alarmData.sendMailDelay})
