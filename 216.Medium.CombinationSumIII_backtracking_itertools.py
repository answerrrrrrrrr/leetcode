class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
# backtracking
    # 40ms
        return self.dfs(k, n, 1)
    def dfs(self, k, n, start):
        if k < 0 or start > n:
            return []
        if k == 1:
            return [[n]] if n < 10 else []
        res = []
        for num in xrange(start, 10):
            res += [[num] + c for c in self.dfs(k-1, n-num, num+1)]
        return res



    # 44ms
        res = []
        self.dfs(k, n, 1, [], res)
        return res
    def dfs(self, k, n, start, path, res):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            res.append(path)
        for i in xrange(start, 10):
            self.dfs(k-1, n-i, i+1, path+[i], res)



# https://leetcode.com/discuss/37166/clean-1-6-7-liners-ac
    # itertools.combinations
        return [c for c in itertools.combinations(xrange(1,10), k) if sum(c) == n]

    # other Stephan tricks