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
    # DFS rcs
    # 48ms+
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



# https://leetcode.com/discuss/52239/python-solutions-dfs-stack-bfs-queue-dfs-recursively
    # BFS stack
    # 48ms+
        if not root:
            return []
        res = []
        stack = [(root, '')]
        while stack:
            node, path = stack.pop(0) # [DFS] stack.pop()
            v = str(node.val)
            if node.left is node.right is None:
                res.append(path + v)
            if node.left: # [DFS] node.right
                stack.append((node.left, path + v + '->'))
            if node.right: # [DFS] node.left
                stack.append((node.right, path + v + '->'))
        return res















