import time
import numpy as np

def isValidBoard(board, row, col):
    valid = True

    # check rows
    for c in range(len(board)):
        if board[row, c] == 1:
            valid = False

    # check diag1
    r = row
    c = col
    while c >= 0 and r >= 0:
        if board[r, c] == 1:
            valid =  False
        c -= 1
        r -= 1

    # chcek diag2
    r = row
    c = col
    while c >= 0 and r < len(board):
        if board[r, c] == 1:
            valid =  False
        r += 1
        c -= 1

    return valid


def getRows(board, queen):
    rows = []
    for row in range(len(board)):
        if isValidBoard(board, row, queen):
            rows.append(row)
    return rows

def getDomain(board, queen):
    domain = []
    for r in range(len(board)):
        for c in range(queen+1, len(board)):
            if board[r, c] == 0 and isValidBoard(board, r, c):
                domain.append([r,c])
    return domain


def check(board, row, col):
    rows = getRows(board, col)
    temp = list(rows)

    for r in rows:
        if not isValidBoard(board, r, col):
            temp.remove(r)

    return len(temp)==0


def forwardChecking(board, queen): #forward checking given board and queen/col
    if len(board) == queen: #finished last queen, done.
        print(board)
        return True
    if len(board) == 2 or len(board) == 3:
        print("sol. not possible.")
        return False

    valid_rows = getRows(board, queen)
    for row in valid_rows:
        board[row, queen] = 1

        domain_wipeout = False
        for values in getDomain(board, queen): 
            if check(board, values[0], values[1]):
                domain_wipeout = True
                break
        
        if domain_wipeout == False:
            if forwardChecking(board, queen +1):
                return True
        board[row, queen] = 0


    return False


def main():
    N = int(input("Enter size of board : "))
    board = np.array(np.zeros(shape = (N,N), dtype=int))
    start_time = time.time()
    print(forwardChecking(board, 0))
    end_time = time.time() - start_time
    print("  4wardtracking took " + str(end_time) + "secs to run and print")
    return
#------#

main()