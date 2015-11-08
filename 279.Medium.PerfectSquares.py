class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
# https://leetcode.com/discuss/62229/short-python-solution-using-bfs
    # like BFS for the shortest path of a tree
    # 1700ms+
        sqs = [i**2 for i in xrange(1, int(n**0.5)+1)]
        count = 0 
        level = {n}
        while 0 not in level:
            count += 1
            temp = set()
            for num in level:
                for sq in sqs:
                    if num < sq:
                        break
                    temp.add(num - sq)
            level = temp
        return count
