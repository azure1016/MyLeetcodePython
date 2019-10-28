'''
Input: radii = [1, 1, 1, 2, 2, 3],  numberOfGuests = 6.
Output: 7.0686
Explanation:
Reason being you can take the area of the cake with a radius of 3, and divide by 4. (Area  28.743 / 4  = 7.0686)
Use a similary sized piece from the remaining cakes of radius 2 because total area of cakes with radius 2 are > 7.0686

[1,1,1,4,4,9]
we want find x for n people, y cakes is good for x * n
higher bound is 9
lower bound is 1
mid = 5, how many values are bigger than 5?  6 * 5 > 1+1+1+4+4+9=20
higher = 5,lower is 1
mid = 3, sastisfy 5 people
higher 3, lower is 1
mid = 2, we can satisfy: 2+2+4 = 8 people
lower = 2, higher = 3
mid = 2.5, we can satisfy 1+1+3
lower = 2, high is 2.5
mid = 2.25 satisfy: 1+1+4=6
lower = 2.25, higher = 2.5
'''
import math, sys
class CakeDivider:
    def largestCake_dp(self, cakes, k):
        self.dp = [[float('inf') for _ in range(len(cakes)+1)] for _ in range(k+1)]
        areas = [r**2 for r in cakes]
        areas.sort()
        self.findAllpossible(areas, k, len(areas))
        return self.dp[k][-1] * math.pi

    def findAllpossible(self, areas, remained, index):
        if index == 0: return sys.maxsize
        if remained == 0: return sys.maxsize
        if remained == 1: return areas[index-1]
        if index == 1: return areas[index-1] / float(remained)
        if self.dp[remained][index] != float('inf'): return self.dp[remained][index]
        cur_max = 0
        for i in range(remained):
            cur_max = max(cur_max,
                          min(self.findAllpossible(areas, i, index - 1), areas[index-1] / float(remained - i)))
        self.dp[remained][index] = cur_max
        return cur_max

    def largestCake(self, cakes, k):
        areas = [ r**2 for r in cakes]
        areas.sort()
        high = areas[-1]
        low = areas[0]
        result = 0
        mid = 0
        while high > low+0.00001:
            mid = low + (high - low) / 2.0
            if self.satisfy(mid, k, areas): #
                result = max(result, mid)
                low = mid # maximum
            else:
                high = mid
        return max(result, mid) * math.pi



    def satisfy(self, area, k, areas):
        counter = 0
        for cake in areas[::-1]:
            if cake >= area:
                counter += math.floor(cake / area)
        if counter >= k:
            return 1
        else: return 0

    def test1(self):
        cakes = [1,1,1,2,2,3]
        k = 6
        result = self.largestCake(cakes, k)
        result_dp = self.largestCake_dp(cakes, k)
        print(result_dp)
        print(result)

    def test2(self):
        cakes = [4,3,3]
        k = 3
        print(self.largestCake_dp(cakes, k))
        print(self.largestCake(cakes, k))

sol = CakeDivider()
sol.test2()
