
def check(node, visited):
    if node == '1' and visited == False:
        return True
    else:
        return False
arr = [['1', '0', '1', '1', '1'],
       ['1', '0', '1', '0', '1'],
       ['1', '1', '1', '0', '1']]#,
       #['0', '0', '0', '0', '0']]

# print(get_number_of_islands(arr))

class Solution:
    def numIslands(self, grid):
            #initialize the visited array
        l = len(grid)
        if l == 0:
            return 0
        w = len(grid[0])
        visited = []
        row = []
        for _ in range(l):
            row = []
            for _ in range(w):
                row.append(False)
            visited.append(row)
        count = 0
        idx = 0
        for i in range(l):
            stack_row = []
            for j in range(w):
                if grid[i][j] == '1' and visited[i][j] == False:
                    stack_row.append((i, j, grid[i][j]))
                    while(len(stack_row) > 0):
                        node = stack_row.pop()
                        p, q = node[0], node[1]
                        visited[p][q] = True
                        if p - 1 >= 0 and check(grid[p - 1][q], visited[p - 1][q]):
                            stack_row.append((p - 1, q, grid[p - 1][q]))
                        if p + 1 < l and check(grid[p + 1][q], visited[p + 1][q]):
                            stack_row.append((p + 1, q, grid[p + 1][q]) )
                        if q - 1 >= 0 and check(grid[p][q - 1], visited[p][q - 1]):
                            stack_row.append((p, q - 1, grid[p][q - 1]))
                        if q + 1 < w and check(grid[p][q + 1], visited[p][q + 1]):
                            stack_row.append((p, q + 1, grid[p][q + 1]))
                    count = count + 1
        return count



#s = Solution()
#print(s.numIslands(arr))



s = Solution()
print(s.numIslands(arr))
