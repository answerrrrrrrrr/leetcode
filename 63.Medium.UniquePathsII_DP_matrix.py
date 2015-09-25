class Solution(object):
    def uniquePathsWithObstacles(self, A):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
    # DP, in-place
    # 48ms
        m, n = len(A), len(A[0])
        A[0][0] = 1 - A[0][0]
        for i in range(1, m):
            A[i][0] = A[i-1][0] * (1 - A[i][0])
        for j in range(1, n):
            A[0][j] = A[0][j-1] * (1 - A[0][j])
        for i in range(1, m):
            for j in range(1, n):
                A[i][j] = (A[i-1][j] + A[i][j-1]) * (1 - A[i][j])
        return A[-1][-1]



# https://leetcode.com/discuss/19681/accepted-simple-python-in-place-solution?show=23091#a23091
    # DP, O(m*n) space
    # 44ms
        m, n = len(A), len(A[0])
        res = [[0] * (n+1) for _ in range(m+1)]
        res[0][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if not A[i-1][j-1]:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]