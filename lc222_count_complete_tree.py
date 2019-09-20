# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from lc_util import Tree, TreeNode
class Solution:
    def countNodes(self, root):
        h = -1
        node = root #
        while root:
            root = root.left
            h += 1
        print('height: ', h)
        hi, lo = pow(2, h) - 2, 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            leaf = self.getNode(node, h, mid)
            if leaf:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo + pow(2, h) - 1

    def getNode(self, node, h, i):
        root = node
        lo, hi = 0, 2 ** h - 1
        while root and lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid >= i: #
                root = root.left
                hi = mid - 1
            else:
                root = root.right
                lo = mid + 1
        return root

    def getNode1(self, root, h, i):
        print('height in getNode:', h)
        head, end = 0, pow(2, h) - 1
        print('first end:', end)
        while root and head <= end:
            mid = head + (end - head) // 2
            if i < mid:
                root = root.left
                end = mid
            else:
                root = root.right
                head = mid + 1
        return root


arr = [1]
tree = Tree(arr)
so = Solution()
#count = so.countNodes(tree.root)
#node = so.getNode(tree.root, 2, 2)
#print(count)
