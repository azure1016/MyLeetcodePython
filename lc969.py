import math


class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        last = len(A)
        while (last > 0):
            k = self.max_idx(A[0 : last])  #  point to the k th element
            res.append(k)
            self.flip(A[0: k])
            res.append(last)
            self.flip(A[0: last])
            last = last - 1
        return res

    def max_idx(self, arr):  # dictionary is better
        max = 0
        idx, index = 0, 0
        for i in arr:
            index = index + 1
            if max < i:
                max = i
                idx = index
        return idx

    def flip(self, Arr):
        mid = math.floor(len(Arr) / 2)
        for i in range(0, mid):
            Arr[i], Arr[len(Arr) - i - 1] = Arr[len(Arr) - i - 1], Arr[i]
        return Arr


if __name__ == "__main__":
    s = Solution();
    A = [3, 2, 4, 1]
    print(s.pancakeSort(A))