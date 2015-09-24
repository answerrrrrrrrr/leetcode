class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
# https://leetcode.com/discuss/46720/4-9-lines-python-solutions
    # inside-out
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [range(lo, hi)] + zip(*A[::-1])
        return A



    # inside-out, without extra variables
        A = [[n*n]]
        while A[0][0] > 1:
            A = [range(A[0][0]-len(A), A[0][0])] + zip(*A)[::-1]
        return A * (n>0) # list * 0 = []



    # direct, walk the spiral
        # A = [[0] * n] * n ---> Wrong
        A = [[0]*n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in xrange(1, n*n+1):
            A[i][j] = k
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di 
            i += di 
            j += dj
        return A