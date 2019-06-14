class Solution:
    def threeSum(self, nums):
        if len(nums) < 3: return []
        nums.sort()
        res = {}
        for i in range(len(nums) - 2):
            if nums[i] > 0: return list(res.values())
            if nums[-1] == nums[-2] == nums[-3] == 0: return [[0, 0, 0]]
            sum_ = 0 - nums[i]
            l, h = i + 1, len(nums) - 1
            while l < h:
                addup = nums[l] + nums[h]
                if addup == sum_:
                    key = str(nums[i]) + str(nums[l]) + str(nums[h])
                    # print(key)
                    if key not in res.keys():
                        res[key] = [nums[x] for x in (i, l, h)]
                    l += 1
                elif addup < sum_:
                    l += 1
                else:
                    h -= 1
        return list(res.values())


so = Solution()
arr = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4]
res = so.threeSum(arr)
print(res)