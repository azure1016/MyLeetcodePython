from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.ch = defaultdict(TrieNode)
        self.isEnd = False

    def insert(self, s):
        node = self
        for c in s:
            node = node.ch[c]
        node.isEnd = True

    def search(self, s):
        node = self
        for c in s:
            if c not in node.ch: return None
            node = node.ch[c]
        return node


class Solution:
    def findWords(self, board, words):
        self.buildTrie(words)
        self.result = []
        self.pairs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                # self.DFS(i, j, "", word, board)
                self.DFS(i, j, "", board)

        return self.result

    def DFS(self, row, col, path, board):
        node = self.root.search(path+board[row][col])
        if not node: return
        if node.isEnd:
            self.result.append(path+board[row][col])
            node.isEnd = False

        for dr, dc in self.pairs:
            if dr + row in range(len(board)) and dc + col in range(len(board[0])):
                tmp = board[row][col]
                board[row][col] = '#'
                self.DFS(dr + row, dc + col, path + tmp, board)
                board[row][col] = tmp

    def buildTrie(self, words):
        self.root = TrieNode()
        for word in words:
            self.root.insert(word)

    def preprocess(self, board):
        self.map = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.map.add((i, j, board[i][j]))

    def findWords_TLE(self, board, words):
        self.preprocess(board)
        self.result = set()
        self.pairs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for word in words:
            # points: row, col
            # cell under it would be [row+1, col]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if (i, j, word[0]) in self.map:
                        self.search(i, j, 0, word, board, set())

        return self.result

    def search(self, row, col, index, word, board, used):
        if index == len(word) - 1:
            # if board[row][col] == word[index]: # can't wait to check its adjacent cells
            self.result.add(word)
            return True

        for dr, dc in self.pairs:
            if (dr + row, dc + col, word[index + 1]) in self.map and (dr + row, dc + col, word[index + 1]) not in used:
                # new_used = set(used)
                # new_used.add((row, col, word[index]))
                if self.search(dr + row, dc + col, index + 1, word, board, used.union(set((row, col, word[index])))):
                    return True
        return False

    def search_TLE(self, row, col, index, word, board, used):
        if index == len(word) - 1:
            # if board[row][col] == word[index]: # can't wait to check its adjacent cells
            self.result.add(word)
            return True

        # row, col wouldn't go out bound
        if board[row][col] == word[index]:
            for dr, dc in self.pairs:
                if dr + row in range(len(board)) and dc + col in range(len(board[0])) and (
                dr + row, dc + col, word[index + 1]) in self.map and (dr + row, dc + col, word[index + 1]) not in used:
                    new_used = set(used)
                    new_used.add((row, col, word[index]))
                    if self.search(dr + row, dc + col, index + 1, word, board, new_used):
                        return True
        return False

board = [["a"]]
word = ["a"]
sol = Solution()
res = sol.findWords(board, word)
print(res)




