import time
import random

class n_queens:
    def __init__(self, N, queen_pos):
        self.N = N  # SIZE OF BOARD
        self.queen_pos = queen_pos #ARR[i] RETURNS ROW POS OF COL I QUEEN
        self.nodes_visited = 0

        # fill queen pos array
        for i in range(0,N):
            queen_pos.append(-2*N) #fill array with junk for now

    def is_goal(self):
        row_check = set()
        diag1 = set()
        diag2 = set()
        
        # row _check
        for i in range(self.N):
            row_check.add(self.queen_pos[i])

        # d1 check
        for r,c in enumerate(self.queen_pos):
            diag1.add(r-c)
            diag2.add(r+c)
        return len(row_check) == len(diag1) == len(diag1) == self.N        
    
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
            if self.is_goal() == True:
                if self.backtrack(col+1) == True:
                    return True
            else:
                self.queen_pos[col] = -2*self.N; #failed, go back to def value


class forwardtracking(n_queens):
    def __init__(self, N, queen_pos):
        n_queens.__init__(self, N, queen_pos)
        self.domains = dict()
        temp = [x for x in range(N)]
        for i in range(N):
            random.shuffle(temp)
            self.domains[i]=set(temp[:]) # domains is a dict int->set, where set is valid rows left and int is what queen

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


    
            


def main():
    print("n_queens mulvey\n")
    n = int(input("ENTER size of board ? : "))
    print("\n====!!BACKTRACKING!!====")
    start_time = time.time()
    a = backtracking(n, [])
    a.backtrack(0)
    end_time = time.time() - start_time
    print("BACKTRACKING took " + str(end_time) + "secs to run (and print) with " + str(a.nodes_visited) + " nodes visited")
    # print("\n\n====!!FORWARD-CHECING!!====")
    # start_time = time.time()
    # b = forwardtracking(n, [])
    # b.forwardcheck(0, b.domains)
    # end_time = time.time() - start_time
    # print("FORWARDCHECKING took " + str(end_time) + "secs to run (and print) with " + str(b.nodes_visited) + " nodes visited")
    return

#-----#
main()