class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        when [5, 1, 2, 3, 4, 4]
        lo = 1, hi = 5, mid = 2,split to [1, 2, 3], [5, 4]
        '''
        lo = 1
        hi = len(nums) - 1
        while (lo < hi):
            mid = int((lo + hi) / 2)
            count = 0
            for num in nums:
                if num <= mid:
                    count = count + 1
            if count > mid:
                hi = mid
            else:
                lo = mid + 1
        return lo


test = Solution()
case1 = [1,4,4,2,4]
res = test.findDuplicate(case1)
print(res)
