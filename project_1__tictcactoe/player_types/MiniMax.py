import sys
import re
import random
import copy
import math 
from Player import *

# X IS MAX (computer) O IS MINS (human)
# we will return score based off of X's position
class MiniMax(Player):
    def __init__(self, char='X'):
        self.char = char
        self.kind = 'MiniMax'
        
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
            if spot!='█':
                space_counter+=1
        
        if space_counter==9: #TIE
            return (True,0)

        return (False, 0) # aint over yet chief

    '''
    MINIMAX(s)
    For every a ∊ Actions(s)
        if MIN-VALUE(RESULT(s, a)) > UTILITY(RESULT(s, best))
            best = a
    return best
    
    MIN-VALUE(s)
    If GAME-OVER(s)
        return UTILITY(s)
    For every a ∊ Actions(s)
        sim-utility = MAX-VALUE(RESULT(s, a))
        if sim-utility < worst
            worst = sim-utility
    return worst

    MAX-VALUE(s)
    If GAME-OVER(s)
        return UTILITY(s)
    For every a ∊ Actions(s)
        sim-utility = MIN-VALUE(RESULT(s, a))
        if sim-utility > best
            best = sim-utility
    return best
    '''     

    def move(self, board): #acutal MINIMAX IMPLEMENTATION
        # in order to cut down brnaching factor a bit, IF ai 
        #  is going first, just choose a corner.
        if len( self.available_positions(board) ) == 9:
            return random.choice( [0,2,6,8] )
        
        # ON THE MINIMAX TURN, YOU WANT THE BEST (MAX) OF THE OTHER PLAYERS TURNS(MIN)
        worst_case = 0 #tie in worst case
          
        for moves in self.available_positions(board) :
            board[moves] = self.char
            board_val = self.min_value(board)
            board[moves] = '█'
            if board_val > worst_case:
                return moves

        # if cant find a move there, just take a tie from here.    
        return random.choice(self.available_positions(board))

    def max_value(self, board):
        board_done, return_value = self.is_terminal_state(board)
        if board_done: # if current board is done, return -10, 0 , 10
            return return_value

        value = -10000

        for moves in self.available_positions(board):
            board[moves] = self.char
            value = max( value, self.min_value(board) )
            board[moves] = '█'

        return value

    def min_value(self, board):
        board_done, return_value = self.is_terminal_state(board)
        if board_done:
            return return_value

        value = 10000

        c = ''
        if self.char == 'X':
            c = 'O'
        else:
            c = 'X'

        for moves in self.available_positions(board):
            board[moves] = c
            value = min( value, self.max_value(board) )
            board[moves] = '█'

        return value

    '''
    for move in game.get_available_moves():
		possible_game = game.get_new_state(move)
		scores.append(minimax(possible_game, depth))
		moves.append(move)

	if game.active_turn == 'X':
		max_score_index = scores.index(max(scores))
		choice = moves[max_score_index]
		return scores[max_score_index]
	else:
		min_score_index = scores.index(min(scores))
		choice = moves[min_score_index]
		return scores[min_score_index]
    '''