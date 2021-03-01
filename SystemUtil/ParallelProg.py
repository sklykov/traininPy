# -*- coding: utf-8 -*-
"""
Testing forking / parallel programming
@author: ssklykov
"""
import os


# %% Forking
def child():
    print('Hi from me, the child', os.getpid())
    os._exit(0)


i = 0
# %% os.fork() will work only for Unix based systems
try:
    while i < 3:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('Hi from me, the parent', os.getpid(), newpid)
        i += 1
except AttributeError:
    print("Most probably runned on Windows system")
