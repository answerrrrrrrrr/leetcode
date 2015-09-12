class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        p = 2 * numRows - 2
        lines = ["" for i in range(numRows)]
        d = {}

        for i in xrange(p):
        	if i < numRows:
        		d[i] = i
        	else:
        		d[i] = p - i

        for i in xrange(len(s)):
        	lines[d[i % p]] += s[i]

        return "".join(lines)