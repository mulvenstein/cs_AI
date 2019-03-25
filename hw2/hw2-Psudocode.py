--
CLASS n_queens:
    FUNCTION __init__(self, N, queen_pos):
         N <- N  # SIZE OF BOARD
         queen_pos <- queen_pos #ARR[i] RETURNS ROW POS OF COL I QUEEN
         nodes_visited <- 0
        # fill queen pos array
        FOR i in range(0,N):
            queen_pos[i] <- (-2*N) #fill array with junk for now
        ENDFOR
    ENDFUNCTION

    FUNCTION checkPositions(self, row, col):
        # given a queen in column 'col' AND in row 'row', is it valid vs the rest of the board
        row_to_check <- row
        diag1_check <- row - col
        diag2_check <- row + col
        # loop thru queen pos array to validate positions
        FOR c in range( 0, len( queen_pos) ):
            IF c = col:
                continue # dont want to validate against self
            ENDIF
            cur_row <-  queen_pos[c]
            cur_diag1 <-  queen_pos[c] - c
            cur_diag2 <-  queen_pos[c] + c
            IF row_to_check = cur_row OR diag1_check = cur_diag1 OR diag2_check = cur_diag2:
                RETURN False
            ENDIF
        ENDFOR
        RETURN True
    ENDFUNCTION

ENDCLASS
--
CLASS backtracking(n_queens):
    FUNCTION __init__(self, N, queen_pos):
        n_queens.__init__(self, N, queen_pos)
    ENDFUNCTION

    FUNCTION backtrack(self, col): # col is current col being checked
         nodes_visited += 1
        IF  self.N=2 OR  self.N=3:
            OUTPUT "NO SOLUTIONS EXIST FOR THE GIVEN N"
            RETURN False 
        ENDIF

        IF  N=col:
            RETURN True #done
        ENDIF
        FOR r in range(0,  N,): #loop over every row trying to get a valid solution for column 'col'
            queen_pos[col] <- r
            IF  checkPositions(r, col) = True: # current board setup is valid
                IF  backtrack(col+1) = True:
                    RETURN True
                ENDIF
            ELSE:
                 queen_pos[col] <- -2* N; #failed, go back to default value
            ENDIF
    ENDFUNCTION

ENDCLASS
--
CLASS forwardtracking(n_queens):
      ENDFOR
    FUNCTION __init__(self, N, queen_pos):
        n_queens.__init__(self, N, queen_pos)
         domains <- dict()
        temp <- [x for x in range(N)]
                  ENDFOR
        for i in range(N):
            random.shuffle(temp)
             domains[i]=set(temp[:]) # domains is a dict int->set, where set is valid rows left AND int is what queen
    ENDFUNCTION

        ENDFOR
    FUNCTION domain_wipeout(self, old_domains, row, col):
        #1. eliminate rows
        #2. eliminate r-c, diag1
        #3. eliminate r+c, diag2
        # old_domains is a copy of current stacks current domains
        #1. rows
        for i in range( N):
            IF i==col:
                continue
            ENDIF
            old_domains[i] <- (old_domains[i]).difference({row})
                                               ENDIF
        #2. diag1, row-col
        ENDFOR
        dif <- row - col
         ENDIF
        for i in range( N):
            IF i==col:
                continue
            ENDIF
            old_domains[i] <- (old_domains[i]).difference({i+dif})
                                               ENDIF
        #3. diag2, row+col
        ENDFOR
        add <- row + col
        for i in range( N):
            IF i==col:
                continue
            ENDIF
            old_domains[i] <- (old_domains[i]).difference({add-i})
                                               ENDIF
        ENDFOR
        RETURN old_domains
    ENDFUNCTION

    FUNCTION forwardtrack(self,col, domains): 
        # invalid game size 2 OR 3.
        IF   N = 2 OR  N = 3:
            RETURN False
        # IF N = col, N queens finished
        ENDIF
        IF  N = col:
            RETURN True
        # IF curent columns domain size is zero, backtrack
        ENDIF
        IF len(domains[col])==0:
            RETURN False
        # while there is still a row to try in current domain
        ENDIF
        WHILE length of (domains[col]) > 0 :
            r <- (domains[col]).pop() # top of set, and pops it off
            queen_pos[col] <- r
            IF  current board setup is ok:
                # domain wipeout!
                new_domains <-  domain_wipeout(board setup)
                IF a queen domain size == 0 :
                    break
                ENDIF
                IF  forwardtrack(col+1, new_domains) = True:
                        ENDFOR
                    RETURN True
                ENDIF
            ELSE: 
                queen_pos[col] <- -2* N
            ENDIF
    ENDFUNCTION

ENDCLASS

        ENDWHILE
FUNCTION main():
    OUTPUT "n_queens mulvey\n"
    n <- int(input("ENTER size of board ? : "))
    OUTPUT "\n====!!BACKTRACKING!!===="
    start_time <- time.time()
    a <- backtracking(n, [])
    a.backtrack(0)
    end_time <- time.time() - start_time
    OUTPUT "BACKTRACKING took " + str(end_time) + "secs to run (AND print) with " + str(a.nodes_visited) + " nodes visited"
    OUTPUT "\n\n====!!FORWARD-CHECING!!===="
    start_time <- time.time()
    b <- forwardtracking(n, [])
        ENDFOR
    b.forwardtrack(0, b.domains)
      ENDFOR
    end_time <- time.time() - start_time
    OUTPUT "FORWARDCHECKING took " + str(end_time) + "secs to run (AND print) with " + str(b.nodes_visited) + " nodes visited"
    RETURN
#-----#
ENDFUNCTION

main(
