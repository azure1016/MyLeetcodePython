class Solution:
    def pivotIndex(self, nums):
        n = len(nums)
        accumulate = [0]
        for i in reversed(range(n)):
            accumulate.append(accumulate[-1] + nums[i])
        running_sum = 0
        for i, num in enumerate(nums):
            if (n - i - 1 >= 0 and accumulate[n - i - 1] == running_sum) or (n-i-1 < 0 and running_sum == 0):
                return i
            running_sum += nums[i]
        return -1

arr = [1,5,6]
sol = Solution()
res = sol.pivotIndex(arr)
print(res)