#!/usr/bin/env python
import rospy
import sys
import json
import time
import os
from rosgraph_msgs.msg import Log
# from geometry_msgs.msg import Twist

import socket

HOST = 'localhost'
PORT = 5959

def callback(data, upd_socket):
    msg2dict = _callback(data)
    msg2json = json.dumps(msg2dict)
    _m2udp(upd_socket, HOST, PORT, msg2json)

def _callback(data):
    msg2dict = {}
    type_ = type(data)
    # msg_types = type_._slot_types
    msg_keys = type_.__slots__
    for key in msg_keys:
        value = data.__getattribute__(key)
        if hasattr(value, "_slot_types"):
            value = _callback(value)
        msg2dict[key] = value
    return msg2dict

def _m2udp(sock, host, port, message):
    sock.sendto(message, (str(host), port))

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('rosjson', anonymous=True)

    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    rospy.Subscriber("/rosout", Log, callback, callback_args=s)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()