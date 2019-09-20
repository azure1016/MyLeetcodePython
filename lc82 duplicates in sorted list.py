# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates1(self, head):
        if not head: return head
        newHead = None
        if head.next:
            if head.val == head.next.val:
                head = head.next
                while head and head.next:
                    if head.val != head.next.val:
                        newHead = head.next
                        break
                if not newHead: return None
            else:
                newHead = head
        else:
            newHead = head

    def deleteDuplicates(self, head):
        '''
        prev: the current node
        newHead: initialize to None
        for the very first 2 nodes: if prev != next, then newHead is determined, else:
            if next == prev, go to next, until next != prev, then prev = next; then repeat:  if next == prev, then go to next, until next != prev, prev := next
            repeat body is {if next == prev, go to next, until next != prev, then prev = next;} repeat condition is head and head.next are not None
            until we find a newHead
        set prev to the right node, then we begin deleting other duplicates
        '''
        if not head or not head.next: return head
        prev = head
        newHead = None
        newTail = None
        if head.val != head.next.val:
            newHead = head
            newTail = newHead
            prev = head.next
            head = head.next
            # head = head.next
            # newTail.next = None

        head = head.next

        while head:
            if head.val != prev.val:
                if not head.next:
                    newTail.next = prev
                    newTail = newTail.next
                    newTail.next = head
                    newTail = newTail.next
                    break
                if prev.next == head:
                    if not newHead:
                        newHead = prev
                        newTail = newHead
                        # newHeadTail.next = None
                    newTail.next = prev  # newHead.ext == newHea, a ring?
                    newTail = newTail.next
                    # newTail.next = None
                prev = head
            head = head.next
        newTail.next = None
        return newHead

def serialize(l):
    if not l: return None
    head = ListNode(l[0])
    runner = head
    for i in l[1:]:
        runner.next = ListNode(i)
        runner = runner.next
    return head

def deserialize(head):
    if not head: return None
    l = []
    while head:
        l.append(head.val)
        head = head.next
    return l
arr = [1,2,3,3,4,4,5,6]
so = Solution()
arrlist = serialize(arr)
reslist = so.deleteDuplicates(arrlist)
res = deserialize(reslist)
print(res)
