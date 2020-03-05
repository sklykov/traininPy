# -*- coding: utf-8 -*-
"""
Counting unique words in various texts - an exercise from the edX course
@author: ssklykov
"""

# %% Developing of the function
def countWords(text:str)->dict:
    word_count = {}
    for word in text.split(" "):
        if word in word_count.keys(): # the parenthesis are necessary!
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

# %% Testing conditions
input_text = "We choose to go to the moon. We choose to go to the moon in this decade and do the other things,\
not because they are easy, but because they are hard, because that goal will serve to organize and measure the\
best of our energies and skills, because that challenge is one that we are willing to accept, one we are unwilling\
to postpone, and one which we intend to win, and the others, too."
accounted_words = countWords(input_text)
