from collections import Counter


class Solution:
    def overlap(self, nums1, nums2):
        if len(nums2) > len(nums1):
            nums2, nums1 = nums1, nums2
        d = Counter(nums1)
        res = set()
        for num in nums2:
            if num in d: res.add(num)
        return res

    def overlap_sorted(self, nums1, nums2):
        p1, p2 = 0, 0
        res = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                if not res or res[-1] != nums1[p1]:
                     res.append(nums1[p1])
                # increase either pointer
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]: p1 += 1
            else: p2 += 1
        return res


so = Solution()
input = [1,1,2,2,2,3,4]
inp = [2, 3, 3]
res = so.overlap_sorted(input, inp)
print(res)
