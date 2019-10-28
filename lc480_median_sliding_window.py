from heapq import *


class Solution:
    def __init__(self):
        self.max_heap = []  # store left values of median
        self.min_heap = []  # store right values of median

    def medianSlidingWindow(self, nums, k):
        self.max_heap.append(-nums[0])
        # initializing
        for i in range(1, k):
            self.insert(nums[i])
        result = [self.getMedian()]
        for i in range(k, len(nums)):
            self.insert(nums[i])
            result.append(self.getMedian())
        return result

    def insert(self, val):
        m = self.getMedian()
        if val < m:  # left values
            heappush(self.max_heap, -val)
        else:
            heappush(self.min_heap, val)
        if len(self.min_heap) + 1 < len(self.max_heap):
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def getMedian(self):
        if len(self.min_heap) == len(self.max_heap):
            right = self.min_heap[0]
            left = -self.max_heap[0]
            return (left + right) * 0.5
        return -self.max_heap[0]


sol = Solution()
arr = [1,3,-1,-3,5,3,6,7]
k = 3
res = sol.medianSlidingWindow(arr, k)
print(res)