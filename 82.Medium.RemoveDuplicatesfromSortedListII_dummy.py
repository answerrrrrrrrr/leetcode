# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    # 60ms
        dummy = p = ListNode(0)
        dummy.next = head
        dup = None
        while head and head.next:
            if head.val == head.next.val:
                dup = head.val
                head = p.next = head.next.next
                while head and head.val == dup:
                    head = p.next = head.next
            else:
                p, head = p.next, head.next
        return dummy.next



    # logic optimized, O(1) space
    # 60ms
        dummy = p = ListNode(0)
        dup = None
        while head:
            if head.next and head.val == head.next.val:
                dup = head.val
            if dup != head.val:
                p.next = p = head
            head = head.next
        p.next = head # None
        return dummy.next



    # total in-place
    # 60ms
        dummy = p = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                p.next = head
            else:
                p, head = p.next, head.next
        return dummy.next