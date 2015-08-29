# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    # DFS itr
    # 44ms
        if not root:
            return []
        res = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop() # BFS: pop(0), right before left
            if len(res) < level+1:
                res.append(node.val)
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
        return res

    # DFS rcs --- external def
    # 60ms
        res = []
        self.dfs(root, 0, res)
        return res
    def dfs(self, node, level, res):
        if node:
            if len(res) == level:
                res.append(node.val)
            self.dfs(node.right, level+1, res)
            self.dfs(node.left, level+1, res)



# https://leetcode.com/discuss/40262/5-9-lines-python-48-ms
    # DFS rcs --- internal def 
    # [NOTE]:Try NOT to do this(def in def)
    # 60ms
        # def dfs(node, level):
        #     if node:
        #         if len(res) == level:
        #             res.append(node.val)
        #         dfs(node.right, level+1)
        #         dfs(node.left, level+1)
        # res = []
        # dfs(root, 0)
        # return res

    # Optimized rcs
    # 60ms
        # res = []
        # if root:
        #     res += [root.val]
        #     rsv = self.rightSideView
        #     res += rsv(root.right)
        #     res += rsv(root.left)[len(res)-1:]
        # return res
        
        if not root:
            return []
        r = self.rightSideView(root.right)
        l = self.rightSideView(root.left)
        return [root.val] + r + l[len(r):]

    # BFS itr
    # 48ms
        res = []
        if root:
            level = [root]
            while level:
                res += level[-1].val, # ',' makes it become [level[-1].val,]
                # level = [kid for node in level for kid in (node.left, node.right) if kid]
                level = [kid 
                    for node in level 
                    for kid in (node.left, node.right) 
                    if kid] # More readable
        return res

    


