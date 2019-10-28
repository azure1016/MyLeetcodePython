class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class DoublyListNode(ListNode):
    def __init__(self, val):
        super(DoublyListNode, self).__init__(val)
        self.prev = None

    
def merge_two_sorted_list(l1, l2):
    dummy = tail = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next

def merge_doubly_sorted_list(l1, l2):
    dummy = tail = DoublyListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1.prev = tail
            #l1.next.prev = None
            l1 = l1.next
        else:
            tail.next = l2
            l2.prev = tail
            l2 = l2.next
        tail = tail.next
    if not l1:
        tail.next = l2
        l2.prev = tail
    else:
        tail.next = l1
        l1.prev = tail
    dummy.next.prev = None
    return dummy.next

def test_doubly_linked_list(l1, l2):
    l = merge_doubly_sorted_list(l1, l2)
    print("traverse from left to right:")
    while l and l.next:
        print(l.val)
        l = l.next
    print(l.val)

    print("traverse from right to left:")
    while l and l.prev:
        print(l.val)
        l = l.prev
    print(l.val)


def deserialiseDoublyLinkedList(l):
    nodes = []
    for val in l:
        nodes.append(DoublyListNode(val))
    dummy = head = nodes[0]
    for node in nodes[1:]:
        head.next = node
        node.prev = head
        head = node
    return dummy

l1 = deserialiseDoublyLinkedList([2,3,5,7])
l2 = deserialiseDoublyLinkedList([1,2,3])
test_doubly_linked_list(l1, l2)
