class Solution(object):
    def canFinish(self, n, pres):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
# topological sort
    # defaultdict
    # 72ms
        outs = collections.defaultdict(set)
        ins = collections.defaultdict(set)
        for u, v in pres:
            outs[u].add(v)
            ins[v].add(u)
        stack = [i for i in xrange(n) if not outs[i]]
        count = 0
        while stack:
            v = stack.pop()
            count += 1
            for u in ins[v]:
                outs[u].remove(v)
                if not outs[u]:
                    stack.append(u)
        return count == n



    # deque
    # 52ms
        id = [[] for _ in xrange(n)] # indegree
        od = [0] * n # outdegree
        for u, v in pres:
            od[u] += 1
            id[v].append(u)
        dq = collections.deque()
        for i in xrange(n):
            if od[i] == 0:
                dq.append(i)
        k = 0
        while dq:
            v = dq.popleft()
            k += 1
            for u in id[v]:
                od[u] -= 1
                if od[u] == 0:
                    dq.append(u)
        return k == n



    # rcs
    # 60ms
        def dfs(i):
            if visit[i] == -1: # visiting
                return False # indicates a circle
            if visit[i] == 1: # visited
                return True
            visit[i] = -1
            for v in outs[i]:
                if not dfs(v):
                    return False
            visit[i] = 1
            return True
        outs = [[] for _ in xrange(n)]
        visit = [0] * n
        for u, v in pres:
            outs[u].append(v)
        for i in xrange(n):
            if not dfs(i):
                return False
        return True



