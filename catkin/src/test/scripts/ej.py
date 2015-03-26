#!/usr/bin/env python
import roslib
import rospy
from math import *
from geometry_msgs.msg import Twist
from std_msgs.msg import Int16
global x_speed
global z_speed
x_speed = 0
z_speed  = 0
def procpotx(data):
    global x_speed
    x_speed = data.data
def procpotz(data):
    global z_speed
    z_speed = data.data
if __name__=="__main__":
    rospy.init_node('move')
    p = rospy.Publisher('/turtle1/cmd_vel', Twist)
    rospy.Subscriber("potx", Int16, procpotx)
    rospy.Subscriber("potz", Int16, procpotz)
    twist = Twist()
    rospy.loginfo("About to be moving forward!")
    #
    while not rospy.is_shutdown():
        twist.linear.x = x_speed; 
        twist.angular.z = z_speed;   
        p.publish(twist)
        rospy.sleep(0.1)
    twist = Twist()
    rospy.loginfo("Stopping!")
    p.publish(twist)