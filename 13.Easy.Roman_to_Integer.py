class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        f = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = f[s[-1]]
        for i in range(len(s) - 1):
            if f[s[i]] < f[s[i+1]]:
                ans -= f[s[i]]
            else:
                ans += f[s[i]]
        return ans