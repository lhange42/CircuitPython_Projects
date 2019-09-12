#
#
#

import time
import board
import pulseio
import math
import adafruit_motor
import neopixel
import digitalio
import analogio
import touchio
from adafruit_motor import servo


pwm = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)


Servo_Angle = 0

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)

my_servo = servo.Servo(pwm)

while True:

   if touch_A1.value and Servo_Angle < 180:
        print('A1 Touched')
        Servo_Angle += 1
        my_servo.angle = Servo_Angle

   if touch_A2.value and Servo_Angle > 0:
        print('A2 Touched')
        Servo_Angle -= 1
        my_servo.angle = Servo_Angle



time.sleep(0.001)