class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def oddEvenList(self, head):
        if not head: return head
        dummy = odd = ListNode(-1)
        dummy_even = even = ListNode(-1)
        k = 0
        while head:
            if k % 2 == 0:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            k += 1
        odd.next = dummy_even.next
        even.next = None
        return dummy.next

def deserialize(arr):
    if not arr or len(arr) == 0: return None
    head = ListNode(arr[0])
    dummy = head
    for i in range(1, len(arr)):
        head.next = ListNode(arr[i])
        head = head.next
    return dummy

def serialize(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res
so = Solution()
arr = [1,2,3,4,5]
head = deserialize(arr)
res = so.oddEvenList(head)
new_arr = serialize(res)
print(new_arr)