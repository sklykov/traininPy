# -*- coding: utf-8 -*-
"""
Experiments with threading in Python. _thread - is low-level library for multithreading programs!
@author: ssklykov
"""
# %% Experiments with the simple '_thread module'
import _thread
import time


def child(this_id):
    print('Hello from a thread', this_id)


def parent():
    i = 0
    while i < 5:
        _thread.start_new_thread(child, (i,))  # Take a look to the function arguments
        i += 1
        time.sleep(1)  # making an artificial delay


# %% Testing section
parent()
