#Lukas
#This is the main for the Fancy Led code this section just told it which code to run
#10/2/19

import board #pylint: disable-msg=import-error
from fancyLED import FancyLED

fancy1 = FancyLED( board.D2, board.D3, board.D4)# setting Leds to the these pins
fancy2 = FancyLED( board.D5, board.D6, board.D7)# setting Leds to the these pins

while True:

    fancy1.alternate()#run the alternate code in my FancyLed.py code
    fancy2.blink()#run the blink code in my FancyLed.py code
    fancy1.chase()#run the chase code in my FancyLed.py code
    fancy2.sparkle()#run the sparkle code in my FancyLed.py code


