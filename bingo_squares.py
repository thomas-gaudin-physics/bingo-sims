#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 16:36:21 2021

@author: thomasgaudin
"""

#Bingo Best Squares
#Which squares produce a winning card most often?
    
from random import randint
import numpy as np

def mark_card(card):
    """Marks a random square on the bingo card"""
    row = randint(0, 4)
    column = randint(0, 4)
    
    if card[row, column] == 1:
        pass
    else:
        card[row, column] = 1
    
    return card

def column_checker(card):
    """Checks for winning columns"""
    
    win_cols = []
    
    for ind, column in enumerate(card.T):
        if all(column) == True:
            win_cols.append(ind)
        else:
            pass
        
    return win_cols

def row_checker(card):
    """Checks for winning rows"""
    
    win_rows = []
    
    for index, row in enumerate(card):
        if all(row) == True:
            win_rows.append(index)
        else:
            pass
        
    return win_rows

def diag_checker(card):
    """Checks for winning main diagonal"""
    
    if np.all(np.diagonal(card)) == True:
        return True
    else:
        return False

def anti_diag_checker(card):
    """Checks for winning main anti-diagonal"""
    
    if np.all(np.diagonal(card[::-1])) == True:
        return True
    else:
        return False
        
        

def victory_conditions(card):
    """Checks for a winning path"""
    
    rows = row_checker(card)
    cols = column_checker(card)
    fw_diag = diag_checker(card)
    bw_diag = anti_diag_checker(card)
        
    #checks for any victory conditions
    if rows == True or cols == True or fw_diag == True or bw_diag == True:
        return False
    else:
        return True

def clear_card():
    """Produces a clean slate card."""
    new_card = np.zeros((5, 5))
    new_card[2, 2] = 1
    
    return new_card
    

bingo_card = clear_card()
num_wins = np.zeros((5,5))
 
no_winner = True  
count = 1  

while count <= 10:  
    while no_winner:
        
        bingo_card = mark_card(bingo_card)
        
        if victory_conditions(bingo_card) == False:
            no_winner = False
        else:
            continue 
        
    if row_checker(bingo_card) == True:
        for val in row_checker(bingo_card):
            for col in range(0, 5):
                num_wins[val, col] += 1
                
    if column_checker(bingo_card) == True:
        for val in column_checker(bingo_card):
            for row in range(0, 5):
                num_wins[row, val] += 1
                
    if diag_checker(bingo_card) == True:
        num_wins[0, 0] += 1
        num_wins[1, 1] += 1
        num_wins[2, 2] += 1
        num_wins[3, 3] += 1
        num_wins[4, 4] += 1
        
    if anti_diag_checker(bingo_card) == True:
        num_wins[4, 0] += 1
        num_wins[3, 1] += 1
        num_wins[2, 2] += 1
        num_wins[1, 3] += 1
        num_wins[0, 4] += 1
        
    bingo_card = clear_card()
    
    count += 1
    
print(num_wins)
