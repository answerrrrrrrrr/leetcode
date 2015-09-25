class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
# math
# C(m-1+n-1, m-1) = (m+n-2)!/(m-1)!/(n-1)!

    # reduce
    # 40ms
        # m, n = max(m, n), min(m, n)
        divisor = reduce(operator.mul, range(1, n), 1)
        dividend = reduce(operator.mul, range(m, m+n-1), 1)
        return dividend/divisor

    # factorial
    # 40ms
        return math.factorial(m+n-2) / math.factorial(m-1) / math.factorial(n-1)

    # for-loop
    # 36ms
        # m, n = max(m, n), min(m, n)
        N = m+n-2
        K = m-1
        res = 1
        for i in range(1, K+1):
            res *= 1.0*(N-K+i)/i 
        return int(round(res))



# DP
# https://leetcode.com/discuss/48179/python-easy-to-understand-solutions-math-dp-o-m-n-and-o-n-space
    # O(m*n) space   
        if not m or not n:
            return 0
        dp = [[1 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    # O(n) space 
        if not m or not n:
            return 0
        cur = [1] * n # recycling
        for i in xrange(1, m):
            for j in xrange(1, n):
                cur[j] += cur[j-1]
        return cur[-1]
    