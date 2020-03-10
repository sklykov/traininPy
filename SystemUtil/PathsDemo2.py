# -*- coding: utf-8 -*-
"""
Continuing to test (make) some features related to os and sys modules
@author: ssklykov
"""
# %% Import section
import os

# %% Portability utilities
dirs_separator = os.sep # returning the system-specific directories separator
print(dirs_separator," - system separator")
parent_dir = os.pardir
os.chdir(parent_dir); print(os.getcwd()," - parent directory")
separated_path = os.getcwd().split(dirs_separator) # Separation using specific directories separator
restored_path = os.path.join(os.getcwd(),"SystemUtil")
print(restored_path,"- a restored path after going to a parent directory")
print(os.path.exists(restored_path),' - does restored path exists?')
print(os.path.isdir(restored_path)," - a folder is on the restored path")
os.chdir(restored_path) # change the working directory back
absol_curr_path = os.path.abspath(os.curdir) # Other way to get an absolute path to cwd
absol_parent_path = os.path.abspath(os.pardir) # Other way to get an absolute path to parent directory
print(os.listdir(absol_parent_path), "- list of directories inside this repo")

# %% A bit more features
listOfFilesInCWD = sorted(os.listdir("."))
listOfFilesInPWD = sorted(os.listdir("..")) # sorted list of files in a parent directory

# %% Walking in the directory tree
for (current_directory,sub_dirs,dir_files) in os.walk('.'):
    for fname in dir_files:
        print(os.path.join(current_directory,fname))
