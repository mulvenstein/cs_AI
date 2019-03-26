from os import system, name 
import Player
import MiniMax

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
            print("player v player!")
            x = Player()
            o = Player()
        elif choice is 2:
            print("Minimax_AI vs Player")
        elif choice is 3:
            print("TY FOR COMING")
            return

#=-----#
main();