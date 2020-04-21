# -*- coding: utf-8 -*-
"""
Queue implementation in multiprocessing module - again, demo for the synchronization of trainings
@author: ssklykov
"""
# %% Imports
import time
from multiprocessing import Process, Queue
import os
import queue


# %% Child function
class childProcess(Process):
    state = 0

    def __init__(self, state, queue):
        self.state = state
        self.queue = queue
        Process.__init__(self)  # Standard constructor but it's not obvious how it works

    def run(self):  # Method that should be overriden in a subclass of Process
        for i in range(4):  # Simulation of multiple posting
            time.sleep(0.5)  # Equal sleeping time for ALL CHILD PROCESSES!
            self.state += 1  # Some work
            print("The process with", self.pid, "and state", self.state, "worked")
            self.queue.put([self.pid, self.state])  # Posting some info from this child into a Queue


# %% Main testing process
print("Main process starts with pid", os.getpid())

seq = Queue()  # Simple constructor
process1 = childProcess(1, seq)
process2 = childProcess(10, seq)
process3 = childProcess(100, seq)
numberOfOperations = 9
process1.start(); process2.start(); process3.start()

while numberOfOperations > 0:
    time.sleep(0.4)  # Wait some action from a child process between iterations
    try:
        postedData = seq.get()
    except queue.Empty:  # Dirty hack in the book, I think
        print("There is no data in the queue")
        numberOfOperations -= 1
    else:  # The code below is runned if there is NO EXCEPTION occured!
        numberOfOperations -= 1
        print("Posted data:", str(postedData))

process1.join(); process2.join(); process3.join()
finalPosted = seq.get()
print("Finally posted to the queue", finalPosted)
print("Main thread finished")
