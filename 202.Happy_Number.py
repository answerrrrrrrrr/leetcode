class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        nHistory = []
        while n != 1:
            if n in nHistory:
                return False
            nHistory.append(n)
            n = sum([int(i) ** 2 for i in str(n)])
        return True