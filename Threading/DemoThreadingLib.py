# -*- coding: utf-8 -*-
"""
Demo of using threading module.

@author: ssklykov
"""
import threading
import time


# %% Demo class
class DemoThreadedProcess(threading.Thread):
    """Implementation of demo class with  run method."""

    def __init__(self, count, mutex):
        self.mutex = mutex
        self.count = count
        threading.Thread.__init__(self)

    def run(self):
        """
        Simulate multithread work.

        If the mutex is not acquired by other threaded class instance, enters and sleep.

        Returns
        -------
        None.

        """
        with self.mutex:
            print("assigned count is ", self.count)
            time.sleep((1+abs(self.count))/2)  # Some work emulation


# %% Testing
mutexForAll = threading.Lock()  # lock or semaphore for all threads
listOfThreads = []
for i in range(5):
    new_thread = DemoThreadedProcess(i, mutexForAll)
    new_thread.start()
    listOfThreads.append(new_thread)
# join() method assures that the main program waits till all threads stopped their work
for process in listOfThreads:
    process.join()

print("Main script finishes")
