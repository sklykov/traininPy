# -*- coding: utf-8 -*-
"""
Repeating OOP concepts and saving them in a single file for possible reusing.

@author: sklykov
@license: The Unlicense

"""
import math
from abc import ABCMeta, abstractmethod


class Figure(metaclass=ABCMeta):
    """Classical superclass - for a demo. It's an abstract class - Figure."""

    charVal = 0.0

    @abstractmethod
    def getPerimeter(self) -> float:
        pass

    @abstractmethod
    def getArea(self) -> float:
        pass


class Rectangle(Figure):
    """Classical child - a rectangle - a special figure."""

    def __init__(self, width: float = 1.0, height: float = 1.0):
        w = float(width)
        h = float(height)
        self.charVal = (w, h)  # packing characteristic values as a tuple
        # print("Class: '",Rectangle.__name__,"' initialized with",self.charVal,"as charateristic values")

    def getPerimeter(self):
        (w, h) = self.charVal  # unpacking values
        return 2*(w+h)

    def getArea(self):
        (w, h) = self.charVal  # unpacking values
        return w*h


class Square(Rectangle):
    """Classical child - a square - a special rectangle."""

    def __init__(self, characteristicValue: float = 1.0):
        Rectangle.__init__(self, characteristicValue, characteristicValue)
        print("Class: '", Square.__name__, "' initialized with", self.charVal, "as charateristic values")

    def getPerimeter(self):
        return Rectangle.getPerimeter(self)


class Circle(Figure):
    """Classical child - a circle - a special figure."""

    def __init__(self, characteristicValue: float = 1.0):
        self.charVal = float(characteristicValue)
        print("Class: '", Circle.__name__, "' initialized with", self.charVal, "as a radius")

    def getPerimeter(self):
        return 2*math.pi*self.charVal

    def getArea(self):
        return math.pi*math.pow(self.charVal, 2)


# %% Testing scripts
characteristicValue = 2  # Size of figures
sq1 = Square(characteristicValue)
print("Perimeter of a square", sq1.getPerimeter())
print("Area of a square", sq1.getArea())
rec1 = Rectangle(2, 3); print("Area of a rectangle", rec1.getArea())
crl1 = Circle(2); print("Perimeter of a circle", round(crl1.getPerimeter(), 2))
