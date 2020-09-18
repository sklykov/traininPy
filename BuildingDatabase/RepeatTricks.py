# -*- coding: utf-8 -*-
"""
So, repeating a few of Python tricks (to be continued?):
1) List comprehensions and generators; 2) Lambda functions; 3) Using of map, filter and reduce functions
@author: ssklykov
"""
import functools
# %% Lists and generators
obj = [1, 2, 'raz']; obj2 = [2, 3, 'dva']; obj3 = [3, 4, 'tri']
allObjs = [obj, obj2]; allObjs.append(obj3) # making list of lists - easy and fast
l1 = [1, 2]; l2 = [3, 4]
# Perfoming tasks on the list elements using list comprehensions:
firstValSquared = [x[0]*x[0] for x in allObjs]  # Extraction of list values from object at another list (Generator expression)
sumElemTwoLists = [x+y for x in l1 for y in l2]  # [1,2] + [3,4] = [4,5,5,6] - means that summing made using other rules

# %% Demo of a lambda function (anonymous function w/t docstring, etc)
squaredSpecifiedElements = lambda n, someList: [x[n]*x[n] for x in someList]  # lambda inputArg1,...:returning_val using inputs
firstValSquared2 = squaredSpecifiedElements(0, allObjs)
secondValSquared = squaredSpecifiedElements(1, allObjs)
# Another simple lambda function - calculation of a sum of two elements
anonSum = lambda k, l: k+l; sum2 = anonSum(1, -1)

# %% Map function - performing some defined operation over iterable data type (process all elements)
array = [1, 2, 3, 4, 5]
def sumIncrease(x): return x*2
arrayMod = list(map(sumIncrease, array))
arrayMod2 = list(map(lambda x: x*3, array))
# %% Filter function - implementing some rule over elements of an iterable item
arrayMod3 = list(filter(lambda x: x >= 3, array))  # filtering out all elments which less than 3 from input array
# %%  Reduce function - reducing a sequence to a single value by applying consequently some operation to all elements
d = functools.reduce(lambda x, y: x*y, array)  # calculation of array[0]*array[1]*... = 5!
