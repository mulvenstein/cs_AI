import sys
import re
import random
import copy
from Player import *

# X IS MAX (computer) O IS MINS (human)
# we will return score based off of X's position
class MiniMax(Player):
    def _init__(self, char='X'):
        self.type = 'MiniMax'
        self.char = char # x or o player char

    '''
    Pseudo code for minimax
        If the game is over, return the score from X's perspective.
        Otherwise get a list of new game states for every possible move
        Create a scores list
        For each of these states add the minimax result of that state to the scores list
        If it's X's turn, return the maximum score from the scores list
        If it's O's turn, return the minimum score from the scores list
    
    depth 10: empty board
    depth 9: one move made
    etc
    '''

    def move(self, board): # ACTUAL MINIMAX ALGORITHM
        if len(self.available_positions(board)) == 9:
            return random.choice([0, 2, 6, 8]) #empty board, choose any corner
        #assuming we are here, its our turn to use char self.char 
        