class Solution:
    def nextPermutation(self, nums) :
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) < 2: return
        k = len(nums) - 1
        while k > 0 and nums[k - 1] >= nums[k]: k -= 1
        if k > 0:
            j = len(nums) - 1
            while j > 0 and nums[j] <= nums[k - 1]: j -= 1
            nums[k - 1], nums[j] = nums[j], nums[k - 1]
            nums[k:] = nums[:k-1:-1]
        else:nums[:] = nums[::-1]

so = Solution()
nums = [3,2,1,0,0]
so.nextPermutation(nums)

print(nums[0:])
print(nums[5:-1])
