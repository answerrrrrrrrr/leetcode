# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = p = ListNode(0)
        p.next = head
        for _ in range(k):
            p = p.next
            if not p:
                return head
        p.next = self.reverseKGroup(p.next, k)
        while head != p:
            dummy.next, p.next, head.next = head.next, head, p.next
            head = dummy.next
        return dummy.next
