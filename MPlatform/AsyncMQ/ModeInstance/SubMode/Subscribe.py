#coding=utf8

import sys
from random import randint
import zmq
import time
#
# class SubMode(object):
#     def __init__(self):
#         pass
#
#     def run(self, url=None):
#         ctx = zmq.Context.instance()
#         subscriber = ctx.socket(zmq.SUB)
#         if url is None:
#             url = "tcp://localhost:5556"
#         subscriber.connect(url)
#
#         subscription = b"%03d" % randint(0, 999)
#         subscriber.setsockopt(zmq.SUBSCRIBE, subscription)
#
#         while True:
#             topic, data = subscriber.recv_multipart()
#             assert topic == subscription
#             print data



def run(url=None):
    ctx = zmq.Context.instance()
    subscriber = ctx.socket(zmq.SUB)
    if url is None:
        url = "tcp://192.168.2.107:5556"
    subscriber.connect(url)

    subscription = b"%03d" % randint(0,999)
    subscriber.setsockopt(zmq.SUBSCRIBE, b'')

    while True:
        # topic, data = subscriber.recv_multipart()
        # assert isinstance(subscriber.recv, object)
        data = subscriber.recv()
        # assert topic == subscription
        print data, time.ctime()

# if __name__ == '__main__':
#     main(sys.argv[1] if len(sys.argv) > 1 else None)





