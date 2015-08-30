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
        radius = 1
        for i in xrange(n):
            for k in range(2):
                radius -= 1 # 
                while i-radius >= 0 and i+k+radius < n and s[i-radius:i +1] == s[i+k:i+k+radius +1][::-1]:
                    radius += 1
                subs = s[i-radius +1:i+k+radius]
                if len(subs) > len(ret):
                    ret = subs
        return ret



# https://leetcode.com/discuss/21332/python-o-n-2-method-with-some-optimization-88ms
    # O(n^2), Almost O(n)
    # Traverse, slice backward-only, without subs assignment
    # 100ms
        start = 0
        maxLen = 1
        for i in xrange(len(s)):
            if i-maxLen-1 >= 0 and s[i-maxLen-1:i +1] == s[i-maxLen-1:i +1][::-1]:
                start = i-maxLen-1
                maxLen += 2
                continue
            if i-maxLen >= 0 and s[i-maxLen:i +1] == s[i-maxLen:i +1][::-1]:
                start = i-maxLen
                maxLen += 1
        return s[start:start+maxLen]
        



















        