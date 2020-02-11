# -*- coding: utf-8 -*-
"""
Actually, the Spyder IDE crushed and destroyed previous file! Just for historical notes
Implementation of simple database containing some values (coordinates and intensity - like 2D image)
@author: ssklykov
"""

class ImageDict():
    """Base class - containing a list with points (dictionary)"""
    point = {} # initializer for single point - a dictionary
    arrayOfPoints = [] # enpty list for holding points
    keys = ['x','y','intensity']

    def __init__(self,x:int=0,y:int=0,intensity:int=0):
        values = [x,y,intensity]
        self.point = dict(zip(self.keys,values)) # initializing of point as dictionary using zipping of two lists
        self.arrayOfPoints.append(self.point)

    def insertNewPoint(self,x:int,y:int,intensity:int):
        self.point = {self.keys[0]:x,self.keys[1]:y,self.keys[2]:intensity} # hard coding of assignig values
        self.arrayOfPoints.append(self.point)

    def getPoint(self,n:int):
        try:
            pointToReturn = self.arrayOfPoints[n]
        except IndexError:
            print("There isn't point #",n)
            pointToReturn = None
        return pointToReturn




# %% Testing
image1 = ImageDict(1,2,100)
image1.insertNewPoint(2,2,2)
point1 = image1.getPoint(0)