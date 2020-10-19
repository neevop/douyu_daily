#!/usr/bin/env python
import rospy
import sys
import json
from rosgraph_msgs.msg import Log

def callback(data):
    msg2dict = _callback(data)
    msg2json = json.dumps(msg2dict)
    print(msg2json)

def _callback(data):
    msg2dict = {}
    type_ = type(data)
    msg_types = type_._slot_types
    msg_keys = type_.__slots__
    for key in msg_keys:
        value = data.__getattribute__(key)
        if hasattr(value, "_slot_types"):
            value = _callback(value)
        msg2dict[key] = value
    return msg2dict

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('rosjson', anonymous=True)

    rospy.Subscriber("/rosout", Log, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()