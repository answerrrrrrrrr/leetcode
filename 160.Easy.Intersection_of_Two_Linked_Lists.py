# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        # a' = a + b, b' = b + a
        # len(a') == len(b')
        if None in (headA, headB):
            return None
        p, q = headA, headB
        while p is not q:# extremely faster than p!=q
            p = headB if not p else p.next
            q = headA if not q else q.next
        return p

        # Others
        # https://leetcode.com/discuss/51697/python-solutions-o-m-n-space-and-o-1-space