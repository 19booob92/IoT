#!/bin/python

from twisted.internet.defer import succeed
from controller import Controller
from lampcontroller import LampController
from alarmcontroller import AlarmController

from klein import Klein
from twisted.web.static import File


class IndexController(object, Controller):

    alarmCtrl = AlarmController()
    lampCtrl = LampController()

    app = Klein()

    def __init__(self):
        self.__items__ = {}

    @app.route('/', branch=True)
    def mainPage(self, request):
        request.redirect('/index.html')
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

    @app.route('/saveConfig', methods=['POST'])
    def saveAlarmData(self, request):
        self.alarmCtrl.saveAlarmData(request)
        succeed(None)

    @app.route('/loadAlarmConfig')
    def loadAlarmConfig(self, request):
        return self.alarmCtrl.getAlarmData(request)


if __name__ == '__main__':
    mainController = IndexController()

    mainController.app.run('192.168.8.100', 8081)
