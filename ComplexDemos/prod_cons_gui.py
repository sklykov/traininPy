# -*- coding: utf-8 -*-
"""
Demonstrate implementation of producer-consumer concept on GUI.

@author: sklykov
@license: The Unlicensed

"""
# %% Global imports
import tkinter as tk
from tkinter.ttk import Frame, Button, Label
from tkinter import font  # Explicit import, prevent some bugs
import platform
import ctypes
from threading import Thread, Event
from queue import Queue, Empty
import warnings


# %% GUI class
class ProdConsG(Frame):
    """GUI with buttons and text area for demonstration of communication between threads."""

    def __init__(self):
        # Correct blur of opened GUI on Windows OS
        if platform.system() == "Windows":
            try:
                ctypes.windll.shcore.SetProcessDpiAwareness(2)
            # exceptions below can be encountered in Python and tkinter versions for Windows 7 (and older)
            except FileNotFoundError:
                pass
            except ModuleNotFoundError:
                pass

        # Initialize main widgets
        root_widget = tk.Tk()  # initialize the main widget - container for Frame widget (this class)
        super().__init__(master=root_widget)  # initialize the Frame widget - container for this class (ProdConsG)
        self.master.title("Producer-Consumer"); self.master.geometry("248x110+100+120")
        self.master.protocol("WM_DELETE_WINDOW", self.close)

        # Increase default font size
        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.config(size=self.default_font.cget("size") + 1)

        # Initialize parameters / holders
        self.consumer_live = False; self.consumer = None; self.notifier = None; self.commands_queue = None
        self.idle_events_count = 1; self.idle_delay_ms = 2000; self.event_count = 0

        # Make GUI elements
        self.produce_event_btn = Button(master=self, text="Generate Event", command=self.generate_event)
        self.start_consumer_btn = Button(master=self, text="Start Consumer", command=self.start_consumer)
        self.text_report = Label(master=self, text="Program launched, waiting for events")

        # Put the GUI elements on the Frame
        pad = 10  # in pixels, padding between elements on the Frame
        self.produce_event_btn.grid(row=0, rowspan=1, column=0, columnspan=1, padx=pad, pady=pad)
        self.start_consumer_btn.grid(row=0, rowspan=1, column=1, columnspan=1, padx=pad, pady=pad)
        self.text_report.grid(row=1, rowspan=1, column=0, columnspan=4, padx=pad, pady=pad)
        self.grid(); self.master.update()  # for updating associate with master properties (geometry)

        # Simulate some periodic event within the main (event) loop of the GUI (Frame)
        self.periodic_task = self.after(self.idle_delay_ms, self.idle_event)

        self.mainloop()  # launches the main event loop of the widget (Frame)

    def idle_event(self):
        """
        Make a loop for periodically evoking some idle event.

        Returns
        -------
        None.

        """
        if not self.consumer_live:
            self.text_report.config(text=f"Occured each {round(self.idle_delay_ms/1000, 1)} sec idle event #: {self.idle_events_count}")
            self.idle_events_count += 1
        else:
            self.text_report.config(text=""); self.idle_events_count = 0
        # Below - make a delayed call of this method
        self.periodic_task = self.after(self.idle_delay_ms, self.idle_event)

    def start_consumer(self):
        """
        Start Consumer as the separate Thread, waiting for commands, after clicking on the button.

        Returns
        -------
        None.

        """
        if not self.consumer_live:
            self.text_report.config(text="Wait for the report from Consumer")
            if self.periodic_task is not None:
                self.after_cancel(self.periodic_task); self.periodic_task = None
            # Initialize consumer as a separate Thread and Event for notifying that some data available
            self.notifier = Event()  # simple notifier about an action (some command will be put in the Queue)
            self.commands_queue = Queue(maxsize=1)  # to check that values put / get precisely with single quantity
            self.consumer = Thread(name="Computation Thread", target=self.thread_work)
            self.consumer_live = True; self.start_consumer_btn.config(text="Stop Consumer")
            self.event_count = 0; self.consumer.start()  # start initialized Thread
        else:
            self.clear_queue()  # clear the commands from queue
            self.commands_queue.put_nowait("Stop"); self.notifier.set()
            if self.consumer.is_alive():
                self.consumer.join(timeout=0.01)  # wait 10 ms if the thread still alive and thread_work function doesn't quit
            if not self.consumer.is_alive():
                print("Thread stopped")
            else:
                warnings.warn("Thread is still alive and not properly stopped")
            del self.consumer, self.notifier, self.commands_queue
            self.consumer = None; self.consumer_live = False; self.notifier = None; self.commands_queue = None
            self.idle_events_count = 0
            if self.periodic_task is None:
                self.periodic_task = self.after(self.idle_delay_ms, self.idle_event)
                self.text_report.config(text="Wait for the idle event handle")
            self.start_consumer_btn.config(text="Start Consumer")

    def thread_work(self):
        """
        Associate function to the thread.

        It receives the commands (generated by the button) and handles it. Also, it waits for "Stop" command, evoked on quit or button.

        Returns
        -------
        None.

        """
        if self.consumer_live:
            print("Thread started")
            # Infinite loop for waiting notifier and processing the commands
            while self.consumer_live:
                self.notifier.wait()  # wait that the notifier is set externally
                if self.notifier.is_set():
                    self.notifier.clear()  # set notifier to False
                    command = self.commands_queue.get_nowait()
                    if isinstance(command, str):
                        if command == "Stop":
                            # print("Thread received 'Stop' command")  # debugging
                            break  # break the while loop, because "Stop" command received
                        else:
                            self.text_report.config(text=command)  # represent on GUI the command received from the Queue

    def generate_event(self):
        """
        Generate an event after clicking on the button.

        Returns
        -------
        None.

        """
        if self.consumer_live and self.notifier is not None and self.commands_queue is not None:
            self.event_count += 1
            self.commands_queue.put_nowait(f"Evoked event #: {self.event_count}")  # put the command before the notifier is set
            self.notifier.set()  # makes notifier True, should make the waiting Thread to query the Queue

    def clear_queue(self):
        """
        Clear commands queue on the call.

        Returns
        -------
        None.

        """
        if self.commands_queue is not None and self.consumer_live:
            if self.commands_queue.full():
                while not self.commands_queue.empty():
                    try:
                        self.commands_queue.get_nowait()
                    except Empty:
                        break

    def close(self):
        """
        Handle close button event.

        Returns
        -------
        None.

        """
        if self.consumer_live and self.consumer is not None:
            self.clear_queue()  # clear the commands from queue
            self.commands_queue.put_nowait("Stop"); self.notifier.set()
            self.consumer.join(timeout=0.02)  # wait 20 ms for Thread stopped
            if not self.consumer.is_alive():
                print("Thread stopped")
        else:
            if self.periodic_task is not None:
                self.after_cancel(self.periodic_task); self.periodic_task = None
        self.master.destroy()  # Default method to close and destroy the widget


# %% Testing
if __name__ == "__main__":
    ProdConsG()
