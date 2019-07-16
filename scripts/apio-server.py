#!/usr/bin/env python

# ROS packages
import rospy
from ros_apio.srv import *

def handle_ros_apio(req):
    print ("Returning: {}".format(req.command))
    return RosApioResponse(req.command)

def ros_apio():
    rospy.init_node('ros_apio_server')
    s = rospy.Service('ros_apio_server', RosApio, handle_ros_apio)
    print "Ros Apio Server Ready"
    rospy.spin()

if __name__ == "__main__":
    ros_apio()
