# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
    # reverse & insert
    # 144ms
        if not head:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # reverse the 2rd half
        rev = None
        while slow.next:
            rev, rev.next, slow.next = slow.next, rev, slow.next.next
        # insert 1 by 1
        p = head
        while rev:
            p.next, p = rev, p.next
            rev.next, rev = p, rev.next