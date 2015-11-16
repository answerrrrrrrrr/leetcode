class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
# DP, O(mn) time
    # O((m+1)*(n+1)) space
    # 144ms
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in xrange(m+1)]
        a = 0
        for i in xrange(m):
            for j in xrange(n):
                dp[i+1][j+1] = (min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1) * int(matrix[i][j])
                # a = max(a, dp[i+1][j+1]) # 176ms
        a = max([max(i) for i in dp])
        return a*a



    # O(m*n) space
    # 180ms
        # if not matrix:
        #     return 0
        # m, n = len(matrix), len(matrix[0])
        # dp = [[int(matrix[i][j]) for j in xrange(n)] for i in xrange(m)]
        # a = 0
        # for i in xrange(1, m):
        #     for j in xrange(1, n):
        #         dp[i][j] = (min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1) * int(matrix[i][j])
        # a = max([max(i) for i in dp])
        # return a*a
    # 120ms
    # seems 'int()' is slower than 'if else'
        if not matrix: 
            return 0
        m, n = len(matrix),len(matrix[0])
        dp = [[0 if matrix[i][j]=='0' else 1 for j in xrange(n)] for i in xrange(m)]
        for i in xrange(1,m):
            for j in xrange(1,n):
                if matrix[i][j] == '1': 
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                else: 
                    dp[i][j] = 0
        a = max([max(i) for i in dp])
        return a ** 2 



    # O(n+1) space
    # 112ms
        if not matrix:
            return 0
        m, n = len(matrix),len(matrix[0])
        dp = [0] * (n+1)
        a = 0
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == '0':
                    dp[j+1] = 0
                else:
                    k = min(dp[j], dp[j+1])
                    if matrix[i-k][j-k] == '1': # check the top-left point
                        k += 1
                        a = max(a, k)
                    dp[j+1] = k
        return a*a