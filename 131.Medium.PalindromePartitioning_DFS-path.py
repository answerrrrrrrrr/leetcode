class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
    # dfs, path
        res = []
        self.dfs(s, [], res)
        return res
    def dfs(self, s, path, res):
        if not s:
            res.append(path)
        for i in xrange(1, len(s)+1):
            if s[:i] == s[i-1::-1]:
                self.dfs(s[i:], path + [s[:i]], res)



    # dfs, 1-liner
        return [[s[:i]] + rest for i in xrange(1, len(s)+1)
                               if s[:i] == s[i-1::-1]
                               for rest in self.partition(s[i:])] or [[]]