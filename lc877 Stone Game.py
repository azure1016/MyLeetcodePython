class pair:
    def __init__(self, fir, sec):
        self.fir = fir
        self.sec = sec


class Solution:
    def stoneGame1(self, piles):
        return True

    def stoneGame(self, piles):
        n = len(piles)
        dp = [[pair(0, 0) for _ in range(n)] for _ in range(n)]
        # base case 1:
        for i in range(n):
            dp[i][i] = pair(piles[i], 0)
        # base case 2: for j=0, all is 0

        # status transitting
        '''
        dp[i][j].fir = max(piles[i]+dp[i+1][j].sec, piles[j]+dp[i][j-1].sec)
        dp[i][j].sec = max(dp[i+1][j].fir, dp[i][j-1].fir)

        we must first know i+1 then we can know i --> decreasing i
        must first know j-1, then we can know j -- increasing j
        right-up matrix! coz i <= j
        '''
        for l in range(2, n + 1):  # why l-2? coz should i+1 < l, i-1 <l-1 so i - 1 <= l-2
            for i in range(n - l + 1):  # should j < i
                j = l + i - 1
                # for i in range(l-1):

                if piles[i] + dp[i + 1][j].sec > piles[j] + dp[i][j - 1].sec:
                    dp[i][j].fir = piles[i] + dp[i + 1][j].sec
                    dp[i][j].sec = dp[i + 1][j].fir
                else:
                    dp[i][j].fir = piles[j] + dp[i][j - 1].sec
                    dp[i][j].sec = dp[i][j - 1].fir

                # dp[i][j].fir = max(piles[i]+dp[i+1][j].sec, piles[j]+dp[i][j-1].sec)
                # dp[i][j].sec = max(dp[i+1][j].fir, dp[i][j-1].fir)
        if dp[0][n - 1].fir > dp[0][n - 1].sec:
            return True
        else:
            return False

so = Solution()
piles = [3,7,2,3]
res = so.stoneGame(piles)
print(res)