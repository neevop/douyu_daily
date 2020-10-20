# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import multiprocessing
import socket
import time
import re
import requests
from bs4 import BeautifulSoup
import json

# config socket ip and port
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname("danmuproxy.douyu.com")
port = 8506
client.connect((host, port))

# 获取用户昵称及弹幕信息的正则表达式
danmu = re.compile(b'type@=chatmsg.*?/nn@=(.*?)/txt@=(.*?)/')


def sendmsg(msgstr):
    '''
    msgHead: head of protol
    '''
    msg = msgstr.encode('utf-8')
    data_length = len(msg) + 8
    code = 689
    msgHead = int.to_bytes(data_length, 4, 'little') \
              + int.to_bytes(data_length, 4, 'little') + int.to_bytes(code, 4, 'little')
    client.send(msgHead)
    sent = 0
    while sent < len(msg):
        tn = client.send(msg[sent:])
        sent = sent + tn


def start(roomid):
    '''
    send login request
    '''
    msg = 'type@=loginreq/roomid@={}/\0'.format(roomid)
    sendmsg(msg)
    msg_more = 'type@=joingroup/rid@={}/gid@=-9999/\0'.format(roomid)
    sendmsg(msg_more)

    print('---------------get-danmu-messages--------------'.format(get_name(roomid)))
    while True:
        data = client.recv(1024)
        danmu_more = danmu.findall(data)
        if not data:
            break
        else:
            with open('bullet_curtain.jl', 'a') as f:
                try:
                    for i in danmu_more:
                        dmDict={}
                        dmDict['昵称'] = i[0].decode(encoding='utf-8', errors='ignore')
                        dmDict['弹幕内容'] = i[1].decode(encoding='utf-8', errors='ignore')
                        dmJsonStr = json.dumps(dmDict, ensure_ascii=False)+'\n'
                        print(dmDict['昵称'])
                        f.write(dmJsonStr)
                        danmuNum = danmuNum + 1
                except:
                    continue

def keeplive():
    '''
    发送心跳信息，维持TCP长连接
    心跳消息末尾加入\0
    '''
    while True:
        msg = 'type@=keeplive/tick@=' + str(int(time.time())) + '/\0'
        sendmsg(msg)
        time.sleep(10)


def get_name(roomid):
    '''
    利用BeautifulSoup获取直播间标题
    '''
    r = requests.get("http://www.douyu.com/" + roomid)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup.find('a', {'class', 'zb-name'}).string

# 启动程序
if __name__ == '__main__':
    room_id = 252140
    p1 = multiprocessing.Process(target=start, args=(room_id,))
    p2 = multiprocessing.Process(target=keeplive)
    p1.start()
    p2.start()
