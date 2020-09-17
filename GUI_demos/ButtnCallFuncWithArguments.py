#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo of making GUI program with button calling some function with arguments through lambda call

@author: ssklykov
"""
from tkinter import Tk, Button, RIGHT, LEFT


# %% Some action
def actionArgs(calling: str):
    print("I print for " + calling)


# % Main demo code
topLevelWidget = Tk()
topLevelWidget.geometry("280x200")
topLevelWidget.title("Main window")
buttnExit = Button(topLevelWidget, text='Exit', command=topLevelWidget.destroy)
buttnExit.pack(side=RIGHT)
# Lambda wrapper to call action with arguments - below
buttnDo = Button(topLevelWidget, text='Do something', command=(lambda: actionArgs("Do something button")))
buttnDo.pack(side=LEFT)
# Laborous way of assigning font size to the created buttons
font = ('Liberation Mono', 12)  # Not sure that really Liberation Mono used
buttnDo.config(font=font)
buttnExit.config(font=font)
topLevelWidget.mainloop()
