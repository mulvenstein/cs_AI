import time
from random import *
import queue
from collections import Counter

class n_queens:
    def __init__(self, N, queen_pos):
        self.N = N  # SIZE OF BOARD
        self.queen_pos = queen_pos #ARR[i] RETURNS ROW POS OF COL I QUEEN
        self.nodes_visited = 0

        # fill queen pos array
        for i in range(0,N):
            queen_pos.append(-2*N) #fill array with junk for now

    
    def checkPositions(self, row, col):
        # given a queen in column 'col' and in row 'row', is it valid vs the rest of the board
        row_to_check = row
        diag1_check = row - col
        diag2_check = row + col

        # loop thru queen pos array to validate positions
        for c in range(0, len(self.queen_pos) ):
            if c == col:
                continue #dont want to validate against self
            cur_row = self.queen_pos[c]
            cur_diag1 = self.queen_pos[c] - c
            cur_diag2 = self.queen_pos[c] + c

            if row_to_check == cur_row or diag1_check == cur_diag1 or diag2_check == cur_diag2:
                return False

        return True

    def print_sol(self):
        res = [ [0] * self.N for _ in range(self.N) ]
        for i in range(0, self.N):
            res[i][self.queen_pos[i]] = self.queen_pos[i]+1
        for j in range(0, self.N):
            s = ""
            for k in range(0, self.N):
                if res[j][k] == 0:
                    s += "- " #print("- ")
                else:
                    s+= str(res[j][k]) + " " #print(str(res[j][k]) + " ")
            print(s)
        return

class backtracking(n_queens):
    def __init__(self, N, queen_pos):
        n_queens.__init__(self, N, queen_pos)
    
    def backtrack(self, col): # col is current col being checked
        self.nodes_visited += 1
        if self.N==2 or self.N==3:
            print("NO SOLUTIONS EXIST FOR THE GIVEN N")
            return False #no sols. exist for n=2 or 3
        if self.N==col:
            self.print_sol()
            return True #done
        
        for r in range(0, self.N,): #loop over every row trying to get a valid solution for column 'col'
            self.queen_pos[col] = r
            if self.checkPositions(r, col) == True:
                if self.backtrack(col+1) == True:
                    return True
            else:
                self.queen_pos[col] = -2*self.N; #failed, go back to def value


class forwardtracking(n_queens):
    def __init__(self, N, queen_pos):
        n_queens.__init__(self, N, queen_pos)
        self.domains = dict()
        for i in range(N):
            temp = domain_values(N,i)
            self.domains[i]=temp.domain

    def domain_wipeout(self, old_domains, row, col):
        #1. eliminate rows
        #2. eliminate r-c, diag1
        #3. eliminate r+c, diag2

        # old_domains is a copy of current stacks current domains

        #1. rows
        for i in range(self.N):
            if i==col:
                continue
            old_domains[i] = (old_domains[i]).difference({row})

        #2. diag1, row-col
        dif = row - col
        for i in range(self.N):
            if i==col:
                continue
            old_domains[i] = (old_domains[i]).difference({i+dif})
        
        #3. diag2, row+col
        add = row + col
        for i in range(self.N):
            if i==col:
                continue
            old_domains[i] = (old_domains[i]).difference({add-i})

        return old_domains


    def forwardcheck(self,col, domains): #pretty much same as back track, domains will be copy of previous stack's domains
        self.nodes_visited += 1
        # invalid game size 2 or 3.
        if  self.N == 2 or self.N == 3:
            return False
        # if N == col, N queens finished
        if self.N == col:
            self.print_sol()
            return True
        # if curent columns domain size is zero, backtrack
        if len(domains[col])==0:
            return False
        
        # while there is still a row to try in current domain
        while (domains[col]).__len__() >0 :
            r = (domains[col]).pop()
            # assume current row is good
            self.queen_pos[col] = r
            # if valid
            if self.checkPositions(r, col) == True:
                # domain wipeout!
                temp = domains.copy()
                new_domains = self.domain_wipeout(temp, r, col )
                # if any of the domains are 0, kill stack
                valid = True
                for i in range(col+1,self.N):
                    if new_domains[i].__len__() == 0 :
                        valid = False
                if not valid:
                    break
                # print("CUR COL : " + str(col))
                if self.forwardcheck(col+1, new_domains) == True:
                    return True
            else: 
                self.queen_pos[col] = -2*self.N

class HillClimb:
    def __init__(self, N):
        self.N = N #nxN board
        
    def initial_state(self): #randomly creates board setup
        return list( randrange(self.N) for i in range(self.N) )

    def goal_state(self, current_state): #is current state a valid one?
        c1, c2, c3 =  ( set() for i in range(3) ) #checks for col, diag1 and diag2
        for row, col in enumerate(current_state):
            if col in c1 or row - col in c2 or row + col in c3:
                return False
            c1.add(col)
            c2.add(row - col)
            c3.add(row + col)
        return True

    def h(self, current_state): #h(n), heuristic for # of queens being attacked
        c1, c2, c3 = [Counter() for i in range(3)] # counts for row, diag1, and diag2 being attacked
        for row,col in enumerate(current_state):
            c1[row] = c1[row] + 1
            c2[row - col] = c2[row - col] + 1
            c3[row + col] = c3[row + col] + 1

        collisions = 0
        for c in [c1, c2, c3]:
            for k in c:
                collisions += c[k] * (c[k]-1)/2 #Counter[x] gives number of counts of key X. This will give us total collisions, not incuding colision vs self
        return -collisions 
    
    def children(self, current_state):
        children = []
        for r in range(self.N):
            for c in range(self.N):
                if c != current_state[r]: #if no queen exists for a certain col, append to a list of queens
                    temp = list(current_state)
                    temp[r] = c
                    children.append(list(temp))

        return children

def h_c(state):
    current = state.initial_state()
    while True:
        children = state.children(current)
        if not children: #no where else to go !
            break
        # get worst child
        child = max(children, key=lambda st: state.h(st))
        if state.h(child) <= state.h(current):
            break    
        current = child
    return current

def main():
    print("n_queens mulvey\n")
    n = int(input("ENTER size of board ? : "))
    # print("\n====!!BACKTRACKING!!====")
    # start_time = time.time()
    # a = backtracking(n, [])
    # a.backtrack(0)
    # end_time = time.time() - start_time
    # print("BACKTRACKING took " + str(end_time) + "secs to run (and print) with " + str(a.nodes_visited) + " nodes visited")
    # print("\n\n====!!FORWARD-CHECING!!====")
    # start_time = time.time()
    # b = forwardtracking(n, [])
    # b.forwardcheck(0, b.domains)
    # end_time = time.time() - start_time
    # print("FORWARDCHECKING took " + str(end_time) + "secs to run (and print) with " + str(b.nodes_visited) + " nodes visited")
    d = HillClimb(n)
    ans = h_c(d)
    print(ans)
    return

#-----#
main()