from os import system, name 
import sys

sys.path.append( str(sys.path[0])+"/player_types" )

from Player import *
from MiniMax import *
from TicTacToe import *
from AlphaBeta import *
from QLearnBot import *

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
        print("  3. Watch Minimax vs Minimax")
        print("  4. AB vs Human")
        print("  5. WATCH AB vs MiniMax")
        print("  6. WATCH AB vs AB")
        print("  7. Player vs QLEARN")
        print("  8. Exit")

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
            del p1
            del p2
            print("\n...press enter to continue.")
            a = input()
        elif choice is 3:
            clear()
            print("==!MINIMAX vs MiniMax!==\n")
            p1 = MiniMax('X')
            p2 = MiniMax('O')
            game = TicTacToe(p1, p2)
            game.play_ttt()
            del p1
            del p2
            print("\n...press enter to continue.")
            a = input()
        elif choice is 4:
            clear()
            print("==!ALPHABETA vs HUMAN!==\n")
            p1 = AlphaBeta('X')
            p2 = Player('O')
            game = TicTacToe(p1, p2)
            game.play_ttt()
            del p1
            del p2
            print("\n...press enter to continue.")
            a = input()
        elif choice is 5:
            clear()
            print("==!WATCH ALPHABETA vs MiniMax!==\n")
            p1 = MiniMax('X')
            p2 = AlphaBeta('O')
            game = TicTacToe(p1, p2)
            game.play_ttt()
            del p1
            del p2
            print("\n...press enter to continue.")
            a = input()
        elif choice is 6:
            clear()
            print("==!WATCH ALPHABETA vs ALPHABETA!==\n")
            p1 = AlphaBeta('X')
            p2 = AlphaBeta('O')
            game = TicTacToe(p1, p2)
            game.play_ttt()
            del p1
            del p2
            print("\n...press enter to continue.")
            a = input()
        elif choice is 7:
            clear()
            print("==!PLAYER vs QLEARN!==\n")
            p2 = Player('X')
            p1 = QLearnBot('O')
            game = TicTacToe(p1, p2)
            game.play_ttt()
            del p1
            del p2
            print("\n...press enter to continue.")
            a = input()
        elif choice is 8:
            print("TY FOR COMING")
            return

#=-----#
main();