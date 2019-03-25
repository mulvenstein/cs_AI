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
        self.board = [ '_' for _ in range(9) ] # inits board of 9 '_',
        self.turns_played = 0 #9 max.
  
    def is_winner(self, player): # given player 'x' or 'o' determine if thye are a winner
       return False

    def is_tie(self): # returns true if board is full and neither x nor o won
       return False

    def is_board_full(self): # is board full? 
       return False

    def is_valid_move(self, move): # given move to row,col , is it in the playing area? 
       return False

    def num_turns(self): # returns how many turns have been played
       return False

    def player_at(self, place): # given place in board, return 'x', 'o', or '_'
       return False
    
    def make_move(self, player, move): # given player 'x' or 'o' and a move, make it!
       return False

    def display_board(self): # print the contents of da board
       return False