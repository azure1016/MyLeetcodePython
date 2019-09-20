class Solution:
    def combinationSum2_2(self, nums, target):
        if not nums or len(nums) == 0:
            return []
        nums.sort()
        res = []
        used = [False] * len(nums)
        self.backtrack(nums, res, [], 0, target, used)
        return res

    def backtrack(self, nums, res, temp, start, target, used):
        if target < 0: return
        if target == 0:
            res.append(list(temp))
            return
        for i in range(start, len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            elif nums[i] > target:
                break
            else:
                temp.append(nums[i])
                used[i] = True
                self.backtrack(nums, res, temp, i + 1, target - nums[i], used)
                used[i] = False
                temp.pop()

    def combinationSum2_dp1(self, candidates, target):
        candidates.sort()
        dp = [set() for i in xrange(target+1)]
        dp[0].add(())
        for num in candidates:
            for t in xrange(target, num - 1, -1):
                for prev in dp[t-num]:
                    dp[t].add(prev + (num,))
        return list(dp[-1])

    #dp 2:
    def combinationSum2(self, nums, target):
        nums.sort()
        dp = [set() for _ in range(target + 1)]
        dp[0].add(())
        for num in nums:
            for subtarget in range(target - num + 1):
                dp[subtarget + num] = {prev_list + (num,) for prev_list in dp[subtarget]}
        return list(map(list, dp[-1]))


so = Solution()
test = [10,1,2,7,6,1,5]
res = so.combinationSum2(test, 8)
print(res)