class Solution:
    # this code enters infinite loop!
    def isMatch_fail(self, s, p):
        if len(p) == 0: return len(s) == 0 # if pattern is empty, s must also be empty
        elif len(p) == 1: return (p == '.' and len(s) == 1) or s == p
        else:
            # if p[0] == '.' and p[1] == '*': return self.isMatch()
            if p[1] == '*':
                if len(s) == 0: return self.isMatch(s,p[2:])
                elif s[0] == p[0] or p[0] == '.': return self.isMatch(s[1:], p) or self.isMatch(s[1:], p[2:]) or self.isMatch(s, p[2:])
                else: return self.isMatch(s, p[2:])
            else:
                if len(s) == 0 : return False
                elif s[0] == p[0] or p[0] == '.': return self.isMatch(s[1:], p[1:])
                else: return False

    def isMatch(self, s, p):
        # initialize a 2D array of size: (len(s) + 1) * (len(p) + 1)
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        # set values for base cases:
        # if s & p are empty, return True
        dp[0][0] = True
        # if p is empty: all return False. dp[i][0] = False
        # if s is empty, and p[even_index] == '*': return True
        for j in range(2, len(p) + 1, 2):  # step is 2; why len(p)+1? consider length of 4. we need
            if p[j - 1] == '*': dp[0][j] = True
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if j > 1 and p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or dp[i - 1][j - 1] or dp[i][j - 1]  # count as multiple
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        return dp[len(s)][len(p)]
so = Solution()
s = "aa"
p = "a*"
res = so.isMatch(s,p)
print(res)