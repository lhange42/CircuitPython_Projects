import time #pylint: disable-msg=import-error
import board #pylint: disable-msg=import-error
import digitalio#pylint: disable-msg=import-error
import random

class FancyLED:

    def __init__(self,p1,p2,p3):

        self.led1 = digitalio.DigitalInOut(p1)
        self.led1.direction = digitalio.Direction.OUTPUT

        self.led2 = digitalio.DigitalInOut(p2)
        self.led2.direction = digitalio.Direction.OUTPUT

        self.led3 = digitalio.DigitalInOut(p3)
        self.led3.direction = digitalio.Direction.OUTPUT

      
    def alternate(self):
        self.led1.value = True
        self.led2.value = False
        self.led3.value = True
        time.sleep(.1)

        self.led1.value = False
        self.led2.value = True
        self.led3.value = False

    def blink(self):
        self.led1.value = True
        self.led2.value = True
        self.led3.value = True
        time.sleep(.1)

        self.led1.value = False
        self.led2.value = False
        self.led3.value = False

    def chase(self):
        self.led1.value = True
        self.led2.value = False
        self.led3.value = False
        time.sleep(.25)

        self.led1.value = False
        self.led2.value = True
        self.led3.value = False
        time.sleep(.25)

        self.led1.value = False
        self.led2.value = False
        self.led3.value = True
        time.sleep(.25)

    def sparkle(self):
        n = random.randint(1,3)

        if n == 1:
            self.led1.value = True
            time.sleep(.25)
            self.led1.value = False
        if n == 2:
            self.led2.value = True
            time.sleep(.25)
            self.led2.value = False
        if n == 3:
            self.led3.value = True
            time.sleep(.25)
            self.led3.value = False


    def on(self):
        self.led1.value = True
        self.led2.value = True
        self.led3.value = True
        print("on")
