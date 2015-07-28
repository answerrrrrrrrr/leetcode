# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if head is None or head.next is None:
        	return True
        
        #find middle/first-middle node: slow
        fast = slow = head
        while fast.next and fast.next.next:
        	slow = slow.next
        	fast = fast.next.next

        #reverse the second half: reversal
        reversal = None
        p = slow.next
        while p:
        	q = p.next
        	p.next = reversal
        	reversal = p
        	p = q

        #check palindrome: .val
        p1, p2 = head, reversal
        #p2 may be 1-node shorter
        while p2 and p1.val == p2.val: 
        	p1, p2 = p1.next, p2.next
        # while p2:
        #     if p1.val == p2.val:
        #         p1, p2 = p1.next, p2.next
        #     else:
        #         return False
        return p2 is None
		
		# #resume the second half: resume
		# resume = None
		# p = reversal
		# while p:
		# 	q = p.next
		# 	p.next = resume
		# 	resume = p
		# 	p = q
		# slow.next = resume
