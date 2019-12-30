#!/usr/bin/env python3
# B Rasitha Fernando

import rospy
from std_msgs.msg import String
import signal
from adafruit_servokit import ServoKit
import board
import busio
import time

i2c_bus0=(busio.I2C(board.SCL_1,board.SDA_1))
kit = ServoKit(channels=16)

kit.continuous_servo[3].throttle = 0.0
time.sleep(1)
kit.continuous_servo[3].throttle = 0.05
time.sleep(1)
kit.continuous_servo[3].throttle = 0.1
time.sleep(1)
kit.continuous_servo[3].throttle = 0.2
time.sleep(1)
kit.continuous_servo[3].throttle = 0.3

def callback(data):
      dec = data.data
      print(dec)
      dec = int(dec)
      kit.continuous_servo[3].throttle = 0.23

      if dec == 0:
        kit.continuous_servo[3].throttle = 0
        kit.servo[0].angle = 90
      else:
        kit.servo[0].angle = dec

def listener():
 rospy.init_node('listener', anonymous=True)
 rospy.Subscriber('chatter', String, callback, queue_size=1)
 rospy.spin()

if __name__ == '__main__':
 listener()
