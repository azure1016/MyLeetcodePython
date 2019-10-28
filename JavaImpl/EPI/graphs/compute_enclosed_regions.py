import collections

def fill_surrounded_regions(board):
    n, m = len(board), len(board[0])
    pairs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    q = collections.deque([(i, j) for i, j in ((k, 0), (k, m-1)) for k in range(n)] +
    [(i, j) for i, j in ((0, k), (n-1, k)) for k in range(m)])
    while q:
        x, y = q.popleft()
        if 0 <= x < n and 0 <= y <= m and board[x][y] == 'W':
            board[x][y] = 'T'
            q.extend([(dx+x, dy+y) for dx, dy in pairs])
    board[:] = [['B' if c!='T' else 'W' for c in row] for row in board]

            

