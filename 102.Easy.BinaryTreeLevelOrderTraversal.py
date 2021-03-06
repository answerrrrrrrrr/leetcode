# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
    # BFS 3Lists
    # 60ms+
        # if not root:
        #     return []
        # ret = []
        # level = [root]
        # while level:
        #     ret.append([node.val for node in level])
        #     nextLevel = []
        #     for node in level:
        #         if node.left:
        #             nextLevel.append(node.left)
        #         if node.right:
        #             nextLevel.append(node.right)
        #     level = nextLevel
        # return ret



    # DFS Recursively
    # 50ms+
    #     res = []
    #     self.dfs(root, 0, res)
    #     return res

    # def dfs(self, root, level, res):
    #     if not root:
    #         return
    #     if len(res) < level+1:
    #         res.append([])
    #     res[level].append(root.val)
    #     self.dfs(root.left, level+1, res)
    #     self.dfs(root.right, level+1, res)



    # DFS Stack
    # 60ms+
        res, stack = [], [(root, 0)]
        while stack:
            node, level = stack.pop() # pop(0) is 10ms faster
            if node:
                if len(res) < level+1:
                    res.append([])
                res[level].append(node.val)
                stack.append((node.right, level+1)) 
                stack.append((node.left, level+1)) # left LIFO
        return res



    # https://leetcode.com/discuss/45419/python-short-dfs-solution?show=45422#a45422