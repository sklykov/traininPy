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


# %% Definition of methods
def simpleMethod(label, lock):
    """For conveying with good style of Python code.

    Simple printing function - the competitor for stdout.
    Above also two strings as example of good Pydoc style.
    """
    with lock:
        time.sleep(0.4)  # A delay - resembling some work
        print("The process with data: ", label, os.getpid(), "running")


# %% Main process
lock = Lock()  # The lock for the processes
p = Process(target=simpleMethod, args=("spawned child", lock))
p.start()
p.join()  # Forces the main process to wait until spawned child finished

for i in range(5):
    Process(target=simpleMethod, args=(("process %s" % i), lock)).start()

with lock:
    print("Main thread finished")
