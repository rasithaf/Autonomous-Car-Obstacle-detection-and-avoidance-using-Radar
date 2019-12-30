#!/usr/bin/env python
# B Rasitha Fernando

import rospy
import numpy as np
from can_msgs.msg import Frame
from std_msgs.msg import String
from std_msgs.msg import UInt8MultiArray
import time

def callback(data):
  if data.id != 1343:

    a = UInt8MultiArray
    a = [0,0,0,0,0,0,0,0]
    for i in range (8):
      a[i] = ord(data.data[i])

    byte_L4 = '{0:08b}'.format(a[5])
    byte_H4 = '{0:08b}'.format(a[6])
    Angle = byte_H4[3:8]+byte_L4[0:6]
    Angle = int(Angle,2)
    Angle = Angle*0.1     # scaled value
    if Angle > 102.3:
      Angle = Angle-204.8
    else: Angle = Angle
    Angle = round(Angle, 2)
    Radial_range = int

    theta = 35
    global distance
    distance = 2 #200 cm
    Radial_range1 = 100
    Radial_range2 = 100
    Radial_range3 = 100
    All_Range1.append(Radial_range1)
    All_Range2.append(Radial_range2)
    All_Range3.append(Radial_range3)

    if Angle < theta and Angle > theta-20: #35, 15

      byte_L1 = '{0:08b}'.format(a[0])
      byte_H1 = '{0:08b}'.format(a[1])
      Radial_range = byte_H1[1:8]+byte_L1
      Radial_range = int(Radial_range,2)
      Radial_range = Radial_range*0.01     # scaled value
      Radial_range = round(Radial_range, 2)
      All_Range1.append(Radial_range)

    if Angle < -theta+20 and Angle > -theta:  #-15, -35

      byte_L1 = '{0:08b}'.format(a[0])
      byte_H1 = '{0:08b}'.format(a[1])
      Radial_range = byte_H1[1:8]+byte_L1
      Radial_range = int(Radial_range,2)
      Radial_range = Radial_range*0.01     # scaled value
      Radial_range = round(Radial_range, 2)
      All_Range2.append(Radial_range)

    if Angle < theta-20 and Angle > -theta+20:  #15, -15

      byte_L1 = '{0:08b}'.format(a[0])
      byte_H1 = '{0:08b}'.format(a[1])
      Radial_range = byte_H1[1:8]+byte_L1
      Radial_range = int(Radial_range,2)
      Radial_range = Radial_range*0.01     # scaled value
      Radial_range = round(Radial_range, 2)
      All_Range3.append(Radial_range)

  if data.id >= 1343:
    Radial_range1 = min(All_Range1)
    Radial_range2 = min(All_Range2)
    Radial_range3 = min(All_Range3)

    if Radial_range1 > distance and Radial_range2 > distance:
      dec = 90
      print ("straight")

    elif Radial_range2 < distance:
      dec = 90- 50/distance * (Radial_range2 - distance) +20
      print ("go left")

    elif Radial_range1 < distance:
      dec = 90 + 50/distance *(Radial_range1 - distance) -20
      print ("go right")

    else:
      dec = 0

    if Radial_range3 < 1.6:
      dec = 0
      print ("stop")

    print (Radial_range1,Radial_range2, Radial_range3)
    dec = int(dec)
    y = str(dec)

    del All_Range1[:]
    del All_Range2[:]
    del All_Range3[:]

    pub = rospy.Publisher('chatter', String, queue_size=10)
    pub.publish(y)
    rospy.loginfo(y)

def listener():

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/can_tx', Frame, callback, queue_size=64)
    rospy.spin()

if __name__ == '__main__':
    global All_Range, All_Speed
    All_Range1 = UInt8MultiArray
    All_Range1 = []
    All_Range2 = UInt8MultiArray
    All_Range2 = []
    All_Range3 = UInt8MultiArray
    All_Range3 = []
    listener()
