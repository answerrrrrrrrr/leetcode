# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if not root:
            return True
        return self.s(root.left, root.right)

    def s(self, l, r):
        if l and r:
            return l.val == r.val and self.s(l.left, r.right) and self(l.right, r.left)
        return l == r