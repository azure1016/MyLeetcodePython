import collections

class GraphVertex:
    def __init__(self, label):
        self.label = label
        self.edges = []

def clone_graph(G):
    if not G: return None

    dq = collections.deque([G])
    vertex_map = {G: GraphVertex(G.label)}
    while dq:
        cur = dq.popleft()
        for next in cur.edges:
            if next not in vertex_map:
                vertex_map[next] = GraphVertex(next.lable)
                dq.append(next)
            # not append next but a copy of next!
            # vertex_map[cur].edges.append(next)
            vertex_map[cur].edges.append(vertex_map[next])
    return vertex_map[G]
