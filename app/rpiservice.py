#!/bin/python

import json
import os

class RpiService():

    def getStatus(self, request):
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
        data['top'] = self.processTerminalOutput('top')


    def processTerminalOutput(self, command):
        output = os.popen(command)
        return output.read()