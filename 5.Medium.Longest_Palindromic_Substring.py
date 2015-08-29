class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
    # O(n^2) 
    # Traverse, grow multiple times
    # 1300ms
        ret = ''
        n = len(s)
        for i in xrange(n):
            for k in range(2):
                subs = self.getPalindrome(s, i, i+k)
                if len(subs) > len(ret):
                    ret = subs
        return ret
    def getPalindrome(self, s, l, r):
        n = len(s)
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1; r += 1
        return s[l +1:r]

    # O(n^2)
    # Traverse, grow once, compare by slicing
    # 208ms
        ret = ''
        n = len(s)
        span = 1
        for i in xrange(n):
            for k in range(2):
                span -= 1 # 
                while i-span >= 0 and i+k+span < n and s[i-span:i +1] == s[i+k:i+k+span +1][::-1]:
                    span += 1
                subs = s[i-span +1:i+k+span]
                if len(subs) > len(ret):
                    ret = subs
        return ret





















        