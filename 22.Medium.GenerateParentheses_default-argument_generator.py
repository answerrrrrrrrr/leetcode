class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
# https://leetcode.com/discuss/43122/4-7-lines-python

# about the default argument
# https://leetcode.com/discuss/43122/4-7-lines-python?show=56258#c56258

    # DFS rcs
    # default arg: list
    # 48ms
        def gp(p, left, right, res=[]):
            if left:
                gp(p+'(', left-1, right)
            if right > left:
                gp(p+')', left, right-1)
            if not right:
                res += p, # res.append(p)
            return res
        return gp('', n, n)



    # generator
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left-1, right): yield q
                for q in generate(p + ')', left, right-1): yield q
        return list(generate('', n, n))



    # amended func
    # default arg: int
    def generateParenthesis(self, n, open=0):
        if n > 0 <= open:
            return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + \
                   [')' + p for p in self.generateParenthesis(n, open-1)]
        return [')' * open] * (not n)