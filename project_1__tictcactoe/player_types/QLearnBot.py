import system
import time
import os
import random
from Player import *

class QLearnBot(Player):
    def __init__(self, char):
        self.char = char
        self.kind = "QLEARN"
        if self.char == 'X':
            self.opponent = 'O'
        else :
            self.opponent = 'X'
        self.qtable = {}
        #check for q table
    
        exists = os.path.isfile('qtable.txt')
        if exists:
            print("QTable exsits. using existing functionality") 
            with open('qtable.txt') as f:
                self.qtable = eval(f.read()) # set self.qtable as previous values!
            time.sleep(1.0)
        else:
            print("no qtable found. TRAINING DATA.")
            time.sleep(1.5)


    '''
    is game done given board state?
    '''
    def is_terminal_state(self, board): # same function as minimax. probably shouldve just inherited that class..
        winning_states = ( [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6] )
        for a,b,c in winning_states:
            if board[a]==board[b]==board[c]==self.char:
                return (True, 10) #minimax won!
            elif board[a]==board[b]==board[c]==self.opponent:
                return (True, -10) #other player won
        
        space_counter = 0
        for spot in board:
            if spot=='█':
                space_counter+=1
        
        if space_counter==0: #TIE
            return (True, 0)

        return (False, 0) # aint over yet, chiefton


    def move(self, board):
        return random.choice([range(9)])
    