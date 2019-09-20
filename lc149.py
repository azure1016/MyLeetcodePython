class Solution:
    def maxPoints(self, points):

        res = 0
        for i in range(len(points)):
            overlap = 0
            slope = {}
            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue
                elif (dx != 0 and dy != 0):
                    gcd_ = self.gcd(dx, dy)
                    dx /= gcd_
                    dy /= gcd_
                elif dx == 0: dy = 1
                elif dy == 0: dx = 1
                if (dx, dy) in slope.keys():
                    slope[(dx, dy)] += 1
                else:
                    slope[(dx, dy)] = 2
            if slope:
                res = max(res + overlap, slope[max(slope, key=slope.get)] + overlap)
        return res

    def gcd(self, x, y):
        temp = x % y
        while temp != 0:
            x = y
            y = temp
            temp = x % y
        return y


so = Solution()
points = [[2,3],[3,3],[-5,3]]
result = so.maxPoints(points)
print(result)