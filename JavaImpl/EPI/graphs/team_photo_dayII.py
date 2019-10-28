'''
not tested!
not understood!
this is a generalized problem of 13.9 on page 193!
This is finding the longest path in a DAG
'''

class GraphVertex:
    def __init__(self):
        self.edges = []
        self.max_distances = 0

def find_largest_number_teams(G):
    def build_topological_ordering():
        def dfs(cur):
            cur.max_distance = 1
            for next in cur.edges:
                if not next.max_distance:
                    dfs(next)
            vertex_order.append(cur)

        vertex_order = []
        for g in G:
            if not g.max_distance:
                dfs(g)
        return vertex_order
    
    def find_longest_path(vertex_order):
        max_distance = 0
        while vertex_order:
            u = vertex_order.pop()
            max_distance = max(max_distance, u.max_distance)
            for v in u.edges:
                v.max_distance = max(v.max_distance, u.max_distance + 1)
        return max_distance
    
    return find_longest_path(build_topological_ordering())