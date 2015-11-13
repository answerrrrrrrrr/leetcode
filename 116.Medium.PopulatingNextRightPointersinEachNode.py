# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
    # O(1) space
        level = p = root
        while p and p.left:
            p.left.next = p.right
            if p.next:
                p.right.next = p.next.left
                p = p.next
            else:
                level = p = level.left



    # O(1) space
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next