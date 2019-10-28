from collections import namedtuple, deque
Place = namedtuple('Place', "r, c")
adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Go:
    '''the thinking process: *** BFS is more suitable! ***
    0. if you can't put a 'b' in that cell, directly return 0!!
    1. make sure to start from the cell where you place the new 'b', reason is trivial
    2. there's 2 'direction', 'in' and 'out'. only 'in' will give you the right answer. You choose to do DFS, but there's
    2 possibilities that you would come across 'e': 'in': then you crush; 'out': just change a direction, not crush
    DFS better not handle this. it's better for DFS to crush whenever it finds 'e'. So, we try to branch 4 direction at 'capture'
    3. a traversal of DFS might return 0 in 2 cases: A. it comes across 'e', in this case, you should crush! means you should give up
    all counting including the counts before you see 'e'! B. simply no 'w' or no unvisited 'w'. To distinguish this two
    cases, you need a boolean returned along with the count.
    4. of course you need a 'visited' boolean array. But be consistent with the way you modify 'visited'. Either before you
    perform DFS on that cell or in the DFS of the cell!
    '''
    def dfs(self, grid, cur, visited):
        m, n = len(grid), len(grid[0])
        if cur.r not in range(m) or cur.c not in range(n) or grid[cur.r][cur.c] != 'w': return 0, True
        count = 1 if not visited[cur.r][cur.c] else 0
        visited[cur.r][cur.c] = True
        for (dr, dc) in adj:
            row, col = cur.r + dr, cur.c + dc
            if row not in range(m) or col not in range(n) or grid[row][col] == 'b':continue
            if grid[row][col] == 'e': # should crush whenever you meet 'e';
                visited[cur.r][cur.c] = False
                return 0, False # use a boolean to inform all parents to surrender
            if grid[row][col] == 'w' and not visited[row][col]:
                branch_count, isValid = self.dfs(grid, Place(row, col), visited)
                if not isValid: # maybe unnecessary
                    visited[row][col] = False
                    return 0, False # return 0 immediately and pass the failure signal to parents
                count += branch_count
        return count, True

    def capture(self, grid, place): 
        if grid[place.r][place.c] != 'e': return 0
        m, n = len(grid), len(grid[0])
        grid[place.r][place.c] = 'b'
        visited = [[False for _ in range(n)] for _ in range(m)]
        result = 0
        for (dr, dc) in adj:
            branch_res, _ = self.dfs(grid, Place(place.r+dr, place.c+dc), visited)
            result += branch_res
        return result
    
    def test(self, grid, row, col):
        res = self.capture(grid, Place(row, col))
        print(res)

sol = Go()
grid = [['e', 'e', 'e', 'e', 'b', 'b', 'b'],
        ['e', 'e', 'e', 'e', 'b', 'w', 'b'],
        ['e', 'e', 'e', 'e', 'b', 'e', 'b'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e']]
sol.test(grid, 2, 5) # 1

grid1 = [['e', 'e', 'e', 'e', 'b', 'b', 'b'],
         ['e', 'e', 'e', 'b', 'w', 'w', 'b'],
         ['e', 'e', 'e', 'e', 'b', 'e', 'b'],
         ['e', 'e', 'e', 'e', 'e', 'e', 'e']]

sol.test(grid1, 2, 5) # 2

grid2 = [['e', 'e', 'e', 'b', 'b', 'b', 'b'],
         ['e', 'e', 'b', 'w', 'e', 'w', 'b'],
         ['e', 'e', 'e', 'b', 'b', 'e', 'b'],
         ['e', 'e', 'e', 'e', 'e', 'e', 'e']]
sol.test(grid2, 2, 5) # 0

grid3 = [['e', 'e', 'e', 'e', 'b', 'b', 'b'],
         ['e', 'e', 'e', 'e', 'w', 'w', 'b'],
         ['e', 'e', 'e', 'e', 'b', 'e', 'b'],
         ['e', 'e', 'e', 'e', 'e', 'e', 'e']]
sol.test(grid3, 2, 5) # 0

grid4 = [['w', 'w', 'w'],
         ['w', 'e', 'w'],
         ['w', 'w', 'w']]
sol.test(grid4, 1, 1) # 8

# where 2 directions can capture valid 'w'
grid5 = [['e', 'b', 'b', 'b', 'b', 'b', 'b'],
         ['b', 'w', 'e', 'w', 'w', 'w', 'b'],
         ['b', 'w', 'w', 'w', 'w', 'e', 'b'],
         ['e', 'b', 'b', 'b', 'b', 'e', 'e']]
sol.test(grid5, 2, 5) # 0

# what about this test case:
grid6 = grid = [['e', 'e', 'e', 'e', 'b', 'b', 'b'],
                ['e', 'e', 'e', 'e', 'b', 'w', 'b'],
                ['e', 'e', 'e', 'e', 'b', 'b', 'b'],
                ['e', 'e', 'e', 'e', 'e', 'e', 'e']]
sol.test(grid, 3, 5) # you capture 1 or 0? I think it should be 0

# what about this:
grid7 = [['w', 'w', 'w'],
         ['w', 'e', 'b'],
         ['w', 'e', 'w']]
sol.test(grid7, 2, 1) # should output 1 (right corner) or 0? right corner (I think it should be 1)





