#Lukas Hange
# 9/4/19
# Make a Photo Interruptor read the amount of interruptions in a 4
#second period wihtout using sleep()





import board#pylint: disable-msg=import-error
import math
import time
import digitalio#pylint: disable-msg=import-error
import adafruit_bus_device#pylint: disable-msg=import-error


photoPin = digitalio.DigitalInOut(board.D8)#Sets up pin 8
photoPin.direction = digitalio.Direction.INPUT
photoPin.pull = digitalio.Pull.UP

Interrupts = -1
initial = time.monotonic()

lread = True
fread = True




while True:
    now = time.monotonic()#works as a timer so it counts down

    if now - initial == 4:
        print("Number of interruptions: " + str(Interrupts))# print the amount of interrupts in that period
        initial = time.monotonic()

    if photoPin.value:
        lread = True

    elif fread == lread:# Is an esle if statement
        Interrupts +=1# adds one interrupt
        lread = not lread
