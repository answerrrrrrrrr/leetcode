class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
# Explanation:
    # https://leetcode.com/discuss/48025/6-9-lines-c-python-solutions-with-explanations
    # Top-right

    # O(m+n)
    # 112ms
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n-1
        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                c -= 1 
            else:
                r += 1 
        return False

# https://leetcode.com/discuss/47571/4-lines-c-6-lines-ruby-7-lines-python-1-liners
    # O(mn)
    # 200ms
        return any(target in row for row in matrix)

    # O(m+n)
    # Optimized
    # 100ms
        j = -1
        for row in matrix:
            while len(row) + j and row[j] > target:
                j -= 1
            if row[j] == target:
                return True
        return False
