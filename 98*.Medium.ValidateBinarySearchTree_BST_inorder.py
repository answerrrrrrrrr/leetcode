# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    # rcs, generator
    # too much duplicates
    # 230ms
    #     l = [self.inorder(root)]
    #     for i in xrange(1, len(l)):
    #         if l[i-1] >= l[i]:
    #             return False
    #     return True
    # def inorder(self, root):
    #     if root:
    #         for val in self.inorder(root.left):
    #             yield val 
    #         yield root.val
    #         for val in self.inorder(root.right):
    #             yield val



    # rcs, self var
    # typical inorder recursive function
    # remove duplicates
    # 80ms
        self.res = []
        self.dfs(root)
        return self.res == sorted(self.res) and len(set(self.res)) == len(self.res)
    def dfs(self, root):
        if root:
            self.dfs(root.left)
            self.res.append(root.val)
            self.dfs(root.right)



# https://leetcode.com/discuss/51838/python-iterative-and-recursive-solutions-with-comments
    # rcs, self var
    # one pass
    # 72ms
        self.res, self.flag = [], True
        self.dfs(root)
        return self.flag
    def dfs(self, root):
        if root:
            self.dfs(root.left)
            if res[-1] >= root.val:
                self.flag = False
                return
            self.res.append(root.val)
            self.dfs(root.right)



    # rcs
    # one pass
    # 72ms
        return self.helper(root, float("-inf"), float("inf"))
    def helper(self, root, low, high):
        if not root:
            return True
        if not root.left and not root.right:
            return low < root.val < high
        return low < root.val < high and self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)



    # itr, O(n)
    # inorder 
        stack, res = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return True
            node = stack.pop()
            if res and node.val <= res[-1]:
                return False
            res.append(node.val)
            root = node.right



    # itr, O(1)
    # typical inorder 
        stack, l = [], None
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if l and l.val >= node.val:
                return False
            l = node
            node = node.right