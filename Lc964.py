class Solution:
    def leastOpsExpressTarget(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """
        res = ""
        root = Node(1, None)
        c_root = root
        half = int(x / 2)
        while target != 1 and target > 0:
            if target % x == 0:
                ln = Node(x, c_root)
                c_root.lc = ln
                c_root = ln
                target = target / x
            else: #find the right right-side node
                while half > 0:
                    if (target + half) % x == 0:
                        rn = Node(-half, c_root)
                        c_root.rc = rn
                        #c_root = rt #no need to change your c_root on right branch
                        target = target + half
                        break
                    elif (target - half) % x == 0:
                        rn = Node(half, c_root)
                        c_root.rc = rn
                        target = target - half
                        break
                    half = half - 1
        #traverse the whole tree for |l| times: |l| is the number of leaves
        stk = []
        stk.append(root)
        root.vd = True
        while len(stk) > 0: #use a stack to dfs the tree
            top = stk.pop()
            stk.append(top)
            if top.lc != None or top.rc != None:
                if top.lc != None and top.lc.vd == False: #visit left branch prioritly
                    stk.append(top.lc)
                    top.lc.vd = True
                elif top.rc != None and top.rc.vd == False:
                    stk.append(top.rc)
                    top.rc.vd = True
                else:
                    stk.pop() #this is not a leaf, but an internal node whose children already visited
                continue
            node = top # top.lc and rc is none, so top is a leaf
            stk.pop()
            res = res + self.leaf_to_root(node, x)
        res = res[1:]
        symbol = 0
        for e in res:
            if e == '*' or e == '+' or e == '-' or e == '/':
                symbol = symbol + 1
        return symbol

    #traverse the tree from leaf to root
    def leaf_to_root(self, node, x):
        res = ""
        if node.lc == None and node.rc == None:  # a leaf
            node.vd = True
            if node.data == x:
                poly = "+"
                while node.data != 1:
                    poly = poly + str(node.data) + "*"
                    node = node.par
                poly = poly[0:-1]
                res = poly + res
            elif node.data > 0:
                loop = node.data
                node = node.par
                poly = "+"
                if node.data == 1:
                    poly = poly + str(x) + "/" + str(x)
                    while loop != 0:
                        loop = loop - 1
                        res = res + poly
                else:
                    while node.data != 1:  # not the root
                        poly = poly + str(x) + "*"
                        node = node.par
                    poly = poly[0:-1]
                    while loop != 0:
                        loop = loop - 1
                        res = res + poly
            elif node.data < 0:
                loop = -node.data
                node = node.par
                poly = "-"
                if node.data == 1:
                    poly = poly + str(x) + "/" + str(x)
                    while loop != 0:
                        loop = loop - 1
                        res = res + poly
                while node.data != 1:  # not the root
                    poly = poly + str(x) + "*"
                    node = node.par
                poly = poly[0:-1]
                while loop != 0:
                    loop = loop - 1
                    res = res + poly
        return res


class Node:
    def __init__(self, data, parent, ln = None, rn = None):
        self.data = data
        self.lc = ln
        self.rc = rn
        self.vd = False # it's visited or not
        self.par = parent #parent node

if __name__ == "__main__":
    ins = Solution()
    print(ins.leastOpsExpressTarget(5,6))