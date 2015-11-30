class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
    # https://leetcode.com/discuss/70089/python-solution
    # itertools.combinations
    # 44ms
        n = len(num)
        for i, j in itertools.combinations(range(1, n), 2):
            a, b = num[:i], num[i:j]
            # skip numbers heading with '0'
            if a != str(int(a)) or b != str(int(b)):
                continue
            while j < n:
                c = str(int(a) + int(b))
                if not num.startswith(c, j):
                    break
                a, b = b, c
                j += len(c)
            if j == n:
                return True
        return False



    # https://leetcode.com/discuss/70230/two-missing-test-cases-in-additive-number?show=70256#c70256
        # if num is None or len(num) < 3 or num[0] == '0':
            # return False
        # n = len(num)
        # for i in range(1, n):
            # for j in range(i+1, n):
                # first, second, third = 0, i, j
                # if num[second] == '0' and third > second + 1:
                    # break
                # while third < n:
                    # result = str(int(num[first:second]) + int(num[second:third]))
                    # if num[third:].startswith(result):
                        # first, second, third = second, third, third + len(result)
                    # else:
                        # break
                # if third == n:
                    # return True
        # return False
