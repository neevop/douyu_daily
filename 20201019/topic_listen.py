#!/usr/bin/env python
import rospy
import rostopic
import json

import socket

HOST = 'localhost'
PORT = 5960
NAME = 'rosjson'
TOPICS = ['/rosout', '/turtle1/pose']  # less than 5 topics

class Msg2Udp(object):
    def __init__(self, topics):
        self.udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.topics = topics

        rospy.init_node(NAME, anonymous=True)
        self.rate = rospy.Rate(10)  # why send udp as 3*10Hz?

    def sub_topics(self):
        for topic in self.topics:
            msg_class, real_topic, _ = rostopic.get_topic_class(topic, blocking=True)
            rospy.Subscriber(real_topic, msg_class, self.callback, callback_args=topic)
        rospy.spin()

    def callback(self, data, topic):
        msg2dict = _callback(data)
        uport = PORT + self.topics.index(topic) # any other way to diff topics ?
        try:
            msg2json = json.dumps(msg2dict)
            # print(msg2json)
            self._m2udp(HOST, uport, msg2json)
        except:
            print("dict invaild: %s"%(msg2dict))

    def _m2udp(self, host, port, message):
        # send data to udp port
        self.udpSocket.sendto(message, (str(host), port))

        # limit the sending rate to ros.rate
        self.rate.sleep()

def _callback(data):
    #transform rosmsgs to json

    msg2dict = {}
    type_ = type(data)

    if hasattr(data, "_slot_types"):
        msg_keys = type_.__slots__
        for key in msg_keys:
            value = data.__getattribute__(key)
            value = _callback(value)
            msg2dict[key] = value
        return msg2dict

    elif type_ == bool:
        return 1 if data else 0
    elif type_ in (int, long, float, str):
        return data
    elif type_ in (list, tuple):
        lval = []
        if len(data) == 0:
            return lval
        for val in data:
            lval.append(_callback(val))
        return lval
    else:
        print("data invaild: %s"%(data))
        return ("data invaild: " + str(data))

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    transformer = Msg2Udp(TOPICS)
    transformer.sub_topics()

if __name__ == '__main__':
    listener()