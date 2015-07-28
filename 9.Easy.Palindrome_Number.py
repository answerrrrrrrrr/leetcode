class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
        	return False

        reversal = 0; left = x

        while left > 0:
        	reversal = reversal*10 + left%10
       		left /= 10

       	return reversal == x

