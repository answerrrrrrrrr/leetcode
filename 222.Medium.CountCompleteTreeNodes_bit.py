# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    # TLE
        # res = 0
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         res += 1
        #         stack.append(node.left)
        #         stack.append(node.right)
        # return res



# O(logn * logn), follow the path to the last node
    # itr
    # 160ms
        def getHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        res = 0
        while root:
            lh, rh = getHeight(root.left), getHeight(root.right)
            if lh == rh:
                res += 1 << lh # root + left subtree nodes
                root = root.right
            else:
                res += 1 << rh # root + right subtree nodes
                root = root.left
        return res

    # itr, improved
    # 140ms
        h = self.height(root)
        res = 0
        while root:
            if h-1 == self.height(root.right):
                res += 1 << h 
                root = root.right
            else:
                res += 1 << h-1
                root = root.left
            h -= 1
        return res
    def height(self, root):
            return -1 if not root else 1 + self.height(root.left)



    # rcs
    # 180ms
        def height(root):
            return -1 if not root else 1 + height(root.left)
        if not root:
            return 0
        h = height(root)
        if height(root.right) == h-1:
            return (1 << h) + self.countNodes(root.right)
        else:
            return (1 << h-1) + self.countNodes(root.left)