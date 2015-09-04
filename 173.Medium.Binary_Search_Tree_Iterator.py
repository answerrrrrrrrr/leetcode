# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.helper(root)

    def helper(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack  # or self.stack != []

    # @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()
        self.helper(node.right)
        return node.val     
# O(lgn) space and O(1) time
# https://leetcode.com/discuss/51823/python-concise-solution-o-lgn-space-and-o-1-time?show=54114#c54114

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())