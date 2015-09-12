# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        # dummy = ListNode(-1)
        # dummy.next = head
        # p = dummy
        # while p.next:
        #     if p.next.val == val:
        #         p.next = p.next.next
        #     else:
        #         p= p.next
        # return dummy.next



        # Recursive Solution
        if not head:
            return head
        head.next = removeElements(head.next, val)
        return head.next if head.val == val else head
        # RuntimeError: maximum recursion depth exceeded
        # Works in local environment