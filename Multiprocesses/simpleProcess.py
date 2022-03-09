# -*- coding: utf-8 -*-
"""
Simple multiprocessing Process implementation.

@author: ssklykov
"""
# %% Imports
from multiprocessing import Process
import time
import sys


# %% Class implementation
class SimpleProcess(Process):
    """Simple simulation of Process."""

    def __init__(self, some_id, n_steps: int = 5):
        self.some_id = some_id; self.n_steps = n_steps; self.processed_array = []
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
            time.sleep(0.1)


# %% Tests
if __name__ == "__main__":
    process1 = SimpleProcess(some_id=1, n_steps=5); process2 = SimpleProcess(some_id=2, n_steps=6)
    process1.start(); process2.start(); process1.join(); process2.join()
    print(process1.processed_array); print(process2.processed_array)
