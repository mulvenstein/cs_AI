from queue import *
from random import *

class NQueens:
    def __init__(self, N):
        '''
            N <- SIZE OF BOARD
            queen_positions <- where queen[col] is placed, 0-N is valid
        '''
        self.N = N
        self.queen_positions = [ -2*N for _ in range(N) ]
        return

    def is_valid_state(self):
        '''
            row_check makes sure no queen is on the same row
            diag1_check makes sure no queens are on same lower diag, row+col
            diag2_check makes sure no queens are on same upper diag, row-col
        
            valid move = 0
            invalid = -1
            game done = 1
        '''
        row_check = set()
        diag1_check = set()
        diag2_check = set()

        q_placed = 0

        # check rows
        for col in range(self.N):
            row = self.queen_positions[col]
            if row != -2*self.N:
                q_placed += 1
                row_check.add(row)
                diag1_check.add(row+col)
                diag2_check.add(row-col)
        
        # check if valid move and if  game won
        if ( row_check.__len__() == diag1_check.__len__() == diag2_check.__len__() == q_placed ) :
            if q_placed == self.N :
                return 1
            else:
                return 0
        
        return -1

    def print_sol(self):
        res = [ [0] * self.N for _ in range(self.N) ]
        for i in range(0, self.N):
            res[i][self.queen_positions[i]] = self.queen_positions[i]+1
        for j in range(0, self.N):
            s = ""
            for k in range(0, self.N):
                if res[j][k] == 0:
                    s += "- " #print("- ")
                else:
                    s+= str(res[j][k]) + " " #print(str(res[j][k]) + " ")
            print(s)
        return

class Backtracking(NQueens):
    def __init__(self, N):
        NQueens.__init__(self, N)
        # our queen pos variable will be initial state for backtracking
    def play(self, col):
        if self.N==2 or self.N==3:
            print("no sol exists for given N")
        if self.N == col:
            self.print_sol()
            return True
        
        for r in range(self.N,): #loop over every row trying to get a valid solution for column 'col'
            self.queen_positions[col] = r
            if ( self.is_valid_state() == 0 or self.is_valid_state() == 1 ):
                if self.play(col+1) == True:
                    return True
            else:
                self.queen_positions[col] = -2*self.N; #failed, go back to def value

class ForwardChecking(NQueens):
    def __init__(self, N):
        NQueens.__init__(self, N)
        # set initial state, queen_positions, to random spots on the board
        temp = [ x for x in range(N) ]
        shuffle(temp)
        self.queen_positions = temp[:] # queen positions are random, unique rows
        self.init_domain = dict()
        for i in range(N):
            self.init_domain[i] = set( [ x for x in range(N) ] )
        print("QUEEN POS " + str(self.queen_positions))

    def domain_wipeout(self, col,old_domains):
        #1. eliminate rows
        #2. eliminate r-c, diag1
        #3. eliminate r+c, diag2

        for c,r in enumerate(self.queen_positions): # for every [col, row] ...
            dif = r - c
            add = r + c
            sub = set()
            sub.add(r) # elim rows
            sub.add(dif+c) # elim diag1
            sub.add(add-c) # elim diag2
            for i in range(self.N): #loop over every domain and get rid 
                if i == c:
                    continue 
                

                print("NEW DOMAINS===" + str(old_domains))

        return old_domains


    def play(self, domains):
        '''
            look at self.queens_positions
            is valid? else
              generate domains - threatened
              pick largest 
              repeat 
              game is done when threatening_domains = 0
        ''' 
        if self.is_valid_state() == 1:
            self.print_sol()
            return True  

        print("DOMAINS===" + str(domains))

        new_domains = domains.copy()
        new_domains = self.domain_wipeout(new_domains)

        if(new_domains == "BAD"):
            return False #current q pos is threatened. break stack!
        # since the above if didnt happen, board isnt valid. take largest domain and use that queen
        queen = 0
        for i in range(self.N):
            if queen < (new_domains[i]).__len__() :
                queen = i
        # use this queen!
        while len(new_domains[queen]) > 0:
            # try queen at row domain[queen].get()
            self.queen_positions[queen] = new_domains[queen].pop()
            if self.play(new_domains) == True:
                return True
            

        return False


def main():
    n = int(input("enter N : "))
    print("\nbacktrk----------")
    backtrack = Backtracking(n)
    backtrack.play(0)
    print("\n4ward----------")
    forward = ForwardChecking(n)
    forward.play(forward.init_domain)
    return

#---#
main()