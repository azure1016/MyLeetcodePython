class PipeSolver:
    def __init__(self, houses, cost, cost_pipe):
        self.houses = houses
        self.total_cost = sum(cost)
        self.cost_pipe = self.flatten_sort(cost_pipe)

    def flatten_sort(self, matrix):
        sorted_1D = [(matrix[u][v], u, v) for u in range(len(matrix)) for v in range(len(matrix[0]))]
        sorted_1D.sort()
        return sorted_1D

    def find_MST(self, sorted_1D):
        visited = set() # visited edges
        for (w, u, v) in sorted_1D:
            if u != v and (u not in visited or v not in visited):
                self.total_cost += w
                visited.add(u)
                visited.add(v) # if it's a directed graph, please add tuple (u,v) as an edge
            if len(visited) == self.houses: return

    def solve(self):
        self.find_MST(self.cost_pipe)
        return self.total_cost

# test case:
houses = 4
cost = [0,2,3,1]
cost_pipe = [[0, 15, 6, 5],
             [15, 0, 8, 9],
             [6, 8, 0, 4],
             [5, 9, 4, 0]]
solver = PipeSolver(houses, cost, cost_pipe)
total_cost = solver.solve()
print(total_cost)
