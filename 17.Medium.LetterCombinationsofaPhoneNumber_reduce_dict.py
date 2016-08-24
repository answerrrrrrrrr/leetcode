class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
    # itr
    # 48ms
        if not digits:
            return []
        mapping = [[' '],[''],['a','b','c'], ['d','e','f'], ['g','h','i'], ['j','k','l'], ['m','n','o'], ['p','q','r','s'], ['t','u','v'], ['w','x','y','z']]
        return reduce(self.CartesianProduct, map(lambda x: mapping[int(x)], digits))
    def CartesianProduct(self, A, B):
        cp = []
        for i in A:
            for j in B:
                cp.append(i+j)
        return cp



    # itr, dict
    # 56ms
        if not digits:
            return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        return reduce(lambda L, digit: [a+b for a in L for b in mapping[digit]], digits, [''])



    # rcs
    # 48ms
        if not digits:
            return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        last = mapping[digits[-1]]
        return [p+l for p in prev for l in last]



    # rcs
    # 56ms
        if not digits:
            return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        lc = self.letterCombinations
        return [a+b for a in lc(digits[:-1])
                    for b in lc(digits[-1])] or list(mapping[digits])



    # itertools
        import itertools

        if not digits:
            return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        L = map(lambda x: mapping.get(x), digits)
        return [''.join(x) for x in itertools.product(*L)]
