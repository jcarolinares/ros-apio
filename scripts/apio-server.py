#!/usr/bin/env python

# ROS packages
import rospy
import rospkg
from ros_apio.srv import *

import subprocess

def handle_ros_apio(req):

    # Get the path of the ROS package using RosPack
    rospack = rospkg.RosPack()
    route = rospack.get_path('ros_apio')
    rospy.loginfo()

    print ("Returning: {}".format(req.command))
    if (req.command=="init"):
        subprocess.call("apio init -y -p {}/circuits/ -b icezum".format(route), shell=True)
    elif (req.command == "verify"):
        subprocess.call("apio verify -p {}/circuits/".format(route), shell=True)
    elif (req.command == "build"):
        subprocess.call("apio build -p {}/circuits/".format(route), shell=True)
    elif (req.command == "upload"):
        subprocess.call("apio upload -p {}/circuits/".format(route), shell=True)
    else:
        rospy.logerr("Apio command not valid")
    return RosApioResponse(req.command)

def ros_apio():
    rospy.init_node('ros_apio_server')
    s = rospy.Service('ros_apio_server', RosApio, handle_ros_apio)
    rospy.loginfo("Ros Apio Server Ready")
    rospy.spin()

if __name__ == "__main__":
    ros_apio()
