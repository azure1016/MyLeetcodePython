class Solution:
    def findRedundantConnection(self, edges):
        # if nodes' index start from 0, you can't set parent = [0] * len(edges)
        # in that case, set parent = [-1] * len(edges) or any number not in nodes' indices
        # you can set parent = [0] * len(edges) if you don't wanna add(line23) or minus 1(line8)
        parent = [0] * len(edges)
        for u, v in edges:
            result = self.union(u-1, v-1, parent)
            if result:
                return result
        return None

    def findParent(self, i, parent):
        if parent[i] == 0:
            return i
        parent[i] = self.findParent(parent[i], parent)
        return parent[i]

    def union(self, u, v, parent):
        parent_u = self.findParent(u, parent)
        parent_v = self.findParent(v, parent)
        if parent_u == parent_v:
            return [u+1, v+1]
        else:
            parent[parent_u] = parent_v
        return None


edges = [[1, 2], [1, 3], [2, 3]]
res = Solution().findRedundantConnection(edges)
print(res)
