#!/usr/bin/env python

import sys
import rospy
from ros_apio.srv import *


def apio_request(command):
    rospy.wait_for_service('ros_apio_server')
    try:
        ros_apio = rospy.ServiceProxy('ros_apio_server', RosApio)
        resp1 = ros_apio(command)
        return resp1.response
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    rospy.init_node('ros_apio_client')
    if len(sys.argv) == 2:
        command_argument=sys.argv[1]
        rospy.loginfo("Requesting {}".format(command_argument))
        rospy.loginfo(apio_request(command_argument))
    else:
        rospy.logerr("No enough arguments")
        sys.exit(1)
