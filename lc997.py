def max(ls):
    i, m = -1, -1
    for x in range(0, len(ls)):
        if ls[x] > m:
            m = ls[x]
            i = x + 1
    return i, m
        

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N <= 0:
            return -1
        if N == 1:
            return 1
        if len(trust) == 0:
            return -1
        count = [0 for _ in range(N)] #length N
        #print(count)
        hi_idx = -1 #the judge
        for x in trust:
            count[x[0] - 1] -= 1
            count[x[1] - 1] += 1
        hi_idx, hi = max(count)  
        if hi == N - 1:
            return hi_idx
        return -1

            