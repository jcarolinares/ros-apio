#!/usr/bin/env python

import sys
import rospy
from ros_apio.srv import *


def add_two_ints_client(command):
    rospy.wait_for_service('ros_apio_server')
    try:
        ros_apio = rospy.ServiceProxy('ros_apio_server', RosApio)
        resp1 = ros_apio(command)
        return resp1.response
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    if len(sys.argv) == 2:
        command_argument=sys.argv[1]
    else:
        sys.exit(1)
    print "Requesting {}".format(command_argument)
    print (add_two_ints_client(command_argument))
