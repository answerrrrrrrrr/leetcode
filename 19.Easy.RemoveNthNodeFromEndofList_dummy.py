# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        # p = q = head
        # while n:
        #     q = q.next
        #     n -= 1
        # if not q: # n == len, remove head
        #     return head.next
        # while q.next:
        #     p, q = p.next, q.next
        # p.next = p.next.next
        # return head



        # dummy
        dummy = p = q = ListNode(-1)
        dummy.next = head
        for _ in range(n):
            if not q.next:
                return 'n is out of range'
            q = q.next
        while q.next:
            p, q = p.next, q.next
        # p.next, p.next.next = p.next.next, None
        # MIND THE ORDER
        p.next.next, p.next = None, p.next.next
        return dummy.next   # NOT head
