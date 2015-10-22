# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """ 
        dummy = p = ListNode(0)
        p.next = head
        for _ in xrange(m-1):
            p = p.next
        q = p.next
        for _ in xrange(n-m):
            p.next, q.next.next, q.next = q.next, p.next, q.next.next
        return dummy.next