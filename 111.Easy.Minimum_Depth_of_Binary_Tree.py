# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
    # Recursive Solution
        # if not root:
        #     return 0
        # md = self.minDepth
        # if not root.left or not root.right:
        #     return md(root.left) + md(root.right) + 1
        # return min(md(root.left), md(root.right)) + 1


    # Recursive Solution with map()
        if not root: return 0
        d = map(self.minDepth, (root.left, root.right))
        return 1 + (min(d) or max(d))




    