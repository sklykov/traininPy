# -*- coding: utf-8 -*-
"""
Test capabilities of running multiprocessing processes in the separate script by import the module.

@author: ssklykov
"""
# %% Imports
from simpleProcess import SimpleProcess
from multiprocessing import Queue

# %% Tests
if __name__ == "__main__":
    data_queue1 = Queue(); data_queue2 = Queue()
    process1 = SimpleProcess(1, data_queue1, n_steps=5); process2 = SimpleProcess(2, data_queue2, n_steps=6)
    process1.start(); process2.start(); process1.join(); process2.join()
    # !!! Returns empty arrays, as they initialized - below
    print("Attempt to directly acces to Process variables:", process1.processed_array, process2.processed_array)
    if not(data_queue1.empty()) and (data_queue1.qsize() > 0):
        print("Processed array from 1st process:", data_queue1.get_nowait())
    if not(data_queue2.empty()) and (data_queue2.qsize() > 0):
        print("Processed array from 1st process:", data_queue2.get_nowait())
