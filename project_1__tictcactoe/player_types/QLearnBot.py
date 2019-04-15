import sys
import time
import math
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
    If no q table existed, game needs to be trained. this is where the magic happens, then it will
    play the game specified.
    '''
    def train(self):

        class sample_game: #mini vers of ttt game for training...shhh this is the worst fucking idea ever
            def __init__(self, char):
                self.board = ['_'*9]
                self.char = char
                if self.char == 'X':
                    self.other = 'O'
                else:
                    self.other = 'X'
            def is_win(self, board, char):
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


        max_games = 1000
        for i in range(max_games):
            # training time!
            while True:
                new_game = sample_game('X') # self is X, opp is O
                while (new_game.is_win(new_game.board, new_game.char))[0] is False: # while game aint over
                    action = choose_action(new_game) #pass entire object
                print(i)
        
        return

    def choose_action(board,cur_char, game_num):
        # explore vs exploitation
        prob_random = math.exp(-5*game_num/1000) #f(x) = e**(-5x/1000); x=currgame number and 1000 is max games
        rand_num = random.uniform(0, 1)

        if rand_num < prob_random : #explore!
            #choose random from available positions
            print("shiet")
        else: #exploit
            if cur_char == self.char: #max
                next_action = max(self.qtable) # RETURN MAX VALUE OF CURRENT STATES INDEX IN QTBALE
            else:
                next_action = min(self.qtable) # RETURN MIN VALUE OF CURRENT STATES INDEX IN QTBALE
        return next_action

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

    
    