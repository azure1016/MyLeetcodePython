class Solution:
    def permute(self, nums):
        res = []
        self.backtrack(nums, res, [], 0)
        return res

    def backtrack(self, nums, res, temp, start):
        if start > len(nums): return
        if len(temp) == len(nums):
            res.append(list(temp))
        else:
            # temp[nums[start]] = nums[start]
            for i in range(len(nums)):
                if nums[i] in temp: continue
                temp.append(nums[i])
                self.backtrack(nums, res, temp, i + 1)
                temp.pop()

    # use rules of permutation
    def permute1(self, nums):
        return self.helper(nums, 0)

    def helper(self, nums, start):
        if start >= len(nums) - 1:
            res = []
            elem = nums[start]
            res.append([elem])
            return [[elem]]
            # return res
        res = []
        temp_list = self.helper(nums, start + 1)
        for ls in temp_list:
            for j in range(len(ls)):
                temp = list(ls) #pass by reference!
                temp.insert(j, nums[start])
                res.append(temp)
            temp = list(ls)
            temp.append(nums[start])
            res.append(temp)
        return res

so = Solution()
test = [1,2,3]
res = so.permute(test)
print(res)