# -*- coding: utf-8 -*-
"""
Using a general class as storage item - instead of List of Dictionaries and Dictionaries of Dictionaries
This class itself plays a role of a simple image
@author: ssklykov
"""
class Gen2DImage():
    I = [[]]; H = W = 1
    def __init__(self,H:int=1,W:int=1):
        H = abs(H); W = abs(W)
        if (H == 0):
            H = 1
        if (W == 0):
            W = 1
        self.H = H; self.W = W; self.I = [[0]*W]*H

class Quad2DImage(Gen2DImage):
    size = 1
    def __init__(self,size:int=1):
        size = abs(size);
        if (size == 0):
            size = 1
        self.H = self.W = size
        self.I = [[0]*size]*size



# %% Testing class fetures
if __name__ == '__main__':
    img = Gen2DImage(3,2)
    print(img.I)
    quadImg = Quad2DImage(3)
    print(quadImg.I)
