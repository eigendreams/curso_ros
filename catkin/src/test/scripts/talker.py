#!/usr/bin/env python
import rospy
from std_msgs.msg import String
class Talker:
        def __init__(self, node_name = 'talker'):
                rospy.init_node(node_name)
                self.nodename = rospy.get_name()
                rospy.loginfo("%s", self.nodename)
                self.rate = 10
                self.pub = rospy.Publisher("talker", String)
        def update(self):
                self.pub.publish("Hello World!")
        def spin(self):
                r = rospy.Rate(self.rate)
                while not rospy.is_shutdown():
                        self.update()
                        r.sleep()
if __name__ == "__main__":
        talker = Talker()
        talker.spin()


