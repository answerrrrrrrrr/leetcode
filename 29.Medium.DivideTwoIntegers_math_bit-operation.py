class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = dividend * divisor < 0
        a, b = abs(dividend), abs(divisor)
        ans = 0

        # TLE
        # while a >= b:
        #     a -= b
        #     ans += 1

        # increasing divisor
        while a >= b:
            B, b_times = b, 1
            while a >= B:
                a -= B
                ans += b_times
                B <<= 1
                b_times <<= 1

        if neg:
            ans = -ans

        # overflow may only happen when -2147483648/-1
        return 2147483647 if ans > 2147483647 else ans

