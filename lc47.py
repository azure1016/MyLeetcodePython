class Solution:
    # use rules of permutation
    # if duplicated, insert it after the number
    def permuteUnique(self, nums):
        if not nums or len(nums) == 0: return [[]]
        res = []
        return self.helper(nums, 0)

    def helper(self, nums, start):
        if start == len(nums) - 1: return [[nums[start]]]
        res = []
        temp_list = self.helper(nums, start + 1)
        for ls in temp_list:
            for j in range(len(ls)):
                if nums[start] == ls[j]: continue
                temp = list(ls)
                temp.insert(j, nums[start])
                res.append(list(temp))
            # if ls[-1] == nums[start]:
            ls.append(nums[start])
            res.append(ls)
        return res

so = Solution()
test = [1,1,2]
res = so.permuteUnique(test)
print(res)