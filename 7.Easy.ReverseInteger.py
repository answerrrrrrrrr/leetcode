class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        ra = self.reverseAbs
    	result = ra(x) if x > 0 else -ra(-x)
    	return result if abs(result) < 2147483648 else 0

    def reverseAbs(self, x):
    	return int(str(x)[::-1])