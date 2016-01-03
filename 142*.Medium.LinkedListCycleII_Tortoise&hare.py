# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
# https://leetcode.com/discuss/43146/share-my-python-solution-with-detailed-explanation
        ret = slow = fast = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                while ret is not slow:
                    ret, slow = ret.next, slow.next
                return ret 
        return None