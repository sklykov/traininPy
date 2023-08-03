# -*- coding: utf-8 -*-
"""
Funny utility for generating random passwords with preselected range.

@author: sklykov
@license: The Unlicense

"""
import random
import string


# %% The utility itself
def randPassword(length: int = 1, characters_to_pick: str = "abc") -> str:
    psd = str()
    for i in range(length):
        psd += random.choice(characters_to_pick)
    return psd


# %% Testing utility
sampleCharacters = "0123456789" + string.ascii_lowercase
print(randPassword(5, sampleCharacters))
print(randPassword(3, sampleCharacters))
print(randPassword(10, sampleCharacters))
