class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        ln, lh = len(needle), len(haystack)
        for i in xrange(lh-ln+1):
            if needle[:] == haystack[i:i+ln]:
                return i
        return -1