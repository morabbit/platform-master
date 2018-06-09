#coding=utf8


import threading
import Publish
import Subscribe


threads = []

def publishThdFunc(threadid):
    Publish.run(threadid)

if __name__ == "__main__":

    for i in xrange(3):
        thd = threading.Thread(target=publishThdFunc, args=(i,))
        threads.append(thd)

    for t in threads:
        t.start()



    # Publish.run()
    # Subscribe.run()

