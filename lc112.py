class Treenode:
    def __init__(self, x):
        if x:
            self.val = x
            self.left = None
            self.right = None

class Tree:
    def __init__(self, a_list):
        self.root = None
        if len(a_list) > 0:
            self.root = Treenode(a_list[0])
            que = [self.root]
            i = 0
            while que:
                current = que.pop(0)
                if current != None:
                    if i < len(a_list) - 2:
                        if a_list[i+1] != None:
                            current.left = Treenode(a_list[i+1])
                        else:
                            current.left = None
                        if a_list[i+2] != None:
                            current.right = Treenode(a_list[i+2])
                        else:
                            current.right = None
                        que.append(current.left)
                        que.append(current.right)
                        i = i + 2
                    if i == len(a_list) - 2:
                        current.left = Treenode(a_list[i + 1])
                        que.append(current.left)


class Solution:
    def pathSum(self, root, sum_):
        if not root:
            return []
        if not root.left and not root.right:
            if root.val == sum_:
                return [[root.val]]
            else:
                return []
        else:
            res = []
            r = self.pathSum(root.right, sum_ - root.val)
            l = self.pathSum(root.left, sum_ - root.val)
            if r:
                for x in r:
                    if x:
                        tmp = [root.val]
                        tmp.extend(x)
                        res.append(tmp)
            if l:
                for x in l:
                    if x:
                        tmp = [root.val]
                        tmp.extend(x)
                        res.append(tmp)
            if len(res) > 0:
                return res
            else:
                return []

so = Solution()
a_list = [5,4,8,11,None,13,4,7,2,None,None,5,1]
b_list = [1]
#tree = Tree(a_list)
tree = Tree(b_list)
print(so.pathSum(tree.root, 0))