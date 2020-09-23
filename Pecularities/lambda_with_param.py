#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module for collecting some peculiriaties (inspired by "Programming Python")

@author: ssklykov
"""
# %% Lambda function remembers last assigned values to used parameters
parameter = 1
func = (lambda: parameter + 1)
parameter = 10
print("Instead of exprected 2, it returns 11: ", func())  # Function call resolved at call time, not creation
