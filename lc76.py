from collections import Counter
import sys

'''
76. Minimum Window Substring
Hard

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t): return ""
        T = Counter(t)  # a dict
        start, end, m_s, m_e = 0, 0, 0, 0
        while end < len(s):
            while end < len(s) and max(T.values()) > 0:
                if s[end] in T.keys():
                    T[s[end]] -= 1
                end += 1
            while start < end and max(T.values()) <= 0:
                if s[start] in T.keys():
                    T[s[start]] += 1
                start += 1

            if (not m_e and start) or (end - start) < (m_e - m_s):
                m_e = end
                m_s = start - 1

        return s[m_s:m_e]

    def minWindow2(self, s, t):
        need, missing = Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]

so = Solution()
s = "ADOBECODEBANC"
t = "ABC"
res = so.minWindow(s, t)
print(res)

