# -*- coding: utf-8 -*-
"""
Sys and os path manipulations - refactored.

@author: sklykov
@license: The Unlicense

"""
import os
import sys
from SimpleDatabase_Class import Quad2DImage

# %% Classical way of getting current working directory
# print(sys.path) # Printing all evolved in searching modules paths
# print(os.getcwd()); init_path = str(os.getcwd()) # Classical way for getting


# %% The method returning list of folders in the repository
def projectImportTree() -> list:
    """ Get a list with all folders in the repository (.git folder as an anchor)"""
    anchorFolder = ".git"  # Assuming that this folder always in the holding Git repository
    listOfDirs = os.listdir(os.getcwd())
    print(listOfDirs)
    i = 10  # Maximum number of iterations (in a folder tree)
    while anchorFolder not in listOfDirs:
        os.chdir("..")
        listOfDirs = os.listdir(os.getcwd())
        # print(listOfDirs)  # Debugging
        i += 1
    return os.listdir(os.getcwd())


# %% Simple demo
allDirs = projectImportTree()
# %% The problem - including other folder to the sys.path. Solution inspired by professionals from the StackOverflow
# Getting absolute path to the other folder
print(os.path.abspath(os.curdir))  # Printing path to a current dir
os.chdir("..")  # Unix-like command to go in a directory tree up
head_tree = os.path.abspath(os.curdir)  # get up on one level in a directory tree
listOfDirs = os.listdir(head_tree)  # To avoid many printing statements - refer to the inspection of variables window
go_to_folder = os.listdir(head_tree)[2]
os.chdir(go_to_folder)
other_dir = os.path.abspath(os.curdir)

# Adding this directory in the search path
sysPath = sys.path  # Refer to the inspection window for details

# Checking the added folder and deleting extra ones
if (sys.path.count(other_dir) == 0):
    sys.path.append(other_dir)
elif (sys.path.count(other_dir) > 1):
    for i in (2, sys.path.count(other_dir)):
        sys.path.remove(other_dir)

sysPath = sys.path  # Refer to the inspection window for details

# %% Cause additional folder from the entire repository has been added, below is importing some module from it
qi = Quad2DImage(2)
intensities = qi.I
