class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
    # https://leetcode.com/discuss/49179/fast-short-and-easy-understand-python-solution-11-lines-76ms
    # rcs, dfs
    # 76ms, 97.96%
        def dfs(cols, xydif, xysum):
            x = len(cols)
            if x == n: # x > n-1
                res.append(cols)
                return
            for y in xrange(n):
                if y not in cols and x-y not in xydif and x+y not in xysum:
                    dfs(cols+[y], xydif+[x-y], xysum+[x+y])
        res = []
        dfs([], [], [])
        return ['.'*i + 'Q' + '.'*(n-1-i) for i in cols for cols in res]



    # https://leetcode.com/discuss/63710/ac-python-76-ms-iterative-backtracking-solution
    # itr, backtracking
    # 76ms, 97.96%
