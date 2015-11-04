class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
    # rcs
    # LTE
    # contains a lot of repetitive computations
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)



    # DP, O(n) space
        if n == 1:
            return 1
        res = [0] * n
        res[0], res[1] = 1, 2
        for i in xrange(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]



    # DP, O(1) space
        a, b = 1, 1
        for _ in xrange(n):
            a, b = b, a + b
        return a

# https://leetcode.com/discuss/47946/python-different-solutions-bottom-up-top-down