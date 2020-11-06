# -*- coding: utf-8 -*-
"""Simple demo of multiprocessing module using.
The main idea, seems, that all spawned childrens evoked in a order, but the main thread stops before
all spawned children stopped.
@author: ssklykov
"""
# %% Import section
import os
from multiprocessing import Process, Lock
import time

# TODO: again, examples above not working properly

# %% Definition of methods
def simpleMethod(label, lock):
    """For conveying with good style of Python code.

    Simple printing function - the competitor for stdout.
    Above also two strings as example of good Pydoc style.
    """
    with lock:
        time.sleep(0.5)  # A delay - resembling some work
        print("The process with data: ", label, os.getpid(), "running")


def anotherMethod(some_data: str):
    global value
    # lock.acquire()

    print("Spawned process get the data: ")
    value += 1
    time.sleep(0.6)  # simulation of a work

    # finally:
    #     lock.release()


# %% Main process
# lock = Lock()  # The lock for the processes

# p = Process(target=simpleMethod, args=("spawned child", lock))
# p.start()
# p.join()  # Forces the main process to wait until spawned child finished
value = 0
pr = Process(target=anotherMethod, args=("call from main thread"))
pr.start()
pr.join()

# for i in range(5):
#     Process(target=simpleMethod, args=(("process %s" % i), lock)).start()


print("Main thread finished")
