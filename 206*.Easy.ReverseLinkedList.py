# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        # itr(head)
        new = None
        while head:
            head.next, new, head = new, head, head.next
        return new


        # rcs(tail)
        if not head or not head.next:
            return head
        p = head.next   # become the last node after reverseList(head.next)
        new = self.reverseList(head.next)
        head.next = None
        p.next = head
        return new


        # rcs(head)
        def move(h1, h2):
            if not h1:
                return h2
            new_h1 = h1.next
            h1.next = h2
            new_h2 = h1
            return move(new_h1, new_h2)
        return move(head, None)
