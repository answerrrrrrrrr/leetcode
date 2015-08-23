# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    # rcs 
    # 100ms+
    #     if not root:
    #         return True
    #     ib,md = self.isBalanced, self.maxDepth
    #     if abs(md(root.left) - md(root.right)) > 1:
    #         return False
    #     return ib(root.left) and ib(root.right)
    # def maxDepth(self, root):
    #     if not root:
    #         return 0
    #     md = self.maxDepth
    #     return 1 + max(md(root.left), md(root.right))



    # rcs once
    # 80ms+
        return self.depthAndBalanced(root)[1]
    def depthAndBalanced(self, root):
        if not root:
            return 0, True
        db = self.depthAndBalanced
        ld, lb = db(root.left)
        rd, rb = db(root.right)
        return 1 + max(ld, rd), lb and rb and abs(ld-rd)<=1

