#Lukas Hange
# 9/4/19
# Make a Photo Interruptor read the amount of interruptions in a 4
#second period wihtout using sleep()





import board
import math
import time
import digitalio
import adafruit_bus_device


photoPin = digitalio.DigitalInOut(board.D8)
photoPin.direction = digitalio.Direction.INPUT
photoPin.pull = digitalio.Pull.UP

Interrupts = -1
initial = time.monotonic()

lread = True
fread = True




while True:
    now = time.monotonic()

    if now - initial == 4:
        print("Number of interruptions: " + str(Interrupts))
        initial = time.monotonic()

    if photoPin.value:
        lread = True

    elif fread == lread:
        Interrupts +=1
        lread = not lread
