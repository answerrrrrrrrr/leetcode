# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
    # itr, BFS
    # 44ms
        if not root:
            return []
        res, level = [], []
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop(0)
            if depth > len(res):
                if depth%2 == 0: # if even, reverse the level above
                    level.reverse()
                res.append(level)
                level = []
            level.append(node.val)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        # add the last level
        if len(res)%2 == 1: # if the last level is odd, reverse it
            level.reverse()
        res.append(level)
        return res

    # logic simplified
    # 44ms
        res, level = [], []
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop(0)
            if level and depth > len(res):
                if depth%2 == 0:
                    level.reverse()
                res.append(level)
                level = []
            if node:
                level.append(node.val)
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        return res



    # itr, BFS
        stack, res = [root], []
        while stack:
            level = []
            for _ in xrange(len(stack)):
                node = stack.pop(0)
                if node:
                    level.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
            if level:
                level = level[::-1] if len(res)%2 else level
                res.append(level)
        return res



    # itr, DFS
        res, stack = [], [(root, 0)]
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) == level:
                    res.append([])
                if level%2 == 0:
                    res[level].append(node.val)
                else:
                    res[level].insert(0, node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        return res



    # rcs, DFS
    # 48ms
        res = []
        self.dfs(root, 0, res)
        return res
    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            self.dfs(root.left, level+1, res)
            self.dfs(root.right, level+1, res)