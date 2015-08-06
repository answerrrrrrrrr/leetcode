class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        # nHistory = []
        # while n != 1:
        #     if n in nHistory:
        #         return False
        #     nHistory.append(n)
        #     n = sum([int(i) ** 2 for i in str(n)])
        # return True



        return self.isHappy(sum([int(i) ** 2 for i in str(n)])) if n > 4 else n == 1
        # All non-happy numbers follow sequences that reach the cycle:
        # 4, 16, 37, 58, 89, 145, 42, 20, 4, ...
        # https://en.wikipedia.org/wiki/Happy_number
        # https://leetcode.com/discuss/32828/python-one-line-solution