class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
    # https://leetcode.com/discuss/53987/python-binary-search-solution-o-lgn?show=56469#a56469
    # BS
    # 68ms
        l, r = 0, x
        while l <= r: # =
            m = (l+r)/2
            if m**2 <= x < (m+1)**2:
                return m 
            elif m**2 > x:
                r = m - 1
            else:
                l = m + 1



    # https://leetcode.com/discuss/58631/3-4-short-lines-integer-newton-every-language
    # Math, Newton
    # 56ms
        r = x
        while r**2 > x:
            r = (r + x/r) / 2
        return r 