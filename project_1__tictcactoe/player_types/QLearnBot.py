import sys
import time
import math
import os
import random
import copy
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
            # time.sleep(1.5)
            self.train()

    '''
    If no q table existed, game needs to be trained. this is where the magic happens, then it will
    play the game specified.
    '''
    def train(self):
        print("TRAINING DATA begining")
        class sample_game: #mini vers of ttt game for training...shhh this is the worst fucking idea ever
            def __init__(self, char):
                self.char = char
                if self.char == 'X':
                    self.other = 'O'
                else:
                    self.other = 'X'

            def swap(self): #swaps self char to other char :-)
                if self.char == 'X':
                    self.char = 'O'
                    self.other = 'X'
                else:
                    self.char = 'X'
                    self.other = 'O'

        max_games = 1000
        for i in range(max_games):
            # print(i)
            # training time!
            board = ['█'] * 9
            new_game = sample_game('X')
            while (self.is_terminal_state(board, new_game.char))[0] is False:
                # self is X, opp is O
                action = self.choose_action(board, self.char, i) #pass entire object
                new_board = board.copy()
                new_board[action] = new_game.char
                state = self.is_terminal_state(new_board, new_game.char) #[0] is T/F , [1] is value
                reward = state[1]
                #update q table.
                self.update_q(reward, new_game.char, action, board, new_board) # MAKE THIS FUNCTION BABY
                # print(self.qtable)
                # print(board)
                if state[0] == False:
                    #game isnt over, cont
                    new_game.swap()
                    board = new_board
                else:
                    break
        
        sys.stdout = open("qtable.txt", "w")
        print(self.qtable)
        sys.stdout = sys.__stdout__ #save to file!

        return True

    def update_q(self, reward, char, action, state, new_state):
        # print("IN Q TABLE")
        gamma = .9 
        alpha = .7
        # need to ocnvert board and new board to strings like "OXOOXOXXO" or "_________"
        state = ''.join( str(i) for i in state )
        new_state = ''.join( str(i) for i in new_state )
        action = str(action)

        # check (board, action) DNE in qtable , if so place rand -.1 to .1
        if (state, action) not in self.qtable:
            self.qtable[ (state, action) ] = random.uniform(-.1, .1)
        
        # if next state not in qtable, delta = reward
        if len( [ x[0] for x in self.qtable.keys() if x[0] is new_state ] ) == 0:
            delta = reward
        else : #does exist, update qtable
            if char == 'X' : 
                delta = reward + gamma * min( self.qtable[i] for i in ( x for x in self.qtable.keys() if x[0] is new_state ) ) - self.qtable[(state, action)]
                # delta = reward + gamma * min(self.q_table(next_state,all_valid_actions) -self.q_table(curr_state, curr_action)
            else : # 'O' player
                # delta = reward + gamma * max(Q_table(next_state,all_valid_actions) - Q_table(curr_state, curr_action)
                delta = reward + gamma * max( self.qtable[i] for i in ( x for x in self.qtable.keys() if x[0] is new_state ) ) - self.qtable[(state, action)]
   
        # Q_table(curr_state, curr_action) += alpha * delta
        self.qtable[(state, action)] += alpha*delta
        
        return True

    def choose_action(self, board,cur_char, game_num):
        # explore vs exploitation
        prob_random = math.exp(-5*game_num/1000) #f(x) = e**(-5x/1000); x=currgame number and 1000 is max games
        rand_num = random.uniform(0, 1)

        board = ''.join( str(i) for i in board ) #converts board to string

        if rand_num < prob_random : #explore!
            #choose random from available positions
            free_spots = [ x for x,y in enumerate(board) if str(y)=='█' ]
            next_action = random.choice(free_spots)
        else: #exploit
            if cur_char == self.char: #max
                # grabs board spot with highest value
                # print(" max " + str( max( i[1] for i in ( x for x in self.qtable.keys() if x[0] is board ) ) ) )
                try:
                    next_action = max( i[1] for i in ( x for x in self.qtable.keys() if x[0] is board ) ) # RETURN MAX VALUE OF CURRENT STATES INDEX IN QTBALE
                except: 
                    next_action = random.choice([x for x,y in enumerate(board) if str(y)=='█'])
                    # print("BOARD " + board + "  " + str([x for x in self.qtable.keys() ]) )
                    # input("HEERE")
            else:
                try:
                    next_action = min( i[1] for i in ( x for x in self.qtable.keys() if x[0] is board ) ) # RETURN MIN VALUE OF CURRENT STATES INDEX IN QTBALE
                except:
                    next_action = random.choice([x for x,y in enumerate(board) if str(y)=='█'])
        next_action = int(next_action) # convert to int just in case!
        return next_action

    '''
    is game done given board state?
    '''
    def is_terminal_state(self, board, char): 
        winning_states = ( [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6] )
        
        other = ''
        if char == 'X':
            other = 'O'
        else:
            other = 'X'
        for a,b,c in winning_states:
            if board[a]==board[b]==board[c]==char:
                return (True, 1) #minimax won!
            elif board[a]==board[b]==board[c]==other:
                return (True, -1) #other player won
        
        space_counter = 0
        for spot in board:
            if spot=='█':
                space_counter+=1
        
        if space_counter==0: #TIE
            return (True, 0)

        return (False, 0) # aint over yet, chiefton


    def move(self, board):
        # if we are in move spot, then data has been trained.
        # try to return max of qtable of state, elseeee random choice...
        try:
            b = ''.join( str(i) for i in board )
            # print("state : " + str(b) +" with qtable entries" + str( [ x for x in self.qtable if x[0] is b ]))
            print("state : " + str(b) +" with qtable entries" + str( list( set([x[0] for x in self.qtable.keys()]) ) ))
            input("...")
            return int( max( i[1] for i in ( x for x in self.qtable.keys() if x[0] is board ) ) )
        except:
            return random.choice( [ x for x,y in enumerate(board) if str(y)=='█' ] )

    
    