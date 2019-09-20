#!/usr/bin/python
# -*- coding:utf8 -*-
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def deserialize(ls):
    if not ls or len(ls) == 0: return None
    root = TreeNode(ls[0])
    queue = [root]
    i = 0
    while queue and i < len(ls) - 2:
        cur = queue.pop(0)
        if cur:
            cur.left = TreeNode(ls[i+1]) if ls[i+1] else None
            cur.right = TreeNode(ls[i+2]) if ls[i+2] else None
            queue.append(cur.left)
            queue.append(cur.right)
            i += 2
    if queue and i == len(ls) - 2:
        cur = queue.pop(0)
        cur.left = TreeNode(ls[i+1])
    return root


class Solution:
    def preorderTraversal(self, root):
        res = []
        prev = None
        cur = root   #仅存放两个临时变量，O(1)空间复杂度
        while(cur):   #当前节点为空时，说明访问完成
            if not cur.left:   #左子树不存在时，访问+进入右节点
                res.append(cur.val)
                cur = cur.right
            else:   #左子树存在，寻找前驱节点。
                prev = cur.left
                while(prev.right and prev.right != cur): #注意寻找前驱节点时，会不断深入右子树。不加判断时，若前驱节点的右子树已指向自己，会引起死循环
                    prev = prev.right
                if not prev.right:  #前驱节点未访问过，存放后继节点
                    res.append(cur.val)
                    prev.right = cur
                    cur = cur.left
                else:   # prev.right == cur 前驱节点已访问过，恢复树结构
                    prev.right = None
                    cur = cur.right

        return res

    def inorderTraversal(self, root):
        if not root: return []
        cur, res = root, []
        prev = None
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    res.append(cur.val)
                    cur = cur.right
        return res

    def postorderTraversal(self, root):
        if not root: return []
        prev, dump = None, TreeNode(0)
        dump.left = root
        cur = dump
        res, reverse = [], []
        while cur:
            if not cur.left:
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                else:
                    runner = cur.left
                    while runner != cur:
                        reverse.append(runner.val)
                        runner = runner.right
                    res.extend(reverse[::-1])
                    reverse = []
                    prev.right = None
                    cur = cur.right
        return res
so = Solution()
ls = [4,2,5,1,3,None,6]
tree = deserialize(ls)
res = so.postorderTraversal(tree)
print(res)

