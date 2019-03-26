import sys
import re

pth = str(sys.path[0])
pth = re.sub('Algorithms', '', pth)
sys.path.append(str(pth))

from Board import *

# X IS MAX (computer) O IS MINS (human)
# we will return score based off of X's position
class MiniMax(Board):
    def _init__(self):
        Board.__init__() #inits game board from Board class
        self.score = 0
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
    def play_minimax(self, depth):
        # since depth 10 is empty board, and 9 is human made first move, depth%2==0 is comp/max and depth%2==1 is human/mins
        if self.is_done() is True: #is there a winner?
            if self.winner == 'X':
                self.score = 10 # computer won!
                return "Computer Won"
            else:
                self.score = -10 # human won...
                return "Human Won"
        if self.is_tie() is True: # theres a tie..
            self.score = 0
            return "Nobody Won"
        return False