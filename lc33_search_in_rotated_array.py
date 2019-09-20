class Solution:
    def search(self, nums, target):
        n = len(nums)
        m, idx = self.pivot(nums, 0, n-1)
        head, end = 0, n-1
        while head <= end:
            mid = head + (end - head) // 2
            # true_idx - idx = mid; true-index = idx + mid
            true_index = (mid + idx) % n
            if nums[true_index] == target: return  true_index
            elif nums[true_index] > target: end = mid - 1
            elif nums[true_index] < target: head = mid + 1
        return -1
    def pivot(self, nums, s, e):
        if s > e: return -1, -1
        elif nums[s] <= nums[e]:return nums[e], e+1
        else:
            mid = s + (e - s) // 2
            left = self.pivot(nums, s, mid)
            right = self.pivot(nums, mid+1, e)
            return left if left[0] > right[0] else right

input = [1]
target = 0
so = Solution()
res = so.search(input, target)
print(res)