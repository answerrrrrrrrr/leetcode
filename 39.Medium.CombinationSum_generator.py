class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    # rcs
    # 108ms
        res = []
        candidates.sort()
        for i, v in enumerate(candidates):
            if v < target:
                                                    # avoid duplicate
                sub = self.combinationSum(candidates[i:]             , target-v)
                if sub:
                    res += [[v]+s for s in sub]
            elif v == target:
                res.append([v])
            else:
                break
        return res



# https://leetcode.com/discuss/20942/my-python-recursive-solution-quite-fast-around-100-ms
    # rcs
    # 84ms
        sortedCandidates = sorted(candidates)
        return self.__impl(sortedCandidates, target)
    def __impl(self, sortedCandidatesSub, quota):
        ret = list()
        for i, c in enumerate(sortedCandidatesSub):
            if quota > (c + c): # ingenious
                tails = self.__impl(sortedCandidatesSub[i:], quota - c)
                ret += [[c]+l for l in tails]
            elif quota == c + c:
                ret.append([c, c])
            elif quota == c:
                ret.append([c])
            elif quota < c:
                break
        return ret



# https://leetcode.com/discuss/42670/very-elegant-python-code-using-recursive-yield-iterator
    # rcs, generator
    # 84ms
        def gen(candidates, target):
            if candidates == [] or target < candidates[0]:
                return
            elif candidates[0] == target:
                yield [target]
            else:
                for i in gen(candidates, target-candidates[0]):
                    yield [candidates[0]] + i 
                for j in gen(candidates[1:], target):
                    yield j
        return list(gen(sorted(candidates), target))