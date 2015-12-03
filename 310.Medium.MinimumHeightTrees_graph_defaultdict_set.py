class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
    # https://leetcode.com/discuss/71650/share-my-accepted-bfs-python-code-with-o-n-time
    # BFS, defaultdict
    # O(n)
    # 164ms, 44.3%
        if n == 1:
            return [0]
        neighbors = collections.defaultdict(list)
        degrees = collections.defaultdict(int)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        curLevel, unvisited = [], set(range(n))
        for i in xrange(n):
            if degrees[i] == 1:
                curLevel.append(i)
        while len(unvisited) > 2:
            preLevel, curLevel = curLevel, []
            for u in preLevel:
                unvisited.remove(u)
                for v in neighbors[u]:
                    degrees[v] -= 1
                    if degrees[v] == 1:
                        curLevel.append(v)
        return curLevel



# https://leetcode.com/discuss/71763/share-some-thoughts
    # BFS, set
    # O(n)
    # 104ms, 98.1%
        if n == 1:
            return [0]
        neighbors = [set() for _ in xrange(n)]
        for u, v in edges:
            neighbors[u].add(v)
            neighbors[v].add(u)
        curLevel = [i for i in xrange(n) if len(neighbors[i]) == 1]
        while n > 2:
            n -= len(curLevel)
            preLevel, curLevel = curLevel, []
            for u in preLevel:
                v = neighbors[u].pop()
                neighbors[v].remove(u)
                if len(neighbors[v]) == 1:
                    curLevel.append(v)
        return curLevel
