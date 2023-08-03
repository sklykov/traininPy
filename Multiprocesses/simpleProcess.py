# -*- coding: utf-8 -*-
"""
Simple multiprocessing Process implementation.

@author: sklykov
@license: The Unlicense

"""
# %% Imports
from multiprocessing import Process, Queue
import time
import sys


# %% Class implementation
class SimpleProcess(Process):
    """Simple simulation of Process."""

    def __init__(self, some_id, data_queue: Queue, n_steps: int = 5):
        self.some_id = some_id; self.n_steps = n_steps; self.processed_array = []
        self.data_queue = data_queue
        Process.__init__(self)

    def run(self):
        """
        Simulate some busy process.

        Parameters
        ----------
        n_steps : int, optional
            N of steps for simulation of work. The default is 10.

        Returns
        -------
        None.

        """
        for i in range(self.n_steps):
            self.processed_array.append(i + self.some_id)
            # sys.stdout.write(("appended value:" + str(i + self.some_id)))
            print(str(i + self.some_id), file=sys.stdout, flush=True)
            # sys.stdout.write(str(i + self.some_id) + "\n")
            # self.data_queue.put_nowait(sys.stdout.write(str(i + self.some_id) + "\n"))
            # sys.stdout.flush()
            time.sleep(0.15)  # Simulation of some work
        self.data_queue.put_nowait(self.processed_array)


# %% Tests
if __name__ == "__main__":
    data_queue1 = Queue(); data_queue2 = Queue()
    process1 = SimpleProcess(1, data_queue1, n_steps=2); process2 = SimpleProcess(2, data_queue2, n_steps=3)
    process1.start(); process2.start(); process1.join(); process2.join()
    # For getting back the job results, use Queue
    print("Attempt to directly acces to Process variables:", process1.processed_array, process2.processed_array)
    if not (data_queue1.empty()) and (data_queue1.qsize() > 0):
        print("Processed array from 1st process:", data_queue1.get_nowait())
    if not (data_queue2.empty()) and (data_queue2.qsize() > 0):
        print("Processed array from 1st process:", data_queue2.get_nowait())

    # Tests concerning access to the standard output reimplmented by the Spyder IDE !!!
    b = sys.stdout.__dict__
    # for i in b.keys():
    #     print(i, ":", b[i])
    buffer = sys.stdout._buffer
    print("**************Buffer methods**************")
    print(dir(buffer))
    print(buffer.readlines())
    print("**************Buffer content**************")
    print(buffer.getvalue())

    # ??? The code above will work if ONLY it's run by the Spyder IDE, which substitutes the sys.stdout module
    # with some functionality of _io module instead of io. The buffer NOT retains its content by the end of the call,
    # so the result of calling buffer.getvalue() is different between calls.
    # The aim of tests here was to write to sys.stdout and print it to the console evoked by the Spyder IDE, but
    # it isn't feasible, seems.
    # If this code is run in the dediated independent console, then the stdout works as expected, reporting all the messages
    # called by print statement in the child processes (see print statement above)
