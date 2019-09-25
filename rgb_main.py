import board
import neopixel
import time
import digitalio
import pulseio
import touchio
import adafruit_motor


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







myRGB1.red() # Glow red

myRGB2.green()        # Glow green

time.sleep(1)

myRGB1.blue()         # Glow blue

myRGB2.cyan()         # Glow... you get it...

time.sleep(1)

myRGB1.magenta()      # Did you know magenta isn't in the rainbow?

myRGB2.yellow() # Like you learned in first grade, red and green make... huh?

time.sleep(1)
# extra spicy (optional) part
myRGB1.rainbow(rate1) # Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!

myRGB2.rainbow(rate2) # Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
time.sleep(1)