# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        # p = dummy = ListNode(-1)
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         p.next = l1 
        #         l1 = l1.next
        #     else:
        #         p.next = l2 
        #         l2 = l2.next
        #     p = p.next
        # p.next = l1 or l2 
        # return dummy.next



        # Recursive Solution
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1 
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2