import sys
import re

pth = str(sys.path[0])
pth = re.sub('Algorithms', '', pth)
sys.path.append(str(pth))

from Board import *

class MiniMax(Board):
    def _init__(self):
        Board.__init__() #inits game board from Board class
