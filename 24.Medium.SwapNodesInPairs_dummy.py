# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    # rcs
    # 44ms
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead



    # itr
    # 44ms
        # dummy = p = ListNode(-1)
        # p.next = q = head
        # while q and q.next:
        #     p.next = q.next
        #     q.next = q.next.next
        #     p.next.next = q
        #     q, p = q.next, p.next.next
        # return dummy.next

        dummy = p = ListNode(0)
        dummy.next = head
        while head and head.next:
            h = head.next
            p.next, h.next, head.next = h, head, h.next
            p, head = head, head.next
        return dummy.next
