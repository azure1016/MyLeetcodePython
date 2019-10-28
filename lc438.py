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
            while j < len(s) and max(t.values()) > 0:
                if s[j] in t:
                    t[s[j]] -= 1
                j += 1

            while i < j and max(t.values()) <= 0:
                if s[i] in t:
                    t[s[i]] += 1
                i += 1
            if i and j - i == step - 1: ans.append(i - 1)
        return ans

    from collections import defaultdict, Counter

    # added 10/23/2019
    def findAnagrams2(self, s, p):
        counter = Counter(p)
        pattern = Counter(p)
        start, end = 0, 0
        result = []
        while end < len(s):
            
            while end < len(s) and max(pattern.values()) > 0:
                pattern[s[end]] -= 1
                end += 1
            while start <= end and min(pattern.values()) < 0:
                pattern[s[start]] += 1
                start += 1
            if end - start == len(p):
                result.append(start)
                pattern[s[start]] += 1
                start += 1
            #pattern.update(counter)
        return result
            
    def eqDict(self, d1, d2):
        if len(d1) != len(d2): return False
        for key, val in d2:
            if key not in d1 or d1[key] != val: return False
        return True
        

so = Solution()
s = "cbaebabacd"
p = "abc"
res = so.findAnagrams(s, p)
res2 = so.findAnagrams2(s, p)
print(res2)
