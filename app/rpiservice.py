#!/bin/python

import json
import os
from controller import Controller

class RpiService(object, Controller):

    def getStatus(self, request):
        request.setHeader('Access-Control-Allow-Origin', '*')
        request.setHeader('Content-Type', 'application/json')

        data = {}
        self.getData(data)
        return json.dumps(data)

    def getData(self, data):

        data['temp'] = self.processTerminalOutput('sensors')
        data['uptime'] = self.processTerminalOutput('uptime')
        data['ifconfig'] = self.processTerminalOutput('ifconfig')
        data['space'] = self.processTerminalOutput('df -h')
        data['memory'] = self.processTerminalOutput('free -m')

    def processTerminalOutput(self, command):
        output = os.popen(command)
        return output.read()