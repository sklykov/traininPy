# -*- coding: utf-8 -*-
"""
Training create / read txt files.

@author: sklykov
@license: The Unlicense

"""
import os

lines = ['raz', 'dva', 'tri', 'this is the end']
endline = '\n'
# %% Demo writing
with open("demo.txt", 'w') as wfile:
    for line in lines:
        wfile.write(line + endline)
# %% Demo reading - in old manner
with open("demo.txt", 'r') as rfile:
    lines = rfile.readlines()
    for line in lines:
        print(line, end='')

# %% Demo appending
with open("demo.txt", 'a') as afile:
    afile.write('Now this is the end')

# %% Demo reading - less memory consuming
with open("demo.txt", 'r') as rfile:
    readed_lines = []
    for line in rfile:
        readed_lines.append(line)

# %% Cleaning up
os.remove("demo.txt")
