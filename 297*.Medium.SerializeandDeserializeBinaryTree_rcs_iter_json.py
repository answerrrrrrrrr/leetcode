# Definition for a binary tree node.
# class TreeNode(object):
    # def __init__(self, x):
        # self.val = x
        # self.left = None
        # self.right = None

class Codec:
    # https://leetcode.com/discuss/66147/recursive-preorder-python-and-c-o-n
    # rcs
    # iter, next
    # 200ms
    def serialize(self, root):
        def doit(node):
            if node:
                res.append(node.val)
                doit(node.left)
                doit(node.right)
            else:
                res.append('#') # waste time and space
        res = []
        doit(root)
        return res

    def deserialize(self, data):
        def doit():
            val = data.next()
            if val == '#':
                return None
            node = TreeNode(val)
            node.left = doit()
            node.right = doit()
            return node
        data = iter(data)
        return doit()



    # https://leetcode.com/discuss/66180/tuplify-json-python
    # rcs
    # json
    # 200ms
    def serialize(self, root):
        def tuplify(root):
            return root and (root.val, tuplify(root.left), tuplify(root.right))
        return json.dumps(tuplify(root))

    def deserialize(self, data):
        def detuplify(t):
            if t:
                root = TreeNode(t[0])
                root.left = detuplify(t[1])
                root.right = detuplify(t[2])
                return root
        return detuplify(json.loads(data))



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
