
import random
class Solution:
    def kClosest(self, points, K):
        def compare(p1, p2):
            return p1[0] ** 2 + p1[1] ** 2 - p2[0] ** 2 - p2[1] ** 2 > 0
        def partition(l, r):
            p = l
            while True:
                while l < r and compare(points[p], points[l]):
                    l += 1
                while r > l and compare(points[r], points[p]):
                    r -= 1
                if l >= r: break
                else:
                    points[r], points[l] = points[l], points[r]
            return l

        def partition_TLE(l, r):
            p = random.randint(l, r)
            points[p], points[r] = points[r], points[p]
            i, j = l-1, l
            while j < r:
                if compare(points[r], points[j]):
                    i += 1
                    points[i], points[j] = points[j], points[i]
                j += 1
            i += 1
            points[r], points[i] = points[i], points[r]
            return i

        l, r = 0, len(points) - 1
        pivot = partition(l, r)
        dummy_K = K
        while pivot != K - 1:
            if pivot < K - 1:
                pivot = partition(pivot + 1, r)
            else:
                pivot = partition(l, pivot - 1)
        return points[:dummy_K]


points = [[3,3],[5,-1],[-2,4]]
points2 = [[9,0],[7,10],[-4,-2],[3,-9],[9,1],[-5,-1]]
points3 = [[-2,-5],[8,5],[-10,-3],[-7,-1],[2,-2],[2,8]]
K = 2
K2 = 5
K3 = 5
sol = Solution()
res = sol.kClosest(points3, K3)
print(res)