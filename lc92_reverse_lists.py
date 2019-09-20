from lc_util import ListNode

class Solution:
    def reverseBetween(self, head, m, n):
        k = n - m + 1
        dummy = fast = slow = ListNode(0)
        dummy.next = head
        rev = None
        for _ in range(m - 1):
            fast = fast.next
        prev = fast
        fast = fast.next
        tail = fast
        for _ in range(k):
            rev, fast.next, fast = fast, rev, fast.next
        prev.next = rev
        tail.next = fast
        return dummy.next
