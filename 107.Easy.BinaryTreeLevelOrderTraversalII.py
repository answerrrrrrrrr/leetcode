# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
    # DFS rcs
    # 60ms+
    #     res = []
    #     self.dfs(root, 0, res)
    #     return res
    # def dfs(self, root, level, res):
    #     if root:
    #         if len(res) < level+1:
    #             res.insert(0,[])
    #         res[-1-level].append(root.val)
    #         self.dfs(root.left, level+1, res)
    #         self.dfs(root.right, level+1, res)



    # BFS
    # 60ms+
        res = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop(0)
            if node:
                if len(res) < level+1:
                    res.insert(0, [])
                res[-1-level].append(node.val)
                if node.left:
                    stack.append((node.left, level+1))
                if node.right:
                    stack.append((node.right, level+1))
        return res