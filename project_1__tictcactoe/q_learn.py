import numpy as np
import csv
import random

from os import system, name 
import sys

sys.path.append( str(sys.path[0])+"/player_types" )

from TicTacToe import *
from AlphaBeta import *

q_table = {}
learning_gamma = 0.1
max_games = 1000

