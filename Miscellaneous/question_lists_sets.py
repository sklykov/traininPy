# -*- coding: utf-8 -*-
"""
Сhecking assignment (test) questions

@author: ssklykov
"""
import re
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

# testing regular expressions
line = "numbers: 0, 1, 2, -1, 10, 100, 99, 98.1, 1.06, 2.723, -1.23, -10.987, 99.99, 88.88, 0.67, 2.60, 0.01, 77, -50"
matches = re.findall('[^-\\.]\\b([1-9]\\d)[^\\.\\d]', line)  # Only 2 positive digit integers
matches_decimal = re.findall('[^-]\\b(\\d?\\d\\.\\d[1-9])\\b', line)  # Only positive less than 100 decimal numbers
matches_single = re.findall('[^-\\.]\\b(\\d)[^\\.\\d]', line)  # only single positive integer [0-9]
# !!!: composing pattern below using operator | for selection particular number surrounded by white space or comma
pattern = '(?:[^-\\.]\\b([1-9]\\d|\\d|\\d?\\d\\.\\d[1-9])[^\\.\\d])'
matches_all = re.findall(pattern, line)
