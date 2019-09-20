class Solution:
    def solveNQueens(self, n):
        result = []
        mask = (1 << n) - 1

        def dfs(row, col, pie, na, board):
            if row == n:
                one_board = [self.bit_to_string(row, n) for row in board]
                result.append(one_board)
                return
            bits = ~(col | pie | na) & mask
            while bits:
                p = bits & -bits  # get the last set bit
                dfs(row + 1, col | p, (pie | p) << 1, (na | p) >> 1, board + [p])
                bits &= bits - 1  # unset the last set bit

        board = []
        dfs(0, 0, 0, 0, board)
        return result

    def bit_to_string(self, bits, n):
        res_str = ['.'] * n
        mask = (1 << n) - 1
        for i in range(n):
            num = bits & (1 << i)  # get the n-i-th bit
            if num: res_str[n - i - 1] = 'Q'
        t = type(res_str)

        return "".join(res_str)


sol = Solution()
res = sol.solveNQueens(4)
print(res)

