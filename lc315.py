import bisect
class Solution:
    def countSmaller1(self, nums):
        s = sorted(nums)
        count = []
        for num in nums:
            i = bisect.bisect_left(s, num)
            count.append(i)
            s.pop(i)
        return count
    def BS(self, arr, target):
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] >= target: r = mid
            else: l = mid + 1
        return l
    def countSmaller(self, nums):
        s = sorted(nums)
        count = []
        for num in nums:
            i = self.BS(s, num)
            s.pop(i)
            count.append(i)
        return count


so = Solution()
nums = [5,2,3,6,3,1]
expected = [4,1,1,2,1,0]
print(so.countSmaller(nums))
