class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        # import re
        # a = re.sub(r"\W+", r"", s.lower())
        # return a == a[::-1]



        # s = "".join([c.lower() for c in s if c.isalnum()])
        # return s == s[::-1]
        
        
        
        s = filter(lambda x: x.isalnum(), s.lower())
        return s == s[::-1]