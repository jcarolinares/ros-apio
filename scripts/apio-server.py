#!/usr/bin/env python

# ROS packages
import rospy
import rospkg
from ros_apio.srv import *

import subprocess

route = ""
circuits_folders = ""
board=""

def handle_ros_apio(req):

    global circuits_folders
    global route
    global board

    rospy.loginfo("Requested command: {}".format(req.command))
    if (req.command=="init"):
        subprocess.call("apio init -y -p {}/{}/ -b {}".format(route,circuits_folders,board), shell=True)
    elif (req.command == "verify"):
        rospy.loginfo("apio verify -p {}/{}/".format(route,circuits_folders))
        subprocess.call("apio verify -p {}/{}/".format(route,circuits_folders), shell=True)
    elif (req.command == "build"):
        subprocess.call("apio build -p {}/{}/".format(route,circuits_folders), shell=True)
    elif (req.command == "upload"):
        subprocess.call("apio upload -p {}/{}/".format(route,circuits_folders), shell=True)
    else:
        rospy.logerr("Apio command not valid")
    return RosApioResponse(req.command)


def ros_apio():

    global circuits_folders
    global route
    global board

    rospy.init_node('ros_apio_server')

    # Get the path of the ROS package using RosPack
    rospack = rospkg.RosPack()
    route = rospack.get_path('ros_apio')
    circuits_folders = rospy.get_param('~circuits-folder', 'circuits')
    board = rospy.get_param('~board', 'icezum')
    rospy.loginfo("Board: {}".format(board))
    rospy.loginfo("Circuits folder: {}".format(circuits_folders))

    subprocess.call("apio init -y -p {}/{}/ -b {}".format(route,circuits_folders,board), shell=True)
    rospy.loginfo("Apio init with board: {}".format(board))

    s = rospy.Service('ros_apio_server', RosApio, handle_ros_apio)
    rospy.loginfo("Ros Apio Server Ready")
    rospy.spin()


if __name__ == "__main__":
    ros_apio()
