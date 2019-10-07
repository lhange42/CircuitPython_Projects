#Lukas Hange
# LCD assignment button press with switch this assignment makes while make your button counter go up when switched one way and the other when flipped the other way
#8/30/19


import board #importing everything needed
import math
import time
import digitalio
import adafruit_bus_device

from lcd.lcd import LCD

from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from lcd.lcd import CursorMode


button = digitalio.DigitalInOut(board.D2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP


SwitchState = digitalio.DigitalInOut(board.D3)
SwitchState.direction = digitalio.Direction.INPUT
SwitchState.pull = digitalio.Pull.UP


lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)



counter = 0
oldSwitchState = 0
newSwitchState = 1
adder=1

while True:

    lcd.clear()
    lcd.set_cursor_pos(1,0)
    lcd.print("pressed:")

    lcd.set_cursor_pos(1,9)
    lcd.print(str(counter))




    if button.value:
        print("0")
        time.sleep(0.05)
        oldSwitchState = 0

    elif oldSwitchState == 0 and newSwitchState == 1:

        if SwitchState.value:
            adder = 1
        else:
            adder = -1
        print("1")


        time.sleep(0.05)
        counter += adder

        oldSwitchState = 1
