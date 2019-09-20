# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        if not head or not head.next: return head
        stack = []
        while head and head.next:
            stack.append(head)
            head = head.next
        node = head
        while stack:
            node.next = stack.pop()
            node = node.next
        return head

def serialise(l):
    if len(l) == 0: return None
    head = ListNode(l[0])
    node = head
    for x in l[1:]:
        head.next = ListNode(x)
        head = head.next
    return node

so = Solution()
ls = [1,2,3,4,5,1]
head = serialise(ls)
new_head = so.reverseList(head)
print(new_head.val)
