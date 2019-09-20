from lc_util import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return headA or headB
        pa = headA
        while pa and pa.next:
            pa = pa.next
        breaker = pa
        pa.next = headB
        slow = fast = headA
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast: break
        if not fast or not fast.next:
            breaker.next = None
            return None
        slow = headA
        while slow != fast:
            slow = slow.next
            fast = fast.next
        breaker.next = None
        return slow


def stringToInt(input):
    return int(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            intersectVal = stringToInt(line)
            line = lines.next()
            listA = stringToListNode(line)
            line = lines.next()
            listB = stringToListNode(line)
            line = lines.next()
            skipA = stringToInt(line)
            line = lines.next()
            skipB = stringToInt(line)

            ret = Solution().getIntersectionNode(intersectVal, listA, listB, skipA, skipB)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()