class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
    # DP, in-place
    # 68ms
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]



# https://leetcode.com/discuss/48172/python-solutions-o-m-n-o-n-space
    # DP, O(n) space
    # 52ms
        m, n = len(grid), len(grid[0])
        cur = [0] * n
        cur[0] = grid[0][0]
        for i in range(1, n):
            cur[i] = cur[i-1] + grid[0][i]
        for i in range(1, m):
            cur[0] += grid[i][0]
            for j in range(1, n):
                cur[j] = min(cur[j-1], cur[j]) + grid[i][j]
        return cur[-1]

# https://leetcode.com/discuss/58490/my-python-solution
    # simplified
    # 60ms
        # m=len(grid)
        # n=len(grid[0])
        # helper=[float("inf")]*(n+1)
        # helper[1]=0
        # for i in range(m):
        #     for j in range(1,n+1):
        #         helper[j]=min(helper[j-1],helper[j])+grid[i][j-1]
        # return helper[-1]
        
        m, n = len(grid), len(grid[0])
        cur = [float('inf')] * n
        cur[0] = 0
        for i in range(m):
            cur[0] += grid[i][0]
            for j in range(1, n):
                cur[j] = min(cur[j-1], cur[j]) + grid[i][j]
        return cur[-1]