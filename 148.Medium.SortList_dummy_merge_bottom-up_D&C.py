# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        half = slow.next
        slow.next = None

    # 1. no-dummy
        def merge(l, r):
            if not l or not r:
                return l or r 
            if l.val > r.val:
                l, r = r, l 
            head = p = l 
            l = l.next
            while l and r:
                if l.val < r.val:
                    p.next = l
                    l = l.next
                else:
                    p.next = r 
                    r = r.next
                p = p.next
            p.next = l or r 
            return head

    # 2. dummy
        def merge(l, r):
            if not l or not r:
                return l or r
            dummy = p = ListNode(0)
            while l and r:
                if l.val < r.val:
                    p.next = l 
                    l = l.next
                else:
                    p.next = r
                    r = r.next
                p = p.next
            p.next = l or r 
            return dummy.next

        return merge(self.sortList(head), self.sortList(half))
