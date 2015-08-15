class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        l = sum(([(i, e), (e, j), (i/3, j/3, e)]
                for i, row in enumerate(board)
                for j, e   in enumerate(row)
                if e != '.'), [])
        return len(l) == len(set(l))