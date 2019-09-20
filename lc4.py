class Solution(object):
    ''' Messy code written: you can learn from mistakes
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        start, end = 0, m
        while start <= end:
            i = (start + end) / 2
            j = (n + m + 1)/2 - i

            if i > 0 and nums1[i-1] > nums2[j]:
                end = i - 1
            elif i < m and nums2[j-1] > nums1[i]:
                start = i + 1
            else:
                if i==0:
                    max_left = nums2[j-1]
                    # min_right = min(nums1[i], nums2[j])
                elif i==m:
                    min_right = nums2[j]
                    # max_left = max(nums1[i-1], nums2[j-
                # else:
                if j == 0:
                    max_left = nums1[i - 1]
                    # min_right = min(nums1[i], nums2[j])
                elif j == n:
                    min_right = nums1[i]
                    # max_left = max(nums1[i-1], nums2[j-1])
                else:
                    min_right = min(nums1[i], nums2[j])
                    max_left = max(nums1[i-1], nums2[j-1])
                if (n+m) % 2: #odd
                    return max_left
                else:
                    return (float(min_right) + float(max_left)) / 2
        '''
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            m, n, A, B = n, m, B, A
        start, end = 0, m
        while start <= end:
            i = (start + end) // 2
            j = (m + n + 1)//2 - i
            if i > 0 and A[i-1] > B[j]:#i is too big
                end = i - 1
            elif i < m and B[j-1] > A[i]: #j is too big, then you should increase i to decrease j
                start = i + 1
            else: # i is already perfect
                if i == 0:
                    max_left = B[j-1]
                elif j == 0:
                    max_left = A[i-1]
                else:max_left = max(A[i-1], B[j-1])

                if (m + n) % 2: return max_left

                if i == m:
                    min_right = B[j]
                elif j == n:
                    min_right = A[i]
                else:min_right = min(A[i], B[j])

                return (min_right + max_left) / 2.0

so = Solution()
nums1 = [1,2]
nums2 = [3,4]
res = so.findMedianSortedArrays(nums1, nums2)
print(res)