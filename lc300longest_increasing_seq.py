import bisect


class Solution:
    # beat 90%
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        tails = [0] * len(nums)
        size = 0
        for i in range(len(nums)):
            idx = bisect.bisect_left(tails, nums[i], 0, size)
            tails[idx] = nums[i]
            if idx >= size:
                size += 1
        return size


nums = [10, 9, 2, 5, 3, 7, 101, 18]
res = Solution().lengthOfLIS(nums)
print(res)

nums2 = [2, 2]
