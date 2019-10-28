class BTrieNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BTrie:
    def generateBTrie(self, strings):
        root = BTrieNode("*")
        if not root: return 0
        for s in strings:
            node = root
            for ch in s:
                if ch == '0':
                    if not node.left:
                        node.left = BTrieNode(ch)
                    node = node.left
                else: 
                    if not node.right:
                        node.right = BTrieNode(ch)
                    node = node.right
        return root

    def maxDistance(self, strings):
        root = self.generateBTrie(strings)
        return self.recursion_helper(root)

    def recursion_helper(self, root):
        if not root.left: return self.recursion_helper(root.right)
        if not root.right: return self.recursion_helper(root.left)
        return self.treeDepth(root.left) + self.treeDepth(root.right)
        
    def treeDepth(self, root):
        if not root: return 0
        if not root.left and not root.right: return 1
        if not root.left: return self.treeDepth(root.right) + 1
        elif not root.right: return self.treeDepth(root.left) + 1
        leftDepth = self.treeDepth(root.left) 
        rightDepth = self.treeDepth(root.right) 
        return max(leftDepth, rightDepth) + 1
        
    
    def test(self, strings):
        print("---------------------")
        print(self.maxDistance(strings))
        print("---------------------")

sol = BTrie()
strings1 = ['1011000', '1011110']
strings2 = ['10101110', '10110', '1011101']
sol.test(strings1)
sol.test(strings2)

