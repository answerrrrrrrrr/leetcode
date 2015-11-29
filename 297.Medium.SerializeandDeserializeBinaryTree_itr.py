# Definition for a binary tree node.
# class TreeNode(object):
    # def __init__(self, x):
        # self.val = x
        # self.left = None
        # self.right = None

class Codec:
    # itr
    # 256ms
    def serialize(self, root):
        res, stack = [], [root]
        while stack:
            node = stack.pop(0)
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            else:
                res.append(None) # waste time and space
        while res and res[-1] is None:
            res.pop()
        return res

    def deserialize(self, data):
        if not data:
            return
        data = map(lambda x: None if x is None else TreeNode(x), data)
        data.reverse()
        root = data.pop()
        stack = [root]
        while stack:
            node = stack.pop(0)
            node.left = data.pop() if data else None
            node.right = data.pop() if data else None
            if data:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return root

    # deque
    # https://leetcode.com/discuss/66209/ac-python-solution-level-order-serialization



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
