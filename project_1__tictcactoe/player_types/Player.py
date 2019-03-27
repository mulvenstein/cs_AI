class Player(object):
    def __init__(self, char='X'):
        self.type = 'human'
        self.char = char

    def move(self, board):
        while True: #valid move
            move = int(input('Your move? '))
            if board[move] != "X" and board[move] != "O" and move >= 0 and move <= 9:
                return move

    def available_positions(self, board):
        return [i for i in range(0, 9) if board[i] == '█']