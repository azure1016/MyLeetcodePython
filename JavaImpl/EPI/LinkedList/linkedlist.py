class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
