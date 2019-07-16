#!/usr/bin/env python

# ROS packages
import rospy
from ros_apio.srv import *

# Python libraries
import subprocess

def handle_apio_request(req):
    print ("Service finished")
    return True

def apio_server():
    rospy.init_node('apio_server')
    s = rospy.Service('apio_server', RosApio, handle_apio_request)
    print "Apio ROS service ready."
    rospy.spin()

if __name__ == "__main__":
    apio_server()
