class Treenode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

class Tree:
    def __init__(self, aList):
        if len(aList) == 0:
            self.root = None
            return
        self.root = Treenode(aList[0])
        que = [self.root]
        i = 0
        while (len(que) > 0):
            cur = que.pop(0)
            if i + 1 == len(aList) - 1:
                cur.left = Treenode(aList[i + 1])
                break
            elif i < len(aList) - 2:
                cur = que.pop(0)
                ln = Treenode(aList[i + 1])
                rn = Treenode(aList[i + 2])
                cur.left = ln
                cur.right = rn
                que.append(ln)
                que.append(rn)
            i = i + 2
        return



class Solution:
    def findTilt(self, root):
        if root == None:
            return 0
        tilt = self.node_tilt(root)
        tilt = tilt + self.node_tilt(root.right)
        tilt = tilt + self.node_tilt(root.left)
        return tilt

    def node_tilt(self, node):
        if node == None:
            return 0
        tilt_n = abs(self.sum_tree(node.right) - self.sum_tree(node.left))
        return tilt_n

    def sum_tree(self, node):
        if node == None:
            return 0
        sum_ = node.val
        sum_ = sum_ + self.sum_tree(node.right)
        sum_ = sum_ + self.sum_tree(node.left)
        return sum_

so = Solution()
aList = []

