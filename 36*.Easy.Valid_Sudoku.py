class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        l = sum(([(i, e), (e, j), (i/3, j/3, e)]
                for i, row in enumerate(board)
                for j, e   in enumerate(row)
                if e != '.'), [])
        return len(l) == len(set(l))


# https://leetcode.com/discuss/48737/1-7-lines-python-4-solutions

# Using Counter. One logical line, seven physical lines.

# def isValidSudoku(self, board):
#     return 1 == max(collections.Counter(
#         x
#         for i, row in enumerate(board)
#         for j, c in enumerate(row)
#         if c != '.'
#         for x in ((c, i), (j, c), (i/3, j/3, c))
#     ).values())
# Solution 2

# Using len(set).

# def isValidSudoku(self, board):
#     seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
#                 for i, row in enumerate(board)
#                 for j, c in enumerate(row)
#                 if c != '.'), [])
#     return len(seen) == len(set(seen))
# Solution 3

# Using any.

# def isValidSudoku(self, board):
#     seen = set()
#     return not any(x in seen or seen.add(x)
#                    for i, row in enumerate(board)
#                    for j, c in enumerate(row)
#                    if c != '.'
#                    for x in ((c, i), (j, c), (i/3, j/3, c)))
# Solution 4

# Iterating a different way.

# def isValidSudoku(self, board):
#     seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
#                 for i in range(9) for j in range(9)
#                 for c in [board[i][j]] if c != '.'), [])
#     return len(seen) == len(set(seen))