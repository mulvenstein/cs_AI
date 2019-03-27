from os import system, name 
import sys

sys.path.append( str(sys.path[0])+"/player_types" )

from Player import *
from MiniMax import *
from TicTacToe import *

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def main():
    while True:
        # s = "\n" * 100
        # print(s)    
        clear()  
        print("!===MULVEY TIC TAC TOE===!")
        print("  1. PvP")
        print("  2. Minimax vs Player")
        print("  3. Exit")
        
        choice = int(input("  >> "))
        if choice is 1:
            clear()
            print("==!PLAYER vs PLAYER!==\n")
            p1 = Player('X')
            p2 = Player('O')
            game = TicTacToe(p1, p2)
            game.play_ttt()
            print("\n...press enter to continue.")
            a = input()
        elif choice is 2:
            clear()
            print("==!MINIMAX vs PLAYER!==\n")
            p1 = MiniMax('X')
            p2 = Player('O')
            game = TicTacToe(p1, p2)
            game.play_ttt()
            print("\n...press enter to continue.")
            a = input()
        elif choice is 3:
            print("TY FOR COMING")
            return

#=-----#
main();