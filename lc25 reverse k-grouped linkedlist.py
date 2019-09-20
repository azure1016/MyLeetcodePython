class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(-1)
        runner = dummy
        while head:
            newHead, newTail = self.helper(head, k)
            runner.next = newHead
            if not newTail: return dummy.next
            head = newTail.next
            runner = newTail
        return dummy.next

    def helper(self, head, k):  # returns newHead and newTail
        counter = 0
        if not head: return head
        newTail = head
        while head and counter < k - 1:
            counter += 1
            head = head.next
        if not head:
            return newTail, head  # if less than k nodes
        else:  # counter == k-1, head is the k-th node
            newHead = newTail.next
            newTail.next = head.next  # the next k nodes
            head = newTail
            while counter:
                #newHead, newHead.next, head = newHead.next, head, head.next
                temp = newHead.next
                newHead.next = head
                head = newHead
                newHead = temp
                counter -= 1
        return head, newTail

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

arr = [1,2,3,4,5,6,7]
so = Solution()
head = deserialize(arr)
res = so.reverseKGroup(head, 3)
newArr = serialize(res)
print(newArr)
