#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pecularity of lambda function with parameter call.

@author: sklykov
@license: The Unlicense

"""
# %% Lambda function remembers last assigned values to used parameters
parameter = 1
func = (lambda: parameter + 1)
parameter = 10
print("Instead of exprected 2, it returns 11: ", func())  # Function call resolved at call time, not creation
