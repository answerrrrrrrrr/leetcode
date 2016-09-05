# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
    # 1 new list
        dummy = p = ListNode(0)
        dummy.next = head
        new = q = ListNode(0)
        while head:
            if head.val < x:
                head, p = head.next, p.next
            else:
                q.next = head
                p.next = head.next
                head = head.next
                q = q.next
        q.next = None   # important
        p.next = new.next
        return dummy.next



    # 2 new list
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next
        return h1.next