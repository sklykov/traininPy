# -*- coding: utf-8 -*-
"""
Another demo of using threading module.

@author: sklykov
@license: The Unlicense

"""
from threading import Thread
import time
import random


# %% Demo class
class DemoSubclass(Thread):
    """Implementation of demo class with  run method."""
    arr = []
    sleepTime = 0.1

    def __init__(self, size: int, sleepTimeSec: float):
        self.arr = [0]*size
        Thread.__init__(self)

    def run(self):
        print("Thread starts running: ", len(self.arr))
        time.sleep(0.5)
        for i in range(len(self.arr)):
            self.arr[i] = random.randint(0, 50)


# %% Testing - class above
listOfThreads = []
timeSleep = 0.5
nThreadsRunning = 5

for i in range(nThreadsRunning):
    new_thread = DemoSubclass(i+1, timeSleep)
    listOfThreads.append(new_thread)
# join() method assures that the main program waits till all threads stopped their work
start = time.time()
for thread in listOfThreads:
    thread.start()
for thread in listOfThreads:
    thread.join()
for thread in listOfThreads:
    print("Generated by the thread array:", thread.arr)
print("Script processing time:", round(time.time() - start, 2))
print("There were", nThreadsRunning, "threads runned with each sleeping time:", timeSleep, "s")
print("Main script finishes")
