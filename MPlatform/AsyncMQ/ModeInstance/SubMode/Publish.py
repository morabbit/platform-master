#coding=utf8

#
# Pathological publisher
# Sends out 1,000 topics and then one random update per second
#

import sys
import time

from random import randint

import zmq

def run(threadid,url=None):
    ctx = zmq.Context.instance()
    global publisher
    publisher = ctx.socket(zmq.PUB)
    if url:
        publisher.bind(url)
    else:
        publisher.bind("tcp://*:5556")
    # Ensure subscriber connection has time to complete
    # time.sleep(1)
    # Send out all 1,000 topic messages
    # for topic_nbr in range(1000):
    #     print (topic_nbr)
    #     publisher.send_multipart([
    #         b"%03d" % topic_nbr,
    #         b"Save Roger",
    #     ])

    while True:
        # Send one random update per second
        try:
            time.sleep(0.5)
            print("[threadid:%d] publish add one time=%r" % (threadid, time.ctime()))
            # publisher.send_multipart([
            #     b"%03d" % randint(0,999),
            #     b"Off with his head!",
            # ])
            publisher.send(b"what is this")
            # publisher.send_multipart([
            #     b"66",
            #     b"Off with his head!",
            # ])
        except KeyboardInterrupt:
            print "interrupted"
            break
#
# if __name__ == '__main__':
#     main(sys.argv[1] if len(sys.argv) > 1 else None)