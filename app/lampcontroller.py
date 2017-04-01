#!/bin/python
from controller import Controller

from klein import Klein
from twisted.web.static import File

class LampController(object, Controller):
	isLampOn = False

	def lampState(self, request):
		request.setResponseCode(200);
		return str(isLampOn)


