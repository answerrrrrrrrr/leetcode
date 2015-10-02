class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
    # 180ms
        pilot = None
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                if (matrix[i][j] == 0) and (pilot is None):
                    pilot = (i, j)
                elif matrix[i][j] == 0:
                    matrix[pilot[0]][j] = 0
                    matrix[i][pilot[1]] = 0
        if pilot is None : return

        for i in xrange(m):
            if i == pilot[0] : continue
            for j in xrange(n):
                if j == pilot[1]: continue
                if matrix[i][pilot[1]] == 0 or matrix[pilot[0]][j] == 0:
                    matrix[i][j] = 0

        for i in xrange(m):
            matrix[i][pilot[1]] = 0
        for j in xrange(n):
            matrix[pilot[0]][j] = 0