import sys
import re
import random
import copy
import math 
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

    '''
    is game done given board state?
    returns (TRUE, value of state [10 win, -10 lost] ) or FALSE
    '''
    def is_terminal_state(self, board):
        winning_states = ( [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6] )
        for a,b,c in winning_states:
            if board[a]==board[b]==board[c]==self.char:
                return (True, 10) #minimax won!
            elif board[a]==board[b]==board[c]!=self.char!='█':
                return (True, -10) #other player won
        
        space_counter = 0
        for spot in board:
            if spot=='█':
                space_counter+=1
        
        if space_counter==9: #TIE
            return (True,0)

        return (False, 0)

        def move(self, board): #acutal MINIMAX IMPLEMENTATION
            # in order to cut down brnaching factor a bit, IF ai 
            #  is going first, just choose a corner.
            if len( self.available_positions(board) ) == 0:
                return int( random.choice[0,2,6,8] )
            
            # ON THE MINIMAX TURN, YOU WANT THE BEST (MAX) OF THE OTHER PLAYERS TURNS(MIN)
            max_val = 0 #tie in worst case
            
            for moves in self.available_positions(board) :
                board[moves] = self.char

        