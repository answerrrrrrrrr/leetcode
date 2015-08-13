class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        a, b = 1, 1
        for _ in xrange(n):
            a, b = b, a + b
        return a