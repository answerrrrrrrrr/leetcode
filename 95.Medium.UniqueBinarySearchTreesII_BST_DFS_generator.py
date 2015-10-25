# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.dfs([num for num in xrange(1, n+1)])
    def dfs(self, lst):
        if not lst:
            return [None] # != []
        res = []
        for i in xrange(len(lst)):
            for left in self.dfs(lst[:i]):
                for right in self.dfs(lst[i+1:]):
                    root, root.left, root.right = TreeNode(lst[i]), left, right
                    res.append(root)
        return res



# https://leetcode.com/discuss/28672/python-generator-solution
    # generator
    #     nodes = map(TreeNode, range(1, n+1))
    #     return map(copy.deepcopy, self.buildTree(nodes))
    # def buildTree(self, nodes):
    #     n = len(nodes)
    #     if n == 0:
    #         yield None
    #         return
    #     for i in range(n):
    #         root = nodes[i]
    #         for left in self.buildTree(nodes[:i]):
    #             for right in self.buildTree(nodes[i+1:]):
    #                 root.left, root.right = left, right
    #                 yield root

        return map(copy.deepcopy, self.buildTree([num for num in xrange(1, n+1)]))
        # >>> xrange(3)
        # xrange(3)
        # >>> map(copy.deepcopy, xrange(3))
        # [0, 1, 2]
    def buildTree(self, lst):
        if not lst:
            yield None
            return
        for i in range(len(lst)):
            for left in self.buildTree(lst[:i]):
                for right in self.buildTree((lst[i+1:])):
                    root, root.left, root.right = TreeNode(lst[i]), left, right
                    yield root

    
                    