class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
# https://leetcode.com/discuss/5568/does-anyone-have-better-idea-share-accepted-python-code-here
        array = range(1,n+1)
        k -= 1
        res = ''
        for i in xrange(n-1, -1, -1):
            index, k = divmod(k, math.factorial(i))
            res += str(array.pop(index))
        return res