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
    # Recursive Solution
    #     if not root:
    #         return False
    #     if sum == root.val and not root.left and not root.right:
    #         return True
    #     hps = self.hasPathSum
    #     return hps(root.left, sum - root.val) or hps(root.right, sum - root.val)
        


    # Iterative Solution
        if not root:
            return False
        stack = [(root, sum)]
        while stack:
            node, sum = stack.pop()
            if node.left is node.right is None and node.val == sum:
                return True
            if node.left:
                stack.append((node.left, sum - node.val))
            if node.right:
                stack.append((node.right, sum - node.val))
        return False