class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
# https://leetcode.com/discuss/47769/python-constant-space-solution-bit-manipulation
    # bitwise
    # in place
        res = 0
        for i in xrange(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            remainder = count % 3
            if i == 31 and remainder: # negative
                res -= 1 << 31
            else:
                res |= remainder * (1 << i)
        return res



# https://leetcode.com/discuss/13652/python-implementation-with-negative-numbers?show=21975#a21975
        ret = 0
        neg = sum(i < 0 for i in A)
        sign = -1 if neg % 3 else 1

        for i in range(32):
            val = sum((abs(num) >> i) & 1 for num in A) % 3
            ret += val << i
        return sign * ret