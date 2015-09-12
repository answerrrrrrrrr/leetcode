class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pt = [[1]*(i+1) for i in xrange(numRows)]
        for i in xrange(2, numRows):
            for j in xrange(1, i):
                pt[i][j] = pt[i-1][j-1] + pt[i-1][j]
        return pt