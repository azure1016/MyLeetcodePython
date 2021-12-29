"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        parent, left = root, root.left
        while not self.isLeafNode(parent):
            nextParent = parent.left # leftmost node
            left = parent.left
            while parent and left:
                if parent.left == left:
                    right = parent.right
                else:
                    parent = parent.next
                    if parent:
                        right = parent.left
                    else:
                        right = None
                left.next = right
                left = left.next
            parent = nextParent
        return root

        
    def isLeafNode(self, node):
        return not node.left and not node.right