# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if sum == root.val and not root.left and not root.right:
            return True
        hps = self.hasPathSum
        return hps(root.left, sum - root.val) or hps(root.right, sum - root.val)