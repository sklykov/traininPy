# -*- coding: utf-8 -*-
"""
Testing a bit of functionality of shelve module
@author: ssklykov
"""
# %% Making a simple database containing dictionary of dictionaries
i1 = {'x':1,'y':1,'I':2}
i2 = {'x':2,'y':3,'I':4}
i3 = {'x':4,'y':5,'I':1}
composeDict = {'first':i1,'second':i2}

# %% Demo of using shelve
import shelve
# Creation of database itself
db = shelve.open('points')
# Make the persistent records
for keys in composeDict:
    db[keys] = composeDict[keys]
db.close()

# Open and display stored values
db = shelve.open('points')
for key in db:
    print(key, ' : ', db[key])
db.close()

# %% Cleaning created files through this demo (creation - by shelve module)
import os
os.remove('points.dat'); os.remove('points.dir'); os.remove('points.bak')