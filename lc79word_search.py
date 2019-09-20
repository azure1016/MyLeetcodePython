class Solution:
    def exist(self, board, word):
        self.m = len(board)
        self.n = len(board[0])

        def helper(row, col, idx, state):
            pairs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            if idx >= len(word): return True

            if board[row][col] == word[idx]:
                if idx == len(word) - 1: return True
                for dr, dc in pairs:
                    if dr + row in range(self.m) and dc + col in range(self.n) and (
                    row + dr, col + dc, word[idx + 1]) not in state:
                        new_state = set(state)
                        new_state.add((row, col, word[idx]))
                        if helper(row + dr, col + dc, idx + 1, new_state): return True

            return False

        for i in range(self.m):
            for j in range(self.n):
                if helper(i, j, 0, set()): return True
        return False

arr2 = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
arr = [['a','a']]
word2 = "ABCESEEEFS"
word = "aaa"
sol = Solution()
res = sol.exist(arr, word)
print(res)

