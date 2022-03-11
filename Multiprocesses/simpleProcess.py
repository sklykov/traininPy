# -*- coding: utf-8 -*-
"""
Simple multiprocessing Process implementation.

@author: ssklykov
"""
# %% Imports
from multiprocessing import Process, Queue
import time


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
            time.sleep(0.15)  # Simulation of some work
        self.data_queue.put_nowait(self.processed_array)


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
    # !!! So for returning processed values, use Queue or other communication tools!
