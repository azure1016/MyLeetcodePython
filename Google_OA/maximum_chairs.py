from collections import namedtuple
class Overlap:
    def minChairs(self, S, E):
        TSeries = namedtuple('TSeries', 'time, sign')
        series = []
        for t in S:
            series.append(TSeries(t, 1))
        for t in E:
            series.append(TSeries(t, -1))
        chairs = 0
        max_chairs = 0
        series.sort()
        for tp in series:
            chairs += tp.sign
            max_chairs = max(max_chairs, chairs)
        return max_chairs

    def test1(self):
        S = [1,2,6,5,3,2,5]
        T = [5,5,7,6,8,3,8]
        expected = 3
        print(expected == self.minChairs(S, T))


sol = Overlap()
sol.test1()




