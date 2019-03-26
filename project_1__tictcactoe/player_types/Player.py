class Player(object):
    def __init__(self):
        self.type = 'human'

    def move(self, board):
        return int(input('Your move? '))

    def available_moves(self, board):
        return [i + 1 for i in range(0, 9) if board[i] == ' ']