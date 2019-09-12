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

Servo_angle = 0


pwm = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)

my_servo = servo.Servo(pwm)

while True:

    if touch_A1.value and Servo_angle < 180:
        print('A1 Touched')
        Servo_angle += 5
        my_servo.angle = Servo_angle
        print(Servo_angle)





    if touch_A2.value and Servo_angle > 0:
        print('A2 Touched')
        Servo_angle -= 5
        my_servo.angle = Servo_angle
        print(Servo_angle)

    time.sleep(.01)