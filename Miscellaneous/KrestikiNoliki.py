# -*- coding: utf-8 -*-
"""
Demo for a homework - from the edX course
@author: ssklykov
"""
# %% Import section
import numpy as np

#%% Init function - create board
def create_board():
    board = np.zeros((3,3),dtype=int)
    return board

# %% Placing func
def place(board,player:int,position:tuple):
    if (player < 1) or (player > 2):
        raise("WrongPlayerNumberException")
    (row,col) = position
    if board[row,col] == 0:
        board[row,col] = player

#%% Testing created functions
board = create_board()
