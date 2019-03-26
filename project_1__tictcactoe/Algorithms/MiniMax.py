import sys
import re

pth = str(sys.path[0])
pth = re.sub('Algorithms', '', pth)
sys.path.append(str(pth))

from Board import *

# X IS MAX O IS MINS
class MiniMax(Board):
    def _init__(self):
        Board.__init__() #inits game board from Board class

    # need to add acutal algorithm!
    
    '''
    finds best move given a board.
    returns TRUE if valid, FALSE otherwise
    '''
    def find_best_move(self): #uses self.board!
        return True
