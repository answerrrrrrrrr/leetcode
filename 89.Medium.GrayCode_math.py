class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
# https://en.wikipedia.org/wiki/Gray_code
    # Constructing an n-bit Gray code
    # binary-reflected, rcs
    # 48ms
        if n == 0:
            return [0]
        head = self.grayCode(n-1)
        tail = [2**(n-1) + num for num in head[::-1]]
        return head + tail

    # Converting to and from Gray code
    # map, lambda
    # 56ms
        return map(lambda x: (x>>1)^x, [num for num in range(2**n)])
