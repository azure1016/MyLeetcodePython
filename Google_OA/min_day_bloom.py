from collections import deque
import sys
class Bloom:
    def minDaysBloomDP(self, blooms, k, n):
        windowMax = self.findWindowMax(blooms, k);
        dp = [[sys.maxsize for _ in range(len(blooms)+1)] for _ in range(n+1)]
        # dp[0][j] = 0, no effort to form 0 bouquets
        # actually impossible to form i bouquets without flowers at all! so, 0
        for i in range(len(blooms)+1):
            dp[0][i] = 0
        for i in range(1, n+1): # at least form 1 bouquet
            # impossible to form a bouquet of size k with less than k flowers
            for j in range(k, len(blooms) + 1):
                # windowMax[j-k] actually means the j th window max ending at j
                dp[i][j] = min(dp[i][j-1], max(windowMax[j-k], dp[i-1][j-k]))
        return dp[-1][-1]
    
    def findWindowMax(self, blooms, k):
        windowMax = []
        decrease_queue = deque()
        for i, bloom in enumerate(blooms):
            if i >= k and blooms[i - k] == decrease_queue[0]:
                decrease_queue.popleft()
            while len(decrease_queue) and decrease_queue[-1] < bloom:
                decrease_queue.pop()
            decrease_queue.append(bloom)
            if i >= k-1: windowMax.append(decrease_queue[0])
        return windowMax

    def minDaysBloomBS(self, blooms, k, n):
        windowMax = self.findWindowMax(blooms, k)
        high = max(blooms)
        low = min(blooms)
        while high >= low:
            mid = low + (high - low) // 2
            if self.satisfy(windowMax, k, n, mid):
                high = mid - 1
            else:
                low = mid + 1
        return low

    def satisfy(self, windowMax, k, n, days_after):
        i = 0
        while i < len(windowMax):
            if windowMax[i] <= days_after:
                n -= 1
                i += k
            else: i += 1
        return n <= 0


    def test(self):
        blooms = [1, 2,5,2,6, 4, 9, 3, 4, 1]
        k = 3
        n = 3
        res_dp = self.minDaysBloomDP(blooms, k, n)
        res_bs = self.minDaysBloomBS(blooms, k, n)
        print(res_dp == res_bs)

sol = Bloom()
sol.test()
