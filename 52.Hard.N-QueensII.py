class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(cols, xydif, xysum):
            x = len(cols)
            if x == n:
                res.append(cols)
                return
            for y in xrange(n):
                if y not in cols and x-y not in xydif and x+y not in xysum:
                    dfs(cols+[y], xydif+[x-y], xysum+[x+y])
        res = []
        dfs([], [], [])
        return len(res)
