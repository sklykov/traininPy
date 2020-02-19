# -*- coding: utf-8 -*-
"""
Testing command-line arguments + Shell Variables
@author: ssklykov
"""
import sys
print("For fully exploring of this feature - use the IPython console 'runfile' function")
print(sys.argv,"- passed to this script arguments from a shell")

# %% Fetching Shell variables
import os
keys = list(os.environ.keys())
keys = keys[0:5]
for i in keys:
    print(i,"->",os.environ[i])