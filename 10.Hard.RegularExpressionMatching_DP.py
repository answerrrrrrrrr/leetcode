class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
# https://leetcode.com/discuss/55253/my-dp-approach-in-python-with-comments-and-unittest
    # DP
        m, n = len(s), len(p)
        dp = [[False] * (m+1) for _ in xrange(n+1)]
        dp[0][0] = True

        for i in xrange(2, n+1):
            dp[i][0] = dp[i-2][0] and p[i-1] == '*'

        for i in xrange(1, n+1):
            for j in xrange(1, m+1):
                if p[i-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (p[i-1] == s[j-1] or p[i-1] == '.')
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-2][j]
                    
                    if p[i-2] == s[j-1] or p[i-2] == '.':
                        dp[i][j] |= dp[i][j-1]
        
        # for row in dp: print dp
        
        return dp[-1][-1] # faster than dp[n][m]