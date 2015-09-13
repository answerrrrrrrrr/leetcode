# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, S):
        """
        :type root: TreeNode
        :type S: int
        :rtype: List[List[int]]
        """
    # BFS itr
    # 80ms
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            node, curPath = stack.pop(0)
            curSum = sum(curPath)
            if curSum == S and (node.left is node.right is None):
                res.append(curPath)
            if node.left:
                stack.append((node.left, curPath+[node.left.val]))
            if node.right:
                stack.append((node.right, curPath+[node.right.val]))
        return res



    # DFS rcs
    # 96ms
        if not root:
            return []
        if root.left is root.right is None and S == root.val:
            return [[root.val]]
        ps = self.pathSum
        res = ps(root.left, S-root.val) + ps(root.right, S-root.val)
        return [[root.val]+i for i in res]

# https://leetcode.com/discuss/41197/short-python-solution