import time
from color import *

class Alarm():

    def setUpAlarm(self):
        self.scanPort()
        self.blinkDiode(repts = 5, color = RED)

    def scanPort(self):
        pass

    def disableAlarm(self):
        self.blinkDiode(repts=2, color=BLUE)

    def blinkDiode(self, repts, color):
        for i in range(repts):
            pass

    def setTimeForDisable(self):
        pass

    def disableByKeyboard(self):
        pass
