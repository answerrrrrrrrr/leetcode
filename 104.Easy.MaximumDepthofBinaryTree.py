# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    # DFS rcs
    # 68ms+
        # if not root:
        #     return 0
        # md = self.maxDepth
        # return max(md(root.left), md(root.right)) + 1



    # BFS
    # 80ms+
        # if not root:
        #     return 0
        # stack, maxLevel = [(root, 1)], 1
        # while stack:
        #     node, level = stack.pop(0)
        #     if level > maxLevel:
        #         maxLevel = level
        #     if node.left:
        #         stack.append((node.left, level+1))
        #     if node.right:
        #         stack.append((node.right, level+1))
        # return maxLevel
    # 70ms+
        if not root:
            return 0
        stack = [(root, 1)]
        while stack:
            node, level = stack.pop(0)
            if not node.left and not node.right and not stack:
                return level
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))