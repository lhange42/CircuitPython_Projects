import board#pylint: disable-msg=import-error
import time
import simpleio#pylint: disable-msg=import-error
import pulseio#pylint: disable-msg=import-error

rate1 = 0.005 # setting sleep times
rate2 = 0.01



class RGB: # creates a python library able to be used

    def __init__(self, r, g, b):
        print("you just made an object!")
        self.pwm_r = pulseio.PWMOut(r, frequency=1000, duty_cycle=0)#setting the PWM pins
        self.pwm_g = pulseio.PWMOut(g, frequency=1000, duty_cycle=0)
        self.pwm_b = pulseio.PWMOut(b, frequency=1000, duty_cycle=0)

    def change_name(self, newName):
        self.name = newName

    def change_pins(self, r, g, b):
        self.r = r
        #self.g = g
        #self.b = b

    def red(self):# creates red by only sending a signal to red pin
        self.pwm_r.duty_cycle=0
        self.pwm_g.duty_cycle=2**16-1
        self.pwm_b.duty_cycle=2**16-1

    def green(self):#Creates green by only sending a signal to green pin

        self.pwm_r.duty_cycle=2**16-1
        self.pwm_g.duty_cycle=0
        self.pwm_b.duty_cycle=2**16-1


    def cyan(self): # Creates cyan by sending power to both green and blue pins
        self.pwm_r.duty_cycle=2**16-1
        self.pwm_g.duty_cycle=0
        self.pwm_b.duty_cycle=0


    def magenta(self): # creates magenta by sending power to red and blue pins

        self.pwm_r.duty_cycle=0
        self.pwm_g.duty_cycle=2**16-1
        self.pwm_b.duty_cycle=0


    def yellow(self): # creates yellow by sending power to red and green
        self.pwm_r.duty_cycle=0
        self.pwm_g.duty_cycle=0
        self.pwm_b.duty_cycle=2**16-1

    def blue(self):# creates blue by sending power to blue pin
        self.pwm_r.duty_cycle=2**16-1
        self.pwm_g.duty_cycle=2**16-1
        self.pwm_b.duty_cycle=0

    def rainbow(self, rate):

        for i in range(0,2**16,128):# makes red start off on then decrease as green increases and blue is off
            self.pwm_r.duty_cycle = 0 + i
            self.pwm_g.duty_cycle = 2**16-1-i
            self.pwm_b.duty_cycle = 2**16-1
            time.sleep(rate)
        for i in range(0,2**16,128):# decreases green as red is off and blue increases
            self.pwm_r.duty_cycle = 2**16-1
            self.pwm_g.duty_cycle = 0+i
            self.pwm_b.duty_cycle = 2**16-1-i
            time.sleep(rate)
        for i in range(0,2**16,128):# increases red as blue decreases and green is off
            self.pwm_r.duty_cycle = 2**16-1-i
            self.pwm_g.duty_cycle = 2**16-1
            self.pwm_b.duty_cycle = 0+i
            time.sleep(rate)

