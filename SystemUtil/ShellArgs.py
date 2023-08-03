# -*- coding: utf-8 -*-
"""
Testing command-line arguments + Shell Variables.

@author: sklykov
@license: The Unlicense

"""
import sys
import os
# For fully exploring of this feature - use the IPython console 'runfile(filename = ..., args = ...)' function"
print(sys.argv, "- passed to this script arguments from a shell")

# %% Fetching Shell variables

keys = list(os.environ.keys())
keys = keys[0:5]
for i in keys:
    print(i, "->", os.environ[i])
