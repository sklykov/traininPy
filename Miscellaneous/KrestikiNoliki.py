# -*- coding: utf-8 -*-
"""
Demo for a homework - from the edX course. All implementation in this single file - not really valuable
@author: ssklykov
"""
# %% Import section
import numpy as np
import random; random.seed(1)

#%% Init function - create a board for a game
def create_board():
    board = np.zeros((3,3),dtype=int)
    return board

# %% Placing function - selection of a player #1 or #2
def place(board,player:int,position:tuple):
    if (player < 1) or (player > 2):
        raise("WrongPlayerNumberException")
    (row,col) = position
    if board[row,col] == 0:
        board[row,col] = player

# %% Possible positions
def possibilites(board):
    possible = np.where(board == 0)
    # print(possible) # Debugging
    (xPos,yPos) = possible
    # print(xPos) # Debugging
    possiblepos = []
    for i in range(len(xPos)):
        possiblepos.append((xPos[i],yPos[i]))
    return possiblepos

# %% Random selection of a position to place a cross or a zero
def random_place(board,player:int):
    if len(possibilites(board)) > 0:
        selection = random.choice(possibilites(board))
        place(board,player,selection)
    # try:
    #     selection = random.choice(possibilites(board))
    #     place(board,player,selection)
    # except (IndexError): pass

# %% Testing row winning condition
def row_win(board,player:int) -> bool:
    colsN = len(board[0,:]); # print(colsN)
    rowsN = len(board[:,0]); # print(rowsN)
    res = False
    for i in range(rowsN):
        for j in range(colsN):
            if board[i,j] == player:
                res = True
            else:
                res = False; break # exit from running on the columns
        if res == True: break # exit on the condition
    return res

# %% Testing column winning condition
def col_win(board,player:int) -> bool:
    colsN = len(board[0,:]); # print(colsN)
    rowsN = len(board[:,0]); # print(rowsN)
    res = False
    for j in range(colsN):
        for i in range(rowsN):
            if board[i,j] == player:
                res = True
            else:
                res = False; break # exit from running on the columns
        if res == True: break # exit on the condition
    return res

# %% Testing diagonal winning condition
def diag_win(board,player:int) -> bool:
    colsN = len(board[0,:]); # print(colsN)
    res = False
    # main giagonal
    for i in range(colsN):
        if board[i,i] == player:
            res = True
        else:
            res = False; break # exit from running on the columns
    # secondary diagonal
    for i in range(colsN):
        if board[i,colsN-1-i] == player:
            res = True
        else:
            res = False; break # exit from running on the columns
    return res
# %% Evaluation of a winner in a game
def evaluate(board):
    winner = 0
    for player in [1,2]:
        if row_win(board,player) or diag_win(board,player) or col_win(board,player):
            winner = player; break
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

# %% Game simulation
def play_game(turn:int=1):
    board_game = create_board()
    if turn == 1:
        players = [1,2]
    else:
        players = [2,1]
    condition = True
    while(condition == True):
        for player in players:
            random_place(board_game,player)
        winner = evaluate(board_game)
        if (winner == 1 or winner == 2 or winner == -1):
            condition = False
    return winner

# %% Game simulation - more strategic behaviour
def play_strategic_game(turn:int=1):
    board_game = create_board()
    if turn == 1:
        players = [1,2]
    else:
        players = [2,1]
    condition = True; step = 1
    while(condition == True):
        for player in players:
            if (step == 1) and (player == 1):
                place(board_game,player,(1,1)); step = 2
            else:
                random_place(board_game,player)
        winner = evaluate(board_game)
        if (winner == 1 or winner == 2 or winner == -1):
            condition = False
    # print(board_game) # Debugging
    return winner

# %% Testing created functions
game_board = create_board()
place(game_board,1,(0,0))
posspos = possibilites(game_board); # print(posspos)
random_place(game_board,2)

# %% 2nd Random game
game_board2 = create_board()
for i in range(9):
    random_place(game_board2,1)
    random_place(game_board2,2)
# print(board2); # rowWin1 = row_win(game_board2,1); # colWin1 = col_win(game_board2,1); # diagWin1 = diag_win(game_board2,1)

# %% 1000 games
random.seed(1)
winners = [0]*1000; count1plwin = 0
for i in range(1000):
    if i % 2 == 0:
        turn = 1
    else:
        turn = 2
    winners[i] = play_game(turn)
    if winners[i] == 1:
        count1plwin += 1
print(count1plwin,' - number of wins of 1st player')
# %% 1000 strategic games
random.seed(1);
# testTry = play_strategic_game(1)
winners2 = [0]*1000; count1plwin2 = 0
for i in range(1000):
    if i % 2 == 0:
        turn = 1
    else:
        turn = 2
    winners2[i] = play_strategic_game(turn)
    if winners2[i] == 1:
        count1plwin2 += 1
print(count1plwin2,' - number of wins of 1st player')

