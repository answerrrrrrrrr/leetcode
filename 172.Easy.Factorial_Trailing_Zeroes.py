class Solution(object):
    def trailingZeroes(self, n):
    # http://www.tuicool.com/articles/RZZnQf
    # 40ms+
        # x, ret = 5, 0
        # while n >= x:
        #     ret += n / x
        #     x *= 5
        # return ret
        
    # https://leetcode.com/discuss/19845/o-log5_n-solution-python
    # 50ms+
        # r = 0
        # while n >= 5:
        #     n /= 5
        #     r += n
        # return r
        
    # https://leetcode.com/discuss/19855/my-one-line-solutions-in-3-languages
    # 70ms+
        return 0 if n == 0 else n/5 + self.trailingZeroes(n/5)