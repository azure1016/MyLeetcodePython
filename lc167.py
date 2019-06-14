class Solution:
    def twoSum(self, numbers, target):
        low, high = 0, len(numbers) - 1
        while low < high:
            sum_ = numbers[low] + numbers[high]
            if sum_ == target:return [low, high]
            elif sum_ < target:low += 1
            else:high -= 1
        return [-1, -1]

so = Solution()
arr = [2,7,11,15]
print(so.twoSum(arr, 13))