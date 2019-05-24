public class Solution {
    int row, col;
    public void solve(char[][] board) {
        if (board == null || board.length == 0) return;
        row = board.length;
        col = board[0].length;
        UnionFind uf = new UnionFind(row*col+1);
        int dummy = row*col;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (board[i][j] == 'O') {
                    if (i == 0 || i == row-1 || j == 0 || j == col-1) uf.union(node(i, j), dummy);
                    else {
                        if (i > 0 && board[i-1][j] == 'O') uf.union(node(i, j), node(i-1, j));
                        if (i > 0 && board[i+1][j] == 'O') uf.union(node(i, j), node(i+1, j));
                        if (j > 0 && board[i][j-1] == 'O') uf.union(node(i, j), node(i, j-1));
                        if (j > 0 && board[i][j+1] == 'O') uf.union(node(i, j), node(i, j+1));
                    }
                }
            }
        }
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (uf.isConnected(node(i, j), dummy)) board[i][j] = 'O';
                else board[i][j] = 'X';
            }
        }
    }
    public int node(int i, int j) {
        return i*col+j;
    }
}

class UnionFind {
    int[] parents;
    public UnionFind(int n) {
        parents = new int[n];
        for (int i = 0; i < n; i++) parents[i] = i;
    }
    public void union(int n1, int n2) {
        int r1 = find(n1);
        int r2 = find(n2);
        if (r1 != r2) parents[r1] = r2;
    }
    public int find(int node) {
        if (parents[node] == node) return node;
        parents[node] = find(parents[node]);
        return parents[node];
    }    
    public boolean isConnected(int n1, int n2) {
        return find(n1) == find(n2);
    }
}