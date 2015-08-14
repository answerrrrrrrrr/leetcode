# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if not p or not q:
            return p == q
        st = self.isSameTree
        return p.val == q.val and st(p.left, q.left) and st(p.right, q.right)



# https://leetcode.com/discuss/36879/shortest-simplest-python
# The "proper" way:
# class Solution:
#     def isSameTree(self, p, q):
#         if p and q:
#             return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#         return p == q

# The "tupleify" way:
# class Solution:
#     def isSameTree(self, p, q):
#         def t(n):
#             return n and (n.val, t(n.left), t(n.right))
#         return t(p) == t(q)