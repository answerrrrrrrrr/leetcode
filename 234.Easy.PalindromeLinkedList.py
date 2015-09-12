# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            # slow, slow.next, rev = slow.next, rev, slow --- Error: 'NoneType' object has no attribute 'next'
            rev, slow.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        # while slow:
        #     if slow.val != rev.val:
        #         return False
        #     slow, rev = slow.next, rev.next
        # return True
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        return not rev



    # Solution with Restoring the original list
        rev = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, head.next, head = head, rev, head.next
        tail = head.next if fast else head
        isPali = True
        while rev:
            isPali = isPali and rev.val == tail.val
            tail = tail.next
            rev.next, rev, head = head, rev.next, rev
        return isPali














