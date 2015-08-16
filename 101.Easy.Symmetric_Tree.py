# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}

 # Recursive Solution   
    # def isSymmetric(self, root):
    #     if not root:
    #         return True
    #     return self.s(root.left, root.right)

    # def s(self, l, r):
    #     if l and r:
    #         return l.val == r.val and self.s(l.left, r.right) and self(l.right, r.left)
    #     return l == r



# Iterative Solution
# https://leetcode.com/discuss/26372/python-iterative-way-using-a-queue?show=44691#a44691
    def isSymmetric(self, root):
        if not root:
            return True
        queue = []
        queue.append((root.left, root.right))
        while queue:
            l, r = queue.pop(0)
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            queue.append((l.left, r.right))
            queue.append((l.right, r.left))
        return True