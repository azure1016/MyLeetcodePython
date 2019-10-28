from collections import Counter
class Solution:
    def alternate(self, s, t, maxCost):
        map = {ch: i for i, ch in enumerate("abcdefghijklmnopqrstuvwxyz")}
        s = [map[ch] for ch in s]
        t = [map[ch] for ch in t]
        n = len(s)
        diff = [abs(s[i] - t[i]) for i in range(n)]
        i = j = 0
        I = J = Sum = 0
        sum_ = 0
        while j < n:
            sum_ += diff[j]
            if sum_ <= maxCost: 
                if j - i > J - I:
                    J, I = j, i
            else:
                sum_ -= diff[i]
                i += 1
                if j - i < J - I:
                    J, I = j, i
            j += 1
        return J - I + 1


        
  

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        map = {ch:i for i, ch in enumerate("abcdefghijklmnopqrstuvwxyz")}
        n = len(s)
        dp = [[0, 0, 0]] + [[i-1, i, abs(ord(s[i-1]) - ord(t[i-1]))]
                            for i in range(1, n+1)]  # [start, end, cost]
        for i in range(1, n+1):
            if s[i-1] == t[i-1]:
                dp[i] = [dp[i-1][0], dp[i-1][1]+1, dp[i-1][2]]
            else:
                dp[i] = [dp[i-1][0], dp[i-1][1]+1, dp[i-1][2] +
                         dp[i][2]] if dp[i-1][2] + dp[i][2] <= maxCost+1 else dp[i]
        return max([dp[i][1] - dp[i][0] for i in range(n+1)])

    def test(self, s, t, maxCost):
        print(self.alternate(s, t, maxCost))

sol = Solution()
s = "ujteygggjwxnfl"
t = "nstsenrzttikoy"
sol.test(s, t, 43)
sol.test('abdf', 'bcdh', 3)
