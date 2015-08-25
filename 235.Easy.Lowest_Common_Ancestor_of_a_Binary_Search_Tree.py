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
        while (root.val - p.val)*(root.val - q.val) > 0:
            # root = (root.left, root.right)[p.val > root.val]
            root = root.right if p.val > root.val else root.left
        return root

    # Other way
        a, b = sorted([p.val, q.val])
        while not a <= root.val <= b:
            root = (root.left, root.right)[a > root.val]
        return root