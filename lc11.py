import numpy as np


class Solution:
    def maxArea1(self, height):
        i, j, (cap, I, J) = 0, len(height) - 1, (0, 0, len(height) - 1)
        while i < j:
            cap_now = min(height[i], height[j]) * (j - i)
            if cap < cap_now:
                cap, I, J = cap_now, i, j
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return cap

    def maxArea(self, height):
        idx = np.argsort(-np.array(height))
        cap, width = 0, 0
        for i, x1 in enumerate(idx):
            for j, x2 in enumerate(idx[i + 1:]):
                if abs(x1 - x2) >= width:
                    width = abs(x1 - x2)
                    cap = max(cap, width * height[x2])
        return cap


so = Solution()
height = [1,2,4,3]
print(so.maxArea(height))

