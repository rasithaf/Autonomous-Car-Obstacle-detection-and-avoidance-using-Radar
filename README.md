# Obstacle-detection-and-avoidance-using-Radar

This project was built on Jetson Nano developer kit, RC Car, and Perception SSR 2.0 Radar.

I tested the project on the following environment: (If you are not using ROS environment, remove the ros commands in the code) 

Ubuntu 18.04,
Python,
ROS Melodic,
Numpy,
OpenCV

# Steps to run RC Car in Autonomous mode with Radar: 

• Before executing the commands in the terminal, we have to make sure RC car is setup with radar, CAN device, Jetson Nano mounted on it and all the batteries are connected. 
[ two 11.1V batteries and one 7.4V] 

11.1 V batteries: one is used to power CAN device, other is used to power Jetson Nano 
7.4 V battery is used to power servo motor (don’t connect this before shutting down your system)  

• Remember the PerceptIn Radar has a blind spot of 50 cm. 

Pre-requisite: 

• Clone the kvaser interface into the catkin workspace: https://github.com/astuff/kvaser_interface 

Use the following steps mentioned below to run the RC car with mounted Radar 

• Make a ROS package for radar_publisher.py and servo_subscriber.py 

• ROS node in a new terminal: roscore 

• CAN launch in a new terminal: roslaunch kvaser_interface kvaser_can_bridge.launch 

• Radar code in a new terminal: rosrun radar radar_publisher.py 

• Servo activation in a new terminal: rosrun radar servo_subscriber.py  

** Don’t forget to source devel/setup.bash all new terminals 
** Read the Manual for Perceptin SSR 2.0 Radar to understand the code

Output video: https://www.youtube.com/watch?v=EJrg3fXb-l0
                    

