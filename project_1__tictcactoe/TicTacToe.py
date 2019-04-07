from os import system, name
import time

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

'''
    CLASS that defines the board and its behaviour over a tic tac toe game
'''
class TicTacToe:
    '''
    CONSTRUCTOR: defines board to use in tic tac toe games
        constructor makes empty list of 9 _. 
          0 | 1 | 2
          3 | 4 | 5
          6 | 7 | 8
    ''' 
    def __init__(self, x, o):
        self.board = [ '█' for _ in range(9) ] # inits board of 9 '_',
        self.turns_played = 0 #9 max.
        self.winning_moves = ( [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6] )
        self.winner = None
        self.x = x #whoever is x player, real or AI 
        # note : X ALWAYS GOES FIRST
        self.o = o #whoever is x player, real or AI
        self.turn = self.x #current turn

    '''
    returns TRUE if a player has won, or if there is a tie, FALSE otherwise
    self.winner is updated with either 'X' 'O' or 'TIE'
    '''
    def is_game_done(self): 
        if self.num_turns()<5: #impossible to get win without 5 min moves. save some cpu cycles 
            return False
        else:
            for l in self.winning_moves:
                # print("checking " + self.player_at(l[0]) + " AND " + self.player_at(l[1]) + " AND " + self.player_at(l[2]) )
                if (self.player_at(l[0])) == (self.player_at(l[1])) == (self.player_at(l[2])) and (self.player_at(l[0])) !='█' :
                    self.winner = (self.player_at(l[0]))
                    return True
            if self.num_turns() == 9: #no one won and 9 turns made
                self.winner = 'TIE'
                return True
            return False

    '''
    returns how many valid moves have been played
    '''
    def num_turns(self): 
        return int(self.turns_played)

    '''
    given position in board, return 'x', 'o', or '_'
    '''
    def player_at(self, position):
        if position > 9 or position < 0:
            return "INVALID"
        return self.board[position]
    

    '''
    print the contents of da board
    '''
    def display_board(self):
        s=['█' for _ in range(9)]
        for i in range(0,9):
            if self.board[i] == '█':
                s[i] = i
            else:
                s[i] = self.board[i]

        line1 = "  " + str(s[0]) + " | " + str(s[1]) + " | " + str(s[2])
        filler = "-------------"
        line2 = "  " + str(s[3]) + " | " + str(s[4]) + " | " + str(s[5])
        line3 = "  " + str(s[6]) + " | " + str(s[7]) + " | " + str(s[8])
        print(line1)
        print(filler)
        print(line2)
        print(filler)
        print(line3)
        print("\n")

    '''
    actually play the game!
    '''
    def play_ttt(self):
        
        while True:
            clear()
            self.turns_played += 1
            if self.turn is self.x:
                current_player = self.x
                char = 'X'
            else:
                current_player = self.o
                char = 'O'

            if current_player.kind == 'human':
                self.display_board()

            move = current_player.move(self.board) #get move from player, validation is done within the current_players class
            self.board[move] = char # place move

            if self.is_game_done() is True:
                clear()
                self.display_board()
                if self.winner == "TIE":
                    print("THERES A TIE")
                else:
                    clear()
                    self.display_board()
                    print(str(self.winner) + " HAS WON")
                return True

            if self.x.kind != 'human'  and 'human' != self.o.kind  :
                self.display_board()
                time.sleep(1.5)

            if self.turn == self.x:
                self.turn = self.o
            else:
                self.turn = self.x
