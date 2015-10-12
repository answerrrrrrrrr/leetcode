class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
# https://leetcode.com/discuss/22954/accpeted-python-dp-solution
    # DP
        # dp[i] tells the numbers of ways of s[:i]
        # dp[i] = dp[i-1] if s[i-1] != "0"
        #       + dp[i-2] if "09" < s[i-2:i] < "27"
        if s == "": return 0
        dp = [0 for x in range(len(s)+1)]
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != "0":
                s[i] += s[i-1]
            if i > 1 and "09" < s[i-2:i] < "27":
                dp[i] += dp[i-2]
        return dp[-1]



# https://leetcode.com/discuss/46552/1-liner-o-1-space
    # itr
        pw, w, pd = 0, int(s>''), ''
        for d in s:
            pw, w, pd = w, (d>'0')*w + (9<int(pd+d)<27)*pw, d 
        return w

    # one-liner
        return reduce(lambda (v,w,p), d: (w, (d>'0')*w+(9<int(p+d)<27)*v, d), s, (0, s>'', ''))[1]*1