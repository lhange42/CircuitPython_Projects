#Lukas Hange
#9/11
#Get sensor read distance and change color of inboard Led accordingly.

import board
import neopixel
import math
import time
import digitalio
import adafruit_bus_device
import adafruit_hcsr04
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D11, echo_pin=board.D12)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness = .1)
r = 0
g = 0
b = 0


while True:




    try:
        print((sonar.distance,))

        if sonar.distance < 20 :
            r = simpleio.map_range(sonar.distance,0,20,255,0)
            b = simpleio.map_range(sonar.distance,5,20,0,255)
            g = simpleio.map_range(sonar.distance,20,35,0,255)
        else:
            r = simpleio.map_range(sonar.distance,0,20,255,0)
            b = simpleio.map_range(sonar.distance,35,20,255,0)
            g = simpleio.map_range(sonar.distance,20,35,0,255)

        dot.fill((int(r),int(b),int(g)))
    except RuntimeError:
        print("Retrying!")


    time.sleep(0.1)