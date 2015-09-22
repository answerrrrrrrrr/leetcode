class Solution(object):
    def rotate(self, A):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
# https://leetcode.com/discuss/38426/seven-short-solutions-1-to-7-lines
    # direct, 100% in-place
    # 48ms
        n = len(A)
        for i in range(n/2):
            for j in range(n-n/2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = A[~j][i], A[~i][~j], A[j][~i], A[i][j]



    # list comprehension, using extra space
    # 60ms
        A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]



    # zip --- most Pythonic
    # 40ms
        A[:] = zip(*A[::-1])
        # A[:] = map(list, zip(*A[::-1]))



    # flip flip
    # 40ms
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i],[j]



    # others





    
    # Genuflected...

