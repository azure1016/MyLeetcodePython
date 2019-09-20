class Solution:
    def longestPalindrome_manacher(self, s):
        T = self.preprocess(s)
        P = [0] * len(T)
        c, mirror, R = 1, 0, 0
        for i in range(1, len(T)):
            if R > i:  # prevent from over the bound: "safe-known area: -R ~ R"
                P[i] = min(R - i, P[2 * c - i])
            else:
                P[i] = 0
            while P[i] + i + 1 < len(T) and i - 1 - P[i] > 0 and T[P[i] + i + 1] == T[i - 1 - P[i]]: P[i] += 1
            if i + P[i] > R:
                c = i
                R = P[i] + i
        return self.maxPalin(P, s)

    def maxPalin(self, P, s):
        m = 0
        m_i = 0
        for i in range(len(P)):
            if P[i] > m:
                m = P[i]
                m_i = i
        start = (m_i - P[m_i])//2
        end = start + P[m_i]
        res = s[start:end]
        return res

    def preprocess(self, s):
        res = '^#'
        for ch in s:
            res += ch + "#"
        return res + "$"

    def longestPalindrome(self, s):
        if len(s) == 0 or not s: return ""
        reversed = s[::-1]
        m_len = 0
        start, end = 0, 0
        P = [0] * len(s)
        for i in range(len(s)):
            for j in range(len(s) - 1, -1, -1):
                if s[i] == reversed[j]:
                    if i == 0 or j == 0: P[j] = 1
                    else:P[j] = P[j - 1] + 1
                    beforeRev = len(s) - j - 1
                    if beforeRev + P[j] - 1 == i:
                        if P[j] > m_len:
                            m_len = P[j]
                            start = min(i, j)
                            end = j
                else:
                    P[j] = 0

        return s[start: start+m_len]

so = Solution()
s = "babadabacabad"

res= so.longestPalindrome(s)
print(res)