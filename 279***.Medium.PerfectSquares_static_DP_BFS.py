class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
# https://leetcode.com/discuss/58056/summary-of-different-solutions-bfs-static-and-mathematics


        
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



# https://leetcode.com/discuss/57218/python-accepted-solution
# https://leetcode.com/discuss/57380/python-common-bfs-with-fewer-lines
    # BFS, stack
    # 780ms
        stack = [(0, 0)]
        visited = set()
        while stack:
            i, step = stack.pop(0)
            step += 1
            for j in xrange(1, n+1):
                k = i + j**2
                if k > n:
                    break
                if k == n:
                    return step
                if k not in visited:
                    visited.add(k)
                    stack.append((k, step))

    # BFS, deque
    # 680ms
        queue = collections.deque([(0, 0)])
        visited = set()
        while queue:
            i, step = queue.popleft() # faster than pop(0)
            step += 1
            for j in xrange(1, n + 1):
                k = i + j * j
                if k > n:
                    break
                if k == n:
                    return step
                if k not in visited:
                    visited.add(k)
                    queue.append((k, step))
