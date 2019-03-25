// author : tom mulvey

import java.util.*;

public class N_Queens {
    /*
        @@@ given a number, N, place N queens on a NXN chess board such that they wont attack eachother.
            a) Implement the backtracking algorithm to solve the n-queens problem.
            b) Add forward checking to the backtracking algorithm. Compare backtracking alone versus backtracking with forward checking for an increasing number of queens. 
            Turn in: Cover page, pseudo-code of your algorithm, code, sample outputs, comparison results, conclusion. 
    
        variables: Queen_0 -> Queen_N-1
        domain: rows 0->N-1
        constraints: chess rules. 
            (queen 0 is in the first col, q1 in second, etc)
    */

    public int N; // board size and number of queens
    public int[] queen_positions; //index 0 contains queen0(col)'s row.

    // DEFAULT CONSTRUCTOR
    public N_Queens(){
        // init size N
        Scanner sc = new Scanner(System.in);
        System.out.print("Please enter N: ");
        this.N = sc.nextInt();
        //close sc
        sc.close();
        String x = "---" + this.N + " Queens!---";
        System.out.println(x);

        // explicitly set array to all zeros
        this.queen_positions = new int[this.N];
        Arrays.fill(this.queen_positions, -2*this.N);//if we fill arrays with 0 then it will fail on checking col zero pos zero

        // FOR FORWARD CHECKING WE NEED DOMAINS
        // we will have an map of sets. q_domain[0] will give us the domain of first queen.
        // HashMap<Integer, HashSet<Integer>> q_domains = new HashMap<Integer, HashSet<Integer>>();
        // // fill hashmap with copies of domains
        // HashSet<Integer> set1 = new HashSet<Integer>();
        // for( int i=0; i<this.N; i++){
        //     set1.add(i);
        // }
        // HashSet<Integer> Clone = new HashSet<Integer>()
        // q_domains.put( 0, (HashSet)set1.clone() );
        // // Set<Integer> set2 = set1.stream().map(Integer::new).collect(Collectors.toSet());
    }

    // constructor with intended size
    public N_Queens(int size){
        this.N = size;
        // explicitly fill arr with all zeros
        this.queen_positions = new int[size];
        Arrays.fill(this.queen_positions, -2*this.N);//if we fill arrays with 0 then it will fail on checking col zero pos zero
    }

    public void print_sol() {
        int[][] res = new int[this.N][this.N];
        for (int i = 0; i < this.N; i++) {
            res[i][this.queen_positions[i]] = this.queen_positions[i]+1;
        }
        for (int i = 0; i < this.N; i++) {
            for (int j = 0; j < this.N; j++) {
                if (res[i][j] == 0){
                    System.out.print("-" + " ");
                } else {
                    System.out.print(res[i][j] + " ");
                }
            }
            System.out.println();
        }
        System.out.println("\n");
    }

    public boolean checkPositions(int col, int r){ //=O(N)
        // int col is current column, r is the row we are trying to place on
        // since each index/col of queen arrary is different, we only need to check rows and diagonals
        /* diag 1:
             0 1 2 3
           0   -
           1     Q
           2       -
           3  
             Queen row-col = -1. Thus any other queens row - col cannot = -1. The other diag is adding row+col.
             Also need to make sure no other queen as the same row value. For all i,j in arr, i!=j
           */

        int row_check = r;
        int diag1_check = r - col;
        int diag2_check = col + r;

        for (int i=0; i<this.N; i++) { // loop thru queens pos array to find errors shown above
            // we are given current column, check queens_position[col] vs all other entries
            if(i == col)
                continue;
            
            int i_row = this.queen_positions[i]; 
            int i_diag1 = this.queen_positions[i] - i;
            int i_diag2 = i + this.queen_positions[i];

            if( row_check == i_row || diag1_check == i_diag1 || diag2_check == i_diag2 ){
                return false;
            }
        }

        // we made it! very nice! 
        return true;
    }

    public boolean backtracking(int n, int col){
    // col is current column being tested in backtracking.
    // IMPLEMENTATION OF BACKTRACKING ALGORITHM
        if( n==2 || n==3 ){
            return false; // no solution exists for cases n=2 or n=3
        }
        if( col == n){
            return true;
        }

        for( int r=0; r<n; r++ ){ //loop over every row trying to get a valid solution for column col
            this.queen_positions[col] = r;
            //System.out.println("Checking queen" + col + " at row " + r);
            if( checkPositions(col, r) ){
                //System.out.println("!!!!queen" + col + " at pos " + r + " TRUEE!!!!");
                if( backtracking(n, col+1 ) )
                    return true;       
            } else {
                this.queen_positions[col] = -2*this.N; //failed, go back to def value
            }
        }

        return false;
    }


    public boolean forward_checking(int n, int col, int[][] domains){
        if( n==2 || n==3 ){
            return false; // no solution exists for cases n=2 or n=3
        }
        if( col == n){
            return true;
        }

        // 1. check ALL domain sizes.
        // 2. find value
        // 3. Copy domains, domain wipeout the copies
        // 4. go to next queen


        return false;
    }


    public static void main(String[] args) {
        N_Queens game = new N_Queens();
        System.out.println(game.N + "Queens solution: " + game.backtracking(game.N, 0));
        game.print_sol();
        
        System.out.println(Arrays.toString(game.queen_positions));
    }
}