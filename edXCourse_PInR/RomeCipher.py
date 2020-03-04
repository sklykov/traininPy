# -*- coding: utf-8 -*-
"""
Acient Rome Cipher workings - text processing and so on
@author: ssklykov
"""
# %% Import section
import string

# %% Variables creation
alphabet = " " + string.ascii_lowercase
numbers = [i for i in range(0,27)]
positions = dict(zip(alphabet,numbers))

# %% Very useful and possible re-inventing a wheel - get the key value using a value
def getKey(dictionary:dict,input_value):
    """A bit of web help - the useful function to find a key using a value (different workflow to common one)"""
    retKey = None
    for key,value in dictionary.items():
        if input_value == value:
            retKey = key; break
    return retKey

# %% Encoding messages
def encode(message:str,positions:dict,shift:int=1):
    """Encoding of an input message using specified alphabet as a dicitionary and relative shift"""
    encodedMessage = "" # initialize the returning value
    for i in range(len(message)):
        positionChar = positions[message[i]]
        if (positionChar + shift) > positions['z']:
            positionChar = 0 + (positions['z'] - positionChar) # for preventing index overflow
        else:
            positionChar += shift
        encoded_letter = getKey(positions,positionChar) # get a new, encoded letter
        encodedMessage += encoded_letter # both styles for variables naming :)
    return encodedMessage

# %% Testing
inputMessage = "hi my name is caesar"
encodedMessage1 = encode(inputMessage,positions)
encodedMessage2 = encode(inputMessage,positions,3)