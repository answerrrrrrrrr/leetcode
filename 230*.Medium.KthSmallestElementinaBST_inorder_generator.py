# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
# itr, stack, inorder traverse
    # down to the smallest
    # 84ms
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left 
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right



    # true stack hidden in the 'True' nodes
    # 88ms
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    k -= 1
                    if k == 0:
                        return node.val
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))



# rcs
    # self var
    # 84ms
        self.k = k 
        self.res = 0
        self.dfs(root)
        return self.res
    def dfs(self, root):
        if root:
            self.dfs(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            self.dfs(root.right)



# generator, typical inorder traverse func
    # 80ms
        # for p, v in enumerate(iterate_tree(root)):
        #     if p+1 == k:
        #         return v.val
        for val in self.inorder(root):
            if k == 1:
                return val
            else:
                k -= 1
    def inorder(self, root):
        if root:
            for val in self.inorder(root.left):
                yield val
            yield root.val
            for val in self.inorder(root.right):
                yield val