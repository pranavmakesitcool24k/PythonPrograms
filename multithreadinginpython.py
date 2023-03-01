# multithreading program in python @pranav

import threading
import time


class Thread1(threading.Thread):
    def run(self):
        for i in range(0, 10):
            time.sleep(2)
            print("Thread1: ", i)


class Thread2(threading.Thread):
    def run(self):
        for i in range(0, 10):
            time.sleep(4)
            print("Thread2: ", i)


t1 = Thread1()
t2 = Thread2()
t1.start()
t2.start()
