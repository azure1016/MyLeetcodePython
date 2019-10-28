import java.util.*;

public class go_game_java {
    private int[][] directions = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };

    public int maxCapture(char[][] board, int r, int c) {
        if (board == null || board.length == 0 || isOutOfBounds(board, r, c) || board[r][c] != 'e')
            return 0;
        int m = board.length, n = board[0].length;

        boolean[][] visited = new boolean[m][n];
        visited[r][c] = true;

        int count = 0;
        for (int[] dir : directions) {
            count += bfs(board, visited, r + dir[0], c + dir[1]);
        }
        return count;
    }

    private int bfs(char[][] board, boolean visited[][], int r, int c) {
        int count = 0;
        boolean valid = true;
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[] { r, c });
        while (!queue.isEmpty()) {
            int[] loc = queue.poll();
            int x = loc[0], y = loc[1];
            if (isOutOfBounds(board, x, y) || visited[x][y] || board[x][y] == 'b')
                continue;
            if (board[x][y] == 'e') {
                //valid = false;
                return 0;
            } else {
                visited[x][y] = true;
                for (int[] dir : directions) {
                    queue.offer(new int[] { x + dir[0], y + dir[1] });
                }
                count++;
            }
        }
        //return valid ? count : 0;
        return count;
    }

    private boolean isOutOfBounds(char[][] board, int x, int y) {
        return x < 0 || y < 0 || x > board.length - 1 || y > board[0].length - 1;
    }
// }
// class Main {
    public static void main(String[] args) {
        // expected: 1
        char[][] grid = new char[4][];
        grid[0] = new char[]{'e', 'e', 'e', 'e', 'b', 'b', 'b'};
        grid[1] = new char[]{'e', 'e', 'e', 'e', 'b', 'w', 'b'};
        grid[2] = new char[]{'e', 'e', 'e', 'e', 'b', 'e', 'b'};
        grid[3] = new char[]{'e', 'e', 'e', 'e', 'e', 'e', 'e'};
        go_game_java sol = new go_game_java();
        int res = sol.maxCapture(grid, 2,5);
        System.out.println(res);
        // expected: 2
        char[][] grid2 = new char[4][];
        grid2[0] = new char[] { 'e', 'e', 'e', 'e', 'b', 'b', 'b' };
        grid2[1] = new char[] { 'e', 'e', 'e', 'b', 'w', 'w', 'b' };
        grid2[2] = new char[] { 'e', 'e', 'e', 'e', 'b', 'e', 'b' };
        grid2[3] = new char[] { 'e', 'e', 'e', 'e', 'e', 'e', 'e' };
        System.out.println(sol.maxCapture(grid2, 2, 5));
        // expected: 0
        char[][] grid3 = new char[4][];
        grid3[0] = new char[] { 'e', 'e', 'e', 'e', 'b', 'b', 'b' };
        grid3[1] = new char[] { 'e', 'e', 'e', 'e', 'w', 'w', 'b' };
        grid3[2] = new char[] { 'e', 'e', 'e', 'e', 'b', 'e', 'b' };
        grid3[3] = new char[] { 'e', 'e', 'e', 'e', 'e', 'e', 'e' };
        System.out.println(sol.maxCapture(grid3, 2, 5));
        // expected: 0
        char[][] grid4 = new char[4][];
        grid4[0] = new char[] { 'e', 'e', 'b', 'b', 'b', 'b', 'b' };
        grid4[1] = new char[] { 'e', 'e', 'b', 'w', 'e', 'w', 'b' };
        grid4[2] = new char[] { 'e', 'e', 'b', 'b', 'b', 'e', 'b' };
        grid4[3] = new char[] { 'e', 'e', 'e', 'e', 'e', 'e', 'e' };
        System.out.println(sol.maxCapture(grid4, 2, 5));
        // expected: 8
        char[][] grid5 = new char[3][];
        grid5[0] = new char[] {  'w', 'w', 'w' };
        grid5[1] = new char[] {  'w', 'e', 'w' };
        grid5[2] = new char[] {  'w', 'w', 'w' };
        System.out.println(sol.maxCapture(grid5, 1, 1));
        // expected: 0
        char[][] grid6 = new char[4][];
        grid6[0] = new char[] {'e', 'b', 'b', 'b', 'b', 'b', 'b'};
        grid6[1] = new char[] {'b', 'w', 'e', 'w', 'w', 'w', 'b'};
        grid6[2] = new char[] {'b', 'w', 'w', 'w', 'w', 'e', 'b'};
        grid6[3] = new char[] {'e', 'b', 'b', 'b', 'b', 'e', 'e'};
        System.out.println(sol.maxCapture(grid6, 2, 5));
        // expected: 1
        char[][] grid7 = new char[3][];
        grid7[0] = new char[]{'w', 'w', 'w'};
        grid7[1] = new char[]{'w', 'e', 'b'};
        grid7[2] = new char[]{'w', 'e', 'w'};
        System.out.println(sol.maxCapture(grid7, 2, 1));

        // expected: 0
        char[][] grid8 = new char[4][];
        grid8[0] = new char[] { 'e', 'e', 'e', 'e', 'b', 'b', 'b' };
        grid8[1] = new char[] { 'e', 'e', 'e', 'e', 'b', 'w', 'b' };
        grid8[2] = new char[] { 'e', 'e', 'e', 'e', 'b', 'b', 'b' };
        grid8[3] = new char[] { 'e', 'e', 'e', 'e', 'e', 'e', 'e' };
        int res8 = sol.maxCapture(grid, 3, 5);
        System.out.println(res8);
    }
}