class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
    # library
    # 40ms
        return x**n



# D&C
# https://leetcode.com/discuss/39143/shortest-python-guaranteed
    # rcs
    # 40ms
        p = self.myPow
        if not n:
            return 1
        if n < 0:
            return 1 / p(x, -n)
        if n % 2:
            return x * p(x, n-1)
        return p(x*x, n/2)

    # itr
    # 40ms
        if n < 0:
            x = 1/x
            n = -n 
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow 