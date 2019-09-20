class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        app = {}
        head = 0
        end = 0
        max_len = 1
        while end < len(s):
            if s[end] in app.keys():
                max_len = max(end - head, max_len)
                newhead = app[s[end]] + 1
                for i in s[head:newhead]:
                    # del app[i]
                    app.pop(i)
                head = newhead
                app[s[end]] = end
            else:
                app[s[end]] = end
            end += 1
        return max(max_len, end - head)


so = Solution()
s = "abcabcbb"
res = so.lengthOfLongestSubstring(s)
print(res)