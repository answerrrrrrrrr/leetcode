# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        lca = root
        
        while (p.val < lca.val and q.val < lca.val) or (p.val > lca.val and q.val > lca.val):
            if p.val < lca.val:
                lca = lca.left
            elif p.val > lca.val:
                lca = lca.right
        
        return lca