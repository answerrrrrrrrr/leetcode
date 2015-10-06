class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
    # 500ms+
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, word, i, j):
                    return True
        return False
    def dfs(self, board, word, i, j):
        if len(word) == 0:
            return True
        if i<0 or i==len(board) or j<0 or j==len(board[0]) or board[i][j] != word[0]:
            return False
        used = board[i][j]
        # board[i][j] = None
        board[i][j] = "#" # 200ms faster
        res = self.dfs(board, word[1:], i+1, j) or \
              self.dfs(board, word[1:], i-1, j) or \
              self.dfs(board, word[1:], i, j+1) or \
              self.dfs(board, word[1:], i, j-1)
        board[i][j] = used
        return res



    # 300ms+
        def search(board, word, r, c):
            if word == "":
                return True
            original = board[r][c]
            board[r][c] = "#"
            # for i in [r-1, r+1]:
            #     if 0 <= i < len(board):
            #         if board[i][c] == word[0]:
            #             if search(board, word[1:], i, c):
            #                 return True
            # for j in [c-1, c+1]:
            #     if 0 <= j < len(board[0]):
            #         if board[r][j] == word[0]:
            #             if search(board, word[1:], r, j):
            #                 return True
            for i,j in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[0]:
                    if search(board, word[1:], i, j):
                        return True
            board[r][c] = original
            return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if search(board, word[1:], r, c):
                        return True
        return False