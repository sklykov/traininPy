# -*- coding: utf-8 -*-
"""
Using shelve module for making persistence objects saving (using developed classes)
@author: ssklykov
"""
import shelve
from SimpleDatabase_Class import Quad2DImage
import os

# %% Creation some data
img1 = Quad2DImage(3)
img2 = Quad2DImage(4)

# %% Making persistent data entries
db = shelve.open('images')  # creates or open database
db['img1'] = img1; db['img2'] = img2
db.close()

# %% Read stored data entries
db = shelve.open('images')  # creates or open database
imgRead1 = db['img1']; print(imgRead1.I)
db.close()

# %% Cleaning created files through this demo (creation - by shelve module)
os.remove('images.dat')
os.remove('images.dir')
os.remove('images.bak')
