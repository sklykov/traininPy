# -*- coding: utf-8 -*-
"""
A small utility to count frequency of letters in an input sentence
@author: ssklykov
"""
import string

# %% Utility
def countLetters(sentence:str)->dict:
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    count_letters = {}
    for letter in alphabet:
        i = 0 # count
        for char in sentence:
            if letter == char: i += 1
        count_letters[letter] = i
    return count_letters

# %% Testing
sentence1 = "Examples of affine transformations include translation, scaling, etc"
ctlet = countLetters(sentence1)