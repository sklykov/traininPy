# -*- coding: utf-8 -*-
"""
Demonstrate implementation of producer-consumer concept on GUI.

@author: sklykov
"""
# %% Global imports
import tkinter as tk
from tkinter.ttk import Frame, Button, Label
from tkinter import font  # Explicit import, prevent some bugs
import platform
import ctypes


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
        self.consumer_live = False; self.consumer = None
        self.idle_events_count = 1; self.idle_delay_ms = 5000

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
        if not self.consumer_live:
            self.text_report.config(text="Wait for the report from Consumer")
            if self.periodic_task is not None:
                self.after_cancel(self.periodic_task); self.periodic_task = None
            # TODO: Initialize consumer as a separate Thread
            self.consumer_live = True; self.start_consumer_btn.config(text="Stop Consumer")
        else:
            # TODO: Stop Consumer
            self.consumer = None; self.consumer_live = False
            self.idle_events_count = 0
            if self.periodic_task is None:
                self.periodic_task = self.after(self.idle_delay_ms, self.idle_event)
                self.text_report.config(text="Wait for the idle event handle")
            self.start_consumer_btn.config(text="Start Consumer")

    def generate_event(self):
        pass

    def close(self):
        """
        Handle close button event.

        Returns
        -------
        None.

        """
        if self.consumer_live and self.consumer is not None:
            pass
        else:
            if self.periodic_task is not None:
                self.after_cancel(self.periodic_task); self.periodic_task = None
        self.master.destroy()  # Default method to close and destroy the widget


# %% Testing
if __name__ == "__main__":
    ProdConsG()
