#from collections import set
class Solution(object):
    def fourSum(self, num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        num.sort()
        #one, two, three, four = 0, 1, len(num) - 2, len(num) - 1
        p, i, j, k = 0, 1, 2, len(num) - 1
        while j < k:
            while j < k:
                while j < k:
                    _sum = num[p] + num[i] + num[j] + num[k]
                    if _sum == target:
                        tup = (num[p], num[i], num[j], num[k])
                        #if not self.isDup(res, tup):
                        res.append(tup)
                        j += 1
                        continue
                    elif _sum > target:
                        k -= 1
                    else:
                        j += 1
                i += 1
                j = i + 1
                k = len(num) - 1
            p += 1
            i = p + 1
            j = i + 1
            k = len(num) - 1
        return set(res)
        #return res
    def isDup(self, res, tup):
        if len(res) == 0:
            return False
        for x in res:
            if x[0] == tup[0] and x[1] == tup[1]  and x[2] == tup[2] and x[3] == tup[3]:
                return True
        return False
#def find_array_quadruplet(arr, target):
#def delete_dup(self, res):
#if '__name__' == '__main__':
#arr = [-2, -1, 0, 0, 1, 2]
arr = [-5,-4,-3,-2,-1,0,0,1,2,3,4,5]
s = Solution()
print(s.fourSum(arr, 0))