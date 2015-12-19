class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)




# https://leetcode.com/discuss/70394/2-python-solutions-using-segment-tree
# SegmentTree

# class-based
# 540ms
class SegmentTreeNode(object):
    def __init__(self, val=0, start=0, end=0):
        self.val = val
        self.left = None
        self.right = None
        self.start = start
        self.end = end

class NumArray(object):
    def __init__(self, nums):
        def make_tree(start, end):
            if start == end:
                return SegmentTreeNode(nums[start], start, end)
            node = SegmentTreeNode()
            node.start, node.end = start, end
            mid = (start + end)/2
            node.left, node.right = make_tree(start, mid), make_tree(mid+1, end)
            node.val = node.left.val + node.right.val
            return node
        if nums:
            self.nums = nums
            self.root = make_tree(0, len(nums)-1)

    def update(self, i, val):
        def update_tree(node):
            if node and node.start <= i <= node.end:
                node.val += diff
                update_tree(node.left)
                update_tree(node.right)
        diff = val - self.nums[i]
        self.nums[i] = val
        update_tree(self.root)

    def sumRange(self, i, j):
        def sum_tree(node):
            if not node or j < node.start or node.end < i:
                return 0
            if i <= node.start and node.end <= j:
                return node.val
            return sum_tree(node.left) + sum_tree(node.right)
        if i == j:
            return self.nums[i]
        return sum_tree(self.root)

# array-based
# 440ms







# https://leetcode.com/discuss/70427/0-lines-python
# trickery
# 1196ms
class NumArray(object):
    def __init__(self, nums):
        self.update = nums.__setitem__
        self.sumRange = lambda i, j: sum(nums[i:j+1])

