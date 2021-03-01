# -*- coding: utf-8 -*-
"""
As a small example for possible future reusing or referring to. Only for training purposes.
@author: ssklykov
"""
# %% Imports
import os

# %% Searching and ordering the files in order of their size
os.chdir("..")  # Going on top of directory structure - project structure
projectDir = os.getcwd()
visited_folders = {}  # Visited folders (containing *py files)
sizes_of_files = {}
# currentDir = os.getcwd()
print("The path to the entire project:", projectDir)

# Making a walr around the project folder
# foldersInProject - the for loop below going iteratively through all directories inside the project
for (foldersInProject, subfoldersInTree, filesInTree) in os.walk(projectDir):
    # print(foldersInProject, " - folder in trees")
    # print(smthInTree)
    for file in filesInTree:
        if file.endswith('.py'):
            # Adding the folder containing some python code to the dictionary
            if not (foldersInProject in visited_folders.keys()):
                visited_folders[foldersInProject] = True
            absolutePathToFile = os.path.join(foldersInProject, file)
            sizeOfFile = os.path.getsize(absolutePathToFile)
            # print("file", file, "has the size:", sizeOfFile)
            # The code below will work in assumption of unique file names in each visited folder
            if not(file in sizes_of_files.keys()):
                sizes_of_files[file] = sizeOfFile

# Finding the file with a maximum size. Should exist more elegant and concise way!
sizeMax = 0
fileMax = ''
for k, v in sizes_of_files.items():
    if v > sizeMax:
        sizeMax = v
        fileMax = k
print("The file", fileMax, "has the max size:", sizeMax)
