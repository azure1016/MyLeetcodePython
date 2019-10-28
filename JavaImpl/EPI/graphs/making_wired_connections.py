import collections
'''not tested'''
class GraphVertex:
    def __init__(self):
        self.d = -1
        self.edges = []

def is_any_placement_feasible(G):
    def bfs(s):
        s.d = 0
        dq = collections.deque([s])
        while dq:
            cur = dq.popleft()
            for next_v in cur.edges:
                if next_v.d == -1:
                    next_v.d = cur.d + 1
                    dq.append(next_v)
                elif next_v.d == cur.d:
                    return False # an odd-length cycle
        return True

    return all(bfs(v) for v in G if v.d == -1)
