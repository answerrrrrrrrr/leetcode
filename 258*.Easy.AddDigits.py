class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        return num and (num-1)%9 + 1
        # https://en.wikipedia.org/wiki/Digital_root
        # https://leetcode.com/discuss/52461/python-different-solutions