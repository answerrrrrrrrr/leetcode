class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
# https://leetcode.com/discuss/37021/1-liner-3-liner-4-liner
    # library
        return list(itertools.combinations(range(1,n+1), k))



    # rcs
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(1, n+1)
                          for pre in self.combine(i-1, k-1)]



    # itr
        res = [[]]
        for _ in range(k):
            res = [[i] + c for c in res
                           for i in range(1, c[0] if c else n+1)]
        return res
    # using reduce instead of a loop, not recommend
        # return reduce(lambda C, _: [[i]+c for c in C for i in range(1,c[0] if c else n+1)], range(k), [[]])



# https://leetcode.com/discuss/61607/ac-python-backtracking-iterative-solution
    # itr, backtracking
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1