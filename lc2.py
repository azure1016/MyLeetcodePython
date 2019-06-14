import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        l3 = head
        last_shang = 0
        while l1 and l2:
            sum_ = l1.val + l2.val + last_shang
            yu = sum_ % 10
            last_shang = math.floor(sum_ / 10)
            l3.val = yu
            l3.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        if l1:
            l3.val += l1.val
            l3.next = l1.next
        elif l2:
            l3.val += l2.val
            l3.next = l2.next
        elif l3.val == 0:
            del l3
        return head


so = Solution()
l1 = [2,4,3]
l2 = [5,6,4]

def parse(lst):
    head = ListNode(lst[0])
    nx = head
    for i in range(1, len(lst)):
        nx.next = ListNode(lst[i])
    return head

def deserialize(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

l1n = parse(l1)
l2n = parse(l2)

l3n = so.addTwoNumbers(l1n, l2n)
print(deserialize(l3n))