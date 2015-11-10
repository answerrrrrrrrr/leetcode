# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
    # rcs
    # 60ms
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        tail = root.left
        if tail:
            while tail.right:
                tail = tail.right
            tail.right = root.right
            root.right = root.left    
            root.left = None



    # itr 
    # 48ms
        if not root:
            return
        p = root
        stack = []
        while p:
            if p.right:
                stack.append(p.right)
            if p.left:
                p.left, p.right = None, p.left
            else:
                if not stack:
                    return
                p.right = stack.pop()
            p = p.right



    # itr, dummy
    # 60ms
        if not root:
            return 
        p = TreeNode(0)
        stack = [root]
        while stack:
            node = stack.pop()
            p.left, p.right = None, node
            p = node # p.right
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)