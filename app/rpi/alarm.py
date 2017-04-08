import time
from color import *
from .. mailsender import send_email

class Alarm():

    def setUpAlarm(self):
        self.scanPort()
        self.blinkDiode(repts = 5, color = RED)

    def scanPort(self):
        send_email("Wykryto zagrożenie")
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
