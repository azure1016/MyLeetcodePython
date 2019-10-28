# Definition for singly-linked list.
from linkedlist import *

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = node = ListNode(0)
        dummy.next = head
        n = self.list_length(head)
        for start in range(0, n-k+1, k):
            sub_head, sub_tail = self.reverse_sublist(node.next, 0, k)
        return dummy.next

    def reverse_sublist(self, head, start, finish):
        # index starting from 0,'finish' is exclusive
        dummy = sublist_head = ListNode(0)
        dummy.next = head
        for i in range(start):
            sublist_head = sublist_head.next
        sublist_iter = sublist_head.next
        for i in range(finish - start):
            # if not sublist_iter:

            temp = sublist_iter.next
            sublist_head.next, temp.next, sublist_iter = temp, sublist_head.next, temp.next
        
        return dummy.next

    def list_length(self, nodes):
        head = nodes
        count = 0
        while head:
            count += 1
            head = head.next
        return count


# def deserialise(l):
#     head = dummy = ListNode(l[0])
#     for val in l[1:]:
#         head.next = ListNode(val)
#         head = head.next
#     return dummy

def test(l, k):
    head = deserialise(l)
    sol = Solution()
    newhead = sol.reverseKGroup(head, k)
    printList(newhead)

test([1,2,3,4,5], 2)
