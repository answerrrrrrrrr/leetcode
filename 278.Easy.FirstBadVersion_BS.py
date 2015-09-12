# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
# Binary search
    # 60ms
        l, r = 1, n
        while l <= r:
            m = (l+r) / 2
            if isBadVersion(m):
                r = m-1
            else:
                l = m+1
        return l



# https://leetcode.com/discuss/56563/1-liner-in-ruby-python
    # bisect
    # 40ms
        class Wrap:
            def __getitem__(self, i):
                return isBadVersion(i)
        return bisect.bisect(Wrap(), False, 0, n)