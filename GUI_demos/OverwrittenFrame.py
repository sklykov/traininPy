#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Subclassing of Frame class from tkinter for simple GUI counter.

@author: ssklykov
"""
from tkinter import Frame, Button, LEFT, RIGHT
# import sys


class SimpleGUI(Frame):
    """Overwrite a few features of the Frame class."""

    count = 0
    message = ""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.count = 0
        self.makeButtons()
        self.mainloop()

    def makeButtons(self):
        """Make buttons and pack them."""
        widget1 = Button(self, text="Counting clicks", command=self.printClicks)
        widget1.pack(side=LEFT)
        widget2 = Button(self, text="QUIT", command=self.quit)  # BUG: after clicking quit function doesn't close widget
        widget2.pack(side=RIGHT)

    def printClicks(self):
        """Count number of clicks on a button."""
        self.count += 1
        print("Clicked %s" % self.count)

    # def exitThis(self):
        # Doesn't fix the bug
    #     # self.quit()
    #     Frame.quit(self)


if __name__ == "__main__":
    SimpleGUI()
    # sys.exit()
