# -*- coding: utf-8 -*-
"""
Make experiment on overriding Process class from multiprocessing library.

@author: ssklykov
"""
# %% Imports
from multiprocessing import Process, Array
import time


# %% Override base class
class simpleProcess(Process):
    intArr = []
    sharedArr = []

    def __init__(self, arr, sharedArray):
        self.intArr = arr
        self.sharedArr = sharedArray
        Process.__init__(self)

    # Overriding run process
    def run(self):
        # Process.start()
        for i in range(len(self.intArr)):
            self.intArr[i] = 2*i
        for i in range(len(self.intArr)):
            self.sharedArr[i] = 2*i
        time.sleep(0.02)
        # return  # redundant?

    def getArr(self):
        return self.intArr

    def getSharedArr(self):
        return self.sharedArr


# %% Main running function
if __name__ == '__main__':
    arr = [1]*5
    sharedArray = Array('i', 5)
    pr = simpleProcess(arr, sharedArray)
    pr.start()
    print("id of a subprocess:", pr.pid)
    pr.join()
    result = pr.getArr()  # really, it doesn't return values here
    resultShared = pr.getSharedArr()[:]  # for returning list instead of shared array (from memory)
