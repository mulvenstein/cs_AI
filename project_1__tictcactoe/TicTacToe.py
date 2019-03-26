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
        self.first_move = x

    '''
    returns LIST of empty places on game board
    '''
    def empty_positions(self):
        res = list()
        for x in self.board:
            if x is not 'X' or x is not 'O':
                res.append(x)
        return res

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

    '''
    given move to row,col , is it in the playing area?
    returns TRUE if yes, FALSE otherwise
    '''
    def is_valid_move(self, move):
        if self.board[int(move)] !='X' and self.board[int(move)] !='O':
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
    given player 'x' or 'o' and a move, make it!
    returns TRUE if valid, FALSE otherwise
    '''
    def make_move(self, player, move): 
        if(self.is_valid_move(int(move))):
            self.board[int(move)] = player
            self.turns_played += 1
            return True
        return False

    '''
    print the contents of da board
    '''
    def display_board(self):
        line1 = "  " + self.board[0] + " | " + self.board[1] + " | " + self.board[2]
        line2 = "  " + self.board[3] + " | " + self.board[4] + " | " + self.board[5]
        line3 = "  " + self.board[6] + " | " + self.board[7] + " | " + self.board[8]
        print(line1)
        print(line2)
        print(line3)

    '''
    actually play the game!
    '''
    def play(self):
        return