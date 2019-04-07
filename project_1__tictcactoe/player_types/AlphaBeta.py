import random
from Player import *

class AlphaBeta(Player):
    def __init__(self, char):
        self.char = char
        self.kind = "AlphaBeta"
        if self.char == 'X':
            self.opponent = 'O'
        else :
            self.opponent = 'X'


    '''
    move calls alphabeta with is maximizing true
    
    def alphabeta(state, depth, is maximizing, alpha,beta)

    if node is a terminal node :
        return value of the node
    
    if isMaximizingPlayer :
        bestVal = -INFINITY 
        for each child node :
            value = alphabeta(node, depth+1, false, alpha, beta)
            bestVal = max( bestVal, value) 
            alpha = max( alpha, bestVal)
            if beta <= alpha:
                break
        return bestVal

    else :
        bestVal = +INFINITY 
        for each child node :
            value = minimax(node, depth+1, true, alpha, beta)
            bestVal = min( bestVal, value) 
            beta = min( beta, bestVal)
            if beta <= alpha:
                break
        return bestVal
    '''

    '''
    is game done given board state?
    returns (TRUE, value of state [10 win, -10 lost] ) or FALSE
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
        '''
        run alpha beta pruning on board passed, choose best path.
        '''
        # cut down pruning a bit and take corner if no other move has been made
        if len( self.available_positions(board) ) == 9:
            return random.choice( [0,2,6,8] )



        return
    

        
