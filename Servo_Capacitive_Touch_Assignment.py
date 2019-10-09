#Lukas Hange
#
#Making a wire turn one way or the other depending on which wire is touched

import time
import board#pylint: disable-msg=import-error
import pulseio#pylint: disable-msg=import-error
import math
import adafruit_motor#pylint: disable-msg=import-error
import neopixel#pylint: disable-msg=import-error
import digitalio#pylint: disable-msg=import-error
import analogio#pylint: disable-msg=import-error
import touchio#pylint: disable-msg=import-error
from adafruit_motor import servo#pylint: disable-msg=import-error

Servo_angle = 0


pwm = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)

touch_A1 = touchio.TouchIn(board.A1)# assigning touch_a1 to pin A1
touch_A2 = touchio.TouchIn(board.A2)# assigning touch_a2 to pin A2

my_servo = servo.Servo(pwm)

while True:

    if touch_A1.value and Servo_angle < 180:# when the first wire is touched and the servo degree<180 make servo angle increase by 5
        print('A1 Touched')
        Servo_angle += 5
        my_servo.angle = Servo_angle
        print(Servo_angle)





    if touch_A2.value and Servo_angle > 0:# when the second wire is touched and the servo degree>0 make servo angle is decreased by 5
        print('A2 Touched')
        Servo_angle -= 5
        my_servo.angle = Servo_angle
        print(Servo_angle)

    time.sleep(.01)