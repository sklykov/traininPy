#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple demo of Exit button

@author: sklykov
@license: The Unlicense

"""
from tkinter import Tk, Button, RIGHT
topLevelWidget = Tk()
topLevelWidget.geometry("250x200")
topLevelWidget.title("Window with Exit")
buttn = Button(topLevelWidget, text='Exit', command=topLevelWidget.destroy)  # Actually, Tk().quit() doesn't work
# But the .destroy works - suprisingly. Proper indentation for this comment - ?
buttn.config(font=('Liberation Sans', 12))
buttn.pack(side=RIGHT)
topLevelWidget.mainloop()
