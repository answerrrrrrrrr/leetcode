class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
# https://leetcode.com/discuss/53566/python-easy-to-understand-solution-divide-and-conquer
    # divide and conquer
    # 60ms+
        if input.isdigit():
            return [int(input)]
        res = []
        dwtc = self.diffWaysToCompute
        for i in range(len(input)):
            if input[i] in '+-*':
                lRes = dwtc(input[:i])
                rRes = dwtc(input[i+1:])
                for l in lRes:
                    for r in rRes:
                        res.append(self.calc(l, r, input[i]))
        return res
    def calc(self, l, r, op):
        if op == '+':
            return l+r 
        elif op == '-':
            return l-r
        else:
            return l*r



# https://leetcode.com/discuss/48468/1-11-lines-python-9-lines-c
    # 48ms
        # The \D is a regular expression meaning "non-digit". 
        # So it matches the operators and thus splitting with it splits at the operators.
        # Putting parentheses around it tells split to include the splitters (i.e. the operators) in the result.
        tokens = re.split('(\D)', input)
        # 在编译原理中，token表示最小不可分割语义单位，强调原子性
        nums = map(int, tokens[::2])
        ops = map({'+':operator.add, '-':operator.sub, '*':operator.mul}.get, tokens[1::2])
        def build(lo, hi):
            if lo == hi:
                return nums[lo]
            return [ops[i](a, b)
                    for i in range(lo, hi)
                    for a in bulid(lo, i)
                    for b in bulid(i+1, hi)]
            return build(0, len(nums)-1)

    # 168ms
        return [eval('a'+ c +'b')
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]

    # 64ms
        return [a+b if c == '+' else a-b if c == '-' else a*b
            for i, c in enumerate(input) if c in '+-*'
            for a in self.diffWaysToCompute(input[:i])
            for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]

    # 188ms[code golf]
        diffWaysToCompute=d=lambda s,t:[eval(`a`+c+`b`)for i,c in enumerate(t)if
            c<'0'for a in s.d(t[:i])for b in s.d(t[i+1:])]or[int(t)]
















