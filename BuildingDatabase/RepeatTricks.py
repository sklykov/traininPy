# -*- coding: utf-8 -*-
"""
So, repeating a few of Python tricks

@author: ssklykov
"""
# %% Lists and generators
obj = [1,2,'raz']; obj2 = [2,3,'dva']; obj3 = [3,4,'tri']
allObjs = [obj,obj2]; allObjs.append(obj3)

# Perfoming task on the list elements:
firstValSquared = [x[0]*x[0] for x in allObjs] # Extraction of list values from object at another list