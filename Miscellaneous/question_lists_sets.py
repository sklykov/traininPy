# -*- coding: utf-8 -*-
"""
Сhecking assignment (test) question

@author: ssklykov
"""
# Using intersection of sets for finding intersections elements in two lists
a = [i for i in range(500)]
b = [i*2 for i in range(1000)]
a = set(a)
b = set(b)
c_set = a & b
с = list(c_set)


def get_intersection(a: list, b: list):
    a = set(a)
    b = set(b)
    return a & b


c2 = get_intersection(a, b)
