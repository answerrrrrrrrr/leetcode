class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
    #
    # 160ms
        s = s + '+'
        res, num, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                num = 10 * num + ord(c) - ord('0') # faster than int(c) 252ms
            # elif s in "+-":
            #     if stack and stack[-1] in "*/": # update number in a "*/" expression
            #         md, val = stack.pop(), stack.pop()
            #         num = val*num if md == "*" else val/num
            #     res, num, sign = res + sign*num, 0, [-1, 1][s=="+"]
            # elif s in "*/":
            #     if stack and stack[-1] in "*/": # update number in a "*/" expression
            #         md, val = stack.pop(), stack.pop()
            #         num = val*num if md == "*" else val/num
            #     stack.extend([num, s]) # if no previous "*/", append directly
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
