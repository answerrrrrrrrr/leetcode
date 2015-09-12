class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # s = str(1.0 * numerator / denominator)
        # res = [s.split('.')[0]]
        # Wrong answer caused by Scientific Notation
        # >>> str(-1*1.0/214748364)
        # '-4.65661289042e-09'

# https://leetcode.com/discuss/22652/do-not-use-python-as-cpp-heres-a-short-version-python-code
    # 44ms
        sign = '-' if numerator * denominator < 0 else ''
        n, remainder = divmod(abs(numerator), abs(denominator))
        res = [sign + str(n) + '.']
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            res.append(str(n))
        index = stack.index(remainder)
        res.insert(index+1, '(')
        res.append(')')
        return ''.join(res).replace('(0)', '').rstrip('.')