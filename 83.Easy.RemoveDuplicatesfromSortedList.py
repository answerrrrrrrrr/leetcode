# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#     def __del__(self):
#         self.val = None
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        p = head
        while p and p.next:
            if p.val == p.next.val:
                q = p.next
                p.next = q.next
                del q
            else:
                p = p.next
        return head