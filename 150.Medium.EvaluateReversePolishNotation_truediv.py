class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
    # WA
    # 6 / -132 = -1 other than 0 in Python
        # ops = ["+", "-", "*", "/"]
        # stack = []
        # for t in tokens:
        #     if t in ops:
        #         b = stack.pop()
        #         a = stack.pop()
        #         stack.append(unicode(eval(a + t + b)))
        #     else:
        #         stack.append(t)
        # return int(stack.pop())



    # float
        ops = {
            "+" : lambda x,y: x + y,
            "-" : lambda x,y: x - y,
            "*" : lambda x,y: x * y,
            "/" : lambda x,y: x / y
        }
        stack = []
        for t in tokens:
            if t in ops:
                stack.append(int(ops[t](stack.pop(-2), stack.pop(-1))))
            else:
                stack.append(float(t))
        return int(stack[0])



    # truediv
        ops = {
            "+" : lambda y, x: operator.add(x, y),
            "-" : lambda y, x: operator.sub(x, y),
            "*" : lambda y, x: operator.mul(x, y),
            "/" : lambda y, x: int(operator.truediv(x, y))
        }
        stack = []
        for t in tokens:
            if t in ops:
                stack.append(ops[t](stack.pop(), stack.pop()))
            else:
                stack.append(int(t))
        return stack[0]