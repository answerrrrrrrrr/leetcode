class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        import re,operator
        tokens = re.split('(\D)', input)
        nums = map(int, tokens[::2])
        ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
        def build(lo, hi):
            if lo == hi:
                return [nums[lo]]
            # return [ops[i](a, b)
            #         for i in xrange(lo, hi)
            #         for a in build(lo, i)
            #         for b in build(i + 1, hi)]
            for i in xrange(lo, hi):
                print 'i=%d:' % i
        return build(0, len(nums) - 1)

def testCases():

    i = '4-1-1-1'


    sol = Solution()
    sol.diffWaysToCompute(i)

def main():
    testCases()
    

if __name__ == "__main__":
    main()