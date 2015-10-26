# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
    # https://leetcode.com/discuss/51961/python-recursive-solution-detailed-comments-operate-directly
    # O(nlogn) time
        if not head:
            return 
        if not head.next:
            return TreeNode(head.val)
        slow = head   # NOT head.next !!!
        fast = head.next.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        tmp = slow.next
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root



# https://leetcode.com/discuss/46272/python-solutions-convert-array-first-approach-bottom-approach
# O(n)
    # list to array
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        return self.helper(ls, 0, len(ls)-1)

    def helper(self, ls, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(ls[start])
        mid = (start+end) >> 1
        root = TreeNode(ls[mid])
        root.left = self.helper(ls, start, mid-1)
        root.right = self.helper(ls, mid+1, end)
        return root



    # bottom-up
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        self.node = head
        return self.convert(0, l-1)

    def convert(self, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        l = self.convert(start, mid-1)
        root = TreeNode(self.node.val)
        root.left = l
        self.node = self.node.next 
        root.right = self.convert(mid+1, end)
        return root
