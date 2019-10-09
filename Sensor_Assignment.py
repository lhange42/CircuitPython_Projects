#Lukas Hange
#9/11
#Get sensor read distance and change color of inboard Led accordingly.

import board#pylint: disable-msg=import-error
import neopixel#pylint: disable-msg=import-error
import math
import time
import digitalio#pylint: disable-msg=import-error
import adafruit_bus_device#pylint: disable-msg=import-error
import adafruit_hcsr04#pylint: disable-msg=import-error
import simpleio#pylint: disable-msg=import-error

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D11, echo_pin=board.D12)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness = .1)
r = 0
g = 0
b = 0


while True:




   while True:

    try:
        print((sonar.distance,))# prints the distance
        if sonar.distance <= 20:# when distance is less then 20 it starts red and goes to blue

            r = simpleio.map_range(sonar.distance, 0,20,255,0)
            b = simpleio.map_range(sonar.distance, 5,20,0,255)
            g = simpleio.map_range(sonar.distance, 20,35,0,255)

        else: # when its not less than or equal to 20 it will go from blue to green
            r = simpleio.map_range(sonar.distance, 0,20,255,0)
            b = simpleio.map_range(sonar.distance, 35,20,0,255)
            g = simpleio.map_range(sonar.distance, 20,35,0,255)

        dot.fill((int(r),int(g),int(b)))
    except RuntimeError:
        print("Retrying!")


    time.sleep(0.1)