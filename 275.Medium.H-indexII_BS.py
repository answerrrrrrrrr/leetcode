class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
# sorted list --- binary search
# https://leetcode.com/discuss/56119/binary-search-in-python
        n = len(citations)
        l, r = 0, n-1
        while l <= r:
            m = (l + r) / 2
            if citations[m] < n-m:
                l = m + 1
            else:
                r = m - 1
        return n - l