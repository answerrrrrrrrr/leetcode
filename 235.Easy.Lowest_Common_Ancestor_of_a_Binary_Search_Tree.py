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
    # itr
    # 132ms
        # lca = root
        # while (p.val < lca.val and q.val < lca.val) or (p.val > lca.val and q.val > lca.val):
        #     if p.val < lca.val:
        #         lca = lca.left
        #     elif p.val > lca.val:
        #         lca = lca.right
        # return lca

# https://leetcode.com/discuss/44959/3-lines-with-o-1-space-1-liners-alternatives        
    # Simplified
    # 126ms
        while (root.val - p.val)*(root.val - q.val) > 0:
            # root = (root.left, root.right)[p.val > root.val]
            root = root.right if p.val > root.val else root.left
        return root

    # 140ms
        a, b = sorted([p.val, q.val])
        while not a <= root.val <= b:
            root = (root.left, root.right)[a > root.val]
        return root



    # rcs
    # 128ms
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    # Trick 1
        next = p.val < root.val > q.val and root.left \
            or p.val > root.val < q.val and root.right
        return self.lowestCommonAncestor(next, p, q) if next else root
        
    # Trick 2
        return root if (root.val - p.val) * (root.val - q.val) < 1 else \
            self.lowestCommonAncestor((root.left, root.right)[p.val > root.val], p, q)
    # Trick 2'
        return self.lowestCommonAncestor((root.left, root.right)[p.val > root.val], p, q) \
            if (root.val - p.val)*(root.val - q.val) > 0 else root














