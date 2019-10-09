import board#pylint: disable-msg=import-error
import neopixel#pylint: disable-msg=import-error
import time
import digitalio#pylint: disable-msg=import-error
import pulseio#pylint: disable-msg=import-error
import touchio#pylint: disable-msg=import-error
import adafruit_motor#pylint: disable-msg=import-error


from rgb import RGB

r1 = board.D3
g1 = board.D4
b1 = board.D5

r2 = board.D1
g2 = board.D2
b2 = board.D7

rate1 = 0.005
rate2 = 0.001

myRGB1 = RGB(r1,g1,b1)   # create a new RGB object, using pins 2, 3, and 4
myRGB2 = RGB(r2,g2,b2)   # create a new RGB object, using pins 5, 6, and 7


#print(myRGB1.kind)
#print(myRGB2.kind)
myRGB1.change_name("rex")







myRGB1.red() # first RGB LED glow red

myRGB2.green()   # second RGB LED glow green

time.sleep(1)

myRGB1.blue()    # first RGB LED glow blue

myRGB2.cyan()   # second RGB LED glow cyan

time.sleep(1)

myRGB1.magenta() # first RGB LED glow magenta

myRGB2.yellow() # second RGB LED glow yellow

time.sleep(1)
# extra spicy (optional) part
myRGB1.rainbow(rate1) # first RGB LED Fade through the colors of the rainbow at the given rate.

myRGB2.rainbow(rate2) # second RGB LEDFade through the colors of the rainbow at the given rate.  
time.sleep(1)