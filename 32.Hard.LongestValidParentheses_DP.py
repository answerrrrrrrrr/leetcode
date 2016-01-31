class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
    # https://leetcode.com/discuss/7609/my-o-n-solution-using-a-stack?show=77082#a77082
    # stack, dummy
    # 80ms, 54.41%
        s, stack, maxLen = '$' + s, [], 0
        for i in xrange(len(s)):
            if s[i] == ")" and s[stack[-1]] == "(":
                stack.pop()
                maxLen = max(maxLen, i - stack[-1])
            else:
                stack.append(i)
        return maxLen



    # https://leetcode.com/discuss/7609/my-o-n-solution-using-a-stack?show=26848#a26848
    # DP
    # 100ms, 12.20%
        dp, left, maxLen = [0]*len(s), 0, 0
        for i in xrange(len(s)):
            if s[i] == '(':
                left += 1
            if s[i] == ')' and left > 0:
                dp[i] += dp[i-1] + 2
                # add previous '(', eg: ()((()))
                if i-dp[i] > 0:
                    dp[i] += dp[i-dp[i]]
                left -= 1
            maxLen = max(maxLen, dp[i])
        return maxLen