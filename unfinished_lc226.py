class Treenode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self, a_list):
        if a_list:
            self.root = Treenode(a_list[0])
            i = 0
            queue = [self.root]
            while queue and i < len(a_list) - 1:
                cur = queue.pop(0)
                if cur:
                    cur.left = Treenode(a_list[i+1])
                    if i < len(a_list) - 2:
                        cur.right = Treenode(a_list[i+2])


class soluton:
    def lowestCommonAncestor(self, root, p, q):
        