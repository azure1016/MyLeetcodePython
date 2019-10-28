import collections
'''not tested'''
def flip_color(x, y, A):
    Coordinate = collections.namedtuple('Coordinate', 'x, y')
    color = A[x][y] # record the original color before flip
    q = collections.deque([Coordinate(x, y)])
    pairs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    A[x][y] = 1 - A[x][y] # flips
    while q:
        cur = q.popleft()
        for dx, dy in pairs:
            next = Coordinate(dx+cur.x, dy+cur.y)
            if next.x not in range(len(A)) or next.y not in range(len(A[0])): continue
            if A[next.x][next.y] == color:
                q.append(next)
                A[next.x][next.y] ^= 1
            
