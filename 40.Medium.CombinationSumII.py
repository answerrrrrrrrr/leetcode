class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    # rcs 
    # 68ms
        sortedCandidates = sorted(candidates)
        return self.__impl(sortedCandidates, target)
    def __impl(self, sortedCandidatesSub, quota):
        ret = list()
        for i, c in enumerate(sortedCandidatesSub):
            if i > 0 and sortedCandidatesSub[i] == sortedCandidatesSub[i-1]:
                continue
            if quota > c:
                tails = self.__impl(sortedCandidatesSub[i+1:], quota - c)
                ret += [[c]+l for l in tails]
            elif quota == c:
                ret.append([c])
            elif quota < c:
                break
        return ret



    # strange DP
    # https://leetcode.com/discuss/17932/dp-solution-in-python