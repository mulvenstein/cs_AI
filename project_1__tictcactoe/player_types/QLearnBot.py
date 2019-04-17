import sys
import time
import math
import os
import random
import copy

sys.path.append( str(sys.path[0])+"/../" )

from TicTacToe import *
from Player import *

class QLearnBot(Player):
    def __init__(self, char, qtable={}, epsilon=0.2, alpha=0.3, gamma=0.9):
        self.char = char
        self.kind = "QLEARN"
        self.qtable = qtable
        self.epsilon = epsilon # e-greedy chance of random exploration
        self.alpha = alpha # learning rate
        self.gamma = gamma # discount factor for future rewards
        self.opponent = 'O' if char is 'X' else 'X'
        self.previous_state = [ '█' for _ in range(9) ]
        self.previous_move = None

    def q_lookup(self, state, action): # state is board, action is where next piece is goin
        state = ''.join( str(i) for i in state ) # convert state to a string to qtable entries are [ (string, int) ] = val
        # "optimistic" explortation 1 initial values
        if self.qtable.get((state, action)) is None:
            self.qtable[(state, action)] = 1.0
        return self.qtable.get((state, action))

    def get_reward(self, value, board):
        if self.previous_move is not None:
            self.learn(self.previous_state, self.previous_move, value, board)

    def learn(self, state, action, reward, result_state):
        prev = self.q_lookup(state, action)
        maxqnew = max( [ self.q_lookup(result_state, a) for a in self.available_positions(state) ] )
        state = ''.join( str(i) for i in state )
        self.qtable[ (state, action) ] = prev + self.alpha * ((reward + self.gamma*maxqnew) - prev)

    def move(self, board):
        self.previous_state = board
        actions = self.available_positions(board)

        if random.random() < self.epsilon: # explore!
            self.previous_move = random.choice(actions)
            return self.previous_move

        qs = [ self.q_lookup(self.previous_state, a) for a in actions ]
        maxQ = max(qs)

        if qs.count(maxQ) > 1:
            # more than 1 best option; choose among them randomly
            best_options = [i for i in range(len(actions)) if qs[i] == maxQ]
            i = random.choice(best_options)
        else:
            i = qs.index(maxQ)

        self.previous_move = actions[i]
        return actions[i]
