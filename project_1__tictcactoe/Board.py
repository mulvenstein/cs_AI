class Board:
    '''
    CLASS that defines the board and its behaviour over a tic tac toe game
    '''

    '''
    CONSTRUCTOR: defines board to use in tic tac toe games
        constructor makes empty list of 9 _. 
          0 | 1 | 2
          3 | 4 | 5
          6 | 7 | 8
    ''' 
    def __init__(self):
        self.board = [ '█' for _ in range(9) ] # inits board of 9 '_',
        self.turns_played = 0 #9 max.
        self.winning_moves = ( [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6] )
        self.winner = None

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
    given player 'x' or 'o' determine if thye are a winner
    returns TRUE if player won, FALSE otherwise
    '''
    def is_winner(self, player): 
        if self.num_turns()<5 or player!='X' and player !='O': 
            # print("HERE")
            return False
        else:
            for l in self.winning_moves:
                # print("checking " + self.player_at(l[0]) + " AND " + self.player_at(l[1]) + " AND " + self.player_at(l[2]) )
                if (self.player_at(l[0])) == (self.player_at(l[1])) == (self.player_at(l[2])) and (self.player_at(l[0])) !='█' :
                    self.winner = (self.player_at(l[0]))
                    return True
            return False

    '''
    given current state, has anyone won??
    '''
    def is_done(self): 
        if self.num_turns()<5: 
            return False
        else:
            for l in self.winning_moves:
                # print("checking " + self.player_at(l[0]) + " AND " + self.player_at(l[1]) + " AND " + self.player_at(l[2]) )
                if (self.player_at(l[0])) == (self.player_at(l[1])) == (self.player_at(l[2])) and (self.player_at(l[0])) !='█' :
                    self.winner = (self.player_at(l[0]))
                    return True
            return False

    '''
    returns TRUE if board is full and neither player has won
    '''
    def is_tie(self):
        if (self.num_turns()) != 9: #not enough movesfor tie
            return False
        if (self.is_winner('X') is False and self.is_winner('Y') is False):
            return True
        return False

    '''
    returns TRUE if board is full (9 valid turns)
    '''
    def is_board_full(self):  
        count = 0
        for char in self.board :
            if char == 'X' or char == 'O':
                count += 1
        return count==9

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