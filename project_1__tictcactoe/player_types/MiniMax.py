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

    '''
    is game filled?
    '''
    def is_full(self, board):
        return board.count('█')==0

    '''
    is game done given board state?
    returns (TRUE, CHAR of WINNER) or FALSE
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

    def is_my_turn(self, board):
        check = self.char
        count = 0
        for i in board:
            if i == check:
                count += 1
                continue
            elif i == '█':
                continue
            count -= 1 
        if (count == 0 and self.char == 'X') or count == -1: 
            return True
        else:
            return False


    def solve(self, board): # ACTUAL MINIMAX ALGORITHM
        # if len(self.available_positions(board)) == 9:
        #     return random.choice([0, 2, 6, 8]) #empty board, choose any corner. this will just help wth branching factor
        # # current setup is 'board'

        if self.is_full(board):
            return 0 # TIE, VALUE IS 0
            
        turn = None
        if self.is_my_turn(board):
            turn = True
        else:
            turn = False
        
        branches = self.available_positions(board)
        branch_evaluations = [solve(twig) for twig in branches]



        