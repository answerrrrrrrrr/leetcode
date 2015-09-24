class Solution(object):
    def spiralOrder(self, A):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
# https://leetcode.com/discuss/46523/1-liner-in-python
    # rotate(zip) and pop
    # like No.48
    # 40ms
        return A and list(A.pop(0)) + self.spiralOrder(zip(*A)[::-1])
        