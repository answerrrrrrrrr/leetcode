class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        for r in xrange(m):
            for c in xrange(n):
                live = 0
                # update the 3x3 matrix around (r,c)
                for i in xrange(max(0, r-1), min(r+2, m)):
                    for j in xrange(max(0, c-1), min(c+2, n)):
                        live += board[i][j] & 1
                if live == 3 or live == board[r][c] + 3:
                    board[r][c] += 2
        for r in xrange(m):
            for c in xrange(n):
                board[r][c] &= 1
