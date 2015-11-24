class Solution(object):
    def findOrder(self, n, pres):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
    # deque
    # 68ms
        od = [0] * n
        id = [[] for _ in xrange(n)]
        for u, v in pres:
            od[u] += 1
            id[v].append(u)
        dq = collections.deque()
        for i in xrange(n):
            if od[i] == 0:
                dq.append(i)
        res = []
        while dq:
            v = dq.popleft()
            res.append(v)
            for u in id[v]:
                od[u] -= 1
                if od[u] == 0:
                    dq.append(u)
        return res if len(res) == n else []



    # rcs
    # 72ms
        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for v in outs[i]:
                if not dfs(v):
                    return False
            visit[i] = 1
            res.append(i)
            return True
        outs = [[] for _ in xrange(n)]
        visit = [0] * n
        res = []
        for u, v in pres:
            outs[u].append(v)
        for i in xrange(n):
            if not dfs(i):
                return []
        return res

