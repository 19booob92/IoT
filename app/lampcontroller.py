#!/bin/python
from controller import Controller

from klein import Klein
from twisted.web.static import File


class LampController(object, Controller):
    isLampOn = False

    def getLampState(self, request):
        request.setHeader('Access-Control-Allow-Origin', '*')
        request.setResponseCode(200);
        return str(self.isLampOn);

    def enableLamp(self, request):
        request.setHeader('Access-Control-Allow-Origin', '*')

        if self.isLampOn:
            request.setResponseCode(405)
            return "lamp is enable yet"
        else:
            self.isLampOn = True
            request.setResponseCode(200);
            return "lamp is on"

    def disableLamp(self, request, pin):
        request.setHeader('Access-Control-Allow-Origin', '*')

        if not self.isLampOn:
            request.setResponseCode(405)
            return "lamp is disable yet"
        else:
            if pin == self.pin:
                self.isLampOn = False
                request.setResponseCode(200);
                return "lamp is off"
            else:
                request.setResponseCode(401);
                return "wrong pin"

