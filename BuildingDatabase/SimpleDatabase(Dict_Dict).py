# -*- coding: utf-8 -*-
"""
Another approach for making simple database - making a dictionary with dictionary inside
The simple demo here, in this file
@author: ssklykov
"""

class Figures():
    overallDict = {}
    keys = ['length','width','height'] # internal values

    def __init__(self,length:float=2.0,width:float=2.0,height:float=2.0,figureDescriptor:str='Cube'):
        values = [abs(length),abs(width),abs(height)]
        fieldInDict = dict(zip(self.keys,values)) # again baking values and keys into single dict
        self.overallDict = {figureDescriptor:fieldInDict}

    def appendNewFigure(self,length:float,width:float,height:float,figureDescriptor:str):
        values = [abs(length),abs(width),abs(height)]
        fieldInDict = dict(zip(self.keys,values)) # again baking values and keys into single dict
        self.overallDict[figureDescriptor] = fieldInDict  # append new value to the dictionary by just pairing key - value

    def getKeys(self):
        outputString = "There are following figures are collected: "
        print(outputString)
        outputString = ""
        for keys in self.overallDict:
            outputString += keys + ", " # collecting all elements in a single string
        outputString = outputString[0:len(outputString)-2] # dirty workaround - just deleting the last elements from composing str
        print(outputString)

    def cuboidVolume(self,figureDescriptor:str) -> float:
        try:
            fig = self.overallDict[figureDescriptor]; a = fig.get(self.keys[0]);
            b = fig.get(self.keys[1]); c = fig.get(self.keys[2])
            return (a*b*c)
        except KeyError:
            print("There isn't this figure appended before:",figureDescriptor)
            return -1

    def getValues(self,figureDescriptor:str):
        try:
           fig = self.overallDict[figureDescriptor]
           outputString = ""
           for keys in fig:
               outputString += keys + ": " + str(fig[keys]) + ", "
           outputString = outputString[0:len(outputString)-2] # dirty workaround again
           print(outputString)
        except KeyError:
            print("There isn't this figure appended before:",figureDescriptor)




# %% Testing
fig1 = Figures()
fig1.appendNewFigure(2,3,4,'Rectangular cuboid')
fig1.getKeys()
fig1.getValues('Cube')
Vol1 = fig1.cuboidVolume('Cube'); print('Volume of a default cube is', Vol1)
fig1.getValues('parallelipiped')