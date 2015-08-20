class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        ret = ''
        while n:
            ret = chr((n - 1) % 26 + ord('A')) + ret
            n = (n - 1) / 26
        return ret