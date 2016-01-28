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