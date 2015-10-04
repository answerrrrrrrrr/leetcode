# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
    # k %= length
    # 56ms
        if not head or k == 0:
            return head
        tail, length = head, 0
        while tail:
            tail = tail.next
            length += 1
        k %= length
        p = q = head
        for _ in xrange(k):
            q = q.next
        while q.next:
            p, q = p.next, q.next
        # head, p.next, q.next = p.next, None, head 
        # WA --> [1,2] & 2 
        # Watch the order
        q.next = head
        head = p.next
        p.next = None
        return head

