class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
    # forwards
    # 180ms
        res, num, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c in '-+':
                res += sign * num
                sign = [-1, 1][c=='+']
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif c == ')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + sign * num



    # backwards, DP
    # 350ms
        stack = [0]
        i = len(s)
        while i:
            c = s[i-1]
            if c == ')':
                stack += 0,
            if c.isdigit():
                end = i
                while i and s[i-1].isdigit():
                    i -= 1
                stack += int(s[i:end]),
                i += 1
            if c in '-+(':
                n = stack.pop()
                stack[-1] += (n, -n)[c == '-']
            i -= 1
        return sum(stack)

