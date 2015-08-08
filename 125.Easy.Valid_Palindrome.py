class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome:
        s = filter(str.isalnum(), s.lower())
        return s == s[::-1]