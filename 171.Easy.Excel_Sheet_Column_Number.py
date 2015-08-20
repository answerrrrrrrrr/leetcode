class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        # ret = 0
        # while s:
        #     ret *= 26
        #     ret += ord(s[0]) - 64
        #     s = s[1:]
        # return ret

    # Optimized 1
        return reduce(lambda x, y: x * 26 + y, [ord(c) - 64 for c in s])

    # Optimized 2
        return sum((ord(c)-64) * 26**exp for exp, c in enumerate(s[::-1]))