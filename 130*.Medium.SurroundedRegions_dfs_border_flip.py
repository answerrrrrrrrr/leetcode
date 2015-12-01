class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
    # dfs
    # 400ms
        def update(i, j, board, visited):
            stack, ready = [(i, j)], []
            failed = False
            while stack:
                i, j = stack.pop()
                visited.add((i, j))
                if i in [0, m-1] or j in [0, n-1]:
                    failed = True
                    continue
                if not failed: # save space but 80ms slower
                    ready.append((i, j))
                for (x, y) in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if board[x][y] == 'O' and (x, y) not in visited:
                        stack.append((x, y))
            if not failed:
                for i, j in ready:
                    board[i][j] = 'X'

        if not board or len(board) < 3:
            return
        m, n = len(board), len(board[0])
        visited = set()
        for i in xrange(1, m-1):
            for j in xrange(1, n-1):
                if (i, j) not in visited and board[i][j] == 'O':
                    update(i, j, board, visited)



# https://leetcode.com/discuss/45746/9-lines-python-148-ms
    # dfs, 2 phases
    # 140ms
        if not any(board):
            return
        m, n = len(board), len(board[0])

        # save every O-region touching the border in a list which do have some duplicates
        # save = [ij for k in range(m+n) for ij in ((0,k),(m-1,k),(k,0),(k,n-1))]

        # fewer costs on space
        save = [p for k in xrange(max(m,n)) for p in ((0,k),(m-1,k),(k,0),(k,n-1))]

        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

        board[:] = [['XO'[c == 'S'] for c in row] for row in board]
