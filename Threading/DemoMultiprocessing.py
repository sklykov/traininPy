# -*- coding: utf-8 -*-
"""Simple demo of multiprocessing module using.
The main idea, seems, that all spawned childrens evoked in a order, but the main thread stops before
all spawned children stopped.
@author: ssklykov
"""
# %% Import section
import os
# import multiprocessing as mp
from multiprocessing import Process, Value, Array
#  from multiprocessing import set_start_method  # Raise RuntimeError
import ctypes  # for assigning directly 'string' type for multiprocessing.Value
import time
import sys

# TODO: now, some calls, especially print() methods in child processes, are not platform or OS agnostic
# BE CAREFUL for using this demo on different platforms


# %% Synchronized method
def simpleMethod(label, lock):
    """For conveying with good style of Python code.

    Simple printing function - the competitor for stdout.
    Above also two strings as example of good Pydoc style.
    """
    with lock:
        time.sleep(0.5)  # A delay - resembling some work
        print("The process with data: ", label, os.getpid(), "running")


# %% For observing result - use 'Execute in an external system terminal'
def anotherMethod(someData):
    # global value
    # lock.acquire()
    print("Spawned process get the data: ", someData)
    # value += 1
    time.sleep(0.1)  # simulation of a work

    # finally:
    #     lock.release()


# !: Most IMPORTANTLY, simple print() method doesn't work in child process in current console and Windows
def simplestMethod():
    time.sleep(0.1)
    print("The simplest method id: ", os.getpid())  # Works for Win only if Run in dedicated console
    print("hi from the simplest method")
    sys.stdout.flush()  # Helps to print on dedicated console


# %% Specification of method that return some value indirectly (using shared variable using class Value)
# For these demo, the example from Python documentation is used
def returnMethod(sharedVar, sharedArr):
    # Drawback - no performing checking of a type that passed in this method
    sharedVar.value = 1.5
    for i in range(len(sharedArr)):
        sharedArr[i] = i*2


# %% Testing of typing into 'string' primitive type
def writeString(sharedStr):
    targetStr = "This value is written by " + str(os.getpid())
    print(targetStr)
    sys.stdout.flush()  # for observing result on Windows and debug this independent process
    sharedStr.value = targetStr.encode()


# %% Main process
# lock = Lock()  # The lock for the processes
# p = Process(target=simpleMethod, args=("spawned child", lock))
# p.start()
# p.join()  # Forces the main process to wait until spawned child finished
if __name__ == '__main__':
    print("******START TESTING******")
    # value = 0
    # pr = Process(target=anotherMethod, args=('call from main thread'))
    pr2 = Process(target=simplestMethod)
    # pr.start()
    # pr.join()
    pr2.start()
    print("Proof that the suprocess launched: ")
    print("pid of a subprocess:", pr2.pid)
    pr2.join()
    print("exit code:", pr2.exitcode)
    print("******NEXT TEST******")
    # sys.stdout.flush()  # doesn't help
    sharedVar = Value('d', 0.0)  # initialization of some value for shared variable
    # !: seems that shared array doesn't support append operation ! So, the array should be initialized with
    # some predifined size!
    sharedArr = Array('i', range(5))  # initialization of an array with integer values - also shared
    print("Before entering to a subprocess, the shared variable is:", sharedVar.value)
    pr3 = Process(target=returnMethod, args=(sharedVar, sharedArr))
    pr3.start()
    pr3.join()
    print("After performing a subprocess, the shared variable is:", sharedVar.value)
    print("After performing a subprocess, the empty array filled with doubled indecies:", sharedArr[:])
    print("******NEXT TEST******")
    # sharedStr = Value(ctypes.c_char_p, b'empty') CREATES CONSTANT CRUSHES!!!
    sharedStr = Array('c', range(40))  # Using bytearray instead of string - thanks Stackoverflow
    pr4 = Process(target=writeString, args=(sharedStr,))
    pr4.start()
    pr4.join()
    print(sharedStr.value.decode())  # decode the bytearray string
    print("******END TESTING******")
    time.sleep(0.1)
    print("Main thread finished")
    # input()  # For preventing closing external terminal


# for i in range(5):
#     Process(target=simpleMethod, args=(("process %s" % i), lock)).start()

# anotherMethod("direct call")
