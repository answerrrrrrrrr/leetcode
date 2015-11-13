# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    # rcs, DFS
    # 56ms
        return sum(map(int, self.dfs(root)))
    def dfs(self, root):
        if not root:
            return []
        if root.left is root.right is None:
            return [str(root.val)]
        return [str(root.val) + path for path in self.dfs(root.left) + self.dfs(root.right)]



    # rcs, DFS
    # 44ms
        self.res = 0
        self.dfs(root, 0)
        return self.res
    def dfs(self, root, v):
        if root:
            val = v * 10 + root.val
            if root.left is root.right is None:
                self.res += val
            self.dfs(root.left, val)
            self.dfs(root.right, val)



    # itr, BFS
    # 44ms
        if not root:
            return 0
        stack = [(root, root.val)]
        res = 0
        while stack:
            node, val = stack.pop(0)
            if node.left:
                stack.append((node.left, val * 10 + node.left.val))
            if node.right:
                stack.append((node.right, val * 10 + node.right.val))
            if node.left is node.right is None:
                res += val
        return res