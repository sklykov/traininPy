# -*- coding: utf-8 -*-
"""
Test capabilities of running multiprocessing processes in the separate script by import the module.

@author: ssklykov
"""
# %% Imports
from simpleProcess import SimpleProcess
from multiprocessing import Queue


# %% Testing the call within the class to the process function
class CallTheProcessFromModule():
    """Invoke a few SimpleProcess classes for getting some data."""

    data_array = []

    def __init__(self, n_processes):
        self.n_processes = n_processes

    def invokeProcesses(self):
        """
        Invoke several processes for collection of their returned through queues data.

        Returns
        -------
        None.

        """
        data_queues = []; processes = []
        for i in range(self.n_processes):  # Invoke processes and collect them in arrays
            data_queue = Queue()
            process = SimpleProcess(i+1, data_queue, n_steps=(i+5))
            print(process)
            process.start()
            data_queues.append(data_queue); processes.append(process)
        for i in range(self.n_processes):  # Wait until all processes finished
            if processes[i].is_alive():
                processes[i].join(); print("Process joined:", processes[i])
        for i in range(self.n_processes):
            if not(data_queues[i].empty()) and (data_queues[i].qsize() > 0):
                data = data_queues[i].get_nowait(); self.data_array.append(data)
                print("Processed array from 1st process:", data)


# %% Tests
if __name__ == "__main__":
    data_queue1 = Queue(); data_queue2 = Queue()
    process1 = SimpleProcess(1, data_queue1, n_steps=5); process2 = SimpleProcess(2, data_queue2, n_steps=6)
    process1.start(); process2.start(); process1.join(); process2.join()
    # print("Attempt to directly acces to Process variables:", process1.processed_array, process2.processed_array)
    # if not(data_queue1.empty()) and (data_queue1.qsize() > 0):
    #     print("Processed array from 1st process:", data_queue1.get_nowait())
    # if not(data_queue2.empty()) and (data_queue2.qsize() > 0):
    #     print("Processed array from 1st process:", data_queue2.get_nowait())
    callClass = CallTheProcessFromModule(2); callClass.invokeProcesses()
    print("Received data: ", callClass.data_array)
