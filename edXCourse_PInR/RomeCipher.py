# -*- coding: utf-8 -*-
"""
Acient Rome Cipher implementation - text processing and so on.

@author: sklykov
@license: The Unlicense

"""
# %% Import section
import string

# %% Variables creation
alphabet = " " + string.ascii_lowercase
numbers = [i for i in range(0, 27)]
positions = dict(zip(alphabet, numbers))


# %% Very useful and possible re-inventing a wheel - get the key value using a value
def getKey(dictionary: dict, input_value):
    """Find a key using a value."""
    retKey = None
    for key, value in dictionary.items():
        if input_value == value:
            retKey = key
            break
    return retKey


# %% Encoding messages
def encode(message: str, positions: dict, shift: int = 1):
    """Encode of an input message using specified alphabet as a dicitionary and relative shift."""
    encodedMessage = ""  # initialize the returning value
    for i in range(len(message)):
        positionChar = positions[message[i]]
        if (positionChar + shift) > positions['z']:
            positionChar = 0 + (positions['z'] - positionChar)  # for preventing index overflow
        else:
            positionChar += shift
        encoded_letter = getKey(positions, positionChar)  # get a new, encoded letter
        encodedMessage += encoded_letter  # both styles for variables naming :)
    return encodedMessage


# %% Decoding messages
def decode(message: str, positions: dict, shift: int = 1) -> str:
    """Decode messages using inversion of a shift used for encode them."""
    decodedMessage = ""
    for i in range(len(message)):
        positionChar = positions[message[i]]
        if (positionChar - shift) < 0:
            positionChar = (positions['z'] + positionChar) - shift  # for preventing index overflow
        else:
            positionChar -= shift
        decoded_letter = getKey(positions, positionChar)  # get a new, encoded letter
        decodedMessage += decoded_letter  # both styles for variables naming :)
    return decodedMessage


# %% Testing
inputMessage = "hi my name is caesar"
encodedMessage1 = encode(inputMessage, positions)
encodedMessage2 = encode(inputMessage, positions, 3)
decodedMessage1 = decode(encodedMessage1, positions)
decodedMessage2 = decode(encodedMessage2, positions, 3)
