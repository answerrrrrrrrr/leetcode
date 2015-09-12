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
    # rcs
    # 120ms+
        if not root:
            return None
        if root in (p, q):
            return root
        lca = self.lowestCommonAncestor
        llca, rlca = lca(root.left, p, q), lca(root.right, p, q)
        # if (llca, rlca) == (p, q) or (llca, rlca) == (q, p):
        if llca and rlca: 
            return root
        return llca or rlca

    # Simplified
    # https://leetcode.com/discuss/45386/4-lines-c-java-python-ruby
    # 110ms+
        if root in (None, p, q):
            return root
        lca = self.lowestCommonAncestor
        llca, rlca = lca(root.left, p, q), lca(root.right, p, q)
        return root if (llca and rlca) else (llca or rlca)

    # Code simplified but slower
    # 200ms+
        # if root in (None, p, q):    return root
        # l, r = (self.lowestCommonAncestor(kid, p, q)
        #     for kid in (root.left, root.right))
        # return root if l and r else l or r



    # itr
    # https://leetcode.com/discuss/45603/iterative-solutions-in-python-c













