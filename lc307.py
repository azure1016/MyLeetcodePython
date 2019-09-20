class SegTreeNode:
    def __init__(self, val, start, end):
        self.val = val
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class NumArray:
    # -------------Fenwick tree ---------------------------------
    #     def __init__(self, nums: List[int]):
    #         # self.tree = [0]+nums
    #         self.nums = [0] * len(nums)
    #         self.tree = [0] * (len(nums) + 1)
    #         for i, num in enumerate(nums):
    #             self.update(i, num)
    #         self.nums = nums

    #     def update(self, i: int, val: int) -> None:
    #         diff = val - self.nums[i]
    #         self.nums[i] = val
    #         i += 1
    #         while i < len(self.tree):
    #             self.tree[i] += diff
    #             i += self.lowbit(i)

    #     def query(self, idx):
    #         idx += 1
    #         sum_ = 0
    #         while idx > 0:
    #             sum_ += self.tree[idx]
    #             idx -= self.lowbit(idx)
    #         return sum_

    #     def sumRange(self, i: int, j: int) -> int:
    #         return self.query(j) - self.query(i-1)
    #     def lowbit(self, x):
    #         return x & (-x)

    # --------------segment tree -------------------------------
    def __init__(self, nums):
        self.root = self.construct(nums, 0, len(nums) - 1, 0)
        self.nums = nums

    def construct(self, nums, start, end, idx):
        if not nums or len(nums) == 0: return None
        root = SegTreeNode(0, start, end)
        if start == end:
            root.val = nums[start]
        else:
            mid = (start + end) // 2
            root.left = self.construct(nums, start, mid, idx * 2 + 1)
            root.right = self.construct(nums, mid + 1, end, idx * 2 + 2)
            root.val = root.left.val + root.right.val
        return root

    def query(self, node, i, j):
        if not node: return 0
        if i>j or j < node.start or i > node.end:
            return 0
        elif i == node.start and j == node.end:
            return node.val
        elif i >= node.start and j <= node.end:
            mid = (node.start + node.end) // 2
            return self.query(node.left, i, min(mid,j)) + self.query(node.right, max(mid+1, i), j)
        else:return self.query(node.left, i, j) + self.query(node.right, i, j)

    def updateTree(self, node, i, delta):
        if node and i <= node.end and i >= node.start:
            node.val += delta
            if node.left or node.right:
                self.updateTree(node.left, i, delta)
                self.updateTree(node.right, i, delta)
            else:
                self.nums[i] += delta  # not until reach the leaf, you dont update self.nums[i]

    def sumRange(self, i, j):
        return self.query(self.root, i, j)

    def update(self, i, val):
        self.updateTree(self.root, i, val - self.nums[i])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

'''
["NumArray","sumRange","sumRange","sumRange","update","update","update","sumRange","update","sumRange","update"]
[[[0,9,5,7,3]],[4,4],[2,4],[3,3],[4,5],[1,7],[0,8],[1,2],[1,9],[4,4],[3,4]]
'''
nums = [0,9,5,7,3]
obj = NumArray(nums)
param_1 = obj.sumRange(4,4)
param_2 = obj.sumRange(2,4)
param_3 = obj.sumRange(3,3)
obj.update(4,5)
obj.update(1,7)
obj.update(0,8)
param_4 = obj.sumRange(1,2)

obj.update(1,9)
param_5 = obj.sumRange(4,4)
print(param_1, param_2, param_3)