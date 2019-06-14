from collections import Counter


class Solution:
    def majorityElement(self, nums):
        record = {}
        for num in nums:
            if num in record.keys():
                record[num] += 1
            else:
                record[num] = 1
        v, k = 0, 0
        for key, val in record.items():
            if val > v:
                v = val
                k = key
        return k

    def majorityElement2(self, nums):
        cand, vote = nums[0], 1
        for i in range(1, len(nums)):
            if vote == 0:
                cand = nums[i]
                vote += 1
            elif cand == nums[i]:
                vote += 1
            else:
                vote -= 1
        return cand

    def majorityElement3(self, nums):
        counter = Counter(nums)
        return counter.most_common(1)[0][0]

so = Solution()
arr = [3,2,3,4,5,6,7,8]
r1 = so.majorityElement(arr)
r2 = so.majorityElement2(arr)
r3 = so.majorityElement3(arr)
print(r1, r2, r3)