class Solution:
    def lengthOfLIS(self, nums):
        dp = [[1] for _ in len(nums)]

    '''
    def lengthOfLIS(self, nums):
        
        #this code faied. Next, try to save the number of elements in dp rather than the index
        dp = [[] for x in range(len(nums))]
        dp[0] = [0]
        for i in range(len(nums) -1):
            if nums[i+1] > nums[i]:
                for j in range(i, -1, -1):
                    if nums[j] > nums[i+1]:
                        dp[i + 1] = list(dp[j])
                        dp[i + 1].pop()
                        dp[i + 1] += range(j+1, i+2)
                        break 
                if dp[i+1] == []:
                    dp[i+1] = range(i+2)
            elif nums[i+1] == nums[i]:
                temp = list(dp[i])
                temp.pop()
                dp[i+1] = temp + [i+1]
            elif nums[i+1] < nums[i]:
                for j in dp[i]:
                    if nums[i+1] <= nums[j]:
                        dp[i+1] = list(dp[j])
                        dp[i+1].pop()
                        dp[i+1] += [i+1]
                        break
        return len(max(dp, key=len))
    '''

so = Solution()
nums = [1,3,6,7,9,4,10,5,6]
res = so.lengthOfLIS(nums)
print(res)