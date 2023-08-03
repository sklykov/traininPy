#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo of making GUI program with button calling some function without arguments.

@author: sklykov
@license: The Unlicense

"""
from tkinter import Tk, Button, RIGHT, LEFT


# %% Some action
def action():
    print("I made something")


# % Main demo code
topLevelWidget = Tk()
topLevelWidget.geometry("280x200")
topLevelWidget.title("Main window")
buttnExit = Button(topLevelWidget, text='Exit', command=topLevelWidget.destroy)
buttnExit.pack(side=RIGHT)
buttnDo = Button(topLevelWidget, text='Do something', command=action)  # If function just assigned without arguments, it works
buttnDo.pack(side=LEFT)
# Laborous way of assigning font size to the created buttons
font = ('Liberation Mono', 12)  # Not sure that really Liberation Mono used
buttnDo.config(font=font)
buttnExit.config(font=font)
topLevelWidget.mainloop()
