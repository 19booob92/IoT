#!/bin/python

from controller import Controller
from lampcontroller import LampController
from alarmcontroller import AlarmController

from klein import Klein
from twisted.web.static import File

class IntexController(object, Controller):

    alarmCtrl = AlarmController()
    lampCtrl = LampController()

    app = Klein()

    def __init__(self):
        self.__items__ = {}

    @app.route('/', branch=True)
    def mainPage(self, request):
        return File('../pages/')

    @app.route('/enableAlarm')
    def satUpAlarm(self, request):
        return self.alarmCtrl.satUpAlarm(request)

    @app.route('/disableAlarm/<int:pin>')
    def disableAlarm(self, request, pin):
        return self.alarmCtrl.disableAlarm(request, pin)

    @app.route('/alarmState')
    def getAlarmState(self, request):
        return self.alarmCtrl.getAlarmState(request)


if __name__ == '__main__':
    mainController = IntexController()

    mainController.app.run('localhost', 10000)
