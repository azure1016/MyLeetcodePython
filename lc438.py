from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        t = Counter(p)
        i, j, ans = 0, 0, []
        step = len(p)
        while j < len(s):
            while j < len(s) and max(t) > 0:
                if s[j] in t:
                    t[s[j]] -= 1
                j += 1

            while i < j and max(t) <= 0:
                if s[i] in t:
                    t[s[i]] += 1
                i += 1
            if i and j - i == step - 1: ans.append(i - 1)
        return ans

so = Solution()
s = "cbaebabacd"
p = "abc"
res = so.findAnagrams(s, p)
print(res)