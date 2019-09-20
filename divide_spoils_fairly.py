import collections

class Solution:
    def divide(self, items):
        total = sum(items) // 2
        # find the maximum combination <= than sum(items) // 2
        # define: dp[i][j] is the maximum sum of subsequence of the first i items that is <= j
        # base case: dp[0][j] = 0, dp[i][0] = 0
        # if j - items[i] < 0:
        # if dp[i-1][j-items[i]] + items[i] > j: dp[i][j] = dp[i-1][j]
        # dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i]]+items[i]
        dp = [[0 for _ in range(total+1)] for _ in range(len(items) + 1)]
        for i in range(1, len(items)+1):
            for j in reversed(range(1, total+1)):
                if j - items[i-1] < 0 or dp[i-1][j-items[i-1]] + items[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i-1]] + items[i-1])
        return dp[-1][-1]

    def divide_with_same_items(self, items):
        m = len(items)
        total = sum(items) // 2
        Spoil = collections.namedtuple('Spoil',['num', 'val'])
        dp = [[Spoil(0,0) for _ in range(total +1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in reversed(range(1, total+1)):
                if  j < items[i-1] or dp[i-1][j-items[i-1]].num >= m // 2 or dp[i-1][j].val >= dp[i-1][j - items[i-1]].val + items[i-1]:
                    dp[i][j] = Spoil(dp[i-1][j].num, dp[i-1][j].val)
                else:
                    dp[i][j] = Spoil(dp[i-1][j-items[i-1]].num + 1, dp[i-1][j-items[i-1]].val + items[i-1])
        return dp[-1][-1].val


items = [65, 35, 245, 195, 65, 150, 275, 155, 120, 320, 75, 40, 200, 100, 220, 99]
items2 = [1,9,2,1,1,1]
sol = Solution()
res = sol.divide(items)
res_with_same_items = sol.divide_with_same_items(items2)
print(res_with_same_items)

