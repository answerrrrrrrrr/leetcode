class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
# https://leetcode.com/discuss/47924/python-different-solutions
    # rcs
    # 200ms
        if m == n:
            return m
        # return reduce(operator.and_, range(m, n)) --- Memory Error
        return self.rangeBitwiseAnd(m>>1, n>>1) << 1



    # itr
    # 212ms
        zeros = 0
        while m != n:
            m >>= 1
            n >>= 1
            zeros += 1
        return m << zeros