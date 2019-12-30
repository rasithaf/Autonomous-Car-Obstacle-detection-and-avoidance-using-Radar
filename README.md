# Obstacle-detection-and-avoidance-using-Radar
Perception SSR 2.0 Radar is used and Programming is done in Python for ROS environment

Steps to run RC Car with Radar: 

• Before executing the commands in the terminal, we have to make sure RC car is setup with radar, CAN device, Jetson Nano mounted on it and all the batteries are connected. 
[ two 11.1V batteries and one 7.4V] 

11.1 V batteries: one is used to power CAN device, other is used to power Jetson Nano 
7.4 V battery is used to power servo motor (don’t connect this before shutting down your system)  

• Remember the PerceptIn Radar has a blind spot of 50 cm. 

Pre-requisite: 

• Clone the kvaser interface into the catkin workspace: https://github.com/astuff/kvaser_interface 

Use the following steps mentioned below to run the RC car with mounted Radar 

• ROS node in a new terminal: roscore 

• CAN launch in a new terminal: roslaunch kvaser_interface kvaser_can_bridge.launch 

• Read the Manual for Perceptin SSR 2.0 Radar to understand the code

• Radar code in a new terminal: rosrun radar radar_publisher.py 

• Servo activation in a new terminal: rosrun radar servo_subscriber.py  

** Don’t forget to source devel/setup.bash all new terminals 
