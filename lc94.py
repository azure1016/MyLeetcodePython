# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self, a_list):
        if len(a_list) == 0:
            self.root = None
            return
        queue = []
        self.root = TreeNode(a_list[0])
        queue.append(self.root)
        i = 0
        while len(queue) > 0:
            cur = queue.pop()
            if i + 1 == len(a_list) - 1:
                if a_list[i + 1] != None:
                    cur.left = TreeNode(a_list[i + 1])
            elif i < len(a_list) - 2:
                if a_list[i + 1] != None:
                    cur.left = TreeNode(a_list[i+1])
                    queue.append(cur.left)
                if a_list[i + 2] != None:
                    cur.right = TreeNode(a_list[i+2])
                    queue.append(cur.right)
            i = i + 2

class Solution:
    def inorderTraversal(self, root):
        res = []
        #self.recurDFS(root, res)
        res = self.iterDFS(root)
        return res

    def iterDFS(self, root):
        res = []
        if root == None:
            return res
        stackTr = [(0, root)]

        while (len(stackTr) > 0):
            cur = stackTr.pop()
            if cur[0] == 1:
                res.append(cur[1].val)
                if cur[1].right != None:
                    stackTr.append((0, cur[1].right))
            else:
                if cur[1].left != None:
                    stackTr.append((1,cur[1]))
                    stackTr.append((0,cur[1].left))
                else:
                    res.append(cur[1].val)
                    if cur[1].right != None:
                        stackTr.append((0,cur[1].right))
        return res

    def recurDFS(self, root, res):
        if root == None:
            return
        self.recurDFS(root.left, res)
        res.append(root.val)
        self.recurDFS(root.right, res)


so = Solution()
test_case = [1, None, 2, 3]
test_case2 = [1, 2, None, 3, None]
test_case3 = [1, None, 2, None, 3]
test_case4 = [1, None, 2, 3, 4, None, 5]
test_case5 = []
a_tree = Tree(test_case4)
res = so.inorderTraversal(a_tree.root)
print(res)

