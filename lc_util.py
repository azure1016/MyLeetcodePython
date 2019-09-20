class ListNode:
    def __init__(self,val):
        self.next = None
        self.val = val

    def deserialize(self, arr):
        if not arr or len(arr) == 0: return None
        head = ListNode(arr[0])
        dummy = head
        for i in range(1, len(arr)):
            head.next = ListNode(arr[i])
            head = head.next
        return dummy

    def serialize(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    # construct a tree with an array
    def __init__(self, a_list):
        if len(a_list) == 0:
            self.root = None
            return
        queue = []
        self.root = TreeNode(a_list[0])
        queue.append(self.root)
        i = 0
        while len(queue) > 0:
            cur = queue.pop(0)
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

    def deserialize(self, ls):
        if not ls or len(ls) == 0: return None
        root = TreeNode(ls[0])
        queue = [root]
        i = 0
        while queue and i < len(ls) - 2:
            cur = queue.pop(0)
            if cur:
                cur.left = TreeNode(ls[i + 1]) if ls[i + 1] else None
                cur.right = TreeNode(ls[i + 2]) if ls[i + 2] else None
                queue.append(cur.left)
                queue.append(cur.right)
                i += 2
        if queue and i == len(ls) - 2:
            cur = queue.pop(0)
            cur.left = TreeNode(ls[i + 1])
        return root