# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        # Iterative Solution
        # last = None
        # while head:
        #     head.next, last, head = last, head, head.next
        # return last





        # Recursive Solution:
        if head is None:
            return None
        if head.next is None:
            return head
        p = head.next
        rHead = self.reverseList(head.next)
        head.next = None
        p.next = head
        return rHead
