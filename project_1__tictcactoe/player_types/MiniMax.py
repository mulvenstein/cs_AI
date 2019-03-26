import sys
import re

pth = str(sys.path[0])
pth = re.sub('player_types', '', pth)
sys.path.append(str(pth))

from Player import *

# X IS MAX (computer) O IS MINS (human)
# we will return score based off of X's position
class MiniMax(Player):
    def _init__(self):
        self.type = 'MiniMax'


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
    def play_minimax(self, board ):
        return False