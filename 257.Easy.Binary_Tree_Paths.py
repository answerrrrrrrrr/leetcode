# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
    # rcs
    # 40ms+
        # if not root:
        #     return []
        # v, btp = str(root.val), self.binaryTreePaths
        # if root.left is root.right is None:
        #     return [v] # NOT return v !!!
        # return [v+'->'+path for path in btp(root.left) + btp(root.right)]
    
    # Simplified 
        # if not root:
        #     return []
        # return [str(root.val) + '->' + path
        #     for kid in (root.left, root.right) if kid
        #     for path in self.binaryTreePaths(kid)] or [str(root.val)]
    
    # Simplified
        if not root:
            return []
        v, btp = str(root.val), self.binaryTreePaths
        return [v+'->'+path for path in btp(root.left) + btp(root.right)] or [v]
