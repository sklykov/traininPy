# -*- coding: utf-8 -*-
"""
Counting unique words in various texts - an exercise from the edX course.

@author: sklykov
@license: The Unlicense

"""


# %% Developing of the function to count unique words in an input text
def countWords(text: str) -> dict:
    """Prototype of a function counting number of appeareances of words in a text."""
    word_count = {}
    text = text.lower()  # to prevent counting We and we as different words
    skips = [".", ",", ";", ":", "'"]
    for character in skips:
        text = text.replace(character, "")
    for word in text.split(" "):
        if word in word_count.keys():  # the parenthesis are necessary!
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


# %% Open and read text as a single, long string
def readText(text_file) -> str:
    """Read a text from a file."""
    text = ""
    with open(text_file, 'r', encoding='utf8') as rtextFile:
        text = rtextFile.read()
        text = (text.replace("\n", "").replace("\r", ""))
    return text


# %% Statistics for the accounting of words in a text
def word_stat(word_counts: dict) -> tuple:
    """Return just numbers of words and their frequencies."""
    unique_words = len(word_counts)
    counts = word_counts.values()
    return (unique_words, counts)


# %% Testing conditions
input_text = "We choose to go to the moon. We choose to go to the moon in this decade and do the other things,\
not because they are easy, but because they are hard, because that goal will serve to organize and measure the\
best of our energies and skills, because that challenge is one that we are willing to accept, one we are unwilling\
to postpone, and one which we intend to win, and the others, too."
accounted_words = countWords(input_text)
