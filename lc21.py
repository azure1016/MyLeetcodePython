class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        if l1.val <= l2.val:
            head = l1
        else:
            head = l2
        while l1 and l2:
            if l1.val <= l2.val:
                temp1 = l1.next
                l1.next = l2
                l1 = l1.next
                l2 = temp1
            else:
                temp = l2.next
                l2.next = l1
                l2 = l2.next
                l1 = temp
        return head
    def mergeTwoLists4(self, l1, l2):
        if not l1:return l2
        elif not l2:return l1
        head = l1 if l1.val <= l2.val else l2
        while l1 and l2:
            while l1.val < l2.val:
                l1 = l1.next
            temp2 = l2.next
            l2.next = l1
            while l2.val < l1.val:
                l2 = l2.next

    def mergeTwoLists3(self, l1, l2):
        if not l1:return l2
        elif not l2:return l1
        head = l1 if l1.val <= l2.val else l2
        while l1 and l2:
            # if l1.next and l1.val < l2.val and l1.next.val > l2.val:
            #     temp1 = l1.next
            #     temp2 = l2.next
            #     l1.next = l2
            #     l2.next = temp1
            #     l1 = l1.next
            #     l2 = temp2
            # elif not l1.next and l1.val < l2.val:
            #     l1.next = l2
            #     break
            # elif l2.next and l2.val < l1.val and l2.next.val > l1.val:
            if l1.val <= l2.val:
                if l1.next:
                    if l1.next.val <= l2.val:
                        l1 = l1.next
                temp1 = l1.next
                l1.next = l2
                l1 = l1.next
                l2 = temp1
                else:
                    l1 = l1.next
                    continue
            else:
                if l2.next and l2.next.val > l1.val:
                    temp2 = l2.next
                    l2.next = l1
                    l2 = l2.next
                    l1 = temp2
                else:
                    l2 = l2.next
                    continue
        return head



    # beat 97%, 5%
    def mergeTwoLists2(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        head = ListNode(0)
        runner = head
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1:
            head.next = l1
        else:
            head.next = l2
        return runner.next

def deserialise(l):
    head = ListNode(l[0])
    runner = head
    for i in range(1, len(l)):
        head.next = ListNode(l[i])
        head = head.next
    return runner

def serialise(listnode):
    res = []
    while listnode:
        res.append(listnode.val)
        listnode = listnode.next
    return res

l1 = deserialise([5])
l2 = deserialise([1,3,4])

so = Solution()
newNode = so.mergeTwoLists(l1, l2)
res = serialise(newNode)
print(res)