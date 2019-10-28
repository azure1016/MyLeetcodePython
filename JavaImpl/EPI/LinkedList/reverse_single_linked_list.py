class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
def reverse_sublist_EPI(L, start, finish):
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next
    
    # reverse sublist
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        # temp.next should be sublist_head.next rather than sublist_iter
        # only in the first round sublist_head.next and sublist_iter point to the same node!!
        sublist_iter.next, temp.next, sublist_head.next = temp.next, sublist_head.next, temp
    return dummy_head.next

def reverse_sublist(L, start, finish):
    # index is starting from 1, so start >= 1
    dummy = node = ListNode(-1)
    dummy.next = L
    for i in range(start):
        node = node.next
        if not node: return dummy
    
    left = node
    rev = node.next
    node = rev.next
    rev.next = None
    for i in range(finish - start):
        rev, node.next, node = node, rev, node.next

    left.next.next = node
    left.next = rev
    return dummy.next

def deserialise(l):
    head = dummy = ListNode(l[0])
    for val in l[1:]:
        head.next = ListNode(val)
        head = head.next
    return dummy


def printList(newHead):
    while newHead:
        print(newHead.val)
        newHead = newHead.next

def test_reverse_sublist(l):
    head = deserialise(l)
    newHead = reverse_sublist(head, 0, len(l) - 1)
    printList(newHead)


def test_EPI(l, start, finish):
    head = deserialise(l)
    newHead = reverse_sublist_EPI(head,start, finish)
    printList(newHead)

#test_reverse_sublist([1,2,3,4,5,6,7,8,9])
test_EPI([1,2,3,4,5,6,7], 1, 3)


    
