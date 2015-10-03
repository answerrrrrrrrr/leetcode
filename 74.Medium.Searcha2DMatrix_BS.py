class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m*n-1
        while lo <= hi:
            mid = (lo + hi)/2
            num = matrix[mid/n][mid%n]
            if num == target:
                return True
            elif num < target:
                lo = mid + 1
            elif num > target:
                hi = mid - 1
        return False