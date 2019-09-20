
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, root):
        if not root or (not root.child and not root.next):
            return root
        else:
            if root.next and not root.child:
                return self.flatten(root.next)
            elif root.child and (not root.next):
                root.next = root.child
                root.child.prev = root
                root.child = None
                return self.flatten(root.next)
            else:
                temp = root.next
                root.next = root.child
                print(root.val)
                root.child.prev = root
                root.child = None
                last_node = self.flatten(root.next)
                last_node.next = temp
                temp.prev = last_node
                return self.flatten(last_node.next)

    def print_linked_list(node, back=False):
        result = ''
        while node:
            result += ('->' if result else '') + str(node.val)
            if back:
                node = node.prev
            else:
                node = node.next
        print(result)
