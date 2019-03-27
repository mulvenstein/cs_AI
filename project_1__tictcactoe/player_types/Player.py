class Player(object):
    def __init__(self):
        self.type = 'human'

    def move(self, board):
        while True: #valid move
            move = int(input('Your move? '))
            if board[move] != "X" and board[move] != "O" and move >= 0 and move <= 9:
                return move

    def available_moves(self, board):
        return [i + 1 for i in range(0, 9) if board[i] == '█']