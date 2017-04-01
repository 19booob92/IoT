#!/bin/python

from controller import Controller

from klein import Klein
from twisted.web.static import File

class AlarmController(object, Controller):

    isAlarmEnable = False

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

