class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
    # stack
    # 160ms
        s = s + '+'
        res, num, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                num = 10 * num + ord(c) - ord('0') # faster than int(c) 252ms
            # elif c in "+-":
            #     if stack and stack[-1] in "*/": # update number in a "*/" expression
            #         md, val = stack.pop(), stack.pop()
            #         num = val*num if md == "*" else val/num
            #     res, num, sign = res + sign*num, 0, [-1, 1][c=="+"]
            # elif c in "*/":
            #     if stack and stack[-1] in "*/": # update number in a "*/" expression
            #         md, val = stack.pop(), stack.pop()
            #         num = val*num if md == "*" else val/num
            #     stack.extend([num, c]) # if no previous "*/", append directly
            #     num = 0
            elif c != ' ':
                if stack and stack[-1] in '*/':
                    op, pre = stack.pop(), stack.pop()
                    num = pre * num if op == '*' else pre / num
                if c in '*/':
                    stack.extend([num, c])
                    num = 0
                if c in '-+':
                    res += sign * num
                    num, sign = 0, [1, -1][c == '-']
            return res



    # stack + dict
    # 288ms
        num, op, stack = 0, '+', [0]
        ops = {
                '+': lambda x, y: y,
                '-': lambda x, y: -y,
                '*': lambda x, y: x*y,
                '/': lambda x, y: int(float(x)/float(y))
              }
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if not c.isdigit() and c != ' ' or i == len(s)-1:
                pre = 0 if op in '+-' else stack.pop()
                stack.append(ops[op](pre, num))
                num, op = 0, c
        return sum(stack)



# https://leetcode.com/discuss/41632/easy-7-12-lines-three-solutions
# re, iter & next
    # split
    # 520ms
        res = 0
        outer = iter(['+'] + re.split('([+-])', s))
                            # >>> re.split('[+-]', '1+2-3')
                            # ['1', '2', '3']
                            # >>> re.split('([+-])', '1+2-3')
                            # ['1', '+', '2', '-', '3']
        for addsub in outer:
            inner = iter(['*'] + re.split('([*/])', next(outer)))
            term = 1
            for muldiv in inner:
                n = int(next(inner))
                term = term * n if muldiv == '*' else term / n
            res += term if addsub == '+' else -term
        return res



    # findall
    # 200ms
        tokens = iter(re.findall('\d+|\S', s))
        res, sign = 0, 1
        for token in tokens:
            if token.isdigit():
                term = int(token)
            elif token in '*/':
                n = int(next(tokens))
                term = term * n if token == '*' else term / n
            else: # '+-'
                res += term * sign
                # sign = ' +'.find(token)
                sign = [1, -1][token == '-']
        return res + term * sign



    # slice
    # 240ms
        t = re.findall('\d+|\S', s + '+0')[::-1]
        t[::2] = map(int, t[::2])
        while len(t) > 3:
            i = len(t) - 5 + 2 * (t[-2] in '*/' or t[-4] not in '*/')
            b, op, a = t[i:i+3]
            t[i:i+3] = a+b if op=='+' else a-b if op=='-' else a*b if op=='*' else a/b,
        return t[2]
