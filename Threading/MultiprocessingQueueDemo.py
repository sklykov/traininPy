# -*- coding: utf-8 -*-
"""
Queue implementation in multiprocessing module - again, demo for the synchronization of trainings.

@author: ssklykov
"""
# %% Imports
import time
from multiprocessing import Process, Queue
import os
# import queue


# %% Child function
class childProcess(Process):
    """Demo implementation of Process class."""

    state = 0

    def __init__(self, state, queue):
        self.state = state
        self.queue = queue
        Process.__init__(self)  # Standard constructor but it's not obvious how it works

    def run(self):  # Method that should be overriden in a subclass of Process
        """Simulate of some process by posting messages to the Queue."""
        for i in range(4):  # Simulation of multiple posting
            time.sleep(0.5)  # Equal sleeping time for ALL CHILD PROCESSES!
            self.state += 1  # Some work
            # print("The process with", self.pid, "and state", self.state, "worked")  # !!! print() asn't acces to the main stdout
            self.queue.put(str(f'The process with pid {self.pid} has state {self.state}'))  # Posting some info from this child into a Queue


# %% Main testing process
if __name__ == "__main__":
    # !!! As it turns out, to make this code to work, it's necessary to put the starting of 3 modules under the __name__ == "__main__"
    print("Main process starts with pid", os.getpid())
    numberOfOperations = 9
    seq = Queue(maxsize=numberOfOperations)  # Simple constructor
    process1 = childProcess(1, seq); process2 = childProcess(10, seq); process3 = childProcess(100, seq)
    process1.start(); process2.start(); process3.start()  # Run all 3 processes

    while numberOfOperations > 0:
        time.sleep(0.6)  # Wait some action from a child process between iterations
        try:
            postedData = seq.get()
        except Queue.Empty:
            print("There is no data in the queue")
            numberOfOperations -= 1
        else:  # The code below is runned if there is NO EXCEPTION occured!
            numberOfOperations -= 1
            print("Posted data:", str(postedData))

    process1.join(); process2.join(); process3.join()
    print("Main thread finished")
