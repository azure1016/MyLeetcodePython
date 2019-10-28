import bisect
import functools

class Solution:
    def maxEnvelopes(self, envelopes):
        '''
        [2, 3], [5, 4], [6, 4], [6, 7]
        '''
        envelopes.sort(key=functools.cmp_to_key(lambda x, y: -1 if (x[0] < y[0] or x[0] == y[0] and x[1] > y[1]) else 1))
        return self.lengOfLIS([e[1] for e in envelopes])

    def lengOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for i in range(len(nums)):
            idx = bisect.bisect_left(tails, nums[i], 0, size)
            tails[idx] = nums[i]
            if idx >= size:
                size += 1
        return size


nums = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
res = Solution().maxEnvelopes(nums)
print(res == 4)
