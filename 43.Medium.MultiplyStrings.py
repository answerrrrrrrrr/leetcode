class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
    # Python trick
    # 48ms
        return str(int(num1) * int(num2))



# https://leetcode.com/discuss/50170/python-understand-solution-without-overflow-with-comments
    # 400ms+
        l1, l2 = len(num1), len(num2)
        res = [0] * (l1+l2)
        for i in xrange(l1-1, -1, -1):
            carry = 0
            for j in xrange(l2-1, -1, -1):
                product = int(num1[i]) * int(num2[j]) + carry
                        # (i+1)+(j+1)-1
                carry, res[i+j+1] = divmod(res[i+j+1] + product, 10)
            # remain carry
            res[i] += carry
        res = ''.join(map(str, res)).lstrip('0')
        return res if res else '0'



# https://leetcode.com/discuss/50707/simple-python-solution-18-lines
    # reversed
    # logic simplified
    # 400ms+
        res = [0] * (len(num1) + len(num2))
        for i1, e1 in enumerate(reversed(num1)):
            for i2, e2 in enumerate(reversed(num2)):
                res[i1 + i2] += int(e1) * int(e2)
                res[i1 + i2 + 1] += res[i1 + i2] / 10
                res[i1 + i2] %= 10
        res = ''.join(map(str, res[::-1])).lstrip('0')
        return res if res else '0'
 