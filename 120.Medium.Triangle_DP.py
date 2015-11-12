class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
# DP
    # O(n) space
        dp = triangle[::-1]
        for i in xrange(1,len(dp)):
            for j in xrange(len(dp[i])):
                dp[i][j] += min(dp[i-1][j], dp[i-1][j+1])
        return dp[-1][-1]



    # O(1) space
    # triangle modified
        for i in xrange(len(triangle)-2, -1, -1):
            for j in xrange(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]