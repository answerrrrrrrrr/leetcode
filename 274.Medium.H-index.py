class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
    # 48ms
        citations.sort()
        h = n = len(citations)
        for i in range(n):
            if citations[i] >= h:
                return h
            h -= 1
        return 0

# https://leetcode.com/discuss/56011/python-o-n-and-2-line-o-nlogn-solutions
