# -*- coding: utf-8 -*-
"""
Synchronized call to the shared object - my own experiments inspired by examples from the book "Programming Python"
Up to the moment, it work with some assumptions or with cludges
@author: ssklykov
"""
import _thread, time
# import random, numpy

# %% Testing functions
globalList = []
semaphore = _thread.allocate_lock() # a lock for multiple threads accessing some shared object

def add_to_list(thisId):
    global globalList,semaphore
    print("The thread with following process evoked:",thisId)
    # print("Semaphore is red?",semaphore.locked())
    isNotTheWorkAccomplished = True
    while(isNotTheWorkAccomplished):
        # various_sleeping_time = numpy.arange(0,0.1,0.02)
        # while(semaphore.locked()):
        #         time.sleep(0.01 + random.choice(various_sleeping_time)) # possible dirty hack
        if (not semaphore.locked()):
            print("The thread",thisId,"acquired semaphore")
            semaphore.acquire()
            globalList.append(thisId);  isNotTheWorkAccomplished = False  # For stopping outer while loop
            print("The global list so far:",globalList)
            time.sleep(1)
            semaphore.release(); print("The thread",thisId,"releases the lock")
        else:
            time.sleep(0.01 + thisId*0.02)


def parentProcess():
    global globalList
    i = 0
    while i < 4:
        _thread.start_new_thread(add_to_list, (i,))
        time.sleep(0.5 + i*0.05)
        # print("The global list so far:",globalList)
        i += 1
    time.sleep(4) # Here also should be guaranteed that the main process, evoking the threads, finishes in the end
    print("Final list",globalList)


# %% Testing of the developed demo functios
parentProcess()