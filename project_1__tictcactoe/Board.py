class board:
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

    '''
    given player 'x' or 'o' determine if thye are a winner
    returns TRUE if player won, FALSE otherwise
    '''
    def is_winner(self, player): 
        return False

    '''
    returns TRUE if board is full and neither player has won
    '''
    def is_tie(self):
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
        return False

    '''
    returns how many valid moves have been played
    '''
    def num_turns(self): 
        return self.num_turns

    '''
    given position in board, return 'x', 'o', or '_'
    '''
    def player_at(self, position):
        return self.board[position]
    
    '''
    given player 'x' or 'o' and a move, make it!
    returns TRUE if valid, FALSE otherwise
    '''
    def make_move(self, player, move): 
        if(is_valid_move(move)):
            self.board[move] = player
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