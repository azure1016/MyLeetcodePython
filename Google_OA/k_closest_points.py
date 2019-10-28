from heapq import *
class Points:
    def kClosest(self, points, k):
        max_heap = [(-x ** 2 - y ** 2, i) for i, (x,y) in enumerate(points[:k])]
        heapify(max_heap)
        for i in range(k, len(points)):
            heappushpop(max_heap, (-points[i][0] ** 2 - points[i][1] ** 2, i))
        return [points[tp[1]] for tp in max_heap]

    def test1(self):
        points = [[1,3],[-2,2]]
        K = 1
        res = self.kClosest(points, K)
        print(res)

    def test2(self):
        points = [[3,3], [5, -1], [-2,4]]
        k = 2
        res = self.kClosest(points, k)
        print(res)

solution = Points()
solution.test2()