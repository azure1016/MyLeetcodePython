# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path = []
        res = []
        path.append((root, 0))
        while(len(path) > 0):
            current = path.pop()
            if current[0] == None:
                continue
            else:
                if current[1] == 1:
                    res.append(current[0].val)
                else:
                    path.append((current[0], 1))
                    if current[0].right != None:
                        path.append((current[0].right, 0))
                    if current[0].left != None:
                        path.append((current[0].left, 0))
        return res
    # recursive
    '''                
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is not None:
            res.extend(self.postorderTraversal(root.left))
            res.extend(self.postorderTraversal(root.right))
            res.append(root.val)
        return res
    '''