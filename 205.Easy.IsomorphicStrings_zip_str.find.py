class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        # if len(s) == len(t):
        #     for i in xrange(len(s)):
        #         if s.index(s[i]) != t.index(t[i]):
        #             return False
        #     return True
        # return False



    # zip, set
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))



    # str.find
        return map(s.find, s) == map(t.find, t)

# https://leetcode.com/discuss/48674/python-different-solutions-dictionary-etc