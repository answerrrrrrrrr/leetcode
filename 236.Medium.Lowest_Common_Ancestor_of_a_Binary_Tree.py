# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
    # 120ms+
        if not root:
            return None
        if root in (p, q):
            return root
        lca = self.lowestCommonAncestor
        llca, rlca = lca(root.left, p, q), lca(root.right, p, q)
        if (llca, rlca) == (p, q) or (llca, rlca) == (q, p):
            return root
        return llca or rlca