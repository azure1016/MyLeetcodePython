class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.rows_ = [[0 for _ in range(9)] for _ in range(9)]
        self.cols_ = [[0 for _ in range(9)] for _ in range(9)]  # can i write cols = rows? maybe i cannot
        self.board_ = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    n = int(board[i][j]) - 1
                    self.rows_[i][n] = 1
                    self.cols_[j][n] = 1
                    self.board_[i // 3 * 3 + j // 3][n] = 1
        self.fill(board, 0, 0)

    def valid(self):
        for constraint in [self.rows_, self.cols_, self.board_]:
            for i in range(9):
                if min(constraint[i]) == 0: return False
        return True

    def fill(self, board, r, c):
        if self.valid(): return True
        n_c = (c + 1) % 9
        n_r = r + 1 if c + 1 >= 9 else r  # new column or stay in the same column
        if board[r][c] != '.':
            return self.fill(board, n_r, n_c)
        for i in range(9):
            if not self.rows_[r][i] and not self.cols_[c][i] and not self.board_[r // 3 * 3 + c // 3][i]:
                board[r][c] = str(i + 1)
                self.board_[r // 3 * 3 + c // 3][i] = 1
                self.rows_[r][i] = 1
                self.cols_[c][i] = 1
                if self.fill(board, n_r, n_c):
                    return True
                else:
                    board[r][c] = '.'
                    self.board_[r // 3 * 3 + c // 3][i] = 0
                    self.rows_[r][i] = 0
                    self.cols_[c][i] = 0
        return False


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
board2 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
sl = Solution()
sl.solveSudoku(board2)
print(board2)